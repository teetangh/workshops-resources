#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t, q, i, j, x, k = 0, m, c = 0, odd = 0, even = 0, h, u, te, temp = 0;
    int s[100000], z[100000] = {0};
    cin >> t;
    for (i = 0; i < t; i++)
    {
        cin >> q;
        for (j = 0; j < q; j++)
        {
            cin >> x;
            s[k++] = x;
            z[s[k - 1]] = 1;
            for (m = 0; m < k; m++)
            {
                h = s[m] ^ x; //calculating XOR
                if (z[h] != 1 && s[m] != x)
                {
                    s[k++] = h;
                    z[s[k - 1]] = 1;
                }
            }
            for (u = 0; u < k; u++) //checking no. of 1's
            {
                c = 0;
                temp = s[u];
                while (temp)
                {
                    temp = temp & (temp - 1);
                    c++;
                }
                if (c % 2 == 0)
                    even++;
                else
                    odd++;
            }
            cout << even << ' ' << odd << endl;
            even = 0;
            odd = 0;
            c = 0;
        }
        for (te = 0; te < k; te++) //Resetting Values
        {
            z[s[te]] = 0;
        }
        k = 0;
    }
    return 0;
}
