#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>
#include <ctime>
using namespace std;

 string getCurrentTime() {
        auto now = chrono::system_clock::now();

        time_t currentTime = chrono::system_clock::to_time_t(now);

        tm* localTime = localtime(&currentTime);

        stringstream timeStream;

        timeStream << put_time(localTime, "%H:%M:%S")<<endl;
        return timeStream.str();
        this_thread::sleep_for(chrono::seconds(1));


}


int main(){
    
    while (true){
        auto now = chrono::system_clock::now();

        time_t currentTime = chrono::system_clock::to_time_t(now);

        tm*localTime = localtime(&currentTime);


        system("clear");
        
        cout<< put_time(localTime, "%H:%M:%S")<<endl;

        this_thread::sleep_for(chrono::seconds(1));

}



 return 0;
}
