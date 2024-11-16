#include<iostream>
using namespace std;
int main()
{
    int pin;
    string user;
    cout<<"\n\n                                                          Username: ";
    cin>>user;
    cout<<"\n\n                                                          Password: ";
    cin>>pin;
    cout<<"\n "<<endl;
    if(pin != 1234 || user !="Joe")
    {
        cout<<"\n                                                        Invalid username or password\n\n"<<endl;
    }
    else{
        cout<<"\n                                                         ACCESS GRANTED! \n\n"<<endl;
    }
    return 0;
}