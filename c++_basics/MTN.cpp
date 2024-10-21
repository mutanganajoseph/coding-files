#include <iostream>
#include <string>
#include <ctime>

using namespace std;

int main() {
    int menuChoice, pin, choose;
    float amount, mtnBalance = 100000, airtelBalance = 2000, airtimeM = 100, airtimeA = 120, fee=0, faccount = 0;
    string number, choice;

    while (true) {
        time_t currentTime = time(0);
        char* timeString = ctime(&currentTime);

        cout << ">";
        cin >> choice;

        if (choice == "*182#") {
            cout << "\n1. MTN\n2. Airtel\n\n> ";
            cin >> choose;

            if (choose == 1) {
                cout << "\n1. Send Money\n2. Buy\n3. Pay Bill\n4. Bank Services\n5. My MoMo Account\n6. MoMo Pay\n7. Stop program\n\n> ";
                cin >> menuChoice;

                if (menuChoice == 1) { // Send Money
                    cout << "\nEnter number start with (078/079): ";
                    cin >> number;

                    if (number.length() != 10 || (number.substr(0,3) != "078" && number.substr(0, 3) != "079")) {
                        cout << "\nInvalid number! Double check\n!" << endl;
                        continue;
                    }

                    cout << "\nEnter amount to send: ";
                    cin >> amount;

                    if (amount <= 0) {
                        cout << "Invalid amount!\n" << endl;
                        continue;
                    }

                    if (amount <= 1000) {
                        fee = 20;
                    } else if (amount <= 5000) {
                        fee = 100;
                    } else if (amount <= 10000) {
                        fee = 250;
                    }

                    if ((amount + fee) > mtnBalance) {
                        cout << "Not enough balance!!" << endl;
                        continue;
                    }

                    cout << "\nYou entered " << number << ", " << amount << "FRW. A fee is " << fee << "FRW." << endl;
                    cout << "\nEnter pin: ";
                    cin >> pin;

                    if (pin != 12345) {
                        cout << "\nInvalid PIN. Process failed!" << endl;
                        continue;
                    }

                    string maskedNumber = number.substr(0,0) + "*******" + number.substr(number.length() - 3);
                    mtnBalance -= (amount + fee);
                    faccount += fee;

                    cout << "\nYou have sent amount of " << amount << " FRW to " << maskedNumber << " successfully at (" << timeString << "). A fee was " << fee << " FRW. Your new balance is " << mtnBalance << " FRW.\n" << endl;
                } 
                else if (menuChoice == 2) { // Buy
                    cout << "\n1. MTN yolo\n2. Super packs\n3. Isanzure\n4. Internet\n\n> ";
                    cin >> choose;

                    if (choose == 1) {
                        cout << "\n1. 100FRW Give you 40Min\n2. 200FRW Give you 70Min\n3. 500FRW 250Min imara icyumweru\n\n> ";
                        cin >> choose;

                        if (choose == 1 && airtimeM >= 100) {
                            airtimeM -= 100;
                            cout << "You activated Yolo of 100FRW Gives you 40Min\n" << endl;
                        } else if (choose == 2 && airtimeM >= 200) {
                            airtimeM -= 200;
                            cout << "You activated Yolo of 200FRW Gives you 70Min\n" << endl;
                        } else if (choose == 3 && airtimeM >= 500) {
                            airtimeM -= 500;
                            cout << "You activated Yolo of 500FRW Gives you 70Min of week\n" << endl;
                        } else {
                            cout << "Not enough airtime or invalid choice!\n" << endl;
                        }
                    } else if (choose == 2) {
                        cout << "Super packs placeholder!\n" << endl;
                    } else if (choose == 3) {
                        cout << "Isanzure Placeholder!\n" << endl;
                    } else if (choose == 4) {
                        cout << "Internet placeholder!\n" << endl;
                    } else {
                        cout << "Invalid choice!\n" << endl;
                    }
                } 
                else if (menuChoice == 3) {
                    cout << "Placeholder for MTN Option 3\n" << endl;
                } 
                else if (menuChoice == 4) {
                    cout << "Placeholder for MTN Option 4\n" << endl;
                } 
                else if (menuChoice == 5) { // My MoMo Account
                    cout << "1. Top-Up\n2. Check balance\n\n> ";
                    cin >> choose;

                    if (choose == 1) {
                        cout << "Top-Up amount:\n> ";
                        cin >> amount;
                        cout << "\n" << endl;
                        if (amount > 1000000)
                        {
                        cout << "You can't top-up higher than one million!\n" << endl;
                        continue;
                        }
                        mtnBalance += amount;
                        cout << "Top-Up amount of " << amount << " FRW done successfully at (" << timeString << "). Your new balance is " << mtnBalance << " FRW.\n" << endl;
                    } else if (choose == 2) {
                        cout << "1.Your MoMo balance is " << mtnBalance << " FRW.\n2. Fee balance is " << faccount << " FRW.\n" << endl;
                    } else {
                        cout << "Wrong input. Please try again!\n" << endl;
                    }
                } 
                else if (menuChoice == 6) {
                    cout << "Placeholder for MTN Option 6\n" << endl;
                } 
                else if (menuChoice == 7) {
                    cout << "Program stopped successfully!" << endl;
                    break;
                } 
                else {
                    cout << "\nInvalid choice. Please try again.\n" << endl;
                }
            } 
            else if (choose == 2) { // Airtel
                cout << "\n1. Send Money\n2. Buy\n3. Pay Bill\n4. Bank Services\n5. My Airtel Account\n6. Airtel Pay\n7. Stop program\n\n> ";
                cin >> menuChoice;

                if (menuChoice == 1) { // Send Money
                    cout << "Enter number start with (072/073): ";
                    cin >> number;

                    if (number.length() != 10 || (number.substr(0, 3) != "072" && number.substr(0, 3) != "073")) {
                        cout << "Invalid number. Process failed!\n" << endl;
                        continue;
                    }

                    cout << "Enter amount to send: ";
                    cin >> amount;

                    if (amount > 0 && amount <= airtelBalance) {
                        cout << "Enter pin: ";
                        cin >> pin;

                        if (pin != 4321) {
                            cout << "Invalid PIN. Process failed!!\n" << endl;
                            continue;
                        }

                        airtelBalance -= amount;
                        string maskedNumber = number.substr(0, 3) + "****" + number.substr(number.length() - 3);
                        cout << "You have sent amount of " << amount << " FRW to " << maskedNumber << " successfully at (" << timeString << "). Your new balance is " << airtelBalance << " FRW." << endl;
                    } else {
                        cout << "Insufficient balance!\n" << endl;
                    }
                } 
                else if (menuChoice == 2) {
                    cout << "Placeholder for Buy\n" << endl;
                } 
                else if (menuChoice == 3) {
                    cout << "Placeholder for Pay Bill\n" << endl;
                } 
                else if (menuChoice == 4) {
                    cout << "Placeholder for Bank Services\n" << endl;
                } 
                else if (menuChoice == 5) { // My Airtel Account
                    cout << "1. Top-Up\n2. Check balance\n\n> ";
                    cin >> choose;

                    if (choose == 1) {
                        cout << "Top-Up amount:\n> ";
                        cin >> amount;
                        airtelBalance += amount;
                        cout << "Top-Up amount of " << amount << " FRW done successfully at " << timeString << ". Your new balance is " << airtelBalance << " FRW." << endl;
                    } else if (choose == 2) {
                        cout << "Your balance is " << airtelBalance << " FRW.\n" << endl;
                    } else {
                        cout << "Wrong input. Please try again!\n" << endl;
                    }
                } 
                else if (menuChoice == 6) {
                    cout << "Placeholder for Airtel Pay\n" << endl;
                } 
                else if (menuChoice == 7) {
                    cout << "Program stopped successfully!" << endl;
                    break;
                } 
                else {
                    cout << "Invalid choice. Please try again.\n" << endl;
                }
            } 
            else {
                cout << "Invalid telecom provider choice. Please try again.\n" << endl;
            }
        } 
        else if (choice == "*131#") {
            cout << "\n1. MTN\n2. Airtel\n\n> ";
            cin >> choose;

            if (choose == 1) {
                cout << "Your AirtimeBalance is " << airtimeM << " FRW.\n" << endl;
            } else if (choose == 2) {
                cout << "Your AirtimeBalance is " << airtimeA << " FRW.\n" << endl;
            } else {
                cout << "Invalid choice!\n" << endl;
            }
        } 
        else {
            cout << "I don't understand. Please try again.\n" << endl;
        }
    }

    return 0;
}