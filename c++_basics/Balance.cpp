#include<iostream>
using namespace std;

int main()
{
    int balance = 0;
    int choice;
    int amount;

    while (true)
    {
        cout << "\n1. Check balance" << endl;
        cout << "2. Top up" << endl;
        cout << "3. Withdraw" << endl;
        cout << "4. Stop program" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1)
        {
            cout << "Current balance: " << balance << endl;
        }
        else if (choice == 2)
        {
            cout << "Enter top-up amount: ";
            cin >> amount;
            if (amount > 0)
            {
                balance += amount;
                cout << "Top-up successful. Your new balance is: " << balance<< endl;
            }
            else
            {
                cout << "Invalid amount. Please enter a positive value." << endl;
            }
        }
        else if (choice == 3)
        {
            cout << "Enter withdrawal amount: ";
            cin >> amount;
            if (amount > 0 && amount <= balance)
            {
                balance -= amount;
                cout << "Withdrawal successful. Your new balance is: " << balance << endl;
            }
            else if (amount <= 0)
            {
                cout << "Invalid amount. Please enter a positive value." << endl;
            }
            else
            {
                cout << "Insufficient balance." << endl;
            }
        }
        else if (choice == 4)
        {
            cout << "Program stopped successfully!" << endl;
            return 0;
        }
        else
        {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
