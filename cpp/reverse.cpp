// Given an Integer N, write a program to reverse it
// Input: first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
// Output: Print the reversed integer N.


#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int rev=0;
        while(n>0){
            rev=rev*10+n%10;
            n=n/10;
        }
        cout<<rev<<endl;
    }
    return 0;
}





