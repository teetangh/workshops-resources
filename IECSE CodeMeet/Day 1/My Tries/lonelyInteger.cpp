#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int *arr = new int[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    for (int i = 0; i < n; i++)
        cout << arr[i];

    int tempProduct = 1;
    int state = 1;

    for (int i = 0; i < n; i++)
    {
        tempProduct ^= arr[i];
        if (tempProduct == 1 && state == 1)
        {
            continue;
        }
        else if (state == 1 && tempProduct == 0)
        {
            state = 2;
        }
        else if (state == 2 && tempProduct == 1)
        {
            cout << arr[i];
        }
    }
}