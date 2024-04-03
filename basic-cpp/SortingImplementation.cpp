#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() { 
    vector<int> v = {4,2,5,3,5,8,3};
    // Sorting Increase
    sort(v.begin(),v.end());

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }

    // Sorting Decrease
    sort(v.rbegin(), v.rend());

    return 0;
}