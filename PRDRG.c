#include <stdio.h>
#include <math.h>

int main(void) {
	long long int t, n, ans, i=0;
	long long int seq[100]={0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525, 699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941, 715827883, 1431655765, 2863311531, 5726623061};
	scanf("%lld", &t);
	
	while(i++<t){
	    
	    scanf("%lld", &n);
	    ans=pow(2, n);
	    printf("%lld %lld ", seq[n], ans);
	}
	return 0;
}
