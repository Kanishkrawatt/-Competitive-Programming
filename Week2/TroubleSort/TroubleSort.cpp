#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,i;
    vector<int> arr;
    cin >> n;
    int num;
    cout << "Array"<<endl;
    for(i = 0;i<n;i++){
        cout << "arr[" << i<<"] : ";
        cin>>num;
        arr.push_back(num);
    }
    cout << "ARRAY : ";
    for(i=0;i<n;i++){
        cout << arr[i] <<" ";
    }
    int done = false;
    while (!done){
        done = true;
        for(i=0;i<n-2;i++){
            if(arr[i]>arr[i+2]){
                done = false;
                int temp = arr[i];
                arr[i] = arr[i+2];
                arr[i+2] = temp;
            }

        }
    }
    cout << "\nARRAY : ";

    for(i=0;i<n;i++){
        cout << arr[i] <<" ";
    }
    if(is_sorted(arr.begin(),arr.end())){
        cout<<"\nOK";
    }
    else{
        cout<<"\nNO OK";
    }
    

}