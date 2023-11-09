age=int(input("enter the age:"))
if age>0 and age<=12:
    print("children")
elif age>13 and age<=19:
    print("teenage")
elif age>20 and age<=59:
    print("adult")
elif age>60 and age<=110:
    print("senior")
else:
    print("dead person or enter the currect age")
    