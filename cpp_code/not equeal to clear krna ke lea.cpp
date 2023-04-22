/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int a=10,b=20,c=30;
    int ans =(a!=b);
    cout<<" "<<a<<" "<<b<<endl;
    a=10;
    b=20;
    int ans =(a=!b);
    cout<<" "<<a<<" "<<b<<endl;
    int ans2=(a==b);
    cout<<ans<<endl;
    cout<<ans2<<endl;
    if((a<=b) && (a==b)){
        cout<<"1"<<endl;
    }
    else if((a<=b)||(c>=a)){
        cout<<"2";
    }
    else{
        cout<<"a";
    }

    return 0;
}
