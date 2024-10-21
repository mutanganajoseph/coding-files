
#include <iostream>

using namespace std;

int main() {
    int marks;

    // Input marks from the user
    cout << "Enter the student's marks: "<<endl;
    cin >> marks;

    // Check marks using switch statement
    switch (marks) {
        case 70 ... 100:
            cout << "Student's marks: " << marks << " (Grade A)" << endl;
            break;
        case 65 ... 69:
            cout << "Student's marks: " << marks << " (Grade B)" << endl;
            break;
        case 60 ... 64:
            cout << "Student's marks: " << marks << " (Grade C)" << endl;
            break;
            case 50 ... 59:
    cout << "Student's marks: " << marks << " (Grade D)" << endl;
    break;
 case 40 ... 49:
    cout << "Student's marks: " << marks << " (Grade E)" << endl;
    break;
    case 20 ... 30:
    cout << "Student's marks: " << marks << " (Grade S)" << endl;
    break;
   
   
    break;
        default:
            cout << "Student's marks: " << marks << " (Fail)" << endl;
    }

    return 0;
}
