hi = int(input("give me the upper limit: "))
lo = 0

while True:
    guess = int((lo + hi) / 2)
    print(f"is {guess} too high(h), too low(l), or correct(c)?")
    answer = input()
    if answer == "h" :
        hi = guess
    elif answer == "l":
        lo = guess
    elif answer == "c":
        print("Yayy")
        break
    elif answer == "end":
        print("Your loss")
        break
    else:
        print("Wrong answer!")

        
        
    
        