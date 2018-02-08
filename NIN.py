# coding: utf-8
import time
from time import sleep
import sys
import itertools
import os

print("███╗   ██╗██╗███╗   ██╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗");
sleep(0.2);
print("████╗  ██║██║████╗  ██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗");
sleep(0.2);
print("██╔██╗ ██║██║██╔██╗ ██║    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝");
sleep(0.2);
print("██║╚██╗██║██║██║╚██╗██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗");
sleep(0.2);
print("██║ ╚████║██║██║ ╚████║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║");
sleep(0.2);
print("╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝");
sleep(0.4);
print("by Neoxidine".rjust(83));

print("\n\n\n Just getting stuff ready \n\n\n")

sleep(0.5)

toolbar_width = 81

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")

print("\n\njust give us 1 second")
sleep(1.0)

os.system('clear')

invalid_input = True


def start():
    print("1) JANUARY \n 2) FEBUARY \n 3) MARCH \n 4) APRIL \n 5) MAY \n 6) JUNE \n 7) JULY \n 8) AUGUST \n 9) SEPTEMBER \n 10) OCTOBER \n 11) NOVEMBER \n 12) DECEMBER \n 13) EXIT")

while invalid_input:
    start()
    
    month = input("What month was the subject born? ")
    if(month == 13):
       invalid_input = False
       sys.exit(0)
    elif(month < 1 or month > 12):
        print ("Sorry, that was an invalid command!")
        sleep(1)
        os.system('clear')
        invalid_input = True
    else:
        os.system('clear')
        print("1) 1990 \n 2) 1991 \n 3) 1992 \n 4) 1993 \n 5) 1994 \n 6) 1995 \n 7) 1996 \n 8) 1997 \n 9) 1998 \n 10) 1999 \n 11) 2000 \n 12) EXIT")
        year = input("What year was the subject born? ")
        if(year == 13):
            exit
        elif(year < 1 or year > 11):
            print ("Sorry, that was an invalid command!")
            sleep(1)
            os.system('clear')
        else:
            os.system('clear')
            invalid_input = False

print("Few seconds and you will have your list. Should be saved in root/NINCrack.txt")
        
filename = "NINCrack.txt"
if (month == 1 and year == 1):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 2):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 3):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 4):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 5):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 6):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 7):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 10):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 8):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 9):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 10):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()

elif (month == 1 and year == 11):
    file = open((filename), "w")
    for i in range(1000000):
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"A\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"B\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"C\n")
        file.write("PE"+str('{:d}'.format(i).zfill(6))+"D\n")
file.close()
    



