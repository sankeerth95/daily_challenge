#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class UnionFind {
public:
    explicit UnionFind(int n) : parent(n), component_size(n, 1), components(n) {
        iota(parent.begin(), parent.end(), 0);
    }

    int root(int value) {
        if (parent[value] != value) {
            parent[value] = root(parent[value]);
        }
        return parent[value];
    }

    bool unite(int first, int second) {
        int first_root = root(first);
        int second_root = root(second);
        if (first_root == second_root) {
            return false;
        }

        if (component_size[first_root] < component_size[second_root]) {
            swap(first_root, second_root);
        }

        parent[second_root] = first_root;
        component_size[first_root] += component_size[second_root];
        --components;
        return true;
    }

    int num_components() const {
        return components;
    }

private:
    vector<int> parent;
    vector<int> component_size;
    int components;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);
    int max_a = 0;
    for (int& value : a) {
        cin >> value;
        max_a = max(max_a, value);
    }

    UnionFind clusters(n);
    long long answer = 0;

    vector<int> index_of(max_a + 1, -1);
    for (int index = 0; index < n; ++index) {
        index_of[a[index]] = index;
    }

    for (int divisor = max_a; divisor >= 1; --divisor) {
        int representative = -1;
        for (int multiple = divisor; multiple <= max_a; multiple += divisor) {
            int index = index_of[multiple];
            if (index == -1) {
                continue;
            }

            if (representative == -1) {
                representative = index;
            } else if (clusters.unite(representative, index)) {
                answer += divisor;
                if (clusters.num_components() == 1) {
                    cout << answer << '\n';
                    return 0;
                }
            }
        }
    }

    cout << answer << '\n';
    return 0;
}
