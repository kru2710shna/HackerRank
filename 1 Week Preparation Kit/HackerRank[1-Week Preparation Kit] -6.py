#!/usr/bin/env python
# coding: utf-8

# # HackerRank 1 Week Preparation Kit 

# ## Day-1 

# ### Problem :1 Plus Minus
# 
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
# Example  There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
# 0.400000
# 0.400000
# 0.200000
# 
# ##### Function Description
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
# int arr[n]: an array of integers
# ##### Print 
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
# ##### Input Format
# The first line contains an integer, , the size of the array. 
# The second line contains  space-separated integers that describe .
# ##### Output Format
# Print the following  lines, each to  decimals:
# proportion of positive values
# proportion of negative values
# proportion of zeros
# ##### Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
# ##### Sample Output
# 0.500000
# 0.333333
# 0.166667

# In[ ]:


def plusMinus(arr):
    # Write your code here
    zero=minus=plus= 0
    for i in range(len(arr)):
        if arr[i] > 0 :
            plus += 1
        if arr[i] < 0 :
            minus += 1
        if arr[i] ==0 :
            zero += 1
        
    print(plus/len(arr)) 
    print(minus/len(arr)) 
    print(zero/len(arr)) 


# ### Problem :2 Mini Max Sum
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# ##### Example 
# The minimum sum is  and the maximum sum is . The function prints
# 16 24
# ###### Function Description
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
# arr: an array of  integers
# ##### Print
# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
# ##### Input Format
# A single line of five space-separated integers.
# ##### Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
# ##### Sample Input
# 1 2 3 4 5
# ##### Sample Output
# 10 14

# In[ ]:


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_value = sum(arr) - arr[0]
    max_value = sum(arr) - arr[len(arr)-1]
    
    print (max_value, min_value)


# ### Problem :3 Time Conversation
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example
# ##### Return '12:01:00'.
# ##### Return '00:01:00'.
# ##### Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
# string s: a time in  hour format
# ##### Returns
# string: the time in  hour format
# ##### Input Format
# A single string  that represents a time in -hour clock format (i.e.:  or ).
# ##### Sample Input
# 07:05:45PM
# ##### Sample Output
# 19:05:45
# 

# In[ ]:


def timeConversion(s):
    # Write your code here
    time_parts = s.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2])  # Remove "AM" or "PM"

    # Check if it's PM and not noon (12 PM)
    if "PM" in s and hours != 12:
        hours += 12
    # Check if it's AM and midnight (12 AM)
    elif "AM" in s and hours == 12:
        hours = 0

    # Format the time in 24-hour format and return as a string
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


# ## Day-2

# ### Problem :4 Lonely In Integer
# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example 
# The unique element is .
# ##### Function Description
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# int a[n]: an array of integers
# ##### Returns
# int: the element that occurs only once
# ##### Input Format
# The first line contains a single integer, , the number of integers in the array. 
# The second line contains  space-separated integers that describe the values in .
# It is guaranteed that  is an odd number and that there is one unique element.
# , where .

# In[ ]:


def lonelyinteger(a):
    # Write your code here
    unique_set = set()
    
    # Loop through the array
    for num in a:
        # If the number is already in the set, remove it
        if num in unique_set:
            unique_set.remove(num)
        else:
            # If the number is not in the set, add it
            unique_set.add(num)
    
    # The remaining element in the set is the unique element
    return unique_set.pop()


# ### Problem :5 Diagonal Difference 
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
# ##### Function description
# Complete the  function in the editor below.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers
# ##### Return
# int: the absolute diagonal difference
# ##### Input Format
# The first line contains a single integer, , the number of rows and columns in the square matrix . 
# Each of the next  lines describes a row, , and consists of  space-separated integers .
# ##### Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
# ##### Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# ##### Sample Output
# 15

# In[ ]:


def diagonalDifference(arr):
    # Write your code here
    leftdiag = rightdiag = 0
    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n-i-1]
    return abs(leftdiag-rightdiag)


# ### Problem :6 
# ##### Comparison Sorting 
# Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).
# Alternative Sorting 
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
# ##### Example 
# 
# All of the values are in the range , so create an array of zeros, . The results of each iteration follow:
# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]
# The frequency array is . These values can be used to create the sorted array as well: .
# Note 
# For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.
# ##### Challenge 
# Given a list of integers, count and return the number of times each value appears as an array of integers.
# Function Description
# Complete the countingSort function in the editor below.
# countingSort has the following parameter(s):
# arr[n]: an array of integers
# ##### Returns
# int[100]: a frequency array
# ##### Input Format
# The first line contains an integer , the number of items in . 
# Each of the next  lines contains an integer  where .
# ##### Sample Input
# 100
# 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33  
# ##### Sample Output
# 0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2 

# In[ ]:


def countingSort(arr):
    # Write your code here
    frequency = [0] * 100
    
    # Count the occurrences of each value in the input array
    for num in arr:
        frequency[num] += 1
    
    return frequency


# ## Day- 3
# 
# ### Problem 7
# ##### In this challenge, the task is to debug the existing code to successfully execute all provided test files.
# Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.
# ##### Example.
# Now if we permute the array as , the result is a zig zag sequence.
# ##### Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.
# Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.
# To restore the original code, click on the icon to the right of the language selector.
# ##### Input Format
# The first line contains  the number of test cases. The first line of each test case contains an integer , denoting the number of array elements. The next line of the test case contains  elements of array .
# ##### Constraints
#  
#  ( is always odd) 
# 
# ##### Output Format
# For each test cases, print the elements of the transformed zig zag sequence in a single line.

# In[ ]:


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)                #modification-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2                          #modification-2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1                     #modification-3

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


# ### Problem: 8 
# Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:
# Initially there are  towers.
# Each tower is of height .
# The players move in alternating turns.
# In each turn, a player can choose a tower of height  and reduce its height to , where  and evenly divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .
# ##### Example.   
# 
# There are  towers, each  units tall. Player  has a choice of two moves: 
# - remove  pieces from a tower to leave  as  
# - remove  pieces to leave 
# Let Player  remove . Now the towers are  and  units tall.
# Player  matches the move. Now the towers are both  units tall.
# Now Player  has only one move.
# Player  removes  pieces leaving . Towers are  and  units tall. 
# Player  matches again. Towers are both  unit tall.
# Player  has no move and loses. Return .
# ##### Function Description
# Complete the towerBreakers function in the editor below.
# towerBreakers has the following paramter(s):
# int n: the number of towers
# int m: the height of each tower
# ##### Returns
# int: the winner of the game
# ##### Input Format
# The first line contains a single integer , the number of test cases. 
# Each of the next  lines describes a test case in the form of  space-separated integers,  and .
# Constraints
# 
# 
# ##### Sample Input
# STDIN   Function
# -----   --------
# 2       t = 2
# 2 2     n = 2, m = 2
# 1 4     n = 1, m = 4
# ##### Sample Output
# 2
# 1
# ##### Explanation
# We'll refer to player  as  and player  as 
# In the first test case,  chooses one of the two towers and reduces it to . Then  reduces the remaining tower to a height of . As both towers now have height ,  cannot make a move so  is the winner.
# In the second test case, there is only one tower of height .  can reduce it to a height of either  or . chooses  as both players always choose optimally. Because  has no possible move,  wins.

# In[ ]:


def towerBreakers(n, m):
    # Write your code here
    # Special Case
    if m==1:
        return 2 
    
    if n == 1:
        return 1 
    
    return 2 if n%2==0 else 1


# ### Problem: 9
# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
# 
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
# The alphabet is rotated by , matching the mapping above. The encrypted string is .
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
# Function Description
# Complete the caesarCipher function in the editor below.
# caesarCipher has the following parameter(s):
# string s: cleartext
# int k: the alphabet rotation factor
# ##### Returns
# string: the encrypted string
# ##### Input Format
# The first line contains the integer, , the length of the unencrypted string. 
# The second line contains the unencrypted string, . 
# The third line contains , the number of letters to rotate the alphabet by.
# ##### Sample Input
# 11
# middle-Outz
# 2
# ##### Sample Output
# okffng-Qwvb

# In[ ]:


def caesarCipher(s, k):
    k = k % 26
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = original_alphabet[k:] + original_alphabet[:k]
    encrypted_text = ""

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()  # Check if the character is uppercase
            char = char.lower()  # Convert the character to lowercase for easier manipulation

            if char in original_alphabet:
                index = original_alphabet.index(char)
                encrypted_char = rotated_alphabet[index]

                if is_upper:
                    encrypted_char = encrypted_char.upper()  # Convert back to uppercase if original was uppercase

                encrypted_text += encrypted_char
            else:
                encrypted_text += char  # Leave non-letter characters unchanged
        else:
            encrypted_text += char  # Leave non-letter characters unchanged

    return encrypted_text
    


# ## DAY -4 

# ### Problem - 10 
# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
# ##### Example 
# The grid is illustrated below.
# a b c
# a d e
# e f g
# The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.
# ##### Function Description
# Complete the gridChallenge function in the editor below.
# gridChallenge has the following parameter(s):
# string grid[n]: an array of strings
# ##### Returns
# string: either YES or NO
# ##### Input Format
# The first line contains , the number of testcases.
# Each of the next  sets of lines are described as follows: 
# - The first line contains , the number of rows and columns in the grid. 
# - The next  lines contains a string of length 
# Each string consists of lowercase letters in the range ascii[a-z]
# Output Format
# For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.
# ##### Sample Input
# STDIN   Function
# -----   --------
# 1       t = 1
# 5       n = 5
# ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# fghij
# olmkn
# trpqs
# xywuv
# ##### Sample Output
# YES
# ##### Explanation
# The x grid in the  test case can be reordered to
# abcde
# fghij
# klmno
# pqrst
# uvwxy
# This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.

# In[ ]:


def gridChallenge(grid):
    # Convert each row to a list of characters and sort them alphabetically
    sorted_rows = [sorted(row) for row in grid]

    # Check if the rows are sorted alphabetically
    for i in range(len(sorted_rows) - 1):
        if sorted_rows[i] > sorted_rows[i + 1]:
            return "NO"

    # Check if the columns are sorted alphabetically
    for j in range(len(grid[0])):
        for i in range(len(grid) - 1):
            if sorted_rows[i][j] > sorted_rows[i + 1][j]:
                return "NO"

    return "YES"


# ### Problem - 11
# We define super digit of an integer  using the following rules:
# Given an integer, we need to find the super digit of the integer.
# If  has only  digit, then its super digit is .
# Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
# For example, the super digit of  will be calculated as:
# 	super_digit(9875)   	9+8+7+5 = 29 
# 	super_digit(29) 	2 + 9 = 11
# 	super_digit(11)		1 + 1 = 2
# 	super_digit(2)		= 2  
#     
# ##### Example 
# The number  is created by concatenating the string   times so the initial .
#     superDigit(p) = superDigit(9875987598759875)
#                   9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
#     superDigit(p) = superDigit(116)
#                   1+1+6 = 8
#     superDigit(p) = superDigit(8)
#     
# All of the digits of  sum to . The digits of  sum to .   is only one digit, so it is the super digit.
# ##### Function Description
# Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.
# superDigit has the following parameter(s):
# string n: a string representation of an integer
# int k: the times to concatenate  to make 
# ##### Returns
# int: the super digit of  repeated  times
# ##### Input Format
# The first line contains two space separated integers, n and k.

# In[1]:


def superDigit(n, k):
    # Write your code here
    initial_sum = sum(int(digit) for digit in n)
    
    # Multiply the initial sum by k
    initial_sum *= k
    
    # Calculate the super digit until it's a single-digit number
    while initial_sum >= 10:
        initial_sum = sum(int(digit) for digit in str(initial_sum))
    
    return initial_sum


# ### Problem: 12
# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
# ##### Example
# If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.
# Person  had to bribe  people to get to the current position. Print Too chaotic.
# Function Description
# Complete the function minimumBribes in the editor below.
# minimumBribes has the following parameter(s):
# int q[n]: the positions of the people after all bribes
# ##### Returns
# No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
# Input Format
# The first line contains an integer , the number of test cases.
# Each of the next  pairs of lines are as follows: 
# - The first line contains an integer , the number of people in the queue 
# - The second line has  space-separated integers describing the final state of the queue.
# Constraints
# 
# 
# Subtasks
# For  score 
# For  score 
# Sample Input
# STDIN       Function
# -----       --------
# 2           t = 2
# 5           n = 5
# 2 1 5 3 4   q = [2, 1, 5, 3, 4]
# 5           n = 5
# 2 5 1 3 4   q = [2, 5, 1, 3, 4]
# ##### Sample Output
# 3
# Too chaotic
bribes = flag = 0
    while(q != sorted(q)):
        for i in range(len(q)-1) :
            if abs(q[i]-1-i) > 2 :
                flag = 1
                break
            if q[i] > q[i+1] :
                q[i],q[i+1] = q[i+1],q[i]
                bribes += 1
        if flag == 1 :
            print("Too chaotic")
            break
    if flag == 0 :
        print(bribes)
# ### Day -5 

# ## Problem: 13 
# This challenge is part of a tutorial track by MyCodeSchool
# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.
# ##### Example 
#  head refers to  1 - 3 - 7 - NULL
#  head refers to  1 - 2 - NULL
# The new list is 
# ##### Function Description
# Complete the mergeLists function in the editor below.
# mergeLists has the following parameters:
# SinglyLinkedListNode pointer headA: a reference to the head of a list
# SinglyLinkedListNode pointer headB: a reference to the head of a list
# ##### Returns
# SinglyLinkedListNode pointer: a reference to the head of the merged list
# ##### Input Format
# The first line contains an integer , the number of test cases.
# The format for each test case is as follows:
# The first line contains an integer , the length of the first linked list. 
# The next  lines contain an integer each, the elements of the linked list. 
# The next line contains an integer , the length of the second linked list. 
# The next  lines contain an integer each, the elements of the second linked list.
# , where  is the  element of the list.
# ##### Sample Input
# 1
# 3
# 1
# 2
# 3
# 2
# 3
# 4
# ##### Sample Output
# 1 2 3 3 4 

# In[ ]:


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    dummy = SinglyLinkedListNode(0)
    curr = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

    return dummy.next


# ## Problem: 14
# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
# A basic queue has the following operations:
# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
# ##### Input Format
# The first line contains a single integer, , denoting the number of queries. 
# Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.
# It is guaranteed that a valid answer always exists for each query of type .
# ##### Output Format
# For each query of type , print the value of the element at the front of the queue on a new line.
# ##### Sample Input
# STDIN   Function
# -----   --------
# 10      q = 10 (number of queries)
# 1 42    1st query, enqueue 42
# 2       dequeue front element
# 1 14    enqueue 42
# 3       print the front element
# 1 28    enqueue 28
# 3       print the front element
# 1 60    enqueue 60
# 1 78    enqueue 78
# 2       dequeue front element
# 2       dequeue front element
# ##### Sample Output
# 14
# 14

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        self.__transfer()
        if self.stack2:
            return self.stack2.pop()

    def front(self):
        self.__transfer()
        if self.stack2:
            return self.stack2[-1]

    def __transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

# Process queries
def process_queries(queries):
    queue = QueueUsingTwoStacks()
    result = []

    for query in queries:
        if query[0] == 1:  # Enqueue
            queue.enqueue(query[1])
        elif query[0] == 2:  # Dequeue
            queue.dequeue()
        elif query[0] == 3:  # Print the front element
            result.append(queue.front())

    return result

# Read the number of queries
q = int(input())
queries = []

# Read and parse the queries
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Process queries and print the front elements
output = process_queries(queries)
for val in output:
    print(val)


# ## Problem: 15
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
# ##### Function Description
# Complete the function isBalanced in the editor below.
# isBalanced has the following parameter(s):
# string s: a string of brackets
# ##### Returns
# string: either YES or NO
# ##### Input Format
# The first line contains a single integer , the number of strings. 
# Each of the next  lines contains a single string , a sequence of brackets.
# where  is the length of the sequence.
# All chracters in the sequences ∈ { {, }, (, ), [, ] }.
# ##### Output Format
# For each string, return YES or NO.
# ##### Sample Input
# STDIN Function ----- -------- 3 n = 3 {[()]} first s = '{[()]}' {[(])} second s = '{[(])}' {{[[(())]]}} third s ='{{[[(())]]}}'
# ##### Sample Output
# YES
# NO
# YES

# In[ ]:


def isBalanced(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return "NO"

    if not stack:
        return "YES"
    else:
        return "NO"


# ## Day -6

# ### Problem : 16
# Implement a simple text editor. The editor initially contains an empty string, &. Perform Qoperations of the following 4 types:
# 1.    append (W) - Append string W to the end of S.
# 2.    delete(B) - Delete the last & characters of 5.
# 3.    print(k) - Print the 1th character of 5.
# 4.    undo - Undo the last (not previously undone) operation of type 1 or 2, reverting 8 to the state it was in prior to that operation.
# Example
# § = 'abede ops = ('1 £g',
# 334
# operation index
# S
# ops [ index]
# explanation
# 2
# abcde
# fg
# abcdefg 3 6
# abcdefg 2 5 ab
# abcdefg 3 7
# abcdefg 4
# abcde 343
# append fg
# print the 6th letter - f delete the last 5 letters undo the last operation, index 2 print the 7th character - g undo the last operation, index o print the 4th character - d
# The results should be printed as:
# TripAdvi
# Com
# Discussions
# Input Format
# The first line contains an integer, Q, denoting the number of operations
# Each line / of the Q subsequent lines (where O S i < Q) defines an operation to be performed. Each operation starts with a single integer, t (where t € {1, 2, 3, 4]), denoting a type of operation as defined in the Problem Statement above. If the operation requires an argument, t is followed by its space-separated argument, For example, ift - 1 and W - "abed", line i will be 1 abed.
# 
# Constraints
# E
# *   1<0 < 10°
# *   1 ≤*≤|SI
# *   The sum of the lengths of all W in the input S 10°
# *   The sum of & over all delete operations ≤ 2 • 10° All input characters are lowercase English letters.
# *   It is guaranteed that the sequence of operations given as input is possible to perform.
# Output Format
# Each operation of type 3 must print the 7* character on a new line
# Sample Input
# STDIN
# Leaderboard
# Function
# 0 = 8
# ops[0] = 11 abc
# ops [1]
# 513:30
# Discussions
# Sample Output
# Explanation
# Initially, S is empty. The following sequence of 8 operations are described below:
# 1.    8 - "* we append abc to S, so S - "abe
# 2.    print the gre character on a new line. Currently, the 3rd
# character is
# 3. Delete the last 3 characters in S (abc), so S=“”
# 1. 
# 2.    Append ay to S, so § = "ay".
# s. print the 254
# * character on a new line. Currently, the 2" character is y
# 1.    Undo the last update to S, making 8 empty again (t.e., S =
# 2.    Undo the next to last update to 8 (the deletion of the last 3 characters), making 5 = "abc"
# 3.    Print the 1*
# * character on a new line. Currently, the 1"
# character is a
# 

# In[ ]:


class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
    
    def append(self, to_add):
        self.history.append(self.text)
        self.text += to_add
    
    def delete(self, n):
        self.history.append(self.text)
        self.text = self.text[:-n]
    
    def print(self, k):
        print(self.text[k - 1])
    
    def undo(self):
        if self.history:
            self.text = self.history.pop()

if __name__ == "__main__":
    editor = TextEditor()
    Q = int(input().strip())
    
    for _ in range(Q):
        op = input().split()
        op_type = int(op[0])
        
        if op_type == 1:
            editor.append(op[1])
        elif op_type == 2:
            editor.delete(int(op[1]))
        elif op_type == 3:
            editor.print(int(op[1]))
        elif op_type == 4:
            editor.undo()


# ### Problem: 17
# You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):
# d	h	w
# 1	1	1
# 1	1	2
# 1	1	3
# 1	1	4
# Using these blocks, you want to make a wall of height  and width . Features of the wall are: 
# 
# - The wall should not have any holes in it. 
# - The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks. 
# - The bricks must be laid horizontally.
# How many ways can the wall be built?
# ##### Example
# The height is n and the width is m. Here are some configurations:
# These are not all of the valid permutations. There are  valid permutations in all.
# ##### Function Description
# Complete the legoBlocks function in the editor below.
# legoBlocks has the following parameter(s):
# int n: the height of the wall
# int m: the width of the wall
# ##### Returns 
# - int: the number of valid wall formations modulo 
# ##### Input Format
# The first line contains the number of test cases .
# Each of the next  lines contains two space-separated integers  and .
# ##### Sample Input
# STDIN   Function
# -----   --------
# 4       t = 4
# 2 2     n = 2, m = 2
# 3 2     n = 3, m = 2
# 2 3     n = 2, m = 3
# 4 4     n = 4, m = 4
# ##### Sample Output
# 3  
# 7  
# 9  
# 3375

# In[1]:


MOD = 10**9 + 7
row_history = [1,2,4,8]
def row(w):
    if w == 0:
        return 1
    if w <= len(row_history):
        return row_history[w - 1]
    return (row(w - 1) + row(w - 2) + row(w - 3) + row(w - 4)) % MOD

for i in range(4, 1000):
    row_history.append(row(i + 1))

tower_history = {}
def tower(h, w):
    result = tower_history.get((h,w))
    if result is None:
        result = row(w) ** h % MOD
        tower_history[(h,w)] = result
    return result

legoblock_history = {}

def legoBlocks(n, m):
    if m <= 1:
        return 1
    result = legoblock_history.get((n,m))
    if result is None:
        result = (tower(n, m) - sum(tower(n, m - x) * legoBlocks(n, x) for x in range(1, m))) % MOD
        legoblock_history[(n,m)] = result
    return result


# ### Problem: 18 Jesse and Cookies
# Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:
# sweetness  Least sweet cookie    2nd least sweet cookie).
# This occurs until all the cookies have a sweetness  .
# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .
# ##### return
# The smallest values are . 
# Remove them then return  to the array. Now . 
# Remove  and return  to the array. Now . 
# Remove , return  and . 
# Finally, remove  and return  to . Now . 
# All values are  so the process stops after  iterations. Return .
# Function Description 
# Complete the cookies function in the editor below.
# cookies has the following parameters:
# int k: the threshold value
# int A[n]: an array of sweetness values
# Returns
# int: the number of iterations required or 
# ##### Input Format
# The first line has two space-separated integers,  and , the size of  and the minimum required sweetness respectively.
# The next line contains  space-separated integers, .
# ##### Sample Input
# STDIN               Function
# -----               --------
# 6 7                 A[] size n = 6, k = 7
# 1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]  
# ##### Sample Output
# 2

# In[ ]:





# ## Day-7

# ### Problem: 19
# Complete the preOrder Traversal function in the editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.
# #### Input Format
# Our test code passes the root node of a binary tree to the preOrder function.
# Constraints
# Nodes in the tree  
# ##### Output Format
# Print the tree's preorder traversal as a single line of space-separated values.
# ##### Sample Input
#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4  
# ##### Sample Output
# 1 2 5 3 4 6 

# In[5]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq

def cookies(k, A):
    count = 0 
    heapq.heapify(A)  # Convert the list into a min-heap

    while A[0] < k and len(A) >= 2:
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        new_cookie = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, new_cookie)
        count += 1

    return count if A[0] >= k else -1


# Complete the PreOrder Traversal function in the editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.
# ##### Input Format
# Our test code passes the root node of a binary tree to the preOrder function.
# Constraints
#  Nodes in the tree  
# ##### Output Format
# Print the tree's preorder traversal as a single line of space-separated values.
# ###### Sample Input
#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4  
# ##### Sample Output
# 1 2 5 3 4 6 

# In[7]:


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    if root is not None:
        print(root.info, end=" ")  # Print the current node's value
        preOrder(root.left)  # Recursively traverse the left subtree
        preOrder(root.right)  # 


# ## Problem: 19
# Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.
# For instance, consider the string ABRACADABRA. There are a total of  characters in the string. This number should match the count in the ultimately determined root of the tree. Our frequencies are A= 5, B=2, R=2, C=1 and D =1 and . The two smallest frequencies are for  and , both C and D equal to 1, so we'll create a tree with them. The root node will contain the sum of the counts of its descendants, in this case 1+1 = 2. The left node will be the first character encountered,C , and the right will contain D. Next we have 3 items with a character count of 2: the tree we just created, the character B and the character R. The tree came first, so it will go on the left of our new root node B will go on the right. Repeat until the tree is complete, then fill in the 1's and 0's for the edges. The finished graph looks like:
# 
# Input characters are only present in the leaves. Internal nodes have a character value of ϕ (NULL). We can determine that our values for characters are:
# A - 0
# B - 111
# C - 1100
# D - 1101
# R - 10
# Our Huffman encoded string is:
# A B    R  A C     A D     A B    R  A
# 0 111 10 0 1100 0 1101 0 111 10 0
# or
# 01111001100011010111100
# To avoid ambiguity, Huffman encoding is a prefix free encoding technique. No codeword appears as a prefix of any other codeword.
# To decode the encoded string, follow the zeros and ones to a leaf and return the character there.
# You are given pointer to the root of the Huffman tree and a binary coded string to decode. You need to print the decoded string.
# Function Description
# Complete the function decode_huff in the editor below. It must return the decoded string.
# decode_huff has the following parameters:
# root: a reference to the root node of the Huffman tree
# s: a Huffman encoded string
# Input Format
# There is one line of input containing the plain string,s . Background code creates the Huffman tree then passes the head node and the encoded string to the function.

# In[8]:


def decodeHuff(root, s):
	#Enter Your Code Here
    decoded_string = ""
    current_node = root

    for bit in s:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_string += current_node.data
            current_node = root  # Reset to the root for the next character

    print(decoded_string)


# ### Problem: 20
# There is a given list of strings where each string contains only lowercase letters from , inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.
# Note If two strings are identical, they are prefixes of each other.
# Example 
# 
# Here 'abcd' is a prefix of 'abcde' and 'bcd' is a prefix of 'bcde'. Since 'abcde' is tested first, print
# BAD SET  
# abcde
# .
# No string is a prefix of another so print
# GOOD SET 
# Function Description 
# Complete the noPrefix function in the editor below.
# noPrefix has the following parameter(s): 
# - string words[n]: an array of strings
# Prints 
# - string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.
# Input Format 
# First line contains , the size of . 
# Then next  lines each contain a string, .
# Constraints 
#  
#  the length of words[i]  
# All letters in  are in the range 'a' through 'j', inclusive.
# Sample Input00
# STDIN       Function
# -----       --------
# 7            words[] size n = 7
# aab          words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
# defgab  
# abcde
# aabcde
# cedaaa
# bbbbbbbbbb
# jabjjjad
# Sample Output00
# BAD SET
# aabcde
# Explanation 
# 'aab' is prefix of 'aabcde' so it is a BAD SET and fails at string 'aabcde'.
# Sample Input01
# 4
# aab
# aac
# aacghgh
# aabghgh
# Sample Output01
# BAD SET
# aacghgh
# Explanation 
# 'aab' is a prefix of 'aabghgh', and aac' is prefix of 'aacghgh'. The set is a BAD SET. 'aacghgh' is tested before 'aabghgh', so and it fails at 'aacghgh'.
# Change Theme
# 

# In[ ]:


def insert(trie, word):
    for i, char in enumerate(word):
        if char in trie:
            if trie[char].get('is_end') or i == len(word) - 1:
                return True
            else:
                trie = trie[char]
        else:
            trie[char] = {}
            trie = trie[char]
        
    trie['is_end'] = True  # Marquer la fin du mot
    return False


def noPrefix(words):
    trie = {}
    for word in words:
        if insert(trie, word):
            print('BAD SET')
            print(word)
            return 
    print('GOOD SET')

