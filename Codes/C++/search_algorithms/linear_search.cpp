#include <iostream>

using namespace std;

// define the size of the array
int N = 10;

int main(){

	int arr[N];
	// input 10 elements for the array
	cout << "Enter " << N<< " elements of the array: " << endl;
	for(int i=0; i<N; i++){ cin >> arr[i]; }

	// input the element you want to search
	cout << "Enter the element you want to search: " ;
	int element; cin >> element;

	// linear search is the most naive approach to search for an element in an array
	// the time complexity of the linear search algorithm is O(n)
	// This is the most naive search approach and is ususually used when the array is not too huge
	// This can simply be achieved by iterating from the the first element to the last or vice versa
	
	for(int i=0; i<N; i++){
		if(arr[i] == element)
			cout << "Element exists in the array" << endl;
			return 0;
	}
	cout << "Element does not exist in the array" << endl;
}
