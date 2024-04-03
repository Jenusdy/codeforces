#include <iostream> 
using namespace std;

int main() {
    int nilai[5] = {1,5,1,2,3};
    int arrayLength = sizeof(nilai)/sizeof(int);

    // Print Array 
    cout << "Array Sebelum di Sorting" << endl;
    for (int i = 0; i < arrayLength; i++) {
        cout << nilai[i] << " ";
    }

    // Sorting Data 
    for (int i = 0; i < arrayLength; i++) {
        for (int j = 0; j < arrayLength - 1; j++){
            if (nilai[j] > nilai[j+1]) {
                swap(nilai[j], nilai[j+1]);
            }
        }
    }
    
    // Print Array 
    cout << "Array Sesudah di Sotring" << endl;
    for (int i = 0; i < arrayLength; i++) {
        cout << nilai[i] << " ";
    }

}