import random
#from easygui import *
#import sqlite3
#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
#import matplotlib.pyplot as plt
import time


TOTAL = {'Peter': 0, 'Chi': 0, 'Yazi': 0, 'Tijana': 0, 'Anne': 0, 'Sean': 0,'Nayereh': 0,'Elliott': 0, 'Tom': 0, 'Lynsey': 0, 'Rui': 0,'Steve': 0, 'Ali': 0,'Stefan': 0, 'Henry': 0, "Bonolo": 0,  "Nadia": 0, "Sarah": 0, "Kylie": 0, "Reni": 0}
CURRENT_NUM = {}
AVG_NUM = 4
NUM_TO_REACH_AVG = 0
NUM_OF_WEEKS_REST = 0
POTENTIAL_MINUTERS = {}
SELECTED_MINUTER = {}
UPDATED_NUM = {}
ABSENT = {}
REST_GROUP = {}
WEEKS_SINCE_MINUTES = {'Peter': 2, 'Chi': 1, 'Tijana': 3, 'Anne': 1, 'Sean': 4,'Nayereh': 5,'Elliott': 8, 'Tom': 12, 'Lynsey': 25, 'Rui': 28,'Steve': 32, 'Ali': 99,'Fjodors': 99}
#db = sqlite3.connect('DB.db')
#c = db.cursor()
#db.text_factory = str
MEMBERS = {}


def AVG_MINUTE_SORTER_OLD():
    for n,v in TOTAL.iteritems():
        if v < AVG_NUM:
            POTENTIAL_MINUTERS[n] = v  # Add new entry
        else:
            REST_GROUP[n] = v
    #print POTENTIAL_MINUTERS

def AVG_MINUTE_SORTER():
    #print AVG_NUM
    for n,v in MEMBERS:
        if v < AVG_NUM:
            POTENTIAL_MINUTERS[n] = v  # Add new entry
        else:
            REST_GROUP[n] = v
    #print POTENTIAL_MINUTERS



def ABSENTEE_LIST():
    for n,v in ABSENT.iteritems():
        POTENTIAL_MINUTERS.pop(n,v)


def CHOOSE_MINUTER():
    SELECTED_MINUTER = random.choice(POTENTIAL_MINUTERS.keys())
    #country, capital = random.choice(list(d.items()))
    print "Chosen minuter is: " + SELECTED_MINUTER
    #ccbox(SELECTED_MINUTER)

def GUI():
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):  # show a Continue/Cancel dialog
        pass  # user chose Continue
        msg = "Do you want to continue?"
    else:  # user chose Cancel
        print "bye"




def getCurrentMembers():
    c.execute("SELECT Name, Total_Minutes FROM Members WHERE Current_Member = 'Yes' ORDER BY Name ASC")
    #ar = c.fetchall()
    #print c.fetchall()
    #MEMBERS = [r[0] for r in c.fetchall()]
    global MEMBERS
    MEMBERS = [r for r in c.fetchall()]


def calAVG():
    global  totalMin
    totalMin = [x[1] for x in TOTAL]
    #print totalMin
    global AVG_NUM
    AVG_NUM = avg(totalMin)
    #print AVG_NUM
    #print np.mean(totalMin)
    #print sum(totalMin) / float(len(totalMin))
    #print reduce(lambda x, y: x + y, totalMin) / len(totalMin)


def avg(l):
    return sum(l, 0.0) / len(l)


def MAIN():
    AVG_MINUTE_SORTER_OLD()
    ABSENTEE_LIST()
    CHOOSE_MINUTER()
    #getCurrentMembers()
    #calAVG()
    #AVG_MINUTE_SORTER()
    #graphTotalMinutes()
    #GUI()



def graphTotalMinutes():
    MemberNames = [x[0] for x in MEMBERS]
    y_pos = np.arange(len(MemberNames))
    MemberMinuteTotals = [x[1] for x in MEMBERS]
    plt.bar(y_pos, MemberMinuteTotals, align='center', alpha=0.5)
    plt.xticks(y_pos, MemberNames)
    plt.xlabel('Member')
    plt.ylabel('Total number')
    plt.title('Total number of times taking minutes')
    plt.savefig('TotalMinutes.png')
    #plt.show()

MAIN()

#msgbox("Hello, world!")

#AVG_MINUTE_SORTER()
#ABSENTEE_LIST()
#CHOOSE_MINUTER()
#getCurrentMembers()
#calAVG()




#print REST_GROUP
