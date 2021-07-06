import java.io.*;
import java.util.*;

public class Make {
    private static int L, C;
    private static char[] arr;
    private static char[] ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        ans = new char[L];
        arr = new char[C];
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i< C ; i++){
            String str = st.nextToken();
            arr[i] = str.charAt(0);
        }
        // 여기에다가 최소 한개의 모음과 두개의 자음 조건 붙이기
        Arrays.sort(arr);
        recur(0,0);
    }

    public static void recur(int where, int from){
        //final condition
        if(where == L){
            if(check()) {
                System.out.println(new String(ans));
            }
            return;
        }
        for (int i = from ; i < C ; i++) {
            ans[where] = arr[i];
            // 이 시점에 미리 자음이랑 모음 개수를 세어 놓을 수 있다.
            // 중간에 잘하면 가지치기가 가능
            recur(where + 1, i + 1);
        }
    }

    public static boolean check() {
        int countMoeum = 0, countJaeum = 0;
        boolean[] isMoeum = new boolean[128];
        isMoeum['a'] = true;
        isMoeum['e'] = true;
        isMoeum['o'] = true;
        isMoeum['i'] = true;
        isMoeum['u'] = true;

        for (int i = 0 ; i < L ; i++) {
            if (isMoeum[ans[i]]) countMoeum++;
            else countJaeum++;
        }
        return countMoeum >= 1 && countJaeum >= 2;
    }
}