"""
bank robbery game
"""


import random


def main():
    """
    the main function which greets player and tells about plot
    """

    print("""
Welcome to the \"Bank Robbery\"! 
You decided to steal money from a bank.  
On your way to the success you'll 
have to complete difficult
but interesting tasks! Good luck!
""")

    registration()


def registration():
    """
    player's registration
    """

    global first_name
    global last_name

    print("""Firstly, you have to create fake passport. 

Enter your new first name:""")
    first_name = input(">>> ")
    while len(first_name) <= 1:
        print("\nName must be consisted at least of 2 letters!")
        print("\nEnter your new name: ")
        first_name = input(">>> ")

    print("\nEnter your new last name: ")
    last_name = input(">>> ")
    while len(last_name) <= 1:
        print("\nLast name must be consisted at least of 2 letters!")
        print("\nEnter your new last name: ")
        last_name = input(">>> ")

    confirmation()


def confirmation():
    """
    asks player whether he is ready to start
    """

    print("\nAre you sure want to start?(type 'yes' or 'no')")
    answer_confirmation = input(">>> ")
    if answer_confirmation == "yes":
        print("\nLet's go!")
        start_game()
    elif answer_confirmation == "no":
        while answer_confirmation != "yes":
            print("""
Think one more time! 
You'll have enough money
to buy everything you want!""")
            print("\nAre you sure want to start?(type 'yes' or 'no')")
            answer_confirmation = input(">>> ")
            if answer_confirmation == "yes":
                print("\nLet's go!")
                start_game()
            elif answer_confirmation == "no":
                return()
            if answer_confirmation == "no":
                return()
            elif answer_confirmation != "yes":
                print("\nI didn't understand you, try again.")
    else:
        print("\nI didn't understand you, try again.")

        confirmation()


def start_game():
    """
    the beginning of the game, first chance to lose
    """

    print("""
You entered the richest bank in your town
through the main entrance and 
tried to enter service room but
the security guard told that you 
are not allowed go there.

So, what would you do?

1 - Tell him that you are warehouse worker

2 - Attack him and try to go through

Type 1 or 2:""")
    answer_start_game = str(input(">>> "))
    if answer_start_game == '1':
        print("\nRight decision, but...")
        guard_question()
    elif answer_start_game == '2':
        print("""
Bank workers noticed 
your attack with videcams and
called the police. You are arrested!
""")
        try_again()
    else:
        print("\nI didn't understand you, try again.")
        start_game()


def guard_question():
    """
    task from a security guard
    """

    random_num = random.randint(1, 30)
    print(f"""
The security guard told 
you that every worker here
knows how to convert integer to octal 
and you have to convert the number he said.
Convert '{random_num}' to octal please.

For example: 0o36, 0o6.

Type your answer:""")
    answer_guard_question = str(input(">>> "))

    if answer_guard_question == str(oct(random_num)):
        print("\nCongrats, now you can go in.")
        service_room()
    else:
        try_again()


def service_room():
    """
    task in a service room
    """

    print("""
You entered service room and 
noticed the lock of a large safe, 
where there is a lot of gold and 
money, but there is video 
surveillance in the room. You can 
cut the power supply to 
the camera by cutting the correct 
wire. Here are 4 wires of 
different colors: green, yellow, blue, 
red. In the same order. 
A friend told you before the robbery 
that the camera is supplied 
with power:

1)NOT the red wire
2)Not the one on the far left
3)Not the one next to the green

What color is the wire you need to cut?

For example: 'green', 'yellow', 'blue' or 'red'.

Typer your answer:""")
    answer_service_room = input(">>> ")

    if answer_service_room == "blue":
        print("\nYes. You're right")
        safe_binary()
    elif answer_service_room == "green" or "yellow" or "red":
        try_again()
    else:
        print("\nI didn't understand you, try again.")
        service_room()


def safe_binary():
    """
    task near safe       
    """

    binaries = ""
    binaries_int_amount = ""

    for random_binary in range(0, 5):
        binaries_int = random.randint(1, 9)
        binaries_int_amount += str(binaries_int) + " "
        binaries += str(bin(binaries_int))
    print(f"""
You have a little time left 
until the security system went 
into action. You went to the 
safe and noticed the code:

{binaries_int_amount}.

You need to calculate every single 
number and convert it to 
binary, then write them together without spaces. 

For example:
1 2 3 4 5 --> 0b10b100b110b1000b101.

Type your answer:""")
    answer_safe_binary = str(input(">>> "))
    if answer_safe_binary == binaries:
        hacker()
    else:
        try_again()


def hacker():
    """
    task with hacker
    """

    global first_name
    global last_name
    random_first_num = random.randint(25, 70)
    random_second_num = random.randint(7, 16)
    operation = [42, 43, 45]
    random_operation = chr(random.choice(operation))
    if ord(random_operation) == 42:
        answer_right_hacker = random_first_num * random_second_num
    elif ord(random_operation) == 43:
        answer_right_hacker = random_first_num + random_second_num
    elif ord(random_operation) == 45:
        answer_right_hacker = random_first_num - random_second_num
    total_answer_hacker_right = str(first_name[0]) + \
        str(last_name[0]) + str(answer_right_hacker)

    print(f"""
You robbed the bank and left it 
in time. Now you are trying to hide, because 
the police are looking for you. You asked the 
hacker to remove the recordings from video
cameras and other evidence, but he said 
that you need to indicate the first letter 
of your first name and the first one from 
the last name that you indicated when creating 
the character + the result of calculating random 
numbers without spaces.

For example, Vlad Shuliar 17 + 76 -> VS93.

{random_first_num} {random_operation} {random_second_num} = ?

Your answer:""")
    answer_hacker = input(">>> ")

    if answer_hacker == total_answer_hacker_right:
        victory()
    else:
        try_again()


def victory():
    """
    if player completed all tasks succesfully it congrats him
    """

    print("""
You've won, congratulations! Here's your money!

                    100       1001                
                    00011     10011               
                    00011     10011               
                    00011     10011               
                  11000000001100011               
              1100000000000000000000011           
           110000000000000000000000000001         
         1000000000000000000000000000000001       
        1000000000000001111111000000000000001     
       000000000011100011     1001000000000000    
      0000000000111100011     10011110000000000   
     1000000000111  00011     10011  11000000001  
     000000000011   00011     10011    10000111   
     000000000011   00011     10011     1111      
     100000000001   00011     10011               
      0000000000001100011     10011               
       0000000000000000001111 10011               
        10000000000000000000000000111             
          100000000000000000000000000001          
             110000000000000000000000000001       
                11100000000000000000000000001     
                    00011100000000000000000001    
                    00011   11100000000000000011  
                    00011     1001100000000000011 
    101             00011     1001111000000000011 
   100001           00011     10011  0000000000111
 100000001          00011     10011  0000000000011
 00000000001        00011     10011 10000000000111
  1000000000011     00011     10011 10000000000111
   100000000000011  00011     1001100000000000011 
     10000000000000000011     1000000000000000111 
       10000000000000000000000000000000000000111  
         10000000000000000000000000000000001111   
           1100000000000000000000000000001111     
              11000000000000000000000011111       
                  1100000000000001111111          
                    0011111111100111              
                    00111     10011               
                    0011      10011               
                    0011      10011               
                     111       1111                                                  

Type 'yes' if you want to play again:""")
    answer_victory = input(">>> ")

    if answer_victory == "yes":
        registration()
    else:
        return()


def try_again():
    """
    chance to try again if player lost
    """

    print("""
You lost but can try again to play this game!
If you would you like to then type 'yes':""")
    try_again_answer = input(">>> ")

    if try_again_answer == 'yes':
        registration()
    else:
        return()


if __name__ == "__main__":
    main()
