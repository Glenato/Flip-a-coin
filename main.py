import random
import colorama
#Creation of heads and tails variables, after which a random number will be chosen between 0 and 1 if it's 0 then it's heads if it's 1 then it's tails
tails = int(0)
head = int(1)
numbertails = int(0)
numberhead = int(0)

#Creating a variable that count how many times the coint was trown
 
n = int(0)

#Printing a nice ascii art

print (colorama.Fore.YELLOW + """\
\n
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \ 
  /`       .-'~"-.       `\ 
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;          /      \\)P    ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`

""")
       
#Creating a variable in witch the user can choose how many times the coin will be tossed

i = int(input (colorama.Fore.WHITE + "How many times do you want the coin to be tossed? ?\n"))

#Creating a loop in with the coin will be flipped as many times as the user asked it

while n < i:
    num = int(random.randint(0,1))
    #percentage system to monitor progress of the algorithm
    percentage = float(n/i*100)
    if num == tails:
        numbertails += 1

    elif num == head:
        numberhead += 1

    else:
        print ("ERRROOOORR")

    print(f"{round(percentage,3)} %")
    n +=1
print("100 %")

#Creating a variable that print in percentage how many times tails and head have appered

percentagetails = float(numbertails/n*100)
percentagehead = float(numberhead/n*100)

print (f"Number of time tails : {numbertails}\nPercentage of appearance of tails : {round(percentagetails,5)} %\nNumber of time head : {numberhead}\nPercentage of appearance of head : {round(percentagehead,5)} %\nNumber of times the coin was tossed : {n}")
