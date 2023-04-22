#include<iostream>
using namespace std;

void fun( int *ptr){
    *ptr = *ptr + 1 ;
cout<< " before" << ptr << endl;
    cout<< " before" << *ptr << endl;
}

int main(){
    int a=5;
    int *ptr = &a;
    int *ptr2;
    int *ptr3 = 0;

    cout << a << endl;
    cout << &a << endl;
    //cout << *a << endl; // give an error
    cout << ptr << endl;
    cout << &ptr << endl;
    cout << *ptr << endl;

    cout << " ptr2 " <<  &ptr2 << endl;
    cout << &ptr3 << endl;
    
    cout << " ------------------" << endl;
    cout<< " before" << ptr << endl;
    cout<< " before" << ptr << endl;

    fun( ptr);
    *ptr = *ptr+1;
    cout<< " before" << ptr << endl;
    cout<< " before" << *ptr << endl;

    cout<<" +++++++++++++++"<<endl;
    int arr[50] = {1,2,3,5,6,7,8};
    cout<<arr<<endl;
    cout<<&arr<<endl;
    cout<<*arr<<endl;
    cout<<arr[0]<<endl;

    *arr = *arr+1;
    cout<<arr<<endl;
    cout<<&arr<<endl;
    cout<<*arr<<endl;
    cout<<arr[0]<<endl;

    cout<<endl<<endl<<endl;
    cout<<*arr<<endl;
    cout<<*(arr+1)<<endl;
    cout<<*(arr+2)<<endl;
    cout<<*(arr+3)<<endl;
    cout<<*(arr+4)<<endl;
    cout<<endl<<endl<<endl;

    int i=0;
    cout<<i[arr]<<endl;
    i++;
    cout<<i[arr]<<endl;
    i++;
    cout<<i[arr]<<endl;
    i++;
    cout<<i[arr]<<endl;
    i++;
    cout<<i[arr]<<endl;
    
    


}