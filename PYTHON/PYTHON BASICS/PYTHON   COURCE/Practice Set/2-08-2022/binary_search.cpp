#include<iostream>
using namespace std;

int bineary_search(int arr[],int size,int key){

    int start = 0;
    int end = size - 1;
    // finding the mid position
    int mid = start + (end-start)/2;  // just because int take 2^32 -1 
    // max number if we add 2 int then size might be out of bound
    // thats why we will write formula like this.
    while(start<=end){
        if(key == arr[mid]){
            return mid;
            }

        if(key > arr[mid]){
            start = mid+1;
            }
        else{
            end = mid-1;
        }

        mid = start + (end-start)/2;
        
            }
    return -1;
    
}
int main(){
    int even[8] = {2,4,8,12,16,23,45,53};
    int odd[5] = {3,5,11,19,27};

    int evenIndex = bineary_search(even,8,23);

    cout<<"The index of 100 is : "<<evenIndex<<endl;


}