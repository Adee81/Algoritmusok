## Kommandó feladat megoldása

### Megoldás lépései

Ezt a feladatot C++ 14 nyelven oldottam meg. 

#### Convex Hull Trick

Mivel a feladat során számos lineáris függvényt kell kezelni, amelyek a harci hatékonyságot ábrázolják különböző katonai csoportokhoz, a CHT segít hatékonyan megtalálni a legjobb vonalat (egyenletet) egy adott pontban. Ezáltal jelentősen gyorsíthatjuk a dinamikus programozási megoldást.

## Struktúra és osztályok

### Line struktúra

Ez a struktúra egyenleteket (vonalakat) reprezentál, amelyek lejtést (slope) és y-metszetet (intercept) tartalmaznak.

```cpp
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
```

### ConvexHullTrick osztály

Ez az osztály tartalmazza a CHT algoritmust, amely hozzáad egy új vonalat és kiválasztja a legjobb vonalat egy adott x értékhez.

```cpp
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
```

### Dinamikus programozás

A maximalis_hatekonysag függvény a maximumra optimalizálja a módosított hatékonyságot a következő lépések alapján:

- Prefix összegek kiszámítása.
- Dinamikus programozási tömb inicializálása.
- A konvex burkoló trükk (CHT) használata az optimalizáláshoz.

```cpp
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
```

### Main függvény

A main függvény beolvassa a bemeneti adatokat, meghívja a dinamikus programozási függvényt, és kiírja az eredményeket.

```cpp
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
```
