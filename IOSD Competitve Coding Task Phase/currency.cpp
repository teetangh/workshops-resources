#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, i, j = 0, rem;
    long int sum = 0, div;
    cin >> n;
    //scanf("%d",&n);
    long int a[n];
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
        //scanf("%ld",&a[i]);
    }
    for (i = 0; i < n; i++)
    {
        rem = a[i] % 100;
        div = a[i] / 100;
        while (rem > 0)
        {
            if (rem >= 50)
            {
                j++;
                rem = rem - 50;
            }
            else if (rem >= 10)
            {
                j++;
                rem = rem - 10;
            }
            else if (rem >= 5)
            {
                j++;
                rem = rem - 5;
            }
            else if (rem >= 2)
            {
                j++;
                rem = rem - 2;
            }
            else if (rem >= 1)
            {
                j++;
                rem = rem - 1;
            }
        }
        cout << (div + j) << endl;
        // printf("%ld\n",(div+j));
        j = 0;
    }
    return 0;
}
