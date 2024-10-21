#include<iostream>
#include<algorithm>
#include<string>
#include <cctype>

using namespace std;

string UpperCase(const string& str){
    string upper = str;
  transform(upper.begin(), upper.end(), upper.begin(), ::toupper);
  return upper;
}


int main(){
  
 bool started = false;
  string command;
 

  while (true){
    
 cout<<"\n> ";
 cin>>command;
 command = UpperCase(command); 
 if(command =="HELP"){
    cout<<"\n Press start to start the car \n Press stop to stop the car \n Press Quit to exit\n ";
 }

else if(command =="START"){
    if(!started){
    cout<<"\n Car started \n";
    started = true;
    }
    
    else {
        cout<<"\ncar already started\n";
    }

 }
 else if (command =="STOP"){
    if (started){
      cout<<"\n Car stoped\n";
      started = false;
    }
    else{
      cout<<"\ncar already Stopped\n";
    }
 }
 else if (command == "QUIT"){
    cout<<"\n\nExiting...\n\n";
    break;
 }
  
 else{
    cout<<"\n I do not understand Press help to get support\n";
 }
  }

return 0;
}