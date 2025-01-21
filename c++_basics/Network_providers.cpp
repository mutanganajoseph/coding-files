#include<iostream>
#include <string>
#include <ctime>
#include <chrono>
#include <thread>
#include <cstdlib>
#include <algorithm> //to tarnasform to Uppercase
#include <iomanip>//For Put local time & setprecision


using namespace std;
string toUpperCase(const string& str) {
    string upperStr = str;
    transform(upperStr.begin(), upperStr.end(), upperStr.begin(), ::toupper);
    return upperStr;
   
}


class Network_providers{
public:
    string sim1, sim2;
    string Sim_mt, Sim_air;
    string name;
    
int count=0;
float mtn_airtime_balance, airtel_airtime_balance;
float MoMo_account=500, amount=0,fee=0;
string number,choice;

  
   time_t joe =time(0);
   char* currentTime = ctime(&joe);

    time_t now=time(0);
    tm* localTime= localtime(&now);

string getCurrentTime(){
   auto now = chrono::system_clock::now();

   time_t currentTime = chrono::system_clock::to_time_t(now);

   tm* localTime = localtime(&currentTime);

   stringstream timeStream;

   timeStream<< put_time(localTime, "%d-%m-%Y  %H:%M:%S")<<endl;
   return timeStream.str();
   


}



void timer(){
   
 float second = 0;

    // Infinite loop to count seconds
    while (true) {
      
        // Display the corresponding word based on 'second'
        if(second ==3){
         system("clear");
         cout<<"\n\n\n";
         cout<<"\n                                                             WELCOME TO NETWORK PROVIDERS.\n\n\n";
        }
        else if (second == 5) {
         system("clear");
         cout<<"\n\n\n";
            cout << "                                                            YOU MUST TYPE *182# OR *131#.\n" << endl;
        } else if (second == 7) {
         system("clear");
         cout<<"\n\n\n";
            cout << "                                                             THEN FOLLOW PROMPT.\n" << endl;
        } else if (second == 9) {
         system("clear");
         cout<<"\n\n\n";
            cout << "                                                              ENJOY YOUR TIME WITH NETWORK PROVIDERS!\n" << endl;
        }
        else if(second ==11){
         system("clear");
          cout<<"\n\n\n";
         cout<<"                                                                    GET READY!\n" <<endl;
         
        }
        else if(second ==13){
         system("clear");
         break;
        }

        // Increment 'second' and wait for 1 second
        second++;
        this_thread::sleep_for(chrono::seconds(1));
    }

}



void wait_timer(){

   int second=0;
      while (true) {
         
         if(second ==0){
            cout<<"\nUSSD code running...\n";
            
            
         }
      else if(second ==1){
      cout<<"";
       system("clear");
      break;
      
    }
   
    second++;
      this_thread::sleep_for(chrono::seconds(1));
   }
}


void exitMtn(){
   while(true){
   wait_timer();
      cout<<"\nThank You For Using MTN!... \n\n ";
      break;
   }
}


void exitAtl(){
   while(true){
      wait_timer();
      cout<<"Thank You For Using Airtel!...\n\n";
      break;
   }

}

void exit(){
   cout<<"Good Bye!...\n\n"; 
}


void Sim() {
   
    // Get input for SIM cards
    cout<< "\n\nNo SIM Card Detected. \n\nPlease Insert SIM Cards with writing them by Its names like MTN or Airtel.\n\n\nFolder1, Enter SIM One On FOlder 1 As MTN or Airtel: \n\n> ";
    cin >> sim1;
    system ("clear");
    
    cout << "   \n\nFolder2, Enter SIM Two On Folder 2 As MTN or Airtel: \n\n> ";
    cin >> sim2;
    system ("clear");
    // Convert input to uppercase
    sim1 = toUpperCase(sim1);
    sim2 = toUpperCase(sim2);

    
    system("clear"); 
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
    
        if(sim1 == Sim_mt){
         
        cout << "Only MTN SIM Is Valid On SIM Folder 1.\n\n";
        cout << "1." << sim1 << "\n\n";
                timer();
               sim_mtn();
               }
        
        else{
         
          cout << "Only Airtel SIM is valid On SIM Folder 1.\n\n";
          cout << "1) " << sim1 << "\n\n"; 
          timer();
          sim_airtel();
      }
        
    } 
    else if (!validSim1 && validSim2) {
      
      if(sim2 == Sim_air){
          system("clear");
         
        cout << "Only Airtel SIM is valid On SIM Folder 2.\n\n";
        cout << "2)" << sim2 << "\n\n";
              timer();
               sim_airtel();
               }
        
      else{
         
         
          cout << "Only MTN SIM Is Valid On SIM Folder 2.\n\n";
          cout << "2)" << sim2 << "\n\n"; 
          timer();
           sim_mtn();
      }
      
        
    } 
    
    else if (!validSim1 && !validSim2) {
    system("clear");
    
   
        cout << "Both SIM cards are invalid. " <<put_time(localTime, "%H:%M:%S")<<"\n\n1."<<sim1<<"\n2."<<sim2<<"\n\n";

        
        Sim();
    } else { // Both SIMs are valid
        if (sim1 == sim2) {
           system ("clear");
            
            cout << "Both SIMs are the same.\n\n";
            if(sim1 == Sim_mt){     
            cout << "You are using MTN only\n\n1) " << sim1 << "\n2) " << sim2 << "\n\n";
               timer();
               sim_mtn_mtn();
            }
            else{
               
               cout<<"You are using AIRTEL only\n\n1) " << sim1 << "\n2) " << sim2 << "\n\n";
               timer();
               sim_airtel_airtel();
            }
                   
        } else if (sim1 == "AIRTEL" && sim2 == "MTN") {
             wait_timer();
            cout << "\nSIM PLACED AS \n\n1) "<<sim1<<"\n2) "<<sim2<<"\n\n";
            
            timer();
            
            sim_airtel_mtn();
            
            
        } else {
         system("clear");
         
            cout << "\nSIM PLACED AS: \n\n1) "<<sim1<<"\n2) "<<sim2<<"\n\n"; 
             timer();
             system("clear");
            sim_mtn_airtel();
           
        }

      
    }}





//while airtel is only valid sim
void sim_airtel() {
   while(true){
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      if (choice == "*182#") {
         
         wait_timer();
         airtel_prompt();
      }
      else if (choice == "*131#") {
         
         wait_timer();
         airtel_airtime();
      }
      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
      } 
   }
}

void sim_mtn() {
   while(true){
   
      cout<<"";
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      if (choice == "*182#") {
         system("clear");
         wait_timer();
         mtn_prompt(); 
      }
      else if (choice == "*131#") {
      
         wait_timer();
         mtn_airtime();    
      }
      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
      } 
   }

}

void sim_airtel_mtn() {
   while(true){
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      wait_timer();
      if (choice == "*182#") {
         
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         if (choice == "1") {
            wait_timer();  
            airtel_prompt();
         }
         else if (choice == "2") {
            
            wait_timer();
            mtn_prompt();
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong Choice!\n\n";
            sim_airtel_mtn();
         }
      }
      else if (choice == "*131#") {
         system("clear");
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         if (choice == "1") {
            cout << "\n";
            
            wait_timer();
            airtel_airtime();
         }
         else if (choice == "2") {
            cout << "\n";
            
            wait_timer();
            mtn_airtime();
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong choice!\n\n";
            
         }
      }
      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
         
      }
   }
}


//while all sim1 and sim2 is mtn
void sim_mtn_mtn() {
   while(true){
      float sim_mtn_balance=200;
      
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      if (choice == "*182#") {
         system("clear");
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         
         if (choice == "1") {
            wait_timer(); 
            mtn_prompt();
         }
         else if (choice == "2") {
            wait_timer();
            mtn_prompt();
         }
         else {
            wait_timer();
            cout << "\nWrong Choice!\n\n";
            sim_mtn_mtn();
         }
      }
      else if (choice == "*131#") {
         system("clear");
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         
         if (choice == "1") {
            cout << "\n";
         wait_timer();
            mtn_airtime();
         }
         else if (choice == "2") {
            system("clear");
            wait_timer();
            cout << "\n";
         
            cout<<"Balance: "<< fixed << setprecision(2)<<sim_mtn_balance<<"F.\n\n";
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong choice! Type *182# OR *131#\n\n";
            sim_mtn_mtn();
         }
      }

      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
      }

   }
}

void sim_airtel_airtel() {
   while(true){
      float sim_airtel_balance=300;
      system("clear");
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      if (choice == "*182#") {
         system("clear");
      
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         
         
         if (choice == "1") {
            wait_timer();   
            airtel_prompt();
         }
         else if (choice == "2") {
            wait_timer();
            airtel_prompt();
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong Choice!\n\n";
         }
      }
      else if (choice == "*131#") {
         system("clear");
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         
         if (choice == "1") {
            cout << "\n";
            wait_timer();
            airtel_airtime();
         }
         else if (choice == "2") {
            cout << "\n";
            wait_timer();
            cout<<"Balance: " << fixed << setprecision(2)<< sim_airtel_balance<<"F.\n\n";
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong choice! Type *182# OR *131#\n\n";
            sim_airtel_airtel();
         }
      }
      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
         
      }
   }
}



void sim_mtn_airtel() {
   while(true){
      cout << "Only *182# Or *131# Are Allowed. \n\n> ";
      cin >> choice;
      system("clear");
      if (choice == "*182#") {
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         if (choice == "1") {
            wait_timer();   
            mtn_prompt();
         }
         else if (choice == "2") {
            wait_timer();
            airtel_prompt();
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong Choice!\n\n";
         }
      }
      else if (choice == "*131#") {
         system("clear");
         wait_timer();
         cout << "\nCall With\n";
         cout << "\n1) " << sim1 << "\n2) " << sim2 << "\n\n> ";
         cin >> choice;
         system("clear");
         if (choice == "1") {
            cout << "\n";
            wait_timer();
            mtn_airtime();
         }
         else if (choice == "2") {
            cout << "\n";
            wait_timer();
            airtel_airtime();
         }
         else {
            system("clear");
            wait_timer();
            cout << "\nWrong choice!\n\n";
         }
      }

      else if(choice =="exit" || choice =="Exit" || choice =="EXIT"){
         exit();
         break;
      }
      else {
         system("clear");
         wait_timer();
         cout << "\nUNKNOWN APPLICATION!\n\n";
      }
   }
}

void mtn_prompt(){
 
   cout<<"\n1) Send Money\n2) Buy\n3) Pay Bill\n4) Bank Services\n5) Loans and Savings\n6) My MoMo Account\n7) Pending Approvals\n8) MoMo Pay\n9) My MoMo Security\nn  Next\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1"){
     wait_timer();
     mtn_send_money();
   }
    
    else if(choice=="2"){
      wait_timer();
      cout<<"\n1) Buy airtime, Voice Pack and Data Bundels\n2) Electricity\n3) Pay Sercives\n4) Solar\5)Pay Transport Fare\n6) Online Shopping Card\n0) Back\n\n> ";
      cin>>choice;
      system("clear");
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="0" ){
         
         wait_timer();
         mtn_prompt();
      }

      else{
         system("clear");
         wait_timer();
         cout<<"Wrong Choice\n\n";
      }
     
   } 
   
   
   else if(choice=="3"){
       wait_timer();
      cout<<"\n1) Pay TV\n2) PostPaid Bill\n3) Pay PSF\n4) RSSB\n5) Water\n6) RWanda Revenue\n7) Irembo Services\n8) Airport Parking\n9) Bussinesss\n0) Back\nn Next\n\n> ";
      cin>>choice;
      system("clear");
      if(choice=="0" || choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="7" || choice=="8" || choice=="9" || choice=="n" || choice=="N" )
      {
         wait_timer();
         mtn_prompt();
      }
       else{
         system("clear");
         wait_timer();
         cout<<"\nWrong choice!\n\n";
      }
   }
   
   
    else if(choice=="4"){
       wait_timer();
      cout<<"\n1) ATM\n2) Send MoMo to Bank\n3) Get Money from Bank Account\n4) Check Account Balance\n5) Delink Bank account\n6) BRD Loan Payment\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="0")
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }
       else{
         system("clear");
          wait_timer();
         cout<<"\nWrong choice!\n\n";
         
      }
   } 
   
   
   else if(choice=="5"){
      wait_timer();
      cout<<"\n1) Mokash\n2) STAFF\n3) KCB\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="0" )
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }
       else{
         system("clear");
         wait_timer();
         cout<<"\nWrong choice!\n\n";

      }
   } 
  else if(choice=="6"){
      wait_timer();
      cout<<"\n1) Check Balance\n2) Mini Statement\n3) Get Latest Electricity Token\n4) Preapprove Transaction\n5) Change Language\n6) My Offers\n7) Exit\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="0")
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }

      else if(choice =="7"){
         exitMtn();
      }
       else{
         system("clear");
          wait_timer();
         cout<<"\nWrong choice!\n\n";

      }
   }

   else if(choice=="7"){
      wait_timer();
      
      cout<<"\nPending approvals\n\n1) CashOut Approvals\n2) Allow CashOut Approval\n3) Request a Reversal\n4) Approval or Decline a Reversal Request\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="0")
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }
       else{
         system("clear");
          wait_timer();
         cout<<"\nWrong choice!\n\n";

      }
   }

   else if(choice=="8"){
      wait_timer();
      cout<<"\nMoMo Pay\n\n";
      cout<<"\n1) Enter MoMo Pay Code\n2) Manage MoMo Paye Account\n\n> ";
      cin>>choice;
      if(choice=="1" || choice =="2")
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }
       else{
         system("clear");
          wait_timer();
         cout<<"\nWrong choice!\n\n";

      }
   }

   else if(choice=="9"){
      wait_timer();
      cout<<"\n1) Reset PIN\n2) Change PIN\n3) Self PIN Reset\n4) Exit\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="0")
      {
         system("clear");
         wait_timer();
         mtn_prompt();
      }

      else if(choice =="4"){
         exitMtn();
      }
       else{
         system("clear");
          wait_timer();
         cout<<"\nWrong choice!\n\n";

      }
   }


   else if(choice=="n" || choice =="N"){
      mtn_next();
   }

   


else{ 
      system("clear");
      wait_timer();
      cout<<"\nWrong Choice! Try again!\n\n";
      mtn_prompt();
      
      
   }
}



void mtn_next(){
  
   wait_timer();
   cout<<"\n10) Insurance\n11) MoMo Terms and Conditions\n12) Macye Macye\n13) Baby Health\n14) Help\n15) Back\n16) Exit\n\n> ";
   cin>>choice;
    system("clear");
    wait_timer();
     if(choice=="10"){
       wait_timer();
      cout<<"\n1) Radiant Yacu\n2) Prime Insurance\n3) Ineza\n4) UAP\n5) SANLAM\n0) Back\n\n> ";
      cin>>choice;
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="0")
      {
         system("clear");
         mtn_next();
      }

       else{
         system("clear");
         wait_timer();
         cout<<"\nWrong Choice!\n\n";
        

      }
   } 
    else if(choice=="11"){
        wait_timer();
      cout<<"\nYou have already confirmed the terms and conditions\n\n1) Top opt-out from eKash services\n0) Exit\n\n> ";
      cin>>choice;
     system("clear");
      if(choice=="1")
      {
         mtn_next();
      }

      else if(choice == "0"){
         exitMtn();
      }
     
       else{
          system("clear");
          wait_timer();
         cout<<"\nWrong Choice!\n\n";
          }
       }

 else if(choice=="12"){
    wait_timer();
      cout<<"\nWelcome To Macye Macye\n\n1) Registration\n2) Info\n\n> ";
      cin>>choice;
      system("clear");
      if(choice=="1" || choice =="2")
      {
         mtn_next();
      }
     
      else{
          system("clear");
          wait_timer();
         cout<<"\nWrong choice.\n\n";

      }
   } 

   else if(choice=="13"){
    wait_timer();
      cout<<"\nExternal Application Down\n\n> ";
      cin>>choice;
      system("clear");
      if(choice=="1" || choice =="2")
      {
         mtn_next();
      }
     
      else{
         system("clear");
          wait_timer();
         cout<<"\nConnection Problem or Invalid MMI Code.\n\n";

      }
   } 

   else if(choice=="14"){
    wait_timer();
      cout<<"\n1) Dial Center\n2) What is Mobile Money\n3) Getting Mobile Money\n4) Charges\n5) Roaming\n6) Transfer to a non Mobile user\n7) Buying\nn  Next\n\n> ";
      cin>>choice;
      system("clear");
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="7" || choice=="n" )
      {
         mtn_next();
      }
     
      else{
         system("clear");
          wait_timer();
           
         cout<<"\nWrong choice.\n\n";

      }
   } 
    
   else if(choice=="15"){
      mtn_prompt();
   }

   else if(choice=="16"){
     exitMtn();
      }


   else{
      wait_timer();
      cout<<"\nWrong Choice. Try Again!\n\n0) Back\n\n>";
      cin>>choice;
      if(choice == "0"){
         system("clear");
         mtn_next();
      }
      else{
         system("clear");
         wait_timer();
         cout<<"Invalid input. This session terminated by '"<<choice<<"'.\n";
      }

   
   }
}




void mtn_send_money() {
   wait_timer();
   cout<<"\n1) MoMo user\n2) Send to eKash\n3) International Remittances\n4) Cancel Vouncher\n5) Display Voucher\n6) List Active Vouncher\n7) Exit\n0) Back\n\n> ";
   
    cin >> choice;
  
     system("clear");
    wait_timer();
    if (choice == "1") {
        mtn_recipient();
        MoMo_amount();
       }
      

    else if (choice == "2") {
       wait_timer();
      cout << "\nThis Choice not Available\n\n0) Back\n\n> ";
      cin>>choice;
      system("clear");
      wait_timer();
      if (choice == "0") {
      mtn_send_money(); 
      }
      else {
         system("clear");
        wait_timer();
        cout << "\n\nWrong choice. Try again Later!\n\n";
        
      }
    }
    else if (choice == "3") {
       wait_timer();
        cout << "\nSorry This Actions Will Not Be Perfomed Now. Enter 0 To go back.\n\n1) To Mobile Number\n2) To AliPay\n3) To Bank\n4) View Recaiver Countries\n0) Back\n\n> ";
        cin>>choice;
        system("clear");
        wait_timer();
          if (choice == "0") {
            system("clear");
            mtn_send_money();
         }
         else {
           wait_timer();
           cout << "\n\nWrong choice. Try again Later!\n\n";
           
         }
    }

    else if(choice =="4"){
      system("clear");
      wait_timer();
      cout<<"\nTo Cancel Vouncer, Will not Work. Enter 0 To go Back\n\n0) Back\n\n> ";
      cin>>choice;
      if(choice =="0"){
         system("clear");
         mtn_send_money();

      }

      else{
         system("clear");
         wait_timer();
         cout<<"\nWhoops! Wrong Choice\n\n";
      }
      
    }

    else if(choice =="5"){
      system("clear");
      wait_timer();
      cout<<"\nTo Display Vouhcer, Will not Work. Enter 0 to go Back\n\n0) Back\n\n> ";
      cin>>choice;
      if(choice =="0"){
         system("clear");
         mtn_send_money();

      }

      else{
         system("clear");
         wait_timer();
         cout<<"\nWhoops! Wrong Choice\n\n";
      }
      
    }

    else if(choice =="6"){
      cout<<"\nList of Active Vouncer, Is Not available. Enter 0 to go Back\n\n0) Back\n\n> ";
      cin>>choice;
      if(choice =="0"){
         system("clear");
         mtn_send_money();

      }

      else{
         system("clear");
         wait_timer();
         cout<<"\nWhoops! Wrong Choice\n\n";
      }
      
    }

    else if (choice == "7") {
        exitMtn();
    }
    else if (choice == "0") {
        mtn_prompt(); 
    }
    else {
       wait_timer();
        cout << "\n\nWrong choice. Try again!\n\n";
        mtn_send_money();
    }
}


void mtn_recipient() {
  
  
    
   cout << "\nEnter recipient 07*******\n\n> ";
        cin >> number;

        if(number == "0780920096"){
         name = "Mutangana Joseph";
        }

         bool all_digits = true;
         bool has_letters = false;
    for (char c : number) {
        if (!isdigit(c)) {
            all_digits = false;
            if (isalpha(c)) {
               has_letters = true;
            }
        }
    }
     if (has_letters) {
       system("clear");
       wait_timer();  
        cout << "\nError: Input contains letters! ("<<number<<") "<<".\n\n"<< endl;
        mtn_recipient();
    }
        
        else if (number.length() != 10 || (number.substr(0, 3) != "078" && number.substr(0, 3) != "079")){
             system("clear");
             wait_timer();
            cout << "\nRecipient not found!\n" << endl; 
            mtn_recipient();
        
        }
}
       



void MoMo_amount() {
    while (true) {
        system("clear"); 
        wait_timer();   
        cout << "\nEnter amount to send to (" << number <<") " << name << ".\n\n > ";
        cin >> amount;   
        system("clear"); 
        wait_timer();   

        if (amount <= 0) {
            system("clear");
            wait_timer();
            cout << "\nInvalid amount\n\n";
            break; 
        } else if (amount > MoMo_account) {
            system("clear");
            wait_timer();
            cout << "\nNot enough balance to perform transaction!\n\n";
            break; 
                  }

        
        if (amount <= 1000) {
            fee = 20;
        } else if (amount <= 10000) {
            fee = 100;
        } else if (amount <= 15000) {
            fee = 250;
        } else if (amount >= 50000) {
            fee = 350;
        }

        
        MoMo_account -= (amount + fee); 
        wait_timer();
        system("clear");
        cout << "\nYou entered " << fixed << setprecision(2)<< amount << "FRW. Fee is " << fixed << setprecision(2)<< fee << "FRW. Money will be sent to ("<< number <<") " <<name << ".\n";

        
        if (amount > 0) {
            mtn_pin(); 
        }

        
        break;
    }
}




void mtn_pin(){
   string pin;
   string confirm_pin;
   cout<<"\nEnter your MoMo Pin to confirm transaction.\n\n> ";
      cin>>pin;  
     bool all_digits = true;
      bool has_letters = false;
    for (char c : pin) {
        if (!isdigit(c)) {
            all_digits = false;
             if (isalpha(c)) {
               has_letters = true;
            }
        }
    }
     if (has_letters){
       system("clear");
       wait_timer();
       cout<<"\n\nPin must only be FIVE digit! try again!\n\n";
       mtn_pin(); 
     }

 else  if(pin.length() !=5 )
   { 
      system("clear");
       wait_timer();
      
      cout<<"\n\nPin must be FIVE digit! try again!\n\n";
      mtn_pin();
       
   }
   
 system("clear");
 wait_timer();
   cout<<"\nConfirm Pin\n\n>";
  cin>>confirm_pin;
    system("clear");
       wait_timer();

 
    if(confirm_pin.length() !=5)
   { 
      system("clear");
       wait_timer();
      cout<<"\n\nConfirm Pin must be 5 digits!\n\n";
      mtn_pin();
   
       }
       else if(confirm_pin !=pin)
       {
          system("clear");
           wait_timer();
         cout<<"\n Pin did not match. try again!\n\n";
         mtn_pin();
       }
       

  else  if(confirm_pin == pin && pin.length() ==5){

       system("clear");
       wait_timer();
      cout<<"\n\n   Money of "<<amount<<"FRW. Transferd succefully to " << name << "(" << number<<") at: " <<getCurrentTime()<<". Fee was "<<fee<<"FRW. Your new balance is "<<MoMo_account<<"FRW.Thank you for using MTN.\n\n"; 
   }
  
}



void airtel_prompt(){
   

 
 
cout<<"\nPlease Select\n\n0. Fund My Wallet\n1. Send Money\n2. Buy Airtime/Packs (5% Cashback)\n3. Cash-out\n4. Payments\n5. My Account/Pin\n6. Bank Services\n7. Gaming\n8. Airtel Pay\n9. Exit\n00 Next\n\n> ";
   cin>>choice;
  system("clear");
 if(choice =="0"){
   system("clear");
   wait_timer();
   cout<<"\n1. Get From My Back\n\n99 MainMenus\n0  Previous\n\n>";
   cin>>choice;
   if(choice =="1" ){
      system("clear");
      wait_timer();
      cout<<"\nNo Performed Action\n\n";
   }

   else if(choice =="99" || choice=="0"){
      system("clear");
      wait_timer();
      airtel_prompt();
   }

   else{
      system("clear");
      wait_timer();
      cout<<"\nWrong Choice! \n";
   }

 }
 
 else if(choice=="1"){
    wait_timer();
    system("clear");
      cout<<"\nPlease Select\n\n1. Send to AirtelMoney\n2. Send to eKash'\'MoMo\n3. International\n4. Send to My Favourites\n\n99 MainMenu\n0  Previous\n\n> ";
      cin>>choice;
      
      if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="99" || choice=="0" )
      {
         system("clear");
         wait_timer();
         airtel_prompt();
      }
      else{
         system("clear");
          wait_timer(); 
      cout<<"\nWrong Choice. Try again Later!\n\n";
   }
   }
    
else if(choice=="2"){
   wait_timer();
   cout<<"\nPlease Select.\n\n1. Airtime for Own Number(5% CashBack)\n2. Airtime for Other Number\n3. For My Favourite\n4. Buy Packs (5% CashBack)\n5. Pay.rw Airtime\n00 Next\n\n> ";
   cin>>choice;

   if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="00")
   { 
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
      cout<<"\nWrong Choice. Try again Later!\n\n";
   }
} 


else if(choice=="3"){
   wait_timer();
   cout<<"\n1. From Main Wallet \n\n99 Main Menu\n0  Previous\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1" ||  choice=="99" || choice=="0" )

   { 
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
      cout<<"\nWrong Choice. Try again Later!\n\n";
   }
}


else if(choice=="4"){
   wait_timer();
   cout<<"\nPlease Select\n\n1. Buy Cash Power\n2. Pay Business\n3. Pay Campus/Bill\n4. Pay Water\n5. Gov services\n6. Pay PSF\n7. Validate Ticket\n8. Mituelle de\n00 Next\n\n> ";
   cin>>choice;

   if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="7" || choice=="8" || choice=="00")
   {
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
      cout<<"\nWrong Choice. Try again Later!\n\n";
   }
} 


else if(choice=="5"){
   system("clear");
   wait_timer();
   cout<<"\nPlease Select\n\n1. Balance Enquiry\n2. My Transaction Reversals\n3. My PIN\n4. Change Language\n5. Manage Favourite\n6. Pending Transaction\n7. Min\n00 Next\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1" || choice=="2" || choice=="3" || choice=="4" || choice=="5" || choice=="6" || choice=="7" || choice=="00" )
   {
      system("clear");
         wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
         wait_timer();
   cout<<"\nWrong Choice. Try again later!\n\n";

   }
} 

else if(choice=="6"){
   system("clear");
   wait_timer();
   cout<<"\nPlease Select\n\n1. Transfer to Bank\n2. Insurance\n3. Savings\n99 MainMenu\n0  Previous\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1" || choice=="2" || choice=="3" || choice=="99" || choice=="0" )
   {
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
     cout<<"\nWrong Choice. Try again Later!\n\n";

   }
}

else if(choice == "7"){
   system("clear");
   wait_timer();
   cout<<"\n1. Gorilla Games\n\n99 MainMenu\n0  Previous\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1" ||  choice=="99" || choice=="0" )
   {
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
     cout<<"\nWrong Choice. Try again Later!\n\n";

   }

}

else if(choice == "8"){
   system("clear");
   wait_timer();
   cout<<"\n1. User Airtel Code\n2. Merchant Wallet Payment\n3. Self-register as a Merchant\n\n99 MainMenu\n0  Previous\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="1" ||  choice=="2" || choice=="3" || choice=="99" || choice=="0" )
   {
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else{ 
      system("clear");
      wait_timer();
     cout<<"\nWrong Choice. Try again Later!\n\n";

   }

}

else if(choice =="9"){
   exitAtl();
}

else if(choice == "00"){
   system("clear");
   wait_timer();
   cout<<"\n10. Pay Canal\n11. Terms and Condition\n12. Cogebanque\n13. Biz Walle\n14. Others\n\n99 MainMenu\n0  Previous\n\n> ";
   cin>>choice;
   system("clear");
   if(choice=="10" ||choice=="12" || choice=="13" ||choice=="14" || choice=="99" || choice=="0" )
   {
      system("clear");
      wait_timer();
      airtel_prompt();
   }
   else if(choice =="11"){
      system("clear");
      wait_timer();
      cout<<"\n1. Accept Terms and Conditions\n2. De-register from eKash\n\n> ";
      cin>>choice;
      if(choice=="1"){
          system("clear");
         wait_timer();
         cout<<"\nThank You For Accepting Terms and Conditions\n\n";

      }

      else if(choice =="2"){
          system("clear");
         wait_timer();
         cout<<"\n You are De-registered From eKash Succefully\n\n";
      }
      else{
          system("clear");
         wait_timer();
         cout<<"\nWrong Choce. Try again Later!\n";
      }
   }
   
   else{ 
      system("clear");
      wait_timer();
     cout<<"\nWrong Choice. Try again Later!\n\n";

   }

}


else{
   system("clear");
   wait_timer();
   cout<<"\nWrong choice. Try Again!\n\n";
   airtel_prompt();
}

}


void mtn_airtime(){
   system("clear");
   float mtn_airtime_balance=120;
   wait_timer();
   cout<<"\nBalance: "<<fixed << setprecision(2)<<mtn_airtime_balance<<"F.\n\n";
    
}



void airtel_airtime(){
  system("clear");
   float airtel_airtime_balance=150;
   wait_timer();
   cout<<"\nBalance: "<< fixed << setprecision(2)<<airtel_airtime_balance<<"F.\n\n";
   
}
};


int main(){
   Network_providers open;
   system("clear");
     open.Sim();
  
}