# Q1
n = int(input("Enter N: "))
num = int(input("Enter number: "))

print("Primes:", end=" ")
for i in range(2, n + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")

fact = 1
for i in range(1, n + 1):
    fact *= i
print("\nFactorial:", fact)

a, b = 0, 1
print("Fibonacci:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

x = num
s = 0
rev = 0

while x > 0:
    d = x % 10
    s += d
    rev = rev * 10 + d
    x //= 10

print("\nDigit Sum:", s)
print("Reverse:", rev)


# Q2
n = int(input("\nEnter pattern size: "))

print("Right Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\nNumber Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nMultiplication Grid")
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j, end="   ")
    print()


# Q3
txt = input("\nEnter a string: ")

rev1 = ""
for ch in txt:
    rev1 = ch + rev1

rev2 = txt[::-1]

clean = ""
for ch in txt:
    if ch != " ":
        clean += ch.lower()

pal = clean == clean[::-1]

vow = 0
con = 0
dig = 0

for ch in txt:
    if ch.isdigit():
        dig += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vow += 1
        else:
            con += 1

print("Loop Reverse:", rev1)
print("Slice Reverse:", rev2)
print("Palindrome:", "Yes" if pal else "No")
print("Vowels:", vow)
print("Consonants:", con)
print("Digits:", dig)


# Q4
name = input("\nCustomer: ")
units = int(input("Units: "))

if units <= 100:
    amt = units * 3.5
elif units <= 200:
    amt = 100 * 3.5 + (units - 100) * 5
elif units <= 300:
    amt = 100 * 3.5 + 100 * 5 + (units - 200) * 7
else:
    amt = 100 * 3.5 + 100 * 5 + 100 * 7 + (units - 300) * 8.5

print("Customer:", name)
print("Units:", units)
print("Amount: ₹", round(amt, 2))


# Q5
amt = int(input("\nWithdrawal Amount: "))

if amt > 20000 or amt % 10 != 0:
    print("Transaction Rejected")
else:
    x = amt

    n500 = x // 500
    x %= 500

    n200 = x // 200
    x %= 200

    n100 = x // 100
    x %= 100

    n50 = x // 50
    x %= 50

    n10 = x // 10

    total = n500 + n200 + n100 + n50 + n10

    print("500 notes:", n500)
    print("200 notes:", n200)
    print("100 notes:", n100)
    print("50 notes:", n50)
    print("10 notes:", n10)
    print("Total Notes:", total)
    print("Amount: ₹", amt)


# Q6
entry = input("\nEntry Time: ")
exit_t = input("Exit Time: ")

eh, em = map(int, entry.split(":"))
xh, xm = map(int, exit_t.split(":"))

start = eh * 60 + em
end = xh * 60 + xm

if end < start:
    end += 24 * 60

duration = end - start
hrs = duration // 60
mins = duration % 60

bill_hrs = (duration + 59) // 60

if bill_hrs <= 1:
    fee = 30
else:
    fee = 30 + (bill_hrs - 1) * 20

print("Parking Duration:", hrs, "hours", mins, "minutes")
print("Billable Hours:", bill_hrs)
print("Parking Fee: ₹", fee)


# Q7
n = int(input("\nNumber of Deliveries: "))

dist = 0
earn = 0

for i in range(1, n + 1):
    d = float(input("Distance for delivery " + str(i) + ": "))
    dist += d

    if d <= 5:
        e = 40
    else:
        e = 40 + (d - 5) * 8

    earn += e

avg = dist / n

print("Total Distance:", round(dist, 2), "km")
print("Total Earnings: ₹", round(earn, 2))
print("Average Distance:", round(avg, 2), "km")


# Q8
x = int(input("\nEnter integer: "))

sign = -1 if x < 0 else 1
x = abs(x)
rev = 0

while x > 0:
    d = x % 10
    rev = rev * 10 + d
    x //= 10

print(sign * rev)


# Q9
x = int(input("\nEnter integer: "))

if x < 0:
    print(False)
else:
    old = x
    rev = 0

    while x > 0:
        d = x % 10
        rev = rev * 10 + d
        x //= 10

    print(old == rev)


# Q10
n = int(input("\nEnter N: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
