#CGPA and SGPA Calculator Created by Bunny.
import sys
import time
import os
#system call
os.system("")
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


#Welcome Screen
print_slow(style.RED + "======================================================\n")
print_slow( style.YELLOW + "=================   Welcome TO   =================\n")
print_slow(style.YELLOW + "===========   CGPA & SGPA calculator    ===========\n")
print_slow(style.RED + "======================================================\n\n")

#time.sleep(3)
print(style.RESET+"Enter Your choice ONLY 1 OR 2 with respective OPTION\n")
print("====================== 1 LET'S START TOOL ==========================")
print("====================== 2 INSTRUCTION ===============================")

choice=int(input("Enter YOUR Choice 1 OR 2\n"))
while choice==2:
    print_slow("======== Befor using This Tool or Calculating Your CGPA or SGPA ====\n")
    print_slow("======== You should alredy have to KNOW Three Things ======\n")
    print_slow("======== FIRST - Your Subject Grades\n ")
    print_slow("======== Second - Perticular Subject Credit \n")
    print_slow("======== Third - Total Cureent Semister Credit \n")
    print_slow(style.RED+"======== NOTE: You can find credit score from your syllabus PDF.\n Download it from your college website ========= \n")
    print_slow(style.RESET+"=========================================================================================================\n")

    choice+=1




dict ={'A++':10,'A+':9,'A':8,'B+':7,'B':6,'C+':5,'D':0}
l=[]
s='.........................................'
def checkGrade(dict,grade):
    if grade in dict:
        gr=(dict[grade])
        def mul(gr,credit):
            mul=gr*credit
            l.append(mul)
            #return(l)
            return(s)
        #calling Multiplication fuction Grade*credit
        print(mul(gr,credit)) 
        return(s)
        
    else:
        print("try again\n")
    
#grade=input("Enter grade\n")
#credit=int(input("enter credit\n"))
#print(checkGrade(dict,grade))


n=int(input("Enter Total Number of Subject do you have in current semister\n NOTE:ONLY SUBJECT NOT PRACTICAL\n"))

for i in range(+1,n+1): 
    print("Enter Suject",i,"Grade =")
    grade=input("").upper()
    credit=int(input("Enter credit\n"))
    checkGrade(dict,grade)


p=int(input("Enter Total Number of  Practical suject\n"))

for i in range(+1,p+1):
    print("Enter Practical",i,"Grade =")
    grade=input("").upper()
    credit=int(input("Enter Credit\n"))
    checkGrade(dict,grade)
    #return(s)



T_credit=int(input("Enter Total Number of Credit for this semister\n"))
#return(s)
#N_sem=int(input("Which Number of Semister This is Enter Number\n"))

Sum=sum(l)   
SGPA=Sum/T_credit
#CGPA=SGPA/N_sem


print(style.MAGENTA+"Your SGPA Score is =",SGPA,"")
#print(style.MAGENTA+ "Your CGPA Score is =",CGPA,"")