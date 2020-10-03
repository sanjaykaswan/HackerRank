#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <array>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    int a[n];
    for (int i=0; i < n; i++) {
        cin>>a[i];
    }  
    int b[n];
    for(int k = 0;k<n;k++){
        b[k] = a[k];
    }
    
    int j;
    j = n - 1;
    for(int l = 0;l<n;l++){
        a[l] = b[j];
        j = j -1; 
    }
    for(int t =0;t<n ; t++){
        cout<<a[t]<<" ";
    }
    return 0;
}