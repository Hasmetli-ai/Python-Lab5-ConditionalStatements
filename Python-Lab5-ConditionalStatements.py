def proyekt1():
    while True:
        try:
            weight=float(input("Please add your weight as kilogram"))
            height=float(input("Please add your height as a metr"))
        except ValueError:
            print("Please add an integer and dont use any symbol or letter.")
        else:
            break
    Bmi=weight/(height**2)
    if Bmi<18.5:
        print("Underweight")
    elif Bmi>=18.5 and Bmi<=24.9:
        print("Normal weight")
    elif Bmi>=25.0 and Bmi<=29.9:
        print("Overweight")
    else:
        print("Obese")



def proyekt2():
    birthyear=int(input("Please enter your birth year"))
    zodiac_cycle={0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",4:"Rat"
                ,5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep"}
    zodiac=zodiac_cycle[birthyear%12]
    print(zodiac)

def proyekt3():
    print("|Welcome to the birthday guessing game!!|")
    set1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
    set2=[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
    set3=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
    set4=[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
    set5=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    print(f" set 1={set1}\n set 2={set2}\n set 3 ={set3}\n set 4 ={set4}\n set 5={set5}\n")
    while True:
        try:
            lst=list(map(int,input("look at the number sets and if you're birhday is in there type 1 except 0 ").split()))
        except ValueError:
            print("Please add an number not a letter or any word ")
        else:
            break       
    first=[1,2,4,8,16]
    sum=0
    for i in range(5):
        if lst[i]==0:
            continue
        sum+=first[i]
    print(f"Your birtdahy is {sum}")
    

while True:
    print("\n MENU")
    print("1-Proje 1")
    print("2-ZodiacCalculator")
    print("3-Birthday Finder")
    print("0-Exit")
    choose = input()
    if choose == "0":
        print("Leaving the program goodbye")
        break
    elif choose == "1":
        print("Loading the program")
        proyekt1()
    elif choose == "2":
        print("Loading the program")
        proyekt2()
    elif choose == "3":
        print("Loading the program")
        proyekt3()
    else:
        print("Invalid choose please try again")
