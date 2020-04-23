using namespace std;
#include <iostream>
#include <math.h>

int count(int n) {
    int output = 0; 
    while (n % 2 == 0) {
         output ++;    
         n /= 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            output++;
            n /= i;
        }
    }
    if (n > 2) {
        output++;
    }
    return output;
}
int main() {
    int n;
    cin >> n;
    cout << count(n) << endl;
    return 0;
}

