#include <stdio.h>

int main(void) {
	int t,n,m,ans;
	scanf("%d",&t);
	for(; t>0; t--){
	    scanf("%d%d", &n, &m);
	    ans=(n*m)-(n+m)+1;
	    printf("%d\n", ans);
	}
	
	return 0;
}
