#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <queue>

using std::pair;
using namespace std;

inline vector<int> range(const int &b) {
    vector<int> container (b);
    for (int i = 0; i < b; i++) container[i] = i;
    return container;
}

template <class T>
vector<pair<T, T>> combinations(vector<T> &base) {
    int n = base.size();
    vector<pair<T, T>> container {};
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            container.push_back(
                make_pair(base[i], base[j])
            );
    return container;
} 

bool isConnected(vector<vector<int>> &G) {
    int order = G.size();
    int count_marked = 0;
    vector<bool> marked(order);
    std::fill(marked.begin(), marked.end(), false);
    queue<int> q; q.push(0); marked[0] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (const int &v : G.at(u))
            if (!marked[v]) {
                q.push(v);
                marked[v] = true;
                count_marked++;
                if (count_marked == order)
                    return true;
            }
    }
    return false;
}

void brute_force (int order) {
    int max_size = order * (order - 1) / 2;
    pair<int, vector<vector<int>>> opt;
    for (int m = max_size; m < max_size; m++) {
    }
}