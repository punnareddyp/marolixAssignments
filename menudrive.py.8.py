print("menu:")
print("1.calucate the area")
print("2.calucate the perimeter")
print("3.exit")
choice=int(input("enter the choice"))
if choice==1:
    l=float(input("enter the length value:"))
    w=float(input("enter the width value:"))
    area=l*w
    print(f"the area of rectangle is:{area}")
elif choice==2:
    l=float(input("enter the length value:"))
    w=float(input("enter the width value:"))
    perimeter=2*(l+w)
    print(f"the perimeter of rectangle is:{perimeter}")
elif choice==3:
    exit
else:
    print("choose the right choice 1 ro 2 or 3")
    
