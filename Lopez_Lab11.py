Grades_List = [ ]
Passers = 0 


while True:
    Grade=input("student grade / type 'done' if finished:")

    if Grade.lower() == 'done':
        break 
    
    
    
    if Grade.isdigit(): 
        Grade = int(Grade)
        
        if 40 > Grade and 100 < Grade: 
            print("Invalid/error, please enter a digit between 40-100")
        
        else: 
            Grades_List.append(Grade)
            if Grade >= 75:
                Passers += 1
        
    else: 
        print("enter a valid number")
            
if Grades_List: 
    Total_Grades = sum(Grades_List)
    Avg= Total_Grades / len(Grades_List)
    Percentage= (Passers/ len(Grades_List))*100

    print(f"Avg grade of all students: {Avg:.2f}")
    print(f"Passers: {Passers}")
    print(f"Passing Rate: {Percentage:.2f}%")
    print(f"Grades: {Grades_List}")
    
else: 
    print("No valid grades entered")
