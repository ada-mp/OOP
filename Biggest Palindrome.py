# -*- coding: utf-8 -*-
'''The first job is to solve Project Euler's problem 4.
Write a code to find the largest palindrome that is a 
product of two 3-digit numbers.
You must write the code in Python in a file with a .py extension,
to be executed directly by the interpreter. The code should print
the requested palindrome value, without expecting any user interaction.'''

def palindromo_numero():
  palindromo = 9009
  for i in range(100,1000):
    for j in range(100,1000):
      prod = i*j
      if str(prod) == str(prod)[::-1]:
        if prod > palindromo:
          palindromo = prod
  return palindromo

print(palindromo_numero())
