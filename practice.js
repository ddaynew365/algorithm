const dgram = require('dgram');
const dns = require('dns');
const net = require('net');
const fs =require('fs');


const socket = dgram.createSocket('udp4');
socket.bind(12020); // bind

socket.on('listening', function(){
    console.log('listening event'); // udp client로부터 메시지 기다리는 중
});

socket.on('message', function(msg, rinfo) {
    request(msg);   // udp client로부터 온 메시지를 받은 경우 Tcp server로 요청
});

// 요청 메소드
const request = function(msg){
    let msgStr = msg.toString();
    console.log(msgStr);
    let a = msgStr.match(/HOST\s*:\s*(?<host>.*)/gmi);

    const ip = a[0].replace(/HOST\s*:\s*/gmi, ''); // 요청 헤더로부터 host 가져오기

    // dns server에서 dns ip 주소 받아오기
    dns.lookup(ip, (err, address, family) =>{
        console.log('(DNS Lookup...)');
        console.log('TCP Connection: %j family: IPv%s', address, family);
        console.log();
        dnsIp = address;
        const tsocket = new net.Socket();
        const port = 80;
        let serverData = '';
        // dns ip 주소와 포트번호로 tcp 서버에 요청
        tsocket.connect({host:dnsIp, port:port}, function() {
            tsocket.write(msg); // udp클라이언트로부터 받은 헤더 전송
            tsocket.end();

            tsocket.on('error', function(error) {
                tsocket.close();
            });
            tsocket.on('data', function(chunk) {
                serverData += chunk;    // 데이터를 모아서 받기
            });

            tsocket.on('end', function() {  // 데이터를 다 받으면 실행
                // console.log(serverData);
                console.log();
                console.log('서버 연결 종료');
                // status code 추출
                let statusCode = serverData.match(/HTTP\/1.1 (?<statusCode>\d*)/).groups.statusCode
                // 응답코드가 30x면 해당 location으로 요청
                if(statusCode >= 300 && statusCode < 310){
                    let location = serverData.match(/Location: (?<location>.*)/).groups.location;
                    console.log(location);
                    let httpRequest = msgStr.split('\r\n');
                    httpRequest[0] = httpRequest[0].replace('/ HTTP/',location+' HTTP/');
                    let strRedirect = httpRequest.join('\r\n');
                    let msgRedirect = new Buffer.from(strRedirect);
                    request(msgRedirect); // 재귀를 사용하여 응답 요청
                }else{ // 응답코드가 정상적인 경우
                    const responseBody = serverData.match(/<body>[\s\S.]*<\/body>/)[0]
                    const responseLine = serverData.match(/(?<responseLine>(.*)?)/).groups.responseLine;
                    const responseContentLength = Buffer.byteLength(responseBody);
                    // http Response 객체 생성
                    const HTTPResposne ={
                        'statusCode': statusCode,
                        'responseLine': responseLine,
                        'contentLength': responseContentLength,
                        'contentFileURL': ip,
                        'body':responseBody
                    }
                    fs.writeFileSync('../db/'+ip+'.txt',JSON.stringify(HTTPResposne));
                }
            });
        });
    });
}