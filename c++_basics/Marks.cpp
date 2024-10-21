#include<iostream>
using namespace std;
int main()
{
    double marks;
    char choice;
bool dataCleared = false;
    while (true) {
        cout<<"Press -1 to clear data and -2 to quit"<<"\n"<<endl;
    cout<<"(enter student marks)"<<endl;
    cin>>marks;

 if (marks == -1) {
    std::cout << "Data cleared." << std::endl;
dataCleared = true;
continue; // Continue to next iteration
} else if (marks == -2) {
std::cout << "Exiting program." << std::endl;
break; // Break out of the loop to quit the program
}
if(marks >= 90 &&  marks <= 100)
{
cout<<"Grade A+"<<endl;
}
else if(marks >= 70 & marks <= 89)
{
cout<<"Grade A"<<endl;
}
else if(marks >= 65 & marks <= 69)
{
cout<<"Grade B"<<endl;
    }
    else if(marks >= 60 & marks <= 64)
    {
        cout<<"Grade C"<<endl;
    }
    else if(marks >=50 & marks <= 59)
    {
   cout<<"Grade D"<<endl;
    }
     else if(marks >=40 & marks <= 49)
 {
cout<<"Grade E"<<endl;
 }
  else if(marks >=20 & marks <= 39)
 {
cout<<"Grade S"<<endl;
 }
  else if(marks >= 0 & marks <= 19)
 {
cout<<"Grade F"<<endl;
}
else
{
cout <<"Invalid marks"<<endl;
 }}
return 0;
}