using namespace std;
#include <iostream>
#include <string>
#include <map>


//brute af but passed
int main() {
        map<string, int> prefixCount;
        int n;
        string word;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> word;
            if (prefixCount.count(word)) {
                cout << prefixCount[word] << endl;
            }
            else {
                cout << 0 << endl;
            }
            for (int i = 0; i < word.length(); i++) {
                    string prefix = word.substr(0, i + 1);
                    if (prefixCount.count(prefix)) {
                        prefixCount[prefix] = prefixCount[prefix] + 1;
                    }
                    else {
                        prefixCount[prefix] = 1;
                    }
            }
        }
    return 0;

}
