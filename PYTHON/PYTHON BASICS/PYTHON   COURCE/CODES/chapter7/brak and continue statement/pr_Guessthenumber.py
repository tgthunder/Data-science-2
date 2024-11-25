n=12
number_of_guess = 1
print("NUMBER OF GUESSES IS LIMITED TO ONLY 5 TIMES")
while (number_of_guess<=5):
    Guess_number =int(input("Guess the number:\n"))
    if Guess_number<12:
        print("INCREASE VALUE\n")
    elif Guess_number>12:
        print("DECREASE VALUE\n")    
    else:
        print("CONGRATULATINS! YOU WON")
        print(number_of_guess,"number of guesses be took to finish")    
        break
    print(5-number_of_guess,"No of guesses left")
    number_of_guess+=1
if (number_of_guess>5):
    print("YOU LOST")