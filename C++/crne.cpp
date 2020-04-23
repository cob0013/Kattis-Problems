using namespace std;
#include <iostream>
#include <math.h>
int main() {
    long n;
    cin >> n;
    long x = n/ 2;
    cout << (x + 1) * (n - x + 1) << endl;
    return 0;
}

//1-2, 3-6, 4 -8, 5 -16, 6-24, 7 -32, 8-40
