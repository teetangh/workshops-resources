#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long int t;
    cin >> t;

    while (t--)
    {
        long int n;
        cin >> n;
        long int j = 0;
        long int count = 0;
        while (n)
        {
            if (n & 1)
            {
                count = count + pow(2, j);
            }
            j++;
            n = n >> 1;
        }
        cout << count << endl;
    }
}