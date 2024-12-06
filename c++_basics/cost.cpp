#include <iostream>
using namespace std;
int main() 
{
    double cost, total1 , total2, n, allcost;
    char choice;
while (true)
{
    cout << "(Choose A or B: )Press q to quit"<<endl;
    cout<<"A.Rice"<<endl;
    cout<<"B.Tomatoes"<<endl;
    cin >> choice;
    if (choice == 'q' || choice == 'Q')
    {
    cout<<"You're exiting....."<<endl;
    break;
    }

    if (choice == 'A' || choice == 'a')
    
     {
        cout<<"How many KG of rice: "<<endl; 
{
       cin>> n;
}
     cout<<"Enter rice cost"<<endl;
    cin>>cost;
        total1=cost*n;
        cout<<"Rice totalcost is"<< total1 <<endl;
    }
     else if (choice == 'B' || choice == 'b')
     {

     cout << "How many KG of the Tomatoes"<<endl;
     cin>>n;
      cout<<"Enter tomatoes cost"<<endl;
      cin>>cost;
        total2=cost*n;
        cout<<"Tomatoes totalCost  is:"<< total2 <<endl;
    }
     else 
     {
        cout << "Invalid choice!"<<endl;
     }
     allcost=total1+total2;
     cout<<"Total cost is:" << allcost <<endl;
}
        return 0;
    }

    