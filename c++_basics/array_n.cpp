#include <iostream>
#include<climits>
using namespace std;

int main() 
{
while(true)
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
if(n <= 0){
cout << "Number of elements must be greater than 0!" << endl;
main();
}
    // Declare an array of size n
    int arr[n];

    // Prompt user to enter n numbers
    cout << "Enter " << n << " numbers:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Enter number " << (i + 1) << ": ";
        cin >> arr[i];
    }

    // Calculate the sum of the numbers
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += arr[i];
    }
    // Display the sum
    cout << "Sum of the numbers is: " << sum <<endl;
    }
    return 0;
}
    