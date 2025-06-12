height=int(input("enter your height in cm:"))
age=int(input("enter your age in years:"))

if height>=120:
    print("valid to go through:")
    if age<=12 :
        print("pay $5")

    if age>=18:
        print("pay $20 per visit:")

    else:
        print("not valid:")