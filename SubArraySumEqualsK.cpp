#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k,c=0,s=0;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=0;i<n;i++){
        s=0;
        for(int j=i;j<n;j++){
            s+=arr[j];
            if(s==k){
                c+=1;
            }
        }
    }
    cout<<c;
}
