#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <random>
#include <ctime>
#include <stdlib.h>
#include <utility>

#define e std::exp(1.0);

using std::vector;
using std::pow;

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_real_distribution<double> real_dis(0, 1);
std::uniform_int_distribution<int> int_dis;

namespace base_defs {

    int sigma(vector<vector<int>> &G) {
        int n = G.size(), sum = 0;
        for (int i = 0; i < n; i++) {
            int m = (int) G[i].size();
            for (int j = 0; j < m; j++) {
                int diff = m - (int) G[j].size();
                sum += (int) pow(diff, 2);
            }
        }
        return (int) sum / 2;
    }

    int sigma_t(vector<vector<int>> &G) {
        int n = G.size(), sum = 0;
        for (int i = 0; i < n; i++) {
            int m = (int) G[i].size();
            for (int j = 0; j < n; j++) {
                int diff = m - (int) G[j].size();
                sum += (int) pow(diff, 2);
            }
        }
        return (int) sum / 2;
    }

    int sigma_ratio(vector<vector<int>> &G) {
        int sG = sigma(G), sGt = sigma_t(G);
        return (sG > 0) ? sGt / sG : 1;
    }

}

double probability(int sigma_i, int sigma_c, double t) {
    return std::exp((sigma_i - sigma_c) / t);
}
double random01() {
    return (double) real_dis(gen);
}
double randint(int a, int b) {
    return std::round(random01() * (b - a) + a);
}

vector<vector<int>> randomGraph(int n, int m) 
{
    int lim = std::round(n * (n - 1) / 2);

    std::random_device rd;
    static vector<int> ids(lim);
    vector<vector<int>> neighbor_list(n);

    int p = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            ids[p++] = i * n + j; 

    std::shuffle(ids.begin(), ids.end(), rd);

    for (int i = 0; i < m; i++) {
        int id = ids[i];
        int enter_node = id % n;
        int exit_node = std::floor((double) id / n);
        neighbor_list[enter_node].push_back(exit_node);
        neighbor_list[exit_node].push_back(enter_node);
    }
    
    return neighbor_list;
}

std::pair<vector<vector<int>>, int>
annealing(int n, int nsim) 
{
    int m_total = n * (n - 1) / 2;
    int G_ratio;

    vector<vector<int>> G;
    std::pair<vector<vector<int>>, int> bestG;
    std::pair<vector<vector<int>>, int> currG;

    G = randomGraph(n, 2 * n);
    G_ratio = base_defs::sigma_ratio(G);
    bestG = std::make_pair(G, G_ratio);
    currG = std::make_pair(G, G_ratio);

    for (int i = 2; i < nsim + 2; i++) {
        double temp = 1 / std::log(i);
        G = randomGraph(n, randint(1, m_total-1));
        G_ratio = base_defs::sigma_ratio(G);

        if (G_ratio >= currG.second) {
            currG.first = G;
            currG.second = G_ratio;
            if (G_ratio >= bestG.second) {
                bestG.first = G;
                bestG.second = G_ratio;
            }
        } else if (
            probability(
                G_ratio, 
                currG.second, 
                temp
            ) > random01()
        ) {
            currG.first = G;
            currG.second = G_ratio;
        }
     }
    return bestG;
}

void graphRepr(vector<vector<int>> &G) {
    std::cout << "printing graph" << std::endl;
    for (vector<int> &node : G) {
        for (int &i : node) 
            std::cout << i << " ";
        std::cout << std::endl;
    }
    std::cout << "exit function" << std::endl;
}

int main() {
    std::pair<vector<vector<int>>, int> s = annealing(30, 10000);
    std::cout << s.second << std::endl;
    std::getchar();
    return 0;
}