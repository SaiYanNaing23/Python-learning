age = int(input("Your Age: ")); 
if age < 18 : print("You are young"); 
elif age>18 and age <30 :print("You are normal age"); 
else : print("you are old"); 

isTired = input("are you tired?  Yes or No? :")

if isTired == "Yes" :
    print("you can rest")
elif isTired == "No" :
    print("you gonna work")
else :
    print("wrong answer try again")

userData1 = input("Please write your name :") ; 
# print(userData);
userData2 =input("Password : ")

if userData1 == "Sai Yan Naing" and userData2 == "pain23":
    print(f"Correct 😎" ); 
else :
    print("Try again invalid Name or Password..."); 
