#include<iostream>
using namespace std;
int main()
{
    float amount, acount=10000, fee;
    int pin,number;
    cout<<"enter number "<<endl;
    cin>>number;
    cout<<"enter amaount"<<endl;
    cin>>amount;
    if (amount >=1 && amount <=1000){
        fee=20;
        acount -=(amount + fee);
        if(amount > acount-fee)
        {
            cout<<"insufficient balance";
        }
        cout<<"You entered " <<number<<", " <<amount<<" FRW.  A fee is " <<fee<<" FRW. "<<endl;
        cout<<"enter pin "<<endl;
        cin>>pin;
        if(pin !=1234)
        {
            cout<<"inavlid pin "<<endl;
        }
        else if(amount >=1001 && amount <=5000){
        fee=100;
       acount -=(amount + fee);
       if(amount > acount-fee)
         {
        cout<<"insufficient balance";
         }
           cout<<"You entered " <<number<<", " <<amount<<" FRW.  A fee is " <<fee<<" FRW. "<<endl;
         cout<<"enter pin "<<endl;
           cin>>pin;
           if(pin !=1234)
          {
           cout<<"inavlid pin "<<endl;
            }
        else {
            cout<<"You have sent " <<amount<<" FWF. to " <<number<< " Balance: "<<acount<<" FRW. Thank you for using MTN"<<endl;
        }}
    }
}