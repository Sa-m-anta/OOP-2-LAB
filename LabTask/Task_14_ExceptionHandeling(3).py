salary = [5, 10, 15, 20]

try:
    try:
        for i in salary:
            b = int(input("Enter a number: "))
            print(i / b)
    except ZeroDivisionError:
        print("Value divided by zero")

    except ValueError:
        print("Value error")
    except TypeError:
        print("Type error")

except NameError:
    print("Name error")
except IndexError:
    print("Arithmetic error")
except:
    print("error occured")
else:
    print("else executed")
finally:
    print("Finally executed")
