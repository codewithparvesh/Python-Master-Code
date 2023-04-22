#include <iostream>
using namespace std;
int main()
{
    int n = 5;
    int count = 1;
    for (int row = 1; row <= n; row++)
    {
        // for each row
        count = row;
        // star
        if (row == 1 || row == n)
        {
            for (int clm = 1; clm <= (n - row + 1); clm++)
            {
                cout << count << " ";
                count++;
            }
        }
        else
        {
            cout << count << " ";
            count++;

            // for sapce
            for (int clm = 1; clm <= (n - row - 1); clm++)
            {
                cout << "  ";
                count++;
            }

            // for star
            cout << count;
            // after each row
        }
        cout << endl;
    }
}