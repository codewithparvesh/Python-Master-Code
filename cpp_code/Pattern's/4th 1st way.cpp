#include <iostream>
using namespace std;

int main()
{
    int n = 5;

    // loogic for pattern
    for (int row = 1; row <= n; row++)
    {
        // for each row
        for (int col = 1; col <= n; col++)
        {
            // space
            if (col < row)
            {
                cout << " ";
            }
            // star
            else
            {
                cout << "*";
            }
        }
        // after each row
        cout << endl;
    }
}