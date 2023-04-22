#include<iostream>
using namespace std;

void  print_array(int arr[], int n){
    for(int x=0; x<n;x++){
        cout<<arr[x]<<" ";
    }
    cout<<endl;
}


void swap(int arr[], int n){
    for(int x=0; x<n;x=x+2){
        swap(arr[x], arr[x+1]);
    }
}



int main(){
    int arr[10]={1,2,3,4,5,6};
    print_array(arr,6);
    swap(arr,6);
    print_array(arr,6);
}