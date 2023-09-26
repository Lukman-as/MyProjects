x = float(input("Number: "))
y = int(input("Root of: "))
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if (guess**y - x) >= 0.0001:
        break
    else:
        guess += 0.0001

guess = round(guess, 3)
print(str(y)+ "th root of " + str(x) + " is " + str(guess))

         