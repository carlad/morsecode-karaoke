# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:11:13 2013

@author: Claudine
"""
def print_welcome(iterations):
    import time
    for index in xrange(iterations):
        print r'''\
.....------....--------................................---------...............
....--------.----------..............................------------..............
...-------------------.............................-------------..........--...
..----..-------..----.............................----.....----..........--....
.----...-----...----..---.--.--...----..----.....----...................--.....
----....---....----.--.--.-----..--.--.--.--....----...........---..-----..--..
---.....--....----.--.--.--...-...--..-----....----..........--.--.--.--.--.--.
--...........----.--.--.--.....--.--.--.......----..........--.--.--.--.-----..
-...........----..---...--.....----..----....----.....----.--.--.--.--.--......
............-----............................------------..---...----..----....
...............----............................--------........................
......----.......----............................................:::::.........
.....----......----.......................--...................:::::::::.......
....----.....----.......................--.....................:::::::::.......
...----....----........................--....................../  \::::........
..----...----.----.--.--..----..----..--..--..---.............//   /...........
.----..----.....--.-----....--.--.--.--.--..--.--............./ \ /............
---------....----.--.....----.--.--.----...-----............./  /..............
---.----...--.--.--....--.--.--.--.--.--..--................/  /...............
--...----..-----..--...-----.----..--..--..---............./  /................
-.....----................................................/  /.................
.......----............................................../  /..................
........----............................................/  /...................
.........----............................................\/....................
..........----.................................................................
'''
        time.sleep(1)
        print r'''\
-----......----........--------------------------------.........---------------
----........-..........------------------------------............--------------
---...................-----------------------------.............----------..---
--....--.......--....-----------------------------....-----....----------..----
-....---.....---....--...-..-..---....--....-----....-------------------..-----
....----...----....-..-..-.....--..-..-..-..----....-----------...--.....--..--
...-----..----....-..-..-..---.---..--.....----....----------..-..-..-..-..-..-
..-----------....-..-..-..-----..-..-..-------....----------..-..-..-..-.....--
.-----------....--...---..-----....--....----....-----....-..-..-..-..-..------
------------.....----------------------------............--...---....--....----
---------------....----------------------------........------------------------
------....-------....-------------------------------------:::::----------------
-----....------....-----------------------..------------:::::::::--------------
----....-----....-----------------------..--------------:::::::::--------------
---....----....------------------------..----------------::::/  \--------------
--....---....-....-..-..--....--....--..--..--...-----------\   \\-------------
-....--....-----..-.....----..-..-..-..-..--..-..------------\ / \-------------
.........----....-..-----....-..-..-....---.....---------------\  \------------
...-....---..-..-..----..-..-..-..-..-..--..--------------------\  \-----------
..---....--.....--..---.....-....--..--..--...-------------------\  \----------
.-----....--------------------------------------------------------\  \---------
--------....-------------------------------------------------------\  \--------
---------....-------------------------------------------------------\/---------
----------....-----------------------------------------------------------------
'''
        time.sleep(1)
    

def print_message(mess_type):
    if mess_type == 'welcome':
        print_welcome(2)
    elif mess_type == 'result1':
        print '''\
result1
'''
    elif mess_type == 'result2':
        print '''\
result2
'''
    elif mess_type == 'result3':
        print '''\
result3
'''
    elif mess_type == 'result4':
        print '''\
result4
'''


def print_funsies():
    import time
    print """
    (._.)
    <) )J
     / \\
    """
    time.sleep(1)
    print """
    ( ._.)
    \( (>
     / \\
    """
    time.sleep(1)
    print """
    (._.)
    <) )J
     / \\
    """
    time.sleep(1)
    print """
    ( ._.)
    \( (>
     / \\

    """
