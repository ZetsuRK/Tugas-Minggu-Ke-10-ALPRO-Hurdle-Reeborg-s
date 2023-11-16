"""
    Kelas    : 2023E
    Prodi    : D4 Manajemen Informatika
    Kelompok : 5

    Nama Anggota :
    1. Achmad Syamsudin       - 23091397164
    2. Ahmad Aryobimo         - 23091397151
    3. Vergi Mutia Rahmasyani - 23091397171
"""
#Hurdle 1 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for i in range(6) :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Hurdle 2 :
Hurdle 2 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal() :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Hurdle 3 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
       move()
    else:
        jump()

#Hurdle 4 :
