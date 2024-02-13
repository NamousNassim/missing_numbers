# search for a single missing number 
numbers = [1,3,4,6,7]

missing_number=0 
missing_numbers=[]
for i in range(len(numbers)):
    if numbers[i] + 1 != numbers[i + 1]: 
        missing_number = numbers[i] + 1 
        break 

# search for multiple missing number 
for i in range(len(numbers) - 1) :
    if  numbers[i]  +   1 !=    numbers[i   +   1]:
        missing_numbers.append(numbers[i] + 1)


print(f"the missing number is {missing_number}")
print(f"the missing numbers are : {missing_numbers}")