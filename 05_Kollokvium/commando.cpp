#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <deque>

using namespace std;

struct Line {
    long long slope;
    long long intercept;
    double xLeft;
    
    Line(long long slope, long long intercept, double xLeft = -numeric_limits<double>::infinity()) :
        slope(slope), intercept(intercept), xLeft(xLeft) {}
    
    bool operator < (const Line& other) const {
        return slope < other.slope;
    }
    
    double intersectionX(const Line& other) const {
        return double(other.intercept - intercept) / (slope - other.slope);
    }
};

class ConvexHullTrick {
private:
    deque<Line> hull;
    
public:
    void addLine(long long slope, long long intercept) {
        Line newLine(slope, intercept);
        while (!hull.empty() && hull.back().intersectionX(newLine) <= hull.back().xLeft) {
            hull.pop_back();
        }
        if (!hull.empty()) {
            newLine.xLeft = hull.back().intersectionX(newLine);
        }
        hull.push_back(newLine);
    }
    
    long long getBest(long long x) {
        while (hull.size() > 1 && hull[1].xLeft <= x) {
            hull.pop_front();
        }
        return hull.front().slope * x + hull.front().intercept;
    }
};

long long maximalis_hatekonysag(int n, int a, int b, int c, const vector<int>& hatekonysag) {
    vector<long long> prefix_sum(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefix_sum[i] = prefix_sum[i - 1] + hatekonysag[i - 1];
    }
    
    vector<long long> dp(n + 1, numeric_limits<long long>::min());
    dp[0] = 0;
    
    ConvexHullTrick cht;
    cht.addLine(0, 0);
    
    for (int i = 1; i <= n; ++i) {
        long long xi = prefix_sum[i];
        dp[i] = a * xi * xi + b * xi + c + cht.getBest(xi);
        cht.addLine(-2 * a * xi, dp[i] + a * xi * xi - b * xi);
    }
    
    return dp[n];
}

int main() {
    int T;
    cin >> T;
    
    vector<long long> eredmenyek(T);
    
    for (int t = 0; t < T; ++t) {
        int n, a, b, c;
        cin >> n >> a >> b >> c;
        
        vector<int> hatekonysag(n);
        for (int i = 0; i < n; ++i) {
            cin >> hatekonysag[i];
        }
        
        eredmenyek[t] = maximalis_hatekonysag(n, a, b, c, hatekonysag);
    }
    
    for (const long long& eredmeny : eredmenyek) {
        cout << eredmeny << endl;
    }
    
    return 0;
}