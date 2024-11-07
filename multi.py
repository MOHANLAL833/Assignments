class multiclass():
 def subfields():
    print("The sub fields in AI are")
    list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
    for i in list:
        print (i)
 def oddeven():
    io=int(input("Enter the number"))
    if io%2==0:
        print(f"{io} is even")
        mess="even"
    else:
        print(f"{io} is odd")
        mess="odd"
        return mess
 def marriage():
    gender=input("Enter your Gender")
    age=int(input("Enter your age"))
    if gender=="Male":
        if age>21:
            print("You are eligible for marriage")
            mar="Eligible"
        else:
            print("you are not eligible for marriage")
            mar="not eligible"
    elif(gender=="Female"):
        if age>18:
             print("You are eligible for marriage")
             mar="Eligible"
        else:
            print("you are not eligible for marriage")
            mar="not eligible"
        return mar
 def percent():
    sub1=int(input("Subject1:"))
    sub2=int(input("Subject2:"))
    sub3=int(input("Subject3:"))
    sub4=int(input("Subject4:"))
    sub5=int(input("Subject5:"))
    total=sub1+sub2+sub3+sub4+sub5
    percentage=total/5
    print("Total",total)
    print("Percentage",percentage)
 def area():
    height=int(input("Height:"))
    breadth=int(input("breadth:"))
    print("Area formula: (Height*Breadth)/2")
    area=(height*breadth)/2
    print("Area of Area of Triangle:",area)
    return area
def perimeter():
    height1=int(input("Height1:"))
    height2=int(input("Height2:"))
    breadth=int(input("Height:"))
    print("Perimeter formula: Height1+Height2+Breadth")
    perimeter=height1+height2+breadth
    print("Perimeter of Triangle:",perimeter)
    return perimeter