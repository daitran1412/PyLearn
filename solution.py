import math
from numpy import double
def fib(n):	
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return fib(n-1) + fib(n-2)
# Exercise 1: Character Input
def charInput():
    name = input()
    age = int(input())
    year = str((2021 - age)+100)
    print(name + " will be 100 years old in the year " + year)
    
# Exercise 2: Rock Paper Scissors
def compare(u1, u2):   # 3 options: rock, paper and scissors
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Try again! You have not entered rock, paper or scissors.")



# Exercise 3: Divisors 
def divisors(n):
    listRange = list(range(1,n+1))
    divisorList = []
    for number in listRange:
        if n % number == 0:
            divisorList.append(number)        
    return divisorList

# Exercise 4: List Remove Duplicates
def removeDuplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

# Exercise 5: List Overlap
def listOverlap(a,b):
    new_list = []
    for num in b:
        if num in a:
            if num not in new_list:
                new_list.append(num)
    return new_list

# Exercise 6: String Lists
def palindrome(string):
    new_str = ""
    for i in string:
        if i.isalnum():
            new_str += (i)
    return new_str.lower()[::-1] == new_str.lower()


# Exercise 7: Check Primality Functions
def checkPrimality(num):
    a = [x for x in range(2, num) if num % x == 0]
    if num > 1:
        if len(a) == 0:
            return True
        else:
            return False
    else:
        return False

# Exercise 8: Reverse Word Order
def reverseWord(w):
      return ' '.join(w.split()[::-1])

# Exercise 9: Fibonacci
def fib(n):	
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return fib(n-1) + fib(n-2)

# Exercise 10: Check Password 
def pwd(s):
    password = list(s)
    if len(password) < 8 or len(password) > 100:
        return False
    if str(s).isupper() == True:
        return False
    if str(s).islower() == True:
        return False
    if str(s).isnumeric() == True:
        return False
    if str(s).isalnum() == True:
        return False
    return True

# Exercise 11: Guess Letters   <nên để ở cuối>
def guessLetter(word):
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("guess letter: ")
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            print(''.join(guessed))
            if letter != '':
                lstGuessed.append(letter.upper())
            letter = input("guess letter: ")

        if '_' not in guessed:
            print("You won!!")
            break

# Exercise 12: Birthday Dictionaries
def birthdayDic():
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}
    for name in birthdays:
        print(name)
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

#------------------------------MIMGO------------------------------
# Exercise 13: Calculate variance
#Medium
def mean(s):                    
    sum = 0
    for i in s:
        sum += double(i)
    tb = sum / double(len(s))
    return tb
#variance
def variance(s):        
    tb = mean(s)
    a = 0
    for i in s:
        a += math.pow(double(i) - tb, 2)
    ps = a / double(len(s))
    return ps

# Exercise 14: Divisible by 5
def dec5(n):
    arr = n.split(",")
    array = []
    for i in arr:
        a = list(i)
        a = a[::-1]
        m = 0
        for j in range(0, len(a)):
             m += (2**int(j))* int(a[j])
        if m % 5 == 0:
            array.append(i)
    print(",".join(array))
# Excercise 15: Make Dictionary
def dictionary (n):
    dic = {}
    for i in range(1,n+1):
        dic.update({i:reverse(i*i)})
    return dic
def reverse (n):
    if n < 10:
        return n
    else:
        i = list(str(n))
        i = i[::-1]
        m = "".join(i)
        m = int(m)
    return m