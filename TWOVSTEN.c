#include <stdio.h>

int main(void) {
	int t, x, ans;
	scanf("%d", &t);
	while(t--){
	    scanf("%d", &x);
	    ans=-1;
	    if((x)==0){
	        ans=0;
	    }
	    else if(x==5){
	        ans=1;
	    }
	    printf("%d\n", ans);
	}
	return 0;
}

