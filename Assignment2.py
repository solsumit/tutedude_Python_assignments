#print sum of 1-50 using for loop

total_sum= 0
for num in range(1,51):
    total_sum = total_sum + num

print(f'the total sum of numbers from 1 to 50 is {total_sum} ')

#print integers odd or even

number= int(input("Enter a number "))

if number % 2 == 0:
    print(f"{number} is an Even number ")

else   :
    print(f"{number} is an odd number ")
