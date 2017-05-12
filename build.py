#Implement fizz buzz
results = []
def fizzbuzz(n):
    if n%3 == 0 and n%5==0:
        print("FizzBuzz")
        results.append("FizzBuzz")
        return True
    elif n%3 == 0:
        print("Fizz")
        results.append("Fizz")
        return True
    elif n%5 == 0:
        print("Buzz")
        results.append("Buzz")
        return True
    else:
        print("Wrong Number")
        results.append(str(n))
        return True
    print(results)
#fizzbuzz(5)