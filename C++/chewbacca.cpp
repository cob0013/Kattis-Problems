using namespace std;
#include <iostream>
int main() {
    long long   n, k, q;
    cin >> n >> k >> q;
    long long sync = k - 2;
    for (long long i = 0; i < q; i++) {
        long long  u, v;
        cin >> u >> v;
        long long moves = 0;
        while (u != v) {
             moves++;
             if (v > u) {
                swap(u, v);
             }
             u = (u + sync) / k;       
        }
        cout << moves << endl;
    }
    return 0;
}
