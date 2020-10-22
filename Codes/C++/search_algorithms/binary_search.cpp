#include <iostream>

using namespace std;

// size of array
int N = 10;

int binary_search(int arr[], int low, int up, int x)
{
    while (low <= up) {
        int middle = low + (up - low) / 2;

        // Check if x is present at mid
        if (arr[middle] == x)
            return middle;

        // If x greater, ignore left half
        if (arr[middle] < x)
            low = middle + 1;

        // If x is smaller, ignore right half
        else
            up = middle - 1;
    }

    // if we reach here, then element was
    // not present
    return -1;
}


int main(){
	int arr[N] = {1,2,5,25,35,67,87,88,90,100};


	for(auto e: arr){ cout << e << " " ;} 
	// input the element
	cout << endl;
	cout << "Enter the element you want to search for: " ;
	int element; cin >> element;
	int found =	binary_search(arr,0,N-1,element);
	found!=-1 ? cout << "Element exists" << endl : cout << "Element does not exist in the array" << endl;
}
