def fun():
    s = int(input("Enter the first number: "))
    a = int(input("Enter the second number: "))

    results=[]
    
    add = s + a
    mul = s * a
    if a != 0:
        div = s / a
        rem = s % a
    else:
        div = "Error: Division by zero"
        rem = "Error: Division by zero"
        #using list
    results.append(add)
    results.append(mul)
    results.append(div)
    results.append(rem)
    
    print("Addition:", add)
    print("Multiplication:", mul)
    print("Division:", div)
    print("Remainder:", rem)
fun()
