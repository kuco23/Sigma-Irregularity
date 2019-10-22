#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <chrono>

using std::vector;
using namespace std::chrono;

std::random_device rd;

int getParent(vector<int> &parent, int i) {
    vector<int> to_rewire{};
    while (parent[i] != i) {
        i = parent[i];
        to_rewire.push_back(i);
    }
    for (const int &k : to_rewire)
        parent[k] = i;
    return i;
}

inline void joinComponents(
    vector<int> &parent, int c0, int c1
) {
    parent[c0] = c1;
}

vector<vector<int>> randomTree_kruskal(int n) {
    vector<int> parent(n);
    vector<int> ids(n * (n - 1) / 2);
    vector<vector<int>> G(n);
    
    int count = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            ids[count++] = i * n + j;
    std::shuffle(ids.begin(), ids.end(), rd);
    
    int i = 0, nedges = 0;
    while (nedges < n - 1) {
        int node0 = std::floor((double) ids[i] / n);
        int node1 = ids[i] % n;
        int component0 = getParent(parent, node0);
        int component1 = getParent(parent, node1);
        if (component0 != component1) {
            G[node0].push_back(node1);
            G[node1].push_back(node0);
            joinComponents(ids, component0, component1);
            nedges++;
        }
        i++;
    }

    return G;
}


int randint(int a, int b) {
   double r01 = std::rand() / RAND_MAX;
   return std::round(r01 * (b - a) + a);
}

vector<vector<int>> randomTree_simple(int n) {
    vector<vector<int>> G(n);
    vector<int> nodes(n);

    for (int i = 0; i < n; i++) 
        nodes[i] = i;
    std::shuffle(nodes.begin(), nodes.end(), rd);

    for (int i = 1; i < n; i++) {
        int j = nodes[i];
        int k = nodes[randint(0, i)];
        G[j].push_back(k);
        G[k].push_back(j);
    }

    return G;
}

int main() {
    auto current_time = std::chrono::system_clock::now();
    auto duration_in_seconds = std::chrono::duration<double>(current_time.time_since_epoch());
    double num_seconds = duration_in_seconds.count();
    std::srand(num_seconds);
    randomTree_simple(10);
    return 0;
}