#include <iostream>
using namespace std;

bool isodd(int num) {

if (num < 1) return false;

if (num % 2 ==0) return false;

//for( int i=1; i<=num; i++)


return true;
}


int main()
{
    int number;

    cout<<"\nEnter a number: ";
    cin>>number;
    bool isnumber = true;
    
    for (char c : number)
    {
     if (!isdigit(c))
     {
        isnumber = false;
        cout<<"Invalid number!";
     }
    }
    cout<<"\nOdd numbers in ("<<number<< ") are: \n";

    for(int i=1; i <=number; i ++)
    {

    if(isodd(i))
    {
    cout<<i<<" \n";
}}
    
return 0;
}