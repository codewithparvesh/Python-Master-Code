#include <iostream>
using namespace std;

int main()
{
  int n = 5;

  for (int row = 1; row <= n; row++)
  {
    // for each row

    // space
    for (int col = 1; col <= n - row; col++)
    {
      cout << " ";
    }
    // star
    for (int col = 1; col <= row; col++)
    {
      cout << "*";
    }

    // after each row
    cout << endl;
  }
}