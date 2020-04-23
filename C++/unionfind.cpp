#include <iostream>
#include <string>
using namespace std;

int _find(int child, int parents[]) {
    if (parents[child] == child) {
        return child;
    }
    parents[child] = _find(parents[child], parents);
    return parents[child];
}

void _union(int x, int y, int parents[]) {
    parents[_find(x, parents)] = parents[_find(y, parents)];
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, Q;
    cin >> N >> Q;
    int parents[N];
    for (int i = 0; i < N; i++) {
        parents[i] = i;
    }
    for (int i = 0; i < Q; i++) {
        string action;
        int x, y;
        cin >> action >> x >> y;
        if (action.compare("?") == 0) {
            int parentX = _find(x, parents);
            int parentY = _find(y, parents);
            if (parentX == parentY) {
                cout << "yes\n";
            }
            else {
                cout << "no\n";
            }
        }
        else {
            _union(x, y, parents);
        }
    }
}
