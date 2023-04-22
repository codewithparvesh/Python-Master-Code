#include<iostream>
using namespace std;
int main(){
    int n=10;
    for(int row=1;row<=n;row++){
        // for each row
        // star
        if(row==1 || row==n){
            for(int clm = 1; clm <= (n-row+1); clm++){
                cout<<"*";
            }
        }
        else{
            cout<<"*";
        
        // for sapce
        for(int clm=1; clm<=(n-row-1); clm++){
            cout<<" ";
        }

        // for star
            cout<<"* ";
        //after each row
        }
        cout<<endl;
    }
}
