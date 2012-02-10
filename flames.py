#!/usr/bin/env python
name1 = " "
name2 = " "
name2bkup = " "
out = " "
flames_list = " "

#Module to accept user input
def getnames():
    global name1, name2
    name1 = raw_input('Enter your name: ')
    name2 = raw_input('Enter the second name: ')
  
#Module to calculate the number to be used in FLAMES
def calculate():
    global name1, name2,name2bkup, out
    name1 = name1.lower()
    name2 = name2.lower()
    name2bkup = name2
    count = 0    #Initializing count, should update to use __init__ soon
    name_length = len(name1) + len(name2)
    for name1_letters in name1:
        for name2_letters in name2:
            if name1_letters==name2_letters:
                name2 = name2.replace(name2_letters,"0",1)
                count = count+1
                break
    out = name_length - (2*count)

#This Module performs the actuval flames function using the number obtained from calculate()
def flames():
    global out, flames_list
    flames_list = ['FRIEND','LOVE','AFFECTION','MARRIAGE','ENEMY','SISTER','0']
    calculated_no = out
    count = 6   #No of letters in flames(6)
    array_adjust = 1
    for n in flames_list:
        if(count <= 1):
            break
        mod_holder = out % count
        array_adjust = mod_holder - 1
        while ((array_adjust<>count)&(array_adjust>=0)):
            flames_list[array_adjust] = flames_list[array_adjust+1]
            array_adjust = array_adjust + 1

        if(mod_holder == 0):    #If mod_holder is zero then last letter is to be removed
            count_cal = 0
            flames_list[count - 1] = 0    #last letter is made zero
        else:
            count_cal = count - mod_holder    #Calculates the no of letters after the removed letter aka 0'd letter in flames_list
        out = calculated_no      #Restore old calculate value
        out = out - count_cal    #Calculate modified value as per new no of letters present
        count = count - 1
        
def say():
    global flames_list, name1, name2bkup
    if flames_list[0] == 'FRIEND':
        print '%s and %s are Friends' %(name1,name2bkup)
    elif flames_list[0] == 'LOVE':
        print '%s and %s are meant to Love each other' %(name1,name2bkup)
    elif flames_list[0] == 'AFFECTION':
        print '%s and %s will show Affection on each other' %(name1,name2bkup)
    elif flames_list[0] == 'MARRIAGE':
        print '%s and %s will get Married soon' %(name1,name2bkup)
    elif flames_list[0] == 'ENEMY':
        print '%s and %s are Enemies forever' %(name1,name2bkup)
    else:
        print '%s is %s`s sister/brother ' %(name1,name2bkup)
    print '',
getnames()
calculate()
flames()
say()



