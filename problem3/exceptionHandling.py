while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print(x, " is a number")
    finally:
        print("Done")
