age=int(input("Enter your age: "))
fess=input("are you payid fess: (select yes or no) ")
testimony=input("do you have a testimony: (select yes or no) ")
if age >=18 <25 and fess=="yes" and testimony=="yes":
    print("you are eligible for the course")
elif age >=25 and fess=="yes":
    print("you are eligible for the course")
else:
    print("you are not eligible for the course")    

