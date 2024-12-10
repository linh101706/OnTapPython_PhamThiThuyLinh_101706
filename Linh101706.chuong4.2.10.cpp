#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <string>
using namespace std;
vector<int> taoMangCongDon(const string& s, char c) {
    int n = s.size();
    vector<int> prefix(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefix[i] = prefix[i - 1] + (s[i - 1] == c ? 1 : 0);
    }
    return prefix;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;

    map<char, vector<int>> prefixArrays;
    for (char c : s) {
        if (prefixArrays.find(c) == prefixArrays.end()) {
            prefixArrays[c] = taoMangCongDon(s, c);
        }
    }

    vector<tuple<int, int, char>> queries;
    for (int i = 0; i < q; ++i) {
        int trai, phai;
        char c;
        cin >> trai >> phai >> c;
        queries.emplace_back(trai - 1, phai - 1, c); 
    }

    for (const auto& query : queries) {
        int trai, phai;
        char c;
        tie(trai, phai, c) = query;
        
        if (prefixArrays.find(c) != prefixArrays.end()) {
            const vector<int>& prefix = prefixArrays[c];
            cout << prefix[phai + 1] - prefix[trai] << "\n";
        } else {
            cout << 0 << "\n"; 
        }
    }

    return 0;
}
