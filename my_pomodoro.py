import time

def pmdro_home():
    '''
    main function!
    '''
    response1 = input("Welcome! Please select how long a study session you would like.\nFor 5 mins -> 1\nFor 10 mins -> 2")
    if response1 == "1":
        timer_loop(300)
    elif response1 == '2':
        timer_loop(600)
    else:
        print("Error. Please try again!")
        pmdro_home()

def timer_loop(number:int):
    '''
    function for handling the countdown sequence. i commented out the 'print # seconds' part because while im studying i really only just
    care about how many minutes there are, not seconds lol
    '''
    while number > 0:
        minute_helper(number)
        #print(number)
        number -= 1
        time.sleep(1)
    print("Timer Done!")

def minute_helper(time_left:int):
    '''
    helper function, called by the timer_loop function. basically just checking if the remaining time is divisable by 60 (meaning there is
    a whole number of minutes left) and printing how many minutes left in the timer.
    '''
    num = time_left / 60
    if num % 1 == 0:
        print ("you have " + str(int(num)) + " minutes left!")

pmdro_home()