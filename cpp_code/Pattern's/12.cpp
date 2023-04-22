#include<iostream>
using namespace std;
int main(){
    int n=10;
    for(int row = 1; row<=n; row++){
        if(row == 1 || row == n){
            for(int clm = 1; clm<=row; clm++){
                cout<<clm<<" ";
            }
        }
        else{
            cout<<1<<" ";
            for(int clm = 2; clm < row;clm++){
                cout<<"  ";
            }
            cout<<row;
        }
        cout<<endl;
    }

}