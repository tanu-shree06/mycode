#code 3
'''
string = input('enter string:')

for i in string.split():
   
   if i.lower() == i[::-1].lower():
      continue

   else:
      print(i, end=' ') 
'''

#code 5
string=input('enter string:')

rev =len(string)

for i in range(len(string)):
   
   if string[i].isalnum() == False:
      
      print(string[i], end='')
      
   else:
      
      while string[rev -1].isalnum() == False:
         
         rev -= 1
         
      print(string[rev - 1], end='')
         
      rev -= 1