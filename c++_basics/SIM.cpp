#include <iostream>
#include <string>
#include <algorithm> // For transform

using namespace std;

// Function to convert a string to uppercase
string toUpperCase(const string& str) {
    string upperStr = str;
    transform(upperStr.begin(), upperStr.end(), upperStr.begin(), ::toupper);
    return upperStr;
    string sim1, sim2;
    string Sim_mt, Sim_air;
    
}

// Functions for MTN and Airtel
void mtn_function() {
    cout << "MTN function called.\n";
}

void airtel_function() {
    cout << "Airtel function called.\n";
}
string sim1, sim2;
    string Sim_mt, Sim_air;


void Sim() {
    
    // Get input for SIM cards
    cout << "No SIM card detected. Please insert SIM cards.\n\nEnter SIM One as MTN or Airtel: \n\n> ";
    cin >> sim1;
    system ("clear");
    cout << "Enter SIM Two as MTN or Airtel: \n\n> ";
    cin >> sim2;
 system ("clear");
    // Convert input to uppercase
    sim1 = toUpperCase(sim1);
    sim2 = toUpperCase(sim2);

    // Clear screen (depends on system)
    system("clear"); // On Windows, use system("cls");

    // Set Sim_mt and Sim_air based on valid inputs
    if (sim1 == "MTN") {
        Sim_mt = sim1;
    } else if (sim1 == "AIRTEL") {
        Sim_air = sim1;
    }

    if (sim2 == "MTN") {
        Sim_mt = sim2;
    } else if (sim2 == "AIRTEL") {
        Sim_air = sim2;
    }

    bool validSim1 = (sim1 == "MTN" || sim1 == "AIRTEL");
    bool validSim2 = (sim2 == "MTN" || sim2 == "AIRTEL");

    // Check if one or both SIM cards are invalid
    if (validSim1 && !validSim2) {
    system ("clear");
        cout << "Only one SIM is valid.\n\n";
        cout << "1. " << sim1 << "\n\n";
        if (Sim_mt == "MTN") mtn_function();
        if (Sim_air == "AIRTEL") airtel_function();
    } else if (!validSim1 && validSim2) {
    system ("clear");
        cout << "Only one SIM is valid.\n\n";
        cout << "1. " << sim2 << "\n\n";
        if (Sim_mt == "MTN") mtn_function();
        if (Sim_air == "AIRTEL") airtel_function();
    } else if (!validSim1 && !validSim2) {
    system ("clear");
        cout << "Both SIM cards are invalid.\n\n";
    } else { // Both SIMs are valid
        if (sim1 == sim2) {
        system ("clear");
            cout << "Both SIMs are the same.\n\n";
            cout << "1. " << sim1 << "\n2. " << sim2 << "\n\n";
        } else if (sim1 == "AIRTEL" && sim2 == "MTN") {
            cout << "SIM cards were swapped to match the program's requirements.\n\n";
            swap(sim1, sim2);
            cout << "1. " << sim1 << "\n2. " << sim2 << "\n\n";
        } else {
            cout << "SIMs are correctly placed.\n\n";
            cout << "1. " << sim1 << "\n2. " << sim2 << "\n\n";
        }

        // Call functions based on valid SIMs
        //if (Sim_mt == "MTN") mtn_function();
       // if (Sim_air == "AIRTEL") airtel_function();
    }}
    int main()
    {
    Sim();
    

    return 0;
}
