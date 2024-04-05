#include <iostream>

using namespace std;

void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int indexMin = i;
        for (int j = i + 1; j < n; j++) {
            if (a[indexMin] > a[j]) {
                indexMin = j;
            }
        }
        int temp = a[i];
        a[i] = a[indexMin];
        a[indexMin] = temp;
    }
}

int main() {
    int intArray[] = {1, 5, 12, 4, 5, 1, 3, 41, 12, 23};
    int n = sizeof(intArray) / sizeof(int);
    selectionSort(intArray, n);
    for (int i = 0; i < n; i++) {
        cout << intArray[i] << " ";
    }
}
