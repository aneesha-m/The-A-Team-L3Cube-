#include<iostream>
#include<stdio.h>

using namespace std;

double paradox(double i)
{
    double p=1;
    double j;
    for (j=1;j<i;j++) 
	{
	      p *= (365.0 - j) / 365.0;
   	}
	return p;
}



int main ()
{
	double i,n;
	double result;
	cout<<"Enter the number of people in the room";
	cin>>n;
	for(i=3;i<n;i++)
	{
		result=paradox(i);
		printf("for %f people, probability is %.4f\n", i, 1 - result);
	}
return 0;
}


