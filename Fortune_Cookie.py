import random
def fortune_cookies():
    r_num = random.randint(0,7)
    if r_num == 1:
        print("Don't pursue happiness – create it.")
    elif r_num == 2:
        print ("All things are difficult before they are easy.")
    elif r_num == 3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif r_num == 4:
        print("Someone in your life needs a letter from you.")
    elif r_num == 5:
        print("Don't just think. Act!")
    elif r_num == 6:
        print("Your heart will skip a beat.")
    elif r_num == 7:
        print("The fortune you search for is in another cookie.")
    else:
        print("Help! I'm being held prisoner in a Chinese bakery!")
fortune_cookies()
fortune_cookies()
fortune_cookies()