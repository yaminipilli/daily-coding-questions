/*Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

solution:*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    int size;
    cin>>size;
    int arr[n];
    for(int i=0;i<size;i++)
    {cin>>arr[i];
    }
    sort(arr, arr+size);
    int min=1;

    for(int i=0; i<size; i++){
        if(arr[i]>min) break;
        if(arr[i]==min)
         min=min+1;
    }
    cout<<min;
    return 0;
}
