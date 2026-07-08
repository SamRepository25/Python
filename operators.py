a=10
b=3
#Arithematic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reminder
print(a**b) #10*10*10
print(a//b) #floor gives round off value

#Comparsion

x=5
y=10

print(x==y)
print(x>y)
print(x<y)
print(x != y)

#Logical

print("Logical")
g=True
v=False

print(g and v)
print(g or v)
print(not g)

#Billing Calculation as Example
print("Example Calc")
amount = 1200
tax = amount * 0.18
total = tax + amount

print(total)

if total > 1000:
    discount = total * 0.10
    total -= discount

print(total)

#Logical and Comparsion Operators Example
print("Logical and Comparsion Oprtators")

age = int(input("Enter your age :"))
student = (input("Are you a Student :"))

if age >= 60 or student == "yes":
    print("Eligible for discount!")
else:
    print("Not Eligible for discount!")