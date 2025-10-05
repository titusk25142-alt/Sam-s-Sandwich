def force_number(message,lower,upper):
    print("force number function")
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break
            else:
                print("Invalid number")
        except:
            print("Error- only type in numbers please")
    return num
def bread_selection():
    bread_list = ["White","Brown","Italian","Granary"]
    count = 0
    print("We have the following breads: ")
    while count < len(bread_list):
        print(count+1," ",bread_list[count])
        count += 1
    bread_selected = force_number("Which bread did you want? Enter a number: ")
    return bread_list[bread_selected]
def meat_selection():
    meat_list = ["Turkey","Salami","Ham","Roasted Chicken"]
    count = 0
    print("We have the following meats: ")
    while count < len(meat_list):
        print(count+1," ",meat_list[count])
        count += 1
    meat_selected = force_number("Which meat did you want? Enter a number: ")
    return meat_list[meat_selected]
def cheese_selection():
    cheese_list = ["Mozarella","Cheddar","Blue Cheese"]
    count = 0
    print("We have the following cheese: ")
    while count < len(cheese_list):
        print(count+1," ",cheese_list[count])
        count += 1
    cheese_selected = force_number("Which cheese did you want? Enter a number: ")
    return cheese_list[cheese_selected]
def dressing_selection():
    dressing_list = ["Mayonese","Ketchup","Mustard"]
    count = 0
    print("We have the following dressing: ")
    while count < len(dressing_list):
        print(count+1," ",dressing_list[count])
        count += 1
    dressing_selected = force_number("Which dressing did you want? Enter a number: ")
    return dressing_list[dressing_selected]
#main program
print("Welocme to Sam's Sandwich Shop")
bread_choice = bread_selection()
meat_choice = meat_selection()
cheese_choice = cheese_selection()
dressing_choice = dressing_selection
print(f"Your selected bread: {bread_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected cheeseL {cheese_choice}")
print(f"Your selected dressing: {dressing_choice}")