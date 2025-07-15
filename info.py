def function(ans):
    return f"{ans}"

num1=(input("enter number:"))
num2=(input("enter number:"))
try:
    if num1.isdigit() and num2.isdigit():
        num1=int(num1)
        num2=int(num2)
        
        if num1<=0 and num2<=0:
            print("u cant enter 0 or negitive numbers")
        else:
            ans=num1+num2
            print(f"your given num1 = {num1} and num2 = {num2} and sum of them is = {function(ans)}")
            
except:
    print("wrong input")

    