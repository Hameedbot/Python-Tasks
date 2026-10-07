# Q1
try:
    n = int(input("Integer: "))
    d = float(input("Decimal: "))

    print("Integer:", n)
    print("Type:", type(n).__name__)
    print("Float:", d)
    print("Type:", type(d).__name__)
    print("Rounded:", round(d))

    x = int(d)
    print(n, "/", x, "=", round(n / x, 4))
    print(n, "//", x, "=", n // x)
    print(n, "%", x, "=", n % x)
    print(n, "** 2 =", n ** 2)
    print("String:", str(n))

except:
    print("Invalid numeric input")


# Q2
msg = input("Message: ")
shift = int(input("Shift: "))

def caesar(s, sh):
    ans = ""

    for ch in s:
        if "A" <= ch <= "Z":
            ans += chr((ord(ch) - 65 + sh) % 26 + 65)
        elif "a" <= ch <= "z":
            ans += chr((ord(ch) - 97 + sh) % 26 + 97)
        else:
            ans += ch

    return ans

enc = caesar(msg, shift)
print("Encrypted:", enc)
print("Decrypted:", caesar(enc, -shift))


# Q3
start = int(input("Start: "))
end = int(input("End: "))

print("Num Prime Perfect Armstrong Palindrome Sum Digits Binary")

for n in range(start, end + 1):
    prime = n >= 2

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    ds = sum(i for i in range(1, n) if n % i == 0)
    perfect = n > 1 and ds == n

    digits = len(str(n))
    x = n
    sm = 0
    rev = 0
    arm = 0

    while x > 0:
        d = x % 10
        sm += d
        rev = rev * 10 + d
        arm += d ** digits
        x //= 10

    pal = n == rev
    armstrong = n == arm

    if n == 0:
        binary = "0"
    else:
        x = n
        binary = ""
        while x:
            binary = str(x % 2) + binary
            x //= 2

    print(n, "Yes" if prime else "No",
          "Yes" if perfect else "No",
          "Yes" if armstrong else "No",
          "Yes" if pal else "No",
          sm, digits, binary)


# Q4
a = int(input("Number 1: "))
b = int(input("Number 2: "))

def base(n, b):
    vals = "0123456789ABCDEF"

    if n == 0:
        return "0"

    ans = ""
    while n:
        ans = vals[n % b] + ans
        n //= b

    return ans

x, y = a, b

while y:
    x, y = y, x % y

gcd = x
lcm = abs(a * b) // gcd if gcd else 0

print("Binary:", base(a, 2))
print("Octal:", base(a, 8))
print("Hex:", base(a, 16))
print("GCD:", gcd)
print("LCM:", lcm)


# Q5
n = int(input("N: "))
d1 = int(input("Divisor 1: "))
w1 = input("Word 1: ")
d2 = int(input("Divisor 2: "))
w2 = input("Word 2: ")

for i in range(1, n + 1):
    if i % d1 == 0 and i % d2 == 0:
        print(w1 + w2)
    elif i % d1 == 0:
        print(w1)
    elif i % d2 == 0:
        print(w2)
    else:
        print(i)


# Q6
cnt = int(input("Students: "))
print("Student Total Average Grade")

for _ in range(cnt):
    data = input().split(":")
    name = data[0].strip()

    try:
        marks = [float(x) for x in data[1].split()]

        if any(x < 0 or x > 100 for x in marks):
            print(name, "Invalid marks")
            continue

        total = sum(marks)
        avg = total / len(marks)

        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "F"

        print(name, int(total), round(avg, 2), grade)

    except:
        print(name, "Invalid marks")


# Q7
n = int(input("Transactions: "))
ok = []
bad = 0

for _ in range(n):
    try:
        amt = float(input())

        if amt < 0:
            bad += 1
        else:
            ok.append(amt)
    except:
        bad += 1

print("Successful Transactions:", len(ok))

if ok:
    total = sum(ok)
    print("Total Amount: ₹", round(total, 2))
    print("Highest Transaction: ₹", round(max(ok), 2))
    print("Lowest Transaction: ₹", round(min(ok), 2))
    print("Average Transaction: ₹", round(total / len(ok), 2))
else:
    print("Total Amount: ₹0.00")
    print("Highest Transaction: ₹0.00")
    print("Lowest Transaction: ₹0.00")
    print("Average Transaction: ₹0.00")

print("Rejected Transactions:", bad)


# Q8
s = input("Input: ")
i = 0

while i < len(s) and s[i] == " ":
    i += 1

sign = 1

if i < len(s) and s[i] in "+-":
    if s[i] == "-":
        sign = -1
    i += 1

num = 0

while i < len(s) and "0" <= s[i] <= "9":
    num = num * 10 + ord(s[i]) - ord("0")
    i += 1

print(sign * num)


# Q9
a = input("a = ")
b = input("b = ")

i = len(a) - 1
j = len(b) - 1
carry = 0
ans = ""

while i >= 0 or j >= 0 or carry:
    total = carry

    if i >= 0:
        total += ord(a[i]) - ord("0")
        i -= 1

    if j >= 0:
        total += ord(b[j]) - ord("0")
        j -= 1

    ans = str(total % 2) + ans
    carry = total // 2

print(ans)


# Q10
n = int(input("Enter number: "))
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    total = 0

    while n:
        d = n % 10
        total += d * d
        n //= 10

    n = total

print(n == 1)
