using namespace std;
#include <iostream>
#include <string>
#include <stack>
int main() {
        int n;
        cin >> n;
        while (n--) {
            int k, p, q;
            char f;
            cin >> k >> p >> f >> q;
            stack <string> path;
            while (p != 1 || q != 1) {
                //right 
                if (p > q) {
                    path.push("R");  
                    p-= q; 
                }
                else {
                    path.push("L");
                    q -= p;
                }
            }
            
            int num = 1;
            while (!path.empty()) {
                string direction = path.top();
                path.pop();
                if (direction.compare("L") == 0) {
                    num *= 2;
                }
                else {
                    num = num * 2 + 1;
                }
            }
            cout << k << " " << num << endl;
        }
    return 0;
}
