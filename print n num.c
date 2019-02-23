#include <stdio.h>
int main()
{
	int b[8],j,m,sum=0;
    int avg;
	scanf("%d",&m);
	for(j=0;j<m;j++)
	{
	    scanf("%d",&b[j]);
	}
	for(j=0;j<m;j++)
	{
	    sum+=b[j];
	}
    avg=sum/m;
	printf("%d",avg);
	return 0;
}
