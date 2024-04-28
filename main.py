print("Давай сыграем в игру. Введи любое число. Если оно делится на 3, я скажу 'Fizz', если оно делится на 5, я скажу 'Buzz', а если оно делится и на 3 и на 5, я скажу 'FizzBuzz'!")
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")