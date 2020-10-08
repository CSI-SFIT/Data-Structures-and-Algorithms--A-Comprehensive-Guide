#include <iostream>

using namespace std;

// funtion to print the elements of an array
void print(int array[5]){
	// iterating using the auto keyword
}

int main(){

	// defining and declaring an integer array of 5 elements
	int array[5] = {1,2,3,4,5};
	cout << "array = " ;
	for(auto element : array)
	{ 
		cout << element << " " ;
	}
	cout << endl << endl; //printing blank lines

	// defining an array and taking user input and inserting into an array
	int array2[5];
	cout << "Enter 5 elements" << endl;
	for(int i=0; i < 5; i++)
	{
		cin >> array2[i];
	}

	cout << "array2 = "
	for(auto element : array2)
	{ 
		cout << element << " " ;
	}
	cout << endl << endl; //printing blank lines

}
