
import random
import pyautogui as pg
import time
list=[]
c=0
while True:
    print("                                             |||||||  Welcome to Message Spammer!  ||||||| ")
    time.sleep(0.5)
    print("                                                        Made By Runaal Bhowmick                           ")
    time.sleep(0.5)
    print("                                                     In Case of Any Issue or Querry                                ")
    time.sleep(0.5)
    print("                                                   Please DM me in Instagram  @runaal._                                                                 ")
    print("\n")
    time.sleep(2)
    times=int(input("Enter the Number of times you want to Spam:-"))
    print("\n")
    n=int(input("Enter the total Number of words you want To Spam with:-"))
    print("\n")
    for i in range (0,n):
        word=input("Input Your Consecutive Words one by one:-")
        print("\n")
        list.append(word)
    print("Words To Spam:-",list)
    print("\n")
    print("Please Switch To your Targeted Person's Chatbox.......")
    print("\n")
    time.sleep(2)
    print("Please Wait for Five Secs..........." )
    print("\n")
    time.sleep(5)
    for i in range(times):             
        a=random.choice(list)
        pg.write(a)
        pg.press('enter')
    print("Spam Suucessful!!!!!")
    print("\n")
    print("To Spam More Continue The Process or Close the Application")
    print("\n")
    time.sleep(2)
    list.clear()




    
'''



import random
import pyautogui as pg
import time
animal=('','')
time.sleep(2)
for i in range(50):
    a=random.choice(animal)
    pg.write(''+a)
    pg.press('enter')

'''