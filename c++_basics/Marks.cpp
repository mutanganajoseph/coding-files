#include<iostream>
using namespace std;
int main()
{
    while (true) {
        double marks;
        char choice;
        bool dataCleared = false;
        
        cout<<"\n(Enter student marks): ";
        cin>>marks;
        if (marks == -1) {
            system("clear");
            cout << "Data cleared.\n" <<endl;
            dataCleared = true;
            continue; 
        } 

        if (marks == -2) {
            cout << "Exiting program.\n" <<endl;
            break; 
        }

        cout<<"\n";

        if(marks > 100){
            cout<<"Maximum marks is 100!\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >= 90 &&  marks <= 100){
            cout<<"Grade A+\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >= 70 & marks <= 89){
            cout<<"Grade A\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }


        if(marks >= 65 & marks <= 69){
            cout<<"Grade B\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >= 60 & marks <= 64){
            cout<<"Grade C\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >=50 & marks <= 59){
            cout<<"Grade D\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >=40 & marks <= 49){
            cout<<"Grade E\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

        if(marks >=20 & marks <= 39){
            cout<<"Grade S\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }
        
        if(marks >= 0 & marks <= 19){
            cout<<"Grade F\n"<<endl;
            cout<<"Press -1 to clear data and -2 to quit\n"<<endl;
        }

    }

return 0;
}