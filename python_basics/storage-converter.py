
def home():
    print("\nSelect Opartion \n\n1.Byte       (B)\n2.Kylobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Terabyte  (TB)\n6.Petabyte  (PB)\n7.Exabyte   (EB)\n8.Zettabyte (ZB)\n9.Yottabyte (YB)")
    return 

def byte():
    while True:
        print("\nConvert Byte to: \n\n1.Kylobyte  (KB)\n2.Megabyte  (MB)\n3.Gigabyte  (GB)\n4.Terabyte  (TB)\n5.Petabyte  (PB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return  

def kilobyte():
    while True:
        print("\nConvert KiloByte to: \n\n1.Byte      (B)\n2.Megabyte  (MB)\n3.Gigabyte  (GB)\n4.Terabyte  (TB)\n5.Petabyte  (PB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return 

def megabyte():
    while True:
        print("\nConvert MegaByte to: \n\n1.Byte      (B)\n2.Kilobyte  (KB)\n3.Gigabyte  (GB)\n4.Terabyte  (TB)\n5.Petabyte  (PB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return  

def gigabyte():
    while True:
        print("\nConvert GigaByte to: \n\n1.Byte      (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Terabyte  (TB)\n5.Petabyte  (PB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return 

def terabyte():
    while True:
        print("\nConvert TeraByte to: \n\n1.Byte       (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Petabyte  (PB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return  

def petabyte():
    while True:
        print("\nConvert PetaByte to: \n\n1.Byte      (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Terabyte  (TB)\n6.Exabyte   (EB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return 


def exabyte():
    while True:
        print("\nConvert exaByte to: \n\n1.Byte       (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Terabyte  (TB)\n6.Petabyte  (PB)\n7.Zettabyte (ZB)\n8.Yottabyte (YB)")
        return 

def zettabyte():
    while True:
        print("\nConvert zettaByte to: \n\n1.Byte       (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Terabyte  (TB)\n6.Petabyte  (PB)\n7.Exabyte   (EB)\n8.Yottabyte (YB)")
        return     

def yottabyte():
    while True:

        print("\nConvert YottaByte to: \n\n1.Byte      (B)\n2.Kilobyte  (KB)\n3.Megabyte  (MB)\n4.Gigabyte  (GB)\n5.Terabyte  (TB)\n6.Petabyte  (PB)\n7.Exabyte   (EB)\n8.Zettabyte (ZB)")
        return     



def main():
    while True:

        home()
        choice = input("\n> ").lower()
        if choice == "1":
            byte()
            choice = input("\n> ").lower()
        elif choice == "2":
            kilobyte()
            choice = input("\n> ").lower()
        elif choice == "3":
            megabyte()
            choice = input("\n>").lower()

        elif choice == "4":
            gigabyte()
            choice = input("\n> ").lower()

        elif choice == "5":
            terabyte()
            choice = input("\n> ").lower()

        elif choice == "6":
            petabyte()
            choice = input("\n >").lower()
            
        elif choice == "7":
            exabyte()
            choice = input("\n> ").lower()
        elif choice == "8":
            zettabyte()
            choice = input("\n> ").lower()
        elif choice == "9":
            yottabyte()
            choice = input("\n> ").lower()
        elif choice == "exit" or choice == "quit":
            break

        else:
            print("Invalid choice. ")
            




if __name__ =="__main__":
    main()