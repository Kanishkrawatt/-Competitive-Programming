// character array
#include <iostream>
using namespace std;

// Driver Code
int main()
{
	char str[20];
	cout << "Enter Your Name::";

	// see the use of getline() with array
	// str also replace the above statement
	// by cin >> str and see the difference
	// in output
	cin.getline(str, 20);

	cout << "\nYour Name is:: " << str[1];
	return 0;
}
