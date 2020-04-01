using namespace std;
#include <iostream>
#include <string>
#include <utility>
#include<bits/stdc++.h> 

int main() {
	char board[5][5];
	int X[8] = { 2, 1, -1, -2, -2, -1, 1, 2 }; 
	int Y[8] = { 1, 2, 2, 1, -1, -2, -2, -1 };
	vector<pair<int, int>> knights;
	for (int i = 0; i < 5; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 5; j++) {
			if (s[j] == 'k') {
			knights.push_back(make_pair(i, j));
			}	
			board[i][j] = s[j];
		}
	}
	if (knights.size() != 9) {
		cout << "invalid\n";
		return 0;
	}
	for (auto k : knights) {
		int r = k.first;
		int c = k.second;
		for (int i = 0; i < 8; i ++) {
			int newr = r + X[i];
			int newc = c + Y[i];
			if (newr >= 0 && newc >= 0 && newr < 5 && newc < 5 && board[newr][newc] == 'k') {
				cout << "invalid\n";
				return 0;
			}
			}
		}
	
	cout << "valid\n";
	return 0;
}
