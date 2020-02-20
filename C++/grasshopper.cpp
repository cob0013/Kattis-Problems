	#include<iostream>
	#include<queue>
	#include<vector>
	#include<set>
	using namespace std;

	bool inBounds(int r, int c, int i, int j) {
		return i < r && r >= 0 && c >= 0 && j < c;
	}

	int main() {
		pair<int, int> neighbors[8] = {{1, 2}, {2, 1}, {-1, 2}, {-1, -2}, {1, -2}, {2, -1}, {-2, -1}, {-2, 1}};

		int r, c, gr, gc, lr, lc;
		
		while (cin >> r && cin>> c && cin >> gr && cin >> gc && cin >> lr && cin >> lc) {

			int visited[r * c] = {0};
			visited[(gr - 1)  * c + gc - 1] = 0;	
			bool found = false;
			queue<pair<int, int>> q;
			q.push({gr - 1, gc - 1});
			while (!q.empty()) {
				int currR = q.front().first;
				int currC = q.front().second;	
				if (currR == lr - 1 && currC == lc - 1 ) {
					cout << visited[currR * c + currC] << endl;
					found = true;
					break;
				}
				q.pop();
				for (pair<int, int> neighbor: neighbors) {
					int deltar = neighbor.first;
					int deltac = neighbor.second;
					int nextr = currR + deltar;
					int nextc = currC + deltac;
					if (visited[nextr * c + nextc] == 0 && inBounds(r, c, nextr, nextc)) {
						q.push({nextr, nextc});
						visited[nextr * c + nextc] = visited[currR * c + currC] + 1;
					}
				}

			}
			if (!found) {
				cout << "impossible" << endl;	
			}

		}
		return 0;

	}
