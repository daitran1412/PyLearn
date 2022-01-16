import unittest
import random
from solution import *
import math
from numpy import double

#------------https://www.practicepython.org---------------------------

# Exercise 1: Character Input
def correct_charInput(name, age):
    year = str((2021 - age) + 100)
    return(name + " will be 100 years old in the year " + year)


# Exercise 2: Fibonacci
def correct_fib(n):	
	if n==1 or n == 2:
		return 1
	else:
		return correct_fib(n-1) + correct_fib(n-2)

# Exercise 3: Rock Paper Scissors
def correct_compare(u1, u2):   # 3 options: rock, paper and scissors
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

# Exercise 4: Divisors 
def correct_divisors(n):
    listRange = list(range(1,n+1))
    divisorList = []
    for number in listRange:
        if n % number == 0:
            divisorList.append(number)        
    return divisorList

# Exercise 5: List Remove Duplicates
def correct_removeDuplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

# Exercise 6: List Overlap
def correct_listOverlap(a,b):
    new_list = []
    for num in b:
        if num in a:
            if num not in new_list:
                new_list.append(num)
    return new_list

# Exercise 7: String Lists
def correct_palindrome(string):
    new_str = ""
    for i in string:
        if i.isalnum():
            new_str += (i)
    return new_str.lower()[::-1] == new_str.lower()


# Exercise 8: Check Primality Functions
def correct_checkPrimality(num):
    a = [x for x in range(2, num) if num % x == 0]
    if num > 1:
        if len(a) == 0:
            return True
        else:
            return False
    else:
        return False

# Exercise 9: Reverse Word Order
def correct_reverseWord(w):
      return ' '.join(w.split()[::-1])

# Exercise 10: Birthday Dictionaries
def correct_birthdayDic(name):
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}
    if name in birthdays:
        return('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        return('Sadly, we don\'t have {}\'s birthday.'.format(name))

#------------------------------MIMGO------------------------------
# Exercise 11: Calculate variance
#Medium
def mean(s):                    
    sum = 0
    for i in s:
        sum += double(i)
    tb = sum / double(len(s))
    return tb
#variance
def correct_variance(s):        
    tb = mean(s)
    a = 0
    for i in s:
        a += math.pow(double(i) - tb, 2)
    ps = a / double(len(s))
    return ps

# Exercise 12: Divisible by 5
def correct_dec5(n):
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
    return(",".join(array))
    
# Excercise 13: Make Dictionary
def correct_dictionary (n):
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

def random_num(n):
    return random.choice([i for i in range(n+1)])

# charInput
class charInput_check(unittest.TestCase):
    def test_1(self):
        assert correct_charInput("Peter", 12) == charInput("Peter", 12)
    def test_2(self):
        assert correct_charInput("Nam", 13) == charInput("Nam", 13)
    def test_3(self):
        assert correct_charInput("Lili", 9 ) == charInput("Lili", 9)
    

# fib
class fib_check(unittest.TestCase):
    def test_1(self):
        assert 0 == fib(1)
    def test_2(self):
        num = random_num(15)
        assert correct_fib(num) == fib(num)
    def test_3(self):
        num = random_num(50)
        assert correct_fib(num) == fib(num)
    
# Rock Paper Scissors
class compare_check(unittest.TestCase):
    def test_1(self):
        assert correct_compare("rock","paper")  == compare("rock","paper")
    def test_2(self):
        assert correct_compare("paper","scissors")  == compare("paper","scissors")
    def test_3(self):
        assert correct_compare("paper","paper")  == compare("paper","paper")

# Divisors 
class divisors_check(unittest.TestCase):
    def test_1(self): 
        assert correct_divisors(10) == divisors(10)
    def test_2(self):
        assert correct_divisors(50) == divisors(50)
    def test_3(self):
        assert correct_divisors(0) == divisors(0)


# List Remove Duplicates
class removeDuplicates_check(unittest.TestCase):
    def test_1(self):
        a = [1,2,2,4,3,5,3,7,6,8,1,5,4,9,0]
        assert correct_removeDuplicates(a) == removeDuplicates(a)
    def test_2(self):
        a = ['a','b','c','a','d','h','c','j','f','a']
        assert correct_removeDuplicates(a) == removeDuplicates(a)
    def test_3(self):
        a = ["Tom Holland", "Andrew Garfield","Tom Holland","Tobey Maguire","Zendaya","Andrew Garfield","Willem Dafoe","Willem Dafoe","Alfred Molina"]
        assert correct_removeDuplicates(a) == removeDuplicates(a)

# List Overlap
class listOverlap_check(unittest.TestCase):
    def test_1(self):
        a = [123,456,789,123,234,567,567,890,345,890]
        b = [123,764,789,789,423,651,567,890,678,890,1234,749]
        assert correct_listOverlap(a,b) == listOverlap(a,b)
    def test_2(self):
        a = ['a','b','c','a','d','h','c','j','f','a']
        b = ['e','a','u','r','c','a','j','c','g','h','d']
        assert correct_listOverlap(a,b) == listOverlap(a,b)
    def test_3(self):
        a = ["Tom Holland", "Andrew Garfield","Tom Holland","Tobey Maguire","Zendaya","Andrew Garfield","Jacob Batalon","Willem Dafoe","Willem Dafoe","Alfred Molina"]
        b = ["Andrew Garfield","Tom Holland","Tom Holland","Tobey Maguire","Andrew Garfield","Willem Dafoe","Willem Dafoe","Alfred Molina","Marisa Tomei"]
        assert correct_listOverlap(a,b) == listOverlap(a,b) 

# String Lists
class palindrome_check(unittest.TestCase): 
    def test_1(self):
        string = "Anna"  
        assert correct_palindrome(string) == palindrome(string)
    def test_2(self):
        string = "21912"  
        assert correct_palindrome(string) == palindrome(string)
    def test_3(self):
        string = "Eva, can I see bees in a cave"  
        assert correct_palindrome(string) == palindrome(string)    

# Check Primality Functions
class checkPrimality_check(unittest.TestCase):
    def test_1(self):
        num = random_num(15)
        assert correct_checkPrimality(num) == checkPrimality(num)
    def test_2(self):
        num = random_num(50)
        assert correct_checkPrimality(num) == checkPrimality(num)
    def test_3(self):
        num = random_num(100)
        assert correct_checkPrimality(num) == checkPrimality(num)

# Reverse Word Order
class reverseWord_check(unittest.TestCase):
    def test_1(self):
        w = "Avengers assemble"
        assert correct_reverseWord(w) == reverseWord(w)
    def test_2(self):
        w = "more power more responsibility"
        assert correct_reverseWord(w) == reverseWord(w)
    def test_3(self):
        w = "study, study more, study forever"
        assert correct_reverseWord(w) == reverseWord(w)

# Birthday Dictionaries
class birthdayDic_check(unittest.TestCase):
    def test_1(self):
        assert correct_birthdayDic("Albert Einstein") == birthdayDic("Albert Einstein")
    def test_2(self):
        assert correct_birthdayDic("Benjamin Franklin") == birthdayDic("Albert Einstein")
    def test_3(self):
        assert correct_birthdayDic("Nikolas Tesla") == birthdayDic("Nikolas Tesla")

# Calculate variance
class variance_check(unittest.TestCase):
    def test_1(self):
        s = []
        n = random_num(20)
        for i in range(0, n+1):
            s.append(random_num(50))
        assert correct_variance(s) == variance(s)
    def test_2(self):
        s = []
        n = random_num(30)
        for i in range(0, n+1):
            s.append(random_num(100))
        assert correct_variance(s) == variance(s)
    def test_3(self):
        s = []
        n = random_num(40)
        for i in range(0, n+1):
            s.append(random_num(200))
        assert correct_variance(s) == variance(s)

# Divisible by 5
class dec5_check(unittest.TestCase):
    def test_1(self):
        assert correct_dec5("0100,0011,1010,1001") == dec5("0100,0011,1010,1001")
    def test_2(self):
        assert correct_dec5("0101,1001,1111,1000") == dec5("0101,1001,1111,1000")
    def test_3(self):
        assert correct_dec5("1100,1110,0000,0001") == dec5("1100,1110,0000,0001")
        
# Make Dictionary
class dictionary_check(unittest.TestCase):
    def test_1(self):
        num = random_num(10)
        assert correct_dictionary(num) == dictionary(num)
    def test_2(self):
        num = random_num(20)
        assert correct_dictionary(num) == dictionary(num)
    def test_3(self):
        num = random_num(50)
        assert correct_dictionary(num) == dictionary(num)
    
if __name__ == "__main__":
	unittest.main()