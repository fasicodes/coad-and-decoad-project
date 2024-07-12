#i take a verible (mess) for taking message 
mess= input("enter the message: ")
words=mess.split(" ")

coding = (input("click 1 for coding and 0 for decoding: "))


coding = True if (coding=="1") else False
if coding :
    nwords=[]       #nwords is empty list and i add coad into
    for word in words:
        if len (word)>=3:
           ran=["rks","ter","yer","ubd","jsu","duy","sli","bhs","kus","alu","kiu","kjs","avx","eqw","gal","ads","okl","fad","qzp","jhg","dgf"]  #ran stand for random characters
           
           from random import choice
           ran1=choice(ran)
           
           
           coad= ran1 + word[1:] + word[0] + ran1 #coad variable convert the word into coad

           nwords.append(coad)
        else:
            nwords.append(word[::-1])
 
    print(" ".join(nwords))

else :
    nwords=[]
    for word in words:
     if len(word)>=3:
        remove = word[3:-3] # remove is veriable and it remove fist and last random characters

        decoad = remove[-1] + remove[:-1]
        nwords.append(decoad)
     else:
        nwords.append(word[::-1])   
    print(" ".join(nwords))
  
     
        



    








           




           




        



