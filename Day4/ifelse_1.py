name=input("Enter your name: ")
age=int(input("Enter your age \"{}\": ".format(name)))

if age<18:
    print("caome back {} year after".format(18-age))
else:
    print("you can vote")
