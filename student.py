#def student_data():
name = input("Enter student name :- ")
class_1 = input("Enter class :- ")
sid = int(input("Enter id :- "))
roll= int(input("Enter roll no :- "))
sub1 = str(input("Enter sub 1 :- "))
sub2 = str(input("Enter sub 2 :- "))
sub3 = str(input("Enter sub 3 :- "))
sub4 = str(input("Enter sub 4 :- "))
student1 = {"Student name":name,"Sid":sid, "roll no": roll, " sub1": sub1," sub2": sub2," sub3": sub3," sub4": sub4}


def exam_data():
    print("Enter marks obtain in :-  "+sub1)
    sub1m = int(input())
    print("Enter marks obtain in :- "+sub2)
    sub2m=int(input())
    print("Enter marks obtain in :- " + sub3)
    sub3m = int(input())
    print("Enter marks obtain in :- " + sub4)
    sub4m = int(input())

    marks={"sub1":sub1m,"sub2":sub2m,"sub3":sub3m,"sub4":sub4m,}
    total_marks_obtained = int(sub1m+sub2m+sub3m+sub4m)
    avg_marks = (total_marks_obtained/4)
    total_marks=400
    pass_marks = .4*total_marks
    print("Total marks obtained",total_marks_obtained)
    print("Average marks",avg_marks)
    if total_marks_obtained < pass_marks:
        print("Fail")
    else:
        print("Pass")
