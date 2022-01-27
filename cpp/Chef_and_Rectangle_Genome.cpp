/**
https://www.codechef.com/problems/GERALD09

 Chef has an empty matrix of NxM. He wants to construct rectangle genome. 
 For this reason Chef should fill the matrix with letters G, С, A, T.
The genome will be stable if it contains K different submatrices.
Of course, Chef wants to make his genome as stable as possible, that is the difference 
between the number of different submatrices in genome and number K should be as small as possible.**/

/**
Input:
2
2 3 5
1 1 1

Output:
AAA
AAA
T
**/

#include<iostream>
int main(){

	// first line contains a single integer T, denoting the number of testcases

    int t;
    scanf("%d",&t);
    while(t--){
	// description of the testcase: three integers N, M, K
    int n, m,k;
    scanf("%d %d %d",&n,&m,&k);
	//loop for creating the matrix 
    for(int i=0;i<n;i++){
        for(int j= 0;j<m;j++)
		// if the difference between the number of different submatrices in 
		// genome and number is as small as possible.
            printf("A");
        printf("\n");
    }
    printf("\n");
    }
    return 0;
}