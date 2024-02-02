import random
import string
name=input("What's your name ? : ")
print(f"Welcome Mr.{name} to our automatic password generator program.")
yes_no=input("Do you want to create a random password ?\n(Type Y for Yes and N for No) : ")
if yes_no == "Y":
    letters=string.ascii_uppercase + string.ascii_lowercase
    numbers=string.digits
    symbols=string.punctuation
    digits_no=int(input("How many digits do you want ? :"))   
    letters_no=int(input("How many letters do you want ? :"))
    numbers_no=int(input("How many numbers do you want ? :"))
    symbols_no=int(input("How many symbols do you want ? :"))
    if (int(letters_no+numbers_no+symbols_no))== digits_no :
        password=""
        for char in range(0,letters_no):
            password+=random.choice(letters)
        for char in range(0,numbers_no):
            password+=random.choice(numbers)
        for char in range(0,symbols_no):
            password+=random.choice(symbols)
        password_list=list(password)
        random.shuffle(password_list)
        shuffled_list=""
        for char in password_list:
            shuffled_list+=char
        print(f"Here is your random generated password : {shuffled_list}")
    else:
        print("The sum of letters, numbers, symbols may exceed or less than total digit.\nPlease check your input again.......")
else:
    print(f"It's ok, Mr.{name}\nSorry for your time-loss")       
