num=int(input("enter the value:"))
cf=input("enter the c or f:")
c=((num-32)*(5/9))
f=(num*(9/5))+32
if cf==c:
    print(f"the conversion of fahrenheit to celsius:{c}")
elif cf==f:
    print(f"the conversion of celsius to fahrenheit:{f}")
else:
    print("please enter c or f")
    