using namespace std;
#include <iostream>
#include <stack>
#include <deque>

int main() {
    string text;
    cin >> text;
    string output;
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == '<') {
            output.pop_back();
        }
        else {
            output.push_back(text[i]);
        }
    }
    cout << output << endl;
    return 0;
}
