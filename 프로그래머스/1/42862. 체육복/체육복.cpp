#include <vector>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n;

    vector<int> uniform(n+2, 1);
    for(int i = 0; i < lost.size(); i++)
        uniform[lost[i]]--;
    for(int i = 0; i < reserve.size(); i++)
        uniform[reserve[i]]++;

    for(int i = 1; i < n+1; i++)
        if(uniform[i-1] == 0 && uniform[i] == 2) {
            uniform[i-1]++;
            uniform[i]--;
        } else if(uniform[i+1] == 0) {
            uniform[i]--;
            uniform[i+1]++;
        }

    for(int i = 1; i <= n; i++)
        if(uniform[i] == 0)
            answer--;

    return answer;
}