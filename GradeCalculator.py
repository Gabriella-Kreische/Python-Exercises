#python will store project score into a variable and exam score into another variable
Project_score = int(input("Please enter you project score: "))
Exam_score = int(input("Please enter your exam score: "))
#the final score will be calculated and it will give the user a final grade
Final_score = int((Project_score + Exam_score) * 0.5)
if (Final_score < 50):
    print("Fail")
elif (Final_score >= 50 and Final_score < 60):
    print("Your Final Grade is D")
elif (Final_score >= 60 and Final_score < 70):
    print("Your Final Grade is C")
elif (Final_score >= 70 and Final_score < 80):
    print("Your Final Grade is B")
else:
    print("Your Final Grade is A")
