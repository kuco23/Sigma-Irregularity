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
    return (double) std::rand() / RAND_MAX;
}

vector<vector<int>> randomGraph(int n, int m) {
    std::random_device rd;
    std::mt19937 generator(rd());

    vector<vector<int>> neighbor_list(n);

    vector<int> sample1{};
    vector<int> sample2{};
    for (int i = 0; i < n; i++) {
        sample1.push_back(i);
        sample2.push_back(i);
    }
 
    std::shuffle(
        sample1.begin(), sample1.end(), rd
    );
    std::shuffle(
        sample2.begin(), sample2.end(), rd
    );

    for (int i : sample1)
        for (int j : sample2)
            if (j < i) {
                neighbor_list[j].push_back(i);
                neighbor_list[i].push_back(j);
            }
    
    return neighbor_list;
}

std::pair<vector<vector<int>>, int>
annealing(int n, int nsim) 
{
    std::random_device rd;
    std::mt19937 generator(rd());

    vector<vector<int>> G;
    std::pair<vector<vector<int>>, int> bestG;
    std::pair<vector<vector<int>>, int> currG;
    int m_total = n * (n - 1) / 2;

    std::uniform_int_distribution<std::mt19937::result_type> 
    distr(1, m_total-1);

    G = randomGraph(n, 2 * n);
    int G_ratio = base_defs::sigma_ratio(G);
    bestG = std::make_pair(G, G_ratio);
    currG = std::make_pair(G, G_ratio);

    for (int i = 2; i < nsim + 2; i ++) {
        double temp = 1 / std::log(i);
        G = randomGraph(n, distr(generator));
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

int main() {
    std::srand(std::time(0));
    vector<vector<int>> G = {
        {1, 2, 3}, 
        {0, 4},
        {0, 4, 3},
        {0, 4, 2},
        {1, 2, 3}
    };
    std::pair<vector<vector<int>>, int> s = annealing(100, 100);
    std::cout << s.second << std::endl;
    std::getchar();
    return 0;
}