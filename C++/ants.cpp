#include <iostream>
using namespace std

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int l, ants;
        cin >> l >> ants;
        int ant;
        int latest = 0;
        int earliest = 0;
       for (int i = 0; i < ants; i++) {
            cin >> ant;
            earliest = max(earliest, min(l - ant, ant));
            latest = max(latest, max(l- ant, ant));
       } 
       cout << earliest << " " << latest << endl;
    }
    return 0;
}
