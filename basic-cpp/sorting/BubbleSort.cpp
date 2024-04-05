#include <iostream>

using namespace std;

void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
            }
        }
    }
}

int main() {
    int arrayInteger[] = {1, 651, 1, 1, 5, 23, 1234, 61, 435, 67, 8, 1, 6, 73, 6};
    int n = sizeof(arrayInteger) / sizeof(int);
    bubbleSort(arrayInteger, n);

    for (int i = 0; i < n; i++) {
        cout << arrayInteger[i] << " ";
    }
}