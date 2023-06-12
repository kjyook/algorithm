#include <iostream>
using namespace std;

int pibo(int a){
    if(a==0)
        return 0;
    else if(a==1)
        return 1;
    else
        return pibo(a-1) + pibo (a-2);
}

int main(){
    int a = 0;
    int b =0;
    cin >> a;

    b = pibo(a);

    cout<< b;
}