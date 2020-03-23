#include <iostream>
using namespace std;

int main()
{
    int vertices;
    int edges;

    cin >> vertices >> edges;

    int graph[100][100];
    int v1, v2;

    for (int j = 0; j < edges; j++)
    {
        cin >> v1 >> v2;
        graph[v1][v2] = 1;
        graph[v2][v1] = 1;
    }

    for (int i = 0; i < vertices; i++)
    {
        for (int j = 0; j < vertices; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}