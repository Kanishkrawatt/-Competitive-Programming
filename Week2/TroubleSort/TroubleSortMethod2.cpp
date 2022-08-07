#include <bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin >> T; 

    for(int tcase = 1; tcase < T+1; tcase++){ 
        int n,i;
        int num;
        cin >> n;
        vector<int> arr;
        cout <<"Insert Elements"<<endl;
        for(i=0;i<n;i++){
            cout<< "arr["<<i<<"] : ";
            cin>>num;
            arr.push_back(num);
        }
        cout << "ARRAY : ";
        for(i=0;i<n;i++){
            cout << arr[i]<<" ";
        }
        cout<<endl;
        vector<int> odd,even;
        for(i=0;i<n;i++){
            if(i%2==0){
                even.push_back(arr[i]);
            }
            else{
                odd.push_back(arr[i]);
            }
        }

        sort(odd.begin(),odd.end());
        sort(even.begin(),even.end());
        vector<int> Tarr;
        for(i=0;i<n;i++){
            if(i%2==0){
                Tarr.push_back(even[0]);
                even.erase(even.begin());
            }
            else{
                Tarr.push_back(odd[0]);
                odd.erase(odd.begin());
            }
        }
        cout <<"ARRAY : ";
        for(i=0;i<n;i++){
            cout << Tarr[i]<<" ";
        }
        cout<<endl;

        int flag =-1;
        for(i=0;i<n-1;i++){
            if(Tarr[i]>Tarr[i+1]){
                flag = i;
                break;
            }
        }
        if(flag == -1)
                cout << "Case #" << tcase << ": OK\n";
        else 
                cout << "Case #" << tcase << ": " << flag << "\n";
    }
}