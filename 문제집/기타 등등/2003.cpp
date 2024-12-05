#include <iostream>
#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

int main(){
    int A[10000] = {0};
    int n, m;
    
    cin >> n>>m;

    for(int i =0; i<n; i++){
        scanf("%d",&A[i]);
    }

    int count = 0;
    int index = 0;

    while(true){
        int sum = 0;
        for (int k = index; k<=n; k++){
            sum += A[k];
        
            if(sum == m){
                count++;
                index++;
                break;
            }
            else if(sum > m){
                index++;
                break;
            }
            else if(k<n-1){
                k++;
            }
            else{
                break;
            }
        }
    }

    cout<<count;
}