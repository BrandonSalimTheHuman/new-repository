x1 = eval(input("Enter the x-coordinate for point 1: "))
y1 = eval(input("Enter the y-coordinate for point 1: "))
x2 = eval(input("Enter the x-coordinate for point 3: "))
y2 = eval(input("Enter the y-coordinate for point 2: "))
print("The slope for the line that connects the points (" + str(x1) + ",", str(y1) + ") and (" + str(x2) + ","
      , str(y2) + ") is", round((y2 - y1) / (x2 - x1), 5))