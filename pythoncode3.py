#Program to check whether the given two strings are anagram or not

def Anagram(str1, str2):
   
        mapping1,mapping2={},{}
        
        for alpha in str1:
           
            num=s.count(alpha)
            mapping1[alpha]=num
            
        for alpha in str2:
            num=t.count(alpha)
            mapping2[alpha]=num
            
        if mapping1==mapping2:
           print('true')
         
        else:
            print('false')
            
str1= input('Enter String1:')
str2= input('Enter String2:')

Anagram(str1,str2)

#program 2
'''program to print
If the input is exactly "0", print smart.
If the number is less than or equal to 0 or greater than 1000, print invalid.
If the number contains the digit 3 and is divisible by 3, print dumb.
If the number contains the digit 3 but is not divisible by 3, print stupid.
If the number does not contain the digit 3, but is divisible by 3, print idiot.
Otherwise, print smart.

'''

n=int(input('Enter no:'))

if n==0:
   print('smart')
   
elif n<=0 or n>1000:
   print('Invalid')
   
elif '3' in str(n):
   
   if n%3 == 0:
      print('dumb')
      
   else:
      print('stupid')
      
elif '3' not in str(n):
   if n%3==0:
      print('idiot')
   else:
      print('smart')
   
else:
   print('smart')


# Keith no
'''
3.A n digit number x is called Keith number if it appears in a special sequence (defined below) generated using its digits. The special sequence has first n terms as digits of x and other terms are recursively evaluated as sum of previous n terms.
The task is to find if a given number is Keith Number or not.
example:
Input : x = 197
Output : Yes
197 has 3 digits, so n = 3
The number is Keith because it appears in the special
sequence that has first three terms as 1, 9, 7 and 
remaining terms evaluated using sum of previous 3 terms.
1, 9, 7, 17, 33, 57, 107, 197, .....

Input : x = 12
Output : No
The number is not Keith because it doesn't appear in
the special sequence generated using its digits.
1, 2, 3, 5, 8, 13, 21, .....

'''


x =(input('Enter number'))

def keithno(n):
   res = [int(digit) for digit in n]

   total=sum(res)
   print(total)

   res.append(total)
   print(res)

   while total <= int(n):

         total= sum(res[-len(n):])

         res.append(total)

         
   print(res)
         
   if int(n) in res:
      print('true')
   
   else:
      print('false')

keithno(x)

      

   


   
   

