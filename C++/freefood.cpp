using namespace std;
#include <iostream>
#include <set>
int main() 
{
	int n, s, t;
	cin >> n;
	set<int> days;
	for (int i = 0; i < n; i++) {
		cin >> s >> t;
		for (int j = s; j <= t; j++) {
			days.insert(j);
		}
	}
	cout << days.size() << endl;
	return 0;
}	
