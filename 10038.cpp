#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    int n;
    while (std::cin >> n) {
        std::vector<int> v(n, 0);
        for (int i = 0; i < n; ++i)
            std::cin >> v[i];
        std::vector<bool> check(n - 1, false);
        for (std::size_t i = 0; i < v.size() - 1; ++i) {
            int idx = abs(v[i] - v[i + 1]) - 1;
            if (idx < 0 || idx >= n)
                break;
            check[idx] = true;
        }
        if (std::any_of(check.begin(), check.end(), [](bool b) { return !b; }))
            std::cout << "Not jolly";
        else
            std::cout << "Jolly";
        std::cout << std::endl;
    }
    return 0;
}
