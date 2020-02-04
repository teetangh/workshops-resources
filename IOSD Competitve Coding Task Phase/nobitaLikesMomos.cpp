#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); //disabling c input and output functions
    cin.tie(NULL);                    //clearing stdout before taking any stdin
    int t, n, m, i, j, x, y, p = 0, q = 0, sum = 0, pos = 0, large = 0;
    cin >> t;
    for (i = 0; i < t; i++) //test cases
    {
        cin >> n >> m;
        int a[n];
        for (j = 0; j < n; j++)
        {
            cin >> a[j];
        }
        for (x = 0; x < n; x++) //selection sort
        {
            large = a[x];
            for (y = x + 1; y < n; y++)
            {
                if (a[y] > large)
                {
                    large = a[y];
                    pos = y;
                }
            }
            a[x] = large;
            a[pos] = a[x];
        }
        for (x = 0; x < n; x++)
        {
            sum = sum + a[x];
            if (sum >= m) //if momos exceed or not
            {
                q = x;
                p = 1; //flag to see if there are enough momos or not
                break;
            }
        }
        if (p == 1)
            cout << q + 1 << endl;
        else
            cout << -1 << endl;
        q = 0;
        p = 0;
        sum = 0;
        pos = 0;
    }
    return 0;
}