#include<cstdio>

int main(void){
    int m,n;
    scanf("%d%d", &n, &m);
    for (int i = 0, a,b, c; i < m; i++){
        scanf("%d%d%d", &a, &b,&c);
        
        if(a == 0){
            p[b] =c;
        }
        else{
            int connected = 0;
            int pb = p[b], pc = p[c];
            while(1){
                if(p[pb] == pb) break;
                pb = p[pb];
            }
            while(1){
                if(p[pc]== pc) break;
                pc =p[pc];
            }
            if (pb ==pc) connected =1;
            
        }
    }
}