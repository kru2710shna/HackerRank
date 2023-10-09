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

# In[3]:


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

# In[4]:


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

# In[5]:


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

# In[6]:


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

# In[7]:


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

# In[8]:


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


# ### Problem - 10 
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


# ### Problem: 11
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
# In[ ]:




