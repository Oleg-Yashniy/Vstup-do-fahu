while True:
    x = float(input("First number:"))
    op = input("Operation")
    y = float(input("Second number:"))

    result = None

    if op == "+":
        result = x+y
    elif op == "-":
        result = x-y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = x/y
    elif op == "**":
        result = x**y
    else:
        print("Unsuccesfull operation")
    if result is not None:
        print("Result:",result)
    end = input("Enter to continue Back to leave")
    if end == ("Back"):
        break
