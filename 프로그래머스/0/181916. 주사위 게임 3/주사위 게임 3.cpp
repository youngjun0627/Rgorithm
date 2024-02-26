#include <array>
#include <algorithm>
#include <cmath>
using namespace std;

int solution(int a, int b, int c, int d) {
    if(a == b && b == c && c == d)
        return 1111 * a;
    array<int, 4> arr{a, b, c, d};
    sort(arr.begin(), arr.end());
    auto [p, q, r, s] = arr;
    if(p == q && r == s)
        return (q + r) * (r - q);
    if(q == r){
        if(p == q || r == s){
            int t = 11 * q + (p == q? s : p);
            return t * t;
        }
        else
            return p * s;
    }
    if(p == q || r == s)
        return p == q? r * s : p * q;
    return p;
}