cat_attributes = {
    "intelligence":10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour=input("Enter Colour:")

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. feed it 4.put it to sleep 5. print stats")
    energysnatcher=-12
    energygiver=+4
    weightsnatcher=-2
    weightgiver=+4
    intelligencesnatcher=-5
    intelligencegiver=+7

    if option == '1':
       cat_attributes.update({"energy":cat_attributes["energy"]-energysnatcher})
       cat_attributes.update({"weight":cat_attributes["weight"]-weightsnatcher})
       
    elif option =="2":
        cat_attributes.update({"energy":cat_attributes["energy"]-energysnatcher})
        cat_attributes.update({"intelligence":cat_attributes["intelligence"]+intelligencegiver})
    elif option=="3":
        cat_attributes.update({"weight":cat_attributes["weight"]+weightgiver})
        cat_attributes.update({"energy":cat_attributes["energy"]-energysnatcher})
    elif option=="4":
        cat_attributes.update({"energy":cat_attributes["energy"]+energygiver})
       
    elif option=="5":
        print(cat_attributes)



    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        print("its dead ")