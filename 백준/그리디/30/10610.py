import sys
"""
30의 배수를 찾기 위해서 나는 3의 배수이면서 10의 배수인 수 중 가장 큰 수를 찾는 방법을 사용해
문제를 해결하였다. 3의 배수는 모든 자리수의 합이 3의 배수인 방법을 사용하였고 10의 배수는 0이 
주어진 입력에 있는지를 판별하는 것을 사용하였다.
첫 번쨰 풀이는 문자열을 리스트로 바꾸고 정수형으로 바꾸고 정렬한 후 다시 문자 자료형을 바꾼 후
합치는 미련한 방법을 사용하였다. 따라서 시간 복잡도가 무지 큰 것을 느꼈다.
두 번쨰 풀이는 문자열을 정렬과 동시에 리스트로 바꾸는 sorted()함수를 사용하였고 정수형 리스트로
바꾸지 않아도 map 객체에서 sum()함수를 바로 사용하였다. 아직 파이썬의 유연성에 대해 제대로
파악하지 못한 것 같다.
"""
# N = list(map(int,list(sys.stdin.readline().strip())))
# ans = 0
# if sum(N) % 3 != 0 or 0 not in N:
#     ans = -1
# else:
#     N.sort(reverse=True)
#     N = list(map(str,N))
#     ans = int(''.join(N))
#
# print(ans)


# map 객체도 sum이 가능하다는 것을 알게 되었다
# sorted 함수의 결과는 리스트(input은 str도 가능하다)

N = sorted(input(),reverse=True)

if '0' not in N or sum(map(int,N))% 3 != 0:
    print(-1)
else:
    print(''.join(N))
