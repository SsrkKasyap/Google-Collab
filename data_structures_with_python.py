# -*- coding: utf-8 -*-
"""Data Structures With Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sWo9COtCoMsu3Qz6CAxribG95MIEd34H
"""

#1
#a.Find minimum among three numbers.
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

minimum = 0

if a < b and a < c :
    minimum  = a
if b < a and b < c :
    minimum = b
if c < a and c < b :
    minimum = c

print(minimum, "is the minimum of three numbers.")

#b. Find hcf Gcd & lcm of two numbers

# Defining function to calculate hcf
def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd

# Reading numbers from user
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

# Function call & displaying output GCD
print('GCD of %d and %d is %d' %(first, second, find_gcd(first, second)))

# Calculating LCM
lcm = first * second / find_gcd(first, second)
print('LCM of %d and %d is %d' %(first, second, lcm))

#c.Check whether the given number is perfect.
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

#d. Print Twin Primes up to a specified limit.

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print("{:d} and {:d}".format(i, j))

generate_twins(2, 100)

#e. Print the prime numbers up to a specific limit.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

#f. Find the sum of digits of a number. Check whether given number is Armstrong number or not.

def getSum(N):
    sum = 0
    for digit in str(n):
      sum += int(digit)
    return sum
print(getSum(n))
N = 12345
# Check whether given number is Armstrong number or not.
num = N
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#g
# Python program to swap two number using temporary variable
x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#h. Performs all the five arithmetic operations.
a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c = a - b
print("Line 2 - Value of c is ", c)

c = a * b
print ("Line 3 - Value of c is ", c)

c = a / b
print("Line 4 - Value of c is ", c)

c = a % b
print("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b
print("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b
print ("Line 7 - Value of c is ", c)

"""##Q2
##A

"""

def copy(arr1):
  arr2 = []
  for i in range(len(arr1)):
    arr2.append(arr1[i])
  return arr2
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = copy(list1)
print("list1 : ",list1)
print("list2 : ",list2)

"""##B


"""

def copy_reverse(arr1):
  arr2 = []
  for i in range(len(arr1)-1,-1,-1):
    arr2.append(arr1[i])
  return arr2
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = copy_reverse(list1)
print("list1 : ",list1)

"""##Q4

Linear Search
"""

def linear_Search(array,length,key):
  for i in range(0,length):
    if array[i]==key:
      return i
  return -1

List= []
l = int(input("Enter the size of list"))
print("Enter list elements")
for i in range(0,l):
  a = int(input(""))
  List.append(a)
key=int(input("Key : "))
ans = linear_Search(List,l,key)
print("Array or list",List)
print("Key element : ",key)

if ans==-1:
  print("key not found")
else:
  print("key found at the index position",ans)

"""###Binary Search-Iterative method"""

def binary_search(array,key):
  low = 0
  high = len(array)-1
  mid = 0
  while low<=high:
    mid = (low+high)//2
    if array[mid] < key:
      low = mid+1
    elif array[mid] > key:
      high = mid-1
    else:
      return mid
  return -1
# MAIN CODE
# Taking input list from user
list1= []
l = int(input("Enter the size of list : "))
print("Enter list elements")
for i in range(0,l):
  a = int(input(" "))
  list1.append(a)
key = int(input("Enter key element"))
print("Key element = ",key)
# Function call
ans = binary_search(list1,key)
if ans==-1:
  print("Key not found")
else:
  print("Key found at index position",ans)

"""####5-SLL"""

class Node:
  def __init__(self,data):
    self.item = data
    self.ref = None
class linkedList:
  def __init__(self):
    self.start_node = None
    l_list = input("Enter elements of the list- ").split()
    if len(l_list)!= 0:
      for i in l_list:
        self.insert_at_end(i)
    self.display()
  def user(self):
    while True:
      print("1. Insert\n2. Delete\n3. Search\n4. Count\n5. Display\n6. Exit")
      x = input("Enter function number -")
      if x=='1':
        self.insert()
      elif x=='2':
        self.delete()
      elif x=='3':
        self.search(input("Value to search -"))
      elif x=='4':
        self.count()
      elif x=='5':
        self.display()
      elif x=='6':
        break
      else:
        print("Invalid Input")

  def insert(self):
    print("1. Insert at beginning\n2. Insert at end\n3. Insert at index")
    x=input("Enter function number -")
    if x=='1':
      self.insert_at_start(input("Value -"))
    elif x=='2':
      self.insert_at_end(input("Value -"))
    elif x=='3':
      self.insert_at_index(input("Value -"),input("Index position of value to be inserted -"))
    else:
      print("Invalid Input")
  def insert_at_start(self,data):
    NewNode = Node(data)
    NewNode.ref = self.start_node
    self.start_node = NewNode
  def insert_at_end(self,data):
    if self.start_node is None:
      return self.insert_at_start(data)
    NewNode = Node(data)
    n = self.start_node
    while n is not None:
      if n.ref is None:
        n.ref = NewNode
        break
      n = n.ref
  def insert_at_index(self,data,ind):
    if ind=='1':
      return self.insert_at_start(data)
    n = self.start_node
    NewNode= Node(data)
    c = 2
    while n is not None:
      if c==int(ind):
        NewNode.ref = n.ref
        n.ref = NewNode
        return
      n = n.ref
      c+=1
    print("index is out of the range")

  def delete(self):
    print("1. Delete at beginning\n2. Delete at end\n3. Delete at index")
    x=input("Enter function number -")
    if x=='1':
      self.delete_at_start()
    elif x=='2':
      self.delete_at_end()
    elif x=='3':
      self.delete_at_index(input("Index position of value to be deleted -"))
    else:
      print("Invalid Input")
  def delete_at_start(self):
    if self.start_node is None:
      return "List is already empty"
    self.start_node = self.start_node.ref
  def delete_at_end(self):
    n = self.start_node
    if n is None:
      print("List is already empty")
    elif n.ref is None:
      self.start_node = None
    else:
      while n.ref.ref is not None:
        n = n.ref
      n.ref = None
  def delete_at_index(self,ind):
    n = self.start_node
    if ind == '1':
      return self.delete_at_start()
    c = 2
    while n is not None:
      if c==int(ind):
        n.ref = n.ref.ref
        return
      n = n.ref
      c+=1
    print("Index is out of the range")

  def search(self,key):
    n = self.start_node
    if n is None:
      return "List is Empty"
    while n is not None:
      if n.item == key:
        print("Given value exists in the list")
        return True
      n = n.ref
    print("Given value does not exists in the list")
    return False

  def count(self):
    n = self.start_node
    if n is None:
      return 0
    c = 0
    while n is not None:
      n = n.ref
      c+=1
    print("Number of elements in the list -",c)
    return c

  def display(self):
    if self.start_node is None:
      print("No elements are there")
      return
    else:
      n = self.start_node
      while n is not None:
        print(n.item, end=",")
        n = n.ref
      print("-")

o = linkedList()
o.user()

"""####6-DLL

"""

class Node:
  def __init__(self,data):
    self.item = data
    self.nref = None
    self.pref = None
class doublyLL:
  def __init__(self):
    self.startNode = None
    d_list = input("Enter elements of the list- ").split()
    for i in d_list[::-1] :
      self.insert_at_start(i)
    self.display()
  def user(self):
    while True:
      print("1. Insert\n2. Delete\n3. Search\n4. Count\n5. Display\n6. Exit")
      x = input("Enter function number -")
      if x=='1':
        self.insert()
      elif x=='2':
        self.delete()
      elif x=='3':
        self.search(input("Value to search -"))
      elif x=='4':
        self.count()
      elif x=='5':
        self.display()
      elif x=='6':
        break
      else:
        print("Invalid Input")

  def insert(self):
    print("1. Insert at beginning\n2. Insert at end\n3. Insert at index")
    x=input("Enter function number -")
    if x=='1':
      self.insert_at_start(input("Value -"))
    elif x=='2':
      self.insert_at_end(input("Value -"))
    elif x=='3':
      self.insert_at_index(int(input("Index position of value to be inserted -")),input("Value -"))
    else:
      print("Invalid Input")
  def insert_at_start(self,data):
    NewNode = Node(data)
    if self.startNode is None:
      self.startNode = NewNode
    else:
      NewNode.nref = self.startNode
      self.startNode.pref = NewNode
      self.startNode = NewNode
  def insert_at_end(self,data):
    n = self.startNode
    if n is None:
      return self.insert_at_start(data)
    NewNode = Node(data)
    while n is not None:
      if n.nref is None:
        n.nref = NewNode
        NewNode.pref = n
        break
      n = n.nref
  def insert_at_index(self,ind,data):
    if ind==1:
      return self.insert_at_start(data)
    n = self.startNode
    c = 2
    while n is not None:
      if c==ind:
        break
      n = n.nref
      c+=1
    NewNode= Node(data)
    if n is None:
      print("index is out of the range")
    elif n.nref is None:
      n.nref = NewNode
      NewNode.pref = n
    else:
      NewNode.nref = n.nref
      n.nref.pref = NewNode
      n.nref = NewNode
      NewNode.pref = n

  def delete(self):
    print("1. Delete at beginning\n2. Delete at end\n3. Delete at index")
    x=input("Enter function number -")
    if x=='1':
      self.delete_at_start()
    elif x=='2':
      self.delete_at_end()
    elif x=='3':
      self.delete_at_index(int(input("Index position of value to be deleted -")))
    else:
      print("Invalid Input")
  def delete_at_start(self):
    if self.startNode is None:
      return "List is already empty"
    self.startNode = self.startNode.nref
    self.startNode.pref = None
  def delete_at_end(self):
    n = self.startNode
    if n is None:
      print("List is already empty")
    elif n.nref is None:
      self.startNode = None
    else:
      while n.nref.nref is not None:
        n = n.nref
      n.nref = None
  def delete_at_index(self,ind):
    n = self.startNode
    if ind == 1:
      return self.delete_at_start()
    c = 2
    while n is not None:
      if c==int(ind):
        break
      n = n.nref
      c+=1
    if n is None:
      print("Index is out of the range")
    elif n.nref.nref is None:
      n.nref = None
    else:
      n.nref = n.nref.nref
      n.nref.pref = n
  def search(self,key):
    n = self.startNode
    if n is None:
      return "List is Empty"
    while n is not None:
      if n.item == key:
        print("Given value exists in the list")
        return True
      n = n.nref
    print("Given value does not exists in the list")
    return False

  def count(self):
    n = self.startNode
    if n is None:
      return 0
    c = 0
    while n is not None:
      n = n.nref
      c+=1
    print("Number of elements in the list -",c)
    return c

  def display(self):
    if self.startNode is None:
      print("No elements are there")
      return
    else:
      n = self.startNode
      while n.nref is not None:
        print(n.item, end=",")
        n = n.nref
      print(n.item)
o = doublyLL()
o.user()

"""####7-CLL"""

class Node:
  def __init__(self,data):
    self.item = data
    self.ref = None
class circularLL:
  def __init__(self):
    self.startNode = None
  def user(self):
    while True:
      print("1. Insert\n2. Delete\n3. Exit")
      x = input("Enter option -")
      if x=='1':
        self.insert()
      elif x=='2':
        self.delete()
      elif x=='3':
        break
      else:
        print("Invalid Input")

  def insert(self):
    print("1. Insert at beginning\n2. Insert at end\n3. Insert at position")
    x=input("Enter function number -")
    if x=='1':
      self.insert_at_start(input("Value -"))
    elif x=='2':
      self.insert_at_end(input("Value -"))
    elif x=='3':
      self.insert_at_position(int(input("Enter position -")),input("Value -"))
    else:
      print("Invalid Input")
  def insert_at_start(self,data):
    n = self.startNode
    if n is None:
      self.startNode = Node(data)
      self.startNode.ref = self.startNode
    else:
      while n.ref is not self.startNode:
        n = n.ref
      n.ref = Node(data)
      n.ref.ref = self.startNode
      self.startNode = n.ref
  def insert_at_end(self,data):
    self.insert_at_start(data)
    self.startNode = self.startNode.ref
  def insert_at_position(self,p,data):
    if p==1:
      return self.insert_at_start(data)
    n = self.startNode
    c = 2
    while n.ref is not self.startNode:
      if c==int(p):
        break
      n = n.ref
      c+=1
    if n.ref is self.startNode:
      if c == p:
        n.ref = Node(data)
        n.ref.ref = self.startNode
      else:
        print("index is out of the range")
    else:
      n.ref,n.ref.ref = Node(data),n.ref

  def delete(self):
    print("1. Delete at beginning\n2. Delete at end\n3. Delete at position")
    x=input("Enter function number -")
    if x=='1':
      self.delete_at_start()
    elif x=='2':
      self.delete_at_end()
    elif x=='3':
      self.delete_at_position(int(input("Enter value's position -")))
    else:
      print("Invalid Input")
  def delete_at_start(self):
    n = self.startNode
    if n is None:
      print("List is already empty")
    elif n.ref == n:
      self.startNode = None
    else:
      while n.ref is not self.startNode:
        n = n.ref
      n.ref = self.startNode.ref
      self.startNode = self.startNode.ref
  def delete_at_end(self):
    n = self.startNode
    if n is None:
      print("List is already empty")
    elif n.ref == n:
      self.startNode = None
    else:
      while n.ref.ref is not self.startNode:
        n = n.ref
      n.ref=n.ref.ref
  def delete_at_position(self,p):
    if p==1:
      return self.delete_at_start()
    n = self.startNode
    c = 2
    while n.ref is not self.startNode:
      if c==int(p):
        n.ref = n.ref.ref
        return
      n = n.ref
      c+=1
    print("index is out of the range")

  def display(self):
    if self.startNode is None:
      print("No elements are there")
      return
    else:
      n = self.startNode
      while n.ref is not self.startNode:
        print(n.item,end=",")
        n = n.ref
      print(n.item)


c=circularLL()
d_list = input("Enter List elements -").split()
for i in d_list[::-1] :
  c.insert_at_start(i)
c.display()
c.insert()
c.display()
c.insert()
c.display()
c.insert()
c.display()

c=circularLL()
d_list = input("Enter List elements -").split()
for i in d_list[::-1] :
  c.insert_at_start(i)
c.display()
c.delete()
c.display()
c.delete()
c.display()
c.delete()
c.display()

"""### 15
###a-Insertion sort
"""

def insertion_sort(b,length):
  for i in range(1,length):
    key = b[i]
    j = i-1
    while j>=0 and key<b[j]:
      b[j+1]=b[j]
      j -= 1
    b[j+1] = key
  return b

a = []
l = int(input("Enter the size of the list: "))
print("Enter the elements of the list: ")
for i in range(0,l):
  n = int(input(""))
  a.append(n)
print("List = ",a)
insertion_sort(a,l)

"""# b-Selection sort"""

def selection_sort(array,l):
  for i in range(l-1):
    minvalue = i

    for j in range(i+1,l):
      if array[j]<array[minvalue]:
        minvalue = j
    if minvalue != i:
      temp = array[i]
      array[i]=array[minvalue]
      array[minvalue] = temp
  return array
# main code
a= []
l = int(input("Enter the size of list"))
print("Enter list elements")
for i in range(0,l):
  n = int(input(" "))
  a.append(n)
print("List = ",a)
selection_sort(a,l)
print("sorted list : ",a)

"""c-Bubble Sort:"""

def bubble_sort(array,length):
  for i in range(0,length):
    for j in range(0,length-i-1):
      if array[j]>array[j+1]:
        array[j],array[j+1]= array[j+1],array[j]



# main code
a= []
l = int(input("Enter the size of list"))
print("Enter list elements")
for i in range(0,l):
  n = int(input(" "))
  a.append(n)
print("List = ",a)
bubble_sort(a,l)
print("sorted list : ",a)

"""###Q8

"""

stack = []
l = int(input("Enter the lenght of array"))
while True:
  option = int(input("Enter 1: Add an element to stack\nEnter 2:Delete an element from stack\nEnter 3:Size of the stack"
                      "\nEnter 4:Top of the stack\nEnter 5:Stack is empty or not\nEnter 6 to exit"))
  if option == 1:
    if len(stack) == 1:
      print("Array size exceeded cannot add any element to stack")
    else:
      value = int(input("Enter the value you want to add::"))
      stack.append(value)
      print("stack=",stack)
      continue
  elif option == 2:
    stack.pop()
    print("stack =",stack)
    continue
  elif option == 3:
    print("Size of stack=",len(stack))
    continue
  elif option == 4:
    print("Top element in stack =",stack[-1])
    continue
  elif option == 5:
    if len(stack) == 0:
      print("Stack is empty")
    else:
      print("Stack is not empty")
    continue
  elif option == 6:
    print("Bye bye ....End of the program!")
    break

"""###Q9"""

# Class to convert the expression
class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False

    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))

# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

"""### Q10"""

Queue = []
l = int(input("Enter the length of the queue: "))
while True:
  option = int(input("\nEnter 1:Add an element to queue\nEnter 2:Delete an element from queue"
                       "\nEnter 3:Size of the queue"
                       "\nEnter 4:Rear and front element of the queue"
                       "\Enter 5:Queue is empty or not"
                       "\nEnter 6:Queue is full or not\nEnter 7:Exit"))
  if option == 1:
    if len(Queue) == l:
      print("Queue is full so cannot add any element to the queue")
    else:
      value = int(input("Enter the value you want to add::"))
      Queue.append(value)
      print("Queue =",Queue)
    continue
  elif option == 2:
    Queue.pop(0)
    print("Queue = ",Queue)
    continue
  elif option == 3:
    print("Size of Queue = ",len(Queue))
    continue
  elif option == 4:
    print("Rear element in queue = ",Queue[-1])
    print("Front element in queue = ",Queue[0])
    continue
  elif option == 5:
    if len(Queue) == 0:
      print("Queue is empty")
    else:
      print("Queue is not empty")
    continue
  elif option == 6:
    if len(Queue) == 1:
      print("Queue is full")
    else:
      print("Queue is not full")
    continue
  elif option == 7:
    print("Bye .....End of the program")
    break
  else:
    print("Wrong option")

"""### Q11"""

class Node:
    def __init__(self,data):
        #Assign data to the new node, set left and right children to None
        self.item = data
        self.left = None
        self.right = None
# Binarytree class which contains all methods
class BinaryTree:
    def __init__(self):
        self.root = None
        self.flag = False
    #insertNode() will add new node to the binary tree
    def insert(self, data):
        #Create a new node
        newNode = Node(data)
        #Check whether tree is empty
        if(self.root == None):
            self.root = newNode
            return
        else:
            queue = []
            #Add root to the queue
            queue.append(self.root)
            while(True):
                node = queue.pop(0)
                #If node has both left and right child, add both the child to queue
                if(node.left != None and node.right != None):
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    #If node has no left child, make newNode as left child
                    if(node.left == None):
                        node.left = newNode
                        queue.append(node.left)
                    else:
                        #If node has left child but no right child, make newNode as right child
                        node.right = newNode
                        queue.append(node.right)
                    break

    #inorder() will perform inorder traversal on binary search tree
    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.item)
            res = res + self.inorder(root.right)
        return res
    #preorder() will perform inorder traversal on binary search tree
    def preorder(self, root):
        res = []
        if root:
            res.append(root.item)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res
    #postorder() will perform inorder traversal on binary search tree
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.item)
        return res
    def search(self,node,key):
      if (node == None):
        return False
      if (node.item == key):
        return True
      """ then recur on left sutree """
      res1 = self.search(node.left,key)
      # node found, no need to look further
      if res1:
        return True
      """ node is not found in left,
      so recur on right subtree """
      res2 = self.search(node.right, key)
      return res2
#main code
b = BinaryTree()
while True:
    option = int(input("Enter 1: Insert\nEnter 2: Search\nEnter 3: Inorder traversal "
                 "\nEnter 4: Preorder Traversal\nEnter 5:Postorder Traversal\nEnter 6:Exit\n"))
    if option == 1:
        value = int(input("Enter value"))
        b.insert(value)
        continue
    elif option == 2:
        key = int(input("Enter key: "))
        if(b.search(b.root,key)):
          print("key found")
        else:
          print("key not found")
        continue
    elif option == 3:
        print(b.inorder(b.root))
        continue
    elif option == 4:
        print(b.preorder(b.root))
        continue
    elif option == 5:
        print(b.postorder(b.root))
        continue
    elif option == 6:
        print("Bye.... End of the program")
        break
    else:
        print("Wrong option")

"""### Q12"""

class BSTNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.item = data
    # insert method
    def insert(self, data):
        if not self.item:
            self.item = data
            return
        if self.item == data:
            return
        if data < self.item:
            if self.left:
                self.left.insert(data)
                return
            self.left = BSTNode(data)
            return
        if self.right:
            self.right.insert(data)
            return
        self.right = BSTNode(data)
    # min value
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        print("Min value = ",current.item)
    #max value
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        print("Max value = ",current.item)
    # deletion method
    def delete(self, data):
        if self == None:
            return self
        if data < self.item:
            if self.left:
                self.left = self.left.delete(data)
            return self
        if data > self.item:
            if self.right:
                self.right = self.right.delete(data)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.item = min_larger_node.item
        self.right = self.right.delete(min_larger_node.item)
        return self
    #search method
    def search(self, data):
        if data == self.item:
            return True
        if data < self.item:
            if self.left == None:
                return False
            return self.left.search(data)
        if self.right == None:
            return False
        return self.right.search(data)
    #preorder() will perform inorder traversal on binary search tree
    def preorder(self, data):
        if self.item is not None:
            data.append(self.item)
        if self.left is not None:
            self.left.preorder(data)
        if self.right is not None:
            self.right.preorder(data)
        return data
    #inorder() will perform inorder traversal on binary search tree
    def inorder(self, data):
        if self.left is not None:
            self.left.inorder(data)
        if self.item is not None:
            data.append(self.item)
        if self.right is not None:
            self.right.inorder(data)
        return data
    #postorder() will perform inorder traversal on binary search tree
    def postorder(self, data):
        if self.left is not None:
            self.left.postorder(data)
        if self.right is not None:
            self.right.postorder(data)
        if self.item is not None:
            data.append(self.item)
        return data
#main code
b = BSTNode()
while True:
    option = int(input("Enter 1: Insert\nEnter 2: Search\nEnter 3: Inorder traversal "
                 "\nEnter 4: Preorder Traversal\nEnter 5:Postorder Traversal\nEnter 6: max value "
                 "\nEnter 7:min value\nEnter 8:Delete\nEnter 9: Exit\n"))
    if option == 1:
        value = int(input("Enter value"))
        b.insert(value)
        continue
    elif option == 2:
        key = int(input("Enter key: "))
        if(b.search(key)):
          print("key found")
        else:
          print("key not found")
        continue
    elif option == 3:
        t = b.inorder([])
        print(t)
        continue
    elif option == 4:
        t= b.preorder([])
        print(t)
        continue
    elif option == 5:
      t = b.postorder([])
      print(t)
      continue
    elif option == 6:
      b.get_max()
      continue
    elif option == 7:
      b.get_min()
      continue
    elif option == 8:
      value = int(input("Enter value to delete from BST"))
      b.delete(value)
      continue
    elif option == 9:
      print("Bye.... End of the program")
      break
    else:
        print("Wrong option")

"""## Q13"""

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0)
    print (s, end = " ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
# main Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')

graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}

def bfs(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)

bfs([], graph, 'A')

"""### Q14

"""

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set() # Set to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# main Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')

# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')