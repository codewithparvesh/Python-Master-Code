#include<iostream>
using namespace std;
int main(){
    int n=10;
    for(int row=1;row<=n;row++){
        // for each row

        // for sapce
        for(int clm=1; clm<=(n-row); clm++){
            cout<<" ";
        }

        // for star
        for(int clm = 1; clm<=row;clm++){
            cout<<"* ";
        }
        //after each row
        cout<<endl;
    }
}
