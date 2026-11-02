#Problem 1 – FizzBuzz
# Difficulty: Easy
# Print numbers from 1 to 100. Print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if
# divisible by both, otherwise print the number.
# Uses: Loop, if-elif-else, % operator.

for i in range(1,51):
   if i%3==0 and i%5==0:
       print("Fizzbuzz")
   elif i%3==0:
     print("Fizz")
   elif i%5==0:
     print("Buzz")
 
   else:
     print(i)


# Find the sum and average of a list without using sum() or statistics.mean().
# Uses: Lists, Loop, Variables.

l = [15,45,43,24,75]
total=0

for i in range(len(l)):
   total=total+l[i]

average = total/len(l)

print("sum:",total)
print("average",average)

# Find the largest element in a list without using max().
# Uses: Lists, Loop, if.

l = [12,45,31,22,65]

largest=l[0]
for i in l:
  if i>largest:
    largest=i

print('largest element is:', largest)


# Prime Number Check
# Check whether a given number is Prime or Not Prime.
# Uses: Loop, if, % operator.

num = int(input("Enter a number: "))

for i in range(2,num):
  if num < 2:
   print("it is not a prime number")
   break
  elif num%i==0:
    print("it is not a prime number")
    break
else:
    print("it is a prime number")


# Find the duplicate elements in a list and display how many times each duplicate occurs:-

num = [2,1,4,6,3,2,1,4]

visited=[]

for i in num:
  if i not in visited:
    count=0

    for j in num:
      if i==j:
        count+=1

  if count>1:
    print(i,"occurs",count,"times")

visited.append(i)


#Given nums = [34, 12, 78, 5, 60] , find the smallest number without using min()

nums = [34,12,78,5,60]

smallest = nums[0]

for i in nums:
  if i<smallest:
    smallest=i

print(smallest,"is smallest")

# Print all prime numbers between 1 and 50, and count how many there are

count =0

for i in range(1,51):
  if i<2:
    continue
  for j in range(2,i):
    if i%j==0:
     break
  else:
      print(i,"is prime")
      count = count + 1
print("total prime numbers are :",count)
  

# Given items = [1, 2, 2, 3, 4, 4, 4, 5] , build a new list with each number
# appearing only once. Expected: [1, 2, 3, 4, 5]

items = [1, 2, 2, 3, 4, 4, 4, 5]

new_list=[]

for i in items:
  if i not in new_list:
    new_list.append(i)
    
print(new_list)


# Given nums = [23, 67, 12, 89, 45] , find the second largest number without
# sorting and without max() . Answer: 67

nums = [23, 67, 12, 89, 45]

largest=second=0

for i in nums:
  if i>largest:
    second=largest
    largest=i
print(second)


# Given items = [3, 1, 3, 2, 3, 1, 2, 3] , find the number that appears the most
# times. Answer: 3 (appears 4 times).

items = [3, 1, 3, 2, 3, 1, 2, 3]

mcont=freq=0

for i in items:
  count=0
  for j in items:
    if i==j:
      count=count+1

  if count>mcont:
    mcont=count
    freq=i

print(freq,"appears",mcont,"times")
