names = []
marks = []

while True:
    
    student_name = input("\nEnter student name: ")
    if student_name:
        names.append(student_name)
    
    while True:
            try:
                 student_mark = int(input("\nEnter student makrks: "))
                 if student_mark:
                      marks.append(student_mark)
                      break
            except ValueError:
                 print("\nInvalid makrs!")
                 break
    choice = input("\nDo you want to enter other student details? Y/N: ").lower()
    if choice == "y":
         continue
    elif choice == "n":
        for entry in marks:
             ascending_marks = sorted(marks)
        print(f"\nAscending marks: {ascending_marks}")

        choice = input("\nDo you want to enter other student details? Y/N: ").lower()
        if choice == "y":
              continue
        elif choice == "n":
            break
    else:
         print("\nInvalid choice!")