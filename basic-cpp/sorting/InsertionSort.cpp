#include <iostream>
using namespace std;

void insertionSort(int a[], int n) {
    for (int i = 0; i < n; ++i) {
        int value = a[i];
        int hole = i;

        while (hole > 0 && a[hole-1] > value) {
            a[hole] = a[hole-1];
            hole = hole-1;
        }
        a[hole] = value;
    }
}

int main() {
    int arrayInteger[] = {1,2,5,1,45,1,5,6,16,66};
    int n = sizeof(arrayInteger)/sizeof(int);
    insertionSort(arrayInteger, n);
    for (int i = 0; i < n; ++i) {
        cout << arrayInteger[i] << " ";
    }
}