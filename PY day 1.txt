# Q1
c = float(input("Enter Celsius: "))
f = c * 9 / 5 + 32
k = c + 273.15

print("Celsius:", round(c, 2))
print("Fahrenheit:", round(f, 2))
print("Kelvin:", round(k, 2))

print("\nConversion Table")
print("Celsius Fahrenheit Kelvin")

for c in range(-40, 101, 10):
    f = c * 9 / 5 + 32
    k = c + 273.15
    print(c, round(f, 2), round(k, 2))


# Q2
a, b, c = map(float, input("\nEnter 3 numbers: ").split())
n = int(input("Enter a number: "))

print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))
print("Average:", round((a + b + c) / 3, 2))

if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    if n % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")


# Q3
yr = int(input("\nYear: "))
m = float(input("Marks: "))

if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
    print(yr, "is a Leap Year")
else:
    print(yr, "is not a Leap Year")

if m < 0 or m > 100:
    print("Invalid marks")
else:
    if m >= 90:
        g = "A+"
    elif m >= 80:
        g = "A"
    elif m >= 70:
        g = "B"
    elif m >= 60:
        g = "C"
    elif m >= 50:
        g = "D"
    else:
        g = "F"
    print("Grade:", g)

items = []

while True:
    x = input("\nEnter price or done: ")

    if x.lower() == "done":
        break

    try:
        p = float(x)
        if p < 0:
            print("Price cannot be negative")
        else:
            items.append(p)
    except:
        print("Enter a valid price")

sub = sum(items)

if sub >= 1000:
    dis_rate = .10
elif sub >= 500:
    dis_rate = .05
else:
    dis_rate = 0

dis = sub * dis_rate
amt = sub - dis
tax = amt * .05
final = amt + tax

print("\nItem Price")
for i, p in enumerate(items, 1):
    print(i, p)

print("Subtotal:", sub)
print("Discount:", dis)
print("Tax:", tax)
print("Final Amount:", final)


# Q4
yr = int(input("\nYear: "))
m = float(input("Marks: "))

if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
    print(yr, "is a Leap Year")
else:
    print(yr, "is not a Leap Year")

if m < 0 or m > 100:
    print("Invalid marks")
else:
    if m >= 90:
        g = "A+"
    elif m >= 80:
        g = "A"
    elif m >= 70:
        g = "B"
    elif m >= 60:
        g = "C"
    elif m >= 50:
        g = "D"
    else:
        g = "F"
    print("Grade:", g)

items = []

while True:
    x = input("\nEnter price or done: ")

    if x.lower() == "done":
        break

    try:
        p = float(x)
        if p < 0:
            print("Price cannot be negative")
        else:
            items.append(p)
    except:
        print("Enter a valid price")

sub = sum(items)

if sub >= 1000:
    dis_rate = .10
elif sub >= 500:
    dis_rate = .05
else:
    dis_rate = 0

dis = sub * dis_rate
amt = sub - dis
tax = amt * .05
final = amt + tax

print("\nItem Price")
for i, p in enumerate(items, 1):
    print(i, p)

print("Subtotal:", sub)
print("Discount:", dis)
print("Tax:", tax)
print("Final Amount:", final)


# Q5
a = int(input("\nEnter a: "))
b = int(input("Enter b: "))

print("Before Swap:", a, b)
a, b = b, a
print("After Swap:", a, b)


# Q6
p = float(input("\nPrincipal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

if p < 0 or t < 0:
    print("Principal and time must be non-negative")
else:
    si = p * r * t / 100
    total = p + si

    print("Principal:", p)
    print("Rate:", r, "%")
    print("Time:", t, "years")
    print("Simple Interest:", si)
    print("Total Amount:", total)

v = input("\nEnter a value: ")
print("Original type:", type(v).__name__)

try:
    x = int(v)
    print("Integer:", x)
    print("Type:", type(x).__name__)
except:
    print("Invalid integer")

try:
    x = float(v)
    print("Float:", x)
    print("Type:", type(x).__name__)
except:
    print("Invalid float")


# Q7
p = float(input("\nPrincipal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

if p < 0 or t < 0:
    print("Principal and time must be non-negative")
else:
    si = p * r * t / 100
    total = p + si

    print("Principal:", p)
    print("Rate:", r, "%")
    print("Time:", t, "years")
    print("Simple Interest:", si)
    print("Total Amount:", total)

v = input("\nEnter a value: ")
print("Original type:", type(v).__name__)

try:
    x = int(v)
    print("Integer:", x)
    print("Type:", type(x).__name__)
except:
    print("Invalid integer")

try:
    x = float(v)
    print("Float:", x)
    print("Type:", type(x).__name__)
except:
    print("Invalid float")


# Q8
a = float(input("\nEnter first value: "))
b = float(input("Enter second value: "))
print("Sum:", a + b)


# Q9
a = 19
b = 3.14
c = "Python"
d = True
e = None

for x in (a, b, c, d, e):
    print("Value:", x, "Type:", type(x).__name__)


# Q10
a = 19
b = 4

print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("-19 // 4 =", -19 // 4)
