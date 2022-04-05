#include <iostream>
#include <vector>
#include <string>
#include <ostream>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

template <typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
	for(size_t i = 0; i < v.size(); ++i) {
		out << v[i] << endl;
	}

	return out;
}

template <typename T>
void printArray(std::vector<T>& v) {
	cout << v;
}

int main() {
	int n;

	// 1st input: number of intergers
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		// 2nd input(s): n integers, 1 per line
		cin >> value;
		int_vector[i] = value;
	}

	// 3rd input: number of strings
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		// 4th input(s): n strings, 1 per line
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
