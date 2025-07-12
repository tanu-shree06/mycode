
print('a Program to count the number of Vowels, Consonants, Digits and White space in a string.\nb Program to delete all occurrences of a character from the String. \nc Program to count the number of occurance of a particular word in thestring.')

n=input('Enter a/b/c for respective program')

if n=='a':
   
   c,v,num,ws=0,0,0,0
   
   string=input('Enter Input to count the number of Vowels, Consonants, Digits and White space in a string:')
   
   for element in string:
      if element in 'aeiouAEIOU':
         v+=1
      if element.isdigit()== True:
         num+=1
      if element not in 'aeiouAEIOU' and element.isalpha() == True:
         c+=1
      if element == ' ':
         ws+=1
   print('Vowels:',v,'\nConsonants:',c,'\nDigits:',num,'\nWhitespace:',ws)

if n=='b':

   string=input('Enter string:')
   char=input('Enter character to delete')

   s=''

   for i in string:
      if i != char:
         s+=i
   print(s)

if n=='c':
   
   string=input('Enter string:')
   word =input('Enter character to count:')

   c=0

   string1=string.replace(',',' ')
   

   for i in string1.split():
      print(i)
      if i==word:
         c+=1
   print('Count:',c)
