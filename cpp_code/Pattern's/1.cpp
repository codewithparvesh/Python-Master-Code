#include <iostream>
using namespace std;

int main()
{
    int x = 5;

    // loogic for pattern
    for (int n = 0; n < x; n++)
    {
        for (int p = 0; p < x; p++)
        {
            if (p <= n)
            {
                cout << "*";
            }
        }
        cout << endl;
    }
}