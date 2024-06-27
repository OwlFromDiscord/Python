import random
symbols = ['🍒', ' 🍇', '🍉', '7️⃣']

def play():
    keep_playing = "Y"
    while keep_playing != "N":    
        results = random.choices(symbols, k=3)
        print(results[0] + "|" + results[1] + "|" + results[2])
        if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
            print("Jackpot! 💰")
        else:
            print("Try Again!")
        keep_playing == (input("Would You Like To Play Again? (Y/N)"))

play()