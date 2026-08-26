#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {
        return 0;
    }

    unordered_map<string, long long> sv;
    for (int i = 0; i < n; ++i) {
        string s;
        long long v;
        cin >> s >> v;
        sv[s] = v;
    }


    // qsum[11][11][11][11][11][11]
    static long long qsum[11][11][11][11][11][11]{0};

    for (int sm = 6; sm <= 60; ++sm) {
        for (int i0 = 1; i0 < 11; ++i0) {
            for (int i1 = 1; i1 < 11; ++i1) {
                for (int i2 = 1; i2 < 11; ++i2) {
                    for (int i3 = 1; i3 < 11; ++i3) {
                        for (int i4 = 1; i4 < 11; ++i4) {


                            int i5 = sm-i0-i1-i2-i3-i4;
                            if(i5 < 1 || i5 > 10) continue;

                            long long total = 0;
                            for (int a0 = 0; a0 < 2; ++a0) {
                                for (int a1 = 0; a1 < 2; ++a1) {
                                    for (int a2 = 0; a2 < 2; ++a2) {
                                        for (int a3 = 0; a3 < 2; ++a3) {
                                            for (int a4 = 0; a4 < 2; ++a4) {
                                                for (int a5 = 0; a5 < 2; ++a5) {

                                                    // if(a0==0&&a1==0&&a2==0&&a3==0&&a4==0&&a5==0) continue;
                                                    int sign = -1 * (2 * a0 - 1) *
                                                                (2 * a1 - 1) *
                                                                (2 * a2 - 1) *
                                                                (2 * a3 - 1) *
                                                                (2 * a4 - 1) *
                                                                (2 * a5 - 1);
                                                    total += sign * qsum[i0-a0][i1-a1][i2-a2][i3-a3][i4-a4][i5-a5];
                                                }
                                            }
                                        }
                                    }
                                }
                            }

                            string key = to_string(i0 - 1) + to_string(i1 - 1) +
                                            to_string(i2 - 1) + to_string(i3 - 1) +
                                            to_string(i4 - 1) + to_string(i5 - 1);
                            auto it = sv.find(key);
                            qsum[i0][i1][i2][i3][i4][i5] = total + (it == sv.end() ? 0 : it->second);
                            
                        }
                    }
                }
            }
        }
    }

    int queries;
    cin >> queries;

    for (int query = 0; query < queries; ++query) {
        string x, y;
        cin >> x >> y;

        array<array<int, 6>, 2> u{};
        for (int dimension = 0; dimension < 6; ++dimension) {
            u[0][dimension] = x[dimension] - '0';
            u[1][dimension] = y[dimension] - '0' + 1;
        }

        bool invalid=false;
        for (int dimension = 0; dimension < 6; ++dimension)
            if (u[0][dimension] > u[1][dimension]) invalid=true;

        long long answer = 0;

        if(!invalid){

            for (int a0 = 0; a0 < 2; ++a0) {
                for (int a1 = 0; a1 < 2; ++a1) {
                    for (int a2 = 0; a2 < 2; ++a2) {
                        for (int a3 = 0; a3 < 2; ++a3) {
                            for (int a4 = 0; a4 < 2; ++a4) {
                                for (int a5 = 0; a5 < 2; ++a5) {
                                    int sign = (2 * a0 - 1) * (2 * a1 - 1) *
                                            (2 * a2 - 1) * (2 * a3 - 1) *
                                            (2 * a4 - 1) * (2 * a5 - 1);
                                    answer += sign * qsum[u[a0][0]][u[a1][1]][u[a2][2]][u[a3][3]][u[a4][4]][u[a5][5]];
                                }
                            }
                        }
                    }
                }
            }

        }
        cout << answer << '\n';
    }

    return 0;
}