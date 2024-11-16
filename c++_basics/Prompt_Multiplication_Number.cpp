#include<iostream>
using namespace std;

int main()
{
while(true){
int num,pro;
string choice;

cout << "\nEnter a number to get it's multiplication.\n\n> ";

cin>>num;
system ("clear");
cout << "\n      Here is multiplication of " <<num <<".\n\n"<< endl;
for(int i=1; i<=12; i++)
{
pro=i*num;

    cout<<"             " <<num<< " * " <<i<< " = " <<pro<<"\n"<<endl;
    }
    cout << "\n\nDo you want to see multiplication of other number (Y/n).\n\n> ";
   
    cin>>choice;
    system ("clear");
    if(choice !="y" && choice !="Y")
    {
    system ("clear");
    cout << "\nExiting...\n\n" << endl;
  
    break;
    }
    
    
    }
    return 0;
}