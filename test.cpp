#include <iostream>
#include <random>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main() {
    unsigned seed = system_clock::now().time_since_epoch().count();
    std::default_random_engine generator(seed);
    std::uniform_int_distribution<int> distribution(1,6);
    for (int i = 0; i < 10; i++)
        cout << distribution(generator) << endl;
    getchar();
    return 0;
}