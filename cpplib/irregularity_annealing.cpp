#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <random>
#include <chrono>

#define e std::exp(1.0);

using namespace std::chrono;
using std::vector;
using std::pair;
using std::pow;
using std::exp;

unsigned seed = system_clock::now().time_since_epoch().count();
std::default_random_engine generator(seed);
std::uniform_int_distribution<int> random_int(1, 1000);
std::uniform_real_distribution<double> random_real(0, 1);

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
        return (int) (sum / 2);
    }

    int sigma_t(vector<vector<int>> &G) {
        int n = G.size(), sum = 0;
        for (int i = 0; i < n; i++) {
            int m = (int) G[i].size();
            for (int j = 0; j < i; j++) {
                int diff = m - (int) G[j].size();
                sum += (int) pow(diff, 2);
            }
        }
        return sum;
    }

    double sigma_ratio(vector<vector<int>> &G) {
        int sG = sigma(G), sGt = sigma_t(G);
        return (sG > 0) ? (double) sGt / (double) sG : 1;
    }

}

double probability(int sigma_i, int sigma_c, double t) {
    return exp((sigma_i - sigma_c) / t);
}
double randint(int a, int b) {
    double ran01 = random_real(generator);
    return std::round(ran01 * (b - a) + a);
}

vector<vector<int>> randomGraph(int n, int m) 
{
    int lim = std::round(n * (n - 1) / 2);
    static vector<int> ids(lim);
    vector<vector<int>> neighbor_list(n);

    int p = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            ids[p++] = i * n + j; 

    std::shuffle(ids.begin(), ids.end(), generator);

    for (int i = 0; i < m; i++) {
        int id = ids[i];
        int enter_node = id % n;
        int exit_node = std::floor((double) id / n);
        neighbor_list[enter_node].push_back(exit_node);
        neighbor_list[exit_node].push_back(enter_node);
    }
    
    return neighbor_list;
}

pair<vector<vector<int>>, double>
simulateAnnealing(int n, int nsim) 
{
    int m_total = n * (n - 1) / 2;
    double G_ratio;

    vector<vector<int>> G;
    pair<vector<vector<int>>, double> bestG;
    pair<vector<vector<int>>, double> currG;

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
            ) > random_real(generator)
        ) {
            currG.first = G;
            currG.second = G_ratio;
        }
     }
    return bestG;
}

void graphRepr(vector<vector<int>> &G) {
    std::cout << "printing graph" << std::endl;
    for (const vector<int> &node : G) {
        for (const int &i : node) 
            std::cout << i << " ";
        std::cout << std::endl;
    }
    std::cout << "exit function" << std::endl;
}

using std::cout;
using std::endl;
int main() {
    auto p = simulateAnnealing(30, 100000);
    cout << p.second << endl;
    std::getchar();
    return 0;
}