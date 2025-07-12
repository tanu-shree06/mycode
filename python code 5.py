#Convert number ruppee to word

rupp = int(input("Enter Number "))

def ruppee_to_word(rupp):
   
    below20 = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    above20 = ["","","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def twodigit(rupp):
        if rupp < 20:
            return below20[rupp]
        else:
            return above20[rupp // 10] + (" " + below20[rupp % 10] if rupp%10 != 0 else "")

    def threedigit(rupp):
        if rupp == 0:
            return ""
        elif rupp < 100:
            return twodigit(rupp)
        else:
            return below20[rupp//100] + 'hundred' + (" " + twodigit(rupp % 100) if rupp%100 != 0 else "")

    list1=[]
    
    crore = rupp//10000000
    
    if crore:
        if len(str(crore))==2:
            list1.append(twodigit(crore)+' crore')
            rupp = rupp%10000000
        else:
            list1.append(threedigit(crore)+' crore')
            rupp=rupp%10000000

    lakh= rupp//100000
    
    if lakh :
        list1.append(twodigit(lakh) + 'Lakh')
        rupp=rupp%100000

    thousand= rupp//1000
    
    if thousand:
       
        list1.append(twodigit(thousand) + "Thousand")
        rupp=rupp%1000

    hundred= rupp//100

    
    if hundred:
       
        list1.append(below20[hundred]+"Hundred")
        rupp=rupp%100

    if rupp:
        if list1:
            list1.append("and "+twodigit(rupp))
        else:
            list1.append(twodigit(rupp))

    return 'Rs '+ ' '.join(list1)

words = ruppee_to_word(rupp)
print(words)









