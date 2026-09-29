expressions=input("Expression: ")
x_str,y,z_str=expressions.split()
x=int(x_str)
z=int(z_str)
if y=="+":
    ans=x+z
    print(float(ans))
elif y=="-":
    ans=x-z
    print(float(ans))
elif y=="*":
    ans=x*z
    print(float(ans))
elif y=="/":
    if z!=0:
        ans=x/z
        print(float(ans))
    else:
        print("Division by zero is not allowed, Please enter differen integer")
else:
    print("invalid expression, Please choose valid expression")

