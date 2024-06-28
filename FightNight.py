import random
print("   [][][][][][][][]       [][][][][]          [][][][]         [][]      [][]       [][][][][][][]")
print("   [][][][][][][][]       [][][][][]        [][][][][][]       [][]      [][]       [][][][][][][]")
print("   [][]                      [][]         [][]                 [][]      [][]            [][]")
print("   [][][][][][][][]          [][]         [][]                 [][]      [][]            [][]")
print("   [][][][][][][][]          [][]         [][]                 [][][][][][][]            [][]")
print("   [][]                      [][]         [][]    [][][][]     [][][][][][][]            [][]")
print("   [][]                      [][]         [][]      [][][]     [][]      [][]            [][]")
print("   [][]                      [][]         [][]       [][]      [][]      [][]            [][]")
print("   [][]                   [][][][][]        [][][][][][]       [][]      [][]            [][]")
print("   [][]                   [][][][][]         [][][][][]        [][]      [][]            [][]")
print("")
print("")
print("[][][][]        [][]       [][][][][]          [][][][]         [][]      [][]       [][][][][][][]")
print("[][][][][]      [][]       [][][][][]        [][][][][][]       [][]      [][]       [][][][][][][]")
print("[][][] [][]     [][]          [][]         [][]                 [][]      [][]            [][]")
print("[][][]  [][]    [][]          [][]         [][]                 [][]      [][]            [][]")
print("[][][]   [][]   [][]          [][]         [][]                 [][][][][][][]            [][]")
print("[][][]    [][]  [][]          [][]         [][]    [][][][]     [][][][][][][]            [][]")
print("[][][]     [][] [][]          [][]         [][]      [][][]     [][]      [][]            [][]")
print("[][][]      [][][][]       [][][][][]        [][][][][][]       [][]      [][]            [][]")
print("[][][]        [][][]       [][][][][]         [][][][][]        [][]      [][]            [][]")
print("")
print("                              Developed by @OwlFromDiscord on Github")
print("                                       All Rights Reserved")
print("")
print("4")
print("Welcome to Fight Night. Please pick up your boxing gloves and put in your mouthguard. Keep your hands up and prepare to land some blows!")

playerHealth = 3
oppHealth = 3

print('''You step into the ring against your matchup for tonight's bout. After the traditional rules statement by the official,
      you touch gloves with your opponent and prepare to fight. Do you want to open up with a bang and go for an uppercut, or
      or choose to play it safe and go for a solid jab to the body? The uppercut hits harder, but is also harder to hit with!
       
                                   1) Go for the uppercut!

                                   2) Jab for the likely hit!''')
while playerHealth > 0 and oppHealth > 0: #Checks to make sure no one has won the fight
    rng = random.randint(1,7)
    action1 = int(input("Input 1 or 2 and press 'Enter' "))
    if playerHealth == 3 and oppHealth == 3: #facilitates different dialogue based on health values, makes a stale and repetitive "game" feel less so
        if action1 == 1 and rng >= 4: #player misses uppercut
            print("You go for the uppercut but you tragically miss!! Your opponent nimbly dodges out of the way as you regain your footing!")
            rng = random.randint(1,3)
            if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                playerHealth -= 1
            elif rng != 1 and oppHealth > 0 : #opponent misses
                print("Your opponent goes for a right hook, but your quick reflexes allow you to nimbly weave out of the way!")
            else: #opponent's health is depleted
                print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
        elif action1 == 1 and rng < 4: #player hits uppercut, dealing 2 dmg to opponent
            print("You go for a big swing to start things off and it pays off!! Your opponent falls flat onto their back, and the referee begins the count. They make it all the way to 4 before your opponent stands back up and returns to the fight!")
            oppHealth -= 2
            rng = random.randint(1,3)
            if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                print("Despite just having been knocked to the floor, your opponent responds with a surprisingly quick right hook. You aren't able to block in time and get hit square in the jaw!")
                playerHealth -= 1
            elif rng != 1 and oppHealth > 0 : #opponent misses
                print("Your opponent goes for a right hook, but it's clumsy and uncoordinated due to the hit he just took! You're able to dodge out of the way with ease!")
            else: #opponent's health is depleted
                print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
        elif action1 == 2 and rng >=4: #player hits Jab:
            print("You decided to go for a quick jab to start things off! As your fist makes contact with your opponent's body, they stumble slightly!")
            oppHealth -= 1
            rng = random.randint(1,3)
            if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                playerHealth -= 1
            elif rng != 1 and oppHealth > 0 : #opponent misses
                print("Your opponent goes for a right hook, but their slowed reflexes due to the blow they suffered allow you to nimbly weave out of the way!")
            else: #opponent's health is depleted
                print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
        elif action1 == 2 and rng < 4:
            print("You decided to go for a quick jab to start things off! Before your fist can make contact, your opponent gets their hands in the way and blocks the punch!")
            rng = random.randint(1,3)
            if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                playerHealth -= 1
            elif rng != 1 and oppHealth > 0 : #opponent misses
                print("Your opponent goes for a right hook, but their slowed reflexes due to the blow they suffered allow you to nimbly weave out of the way!")
            else: #opponent's health is depleted
                print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
    elif playerHealth > 0 and oppHealth > 0:
        print("Another round of fighting begins! What will you do this time: Uppercut or Jab?")
        print("")
        print("")
        print("                             1) Go for the uppercut!")
        print("")
        print("                             2) Jab for the likely hit!")
        rng = random.randint(1,7)
        if playerHealth != 3 or oppHealth != 3: #facilitates different dialogue based on health values, makes a stale and repetitive "game" feel less so
            if action1 == 1 and rng >= 4: #player misses uppercut
                print("You go for the uppercut but you tragically miss!! Your opponent nimbly dodges out of the way as you regain your footing!")
                rng = random.randint(1,3)
                if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                    print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                    playerHealth -= 1
                elif rng != 1 and oppHealth > 0 : #opponent misses
                    print("Your opponent goes for a right hook, but your quick reflexes allow you to nimbly weave out of the way!")
                else: #opponent's health is depleted
                    print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
            elif action1 == 1 and rng < 4: #player hits uppercut, dealing 2 dmg to opponent
                print("You decide that you want to end this quickly with an uppercut!! Your opponent falls flat onto their back, and the referee begins the count. They make it all the way to 4 before your opponent stands back up and returns to the fight!")
                oppHealth -= 2
                rng = random.randint(1,3)
                if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                    print("Despite just having been knocked to the floor, your opponent responds with a surprisingly quick right hook. You aren't able to block in time and get hit square in the jaw!")
                    playerHealth -= 1
                elif rng != 1 and oppHealth > 0 : #opponent misses
                    print("Your opponent goes for a right hook, but it's clumsy and uncoordinated due to the hit he just took! You're able to dodge out of the way with ease!")
                else: #opponent's health is depleted
                    print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
            elif action1 == 2 and rng >=4: #player hits Jab:
                print("You decided to rely on your jab this time! As your fist makes contact with your opponent's body, they stumble slightly!")
                oppHealth -= 1
                rng = random.randint(1,3)
                if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                    print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                    playerHealth -= 1
                elif rng != 1 and oppHealth > 0 : #opponent misses
                    print("Your opponent goes for a right hook, but their slowed reflexes due to the blow they suffered allow you to nimbly weave out of the way!")
                else: #opponent's health is depleted
                    print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
            elif action1 == 2 and rng < 4:
                print("You decided to go for a quick jab to start things off! Before your fist can make contact, your opponent gets their hands in the way and blocks the punch!")
                rng = random.randint(1,3)
                if rng == 1 and oppHealth > 0: #opponent hits, dealing 1
                    print("Your opponent throws a right hook that catches you off-guard! The blow dazes you, but you stay on your feet!")
                    playerHealth -= 1
                elif rng != 1 and oppHealth > 0 : #opponent misses
                    print("Your opponent goes for a right hook, but their slowed reflexes due to the blow they suffered allow you to nimbly weave out of the way!")
                else: #opponent's health is depleted
                    print("Your opponent goes for a lazy swing and you land a devastating left hook to their head. They fall to the ground and stay down. You've won the fight!!")
    else:
        print(" ")
if playerHealth <= 0:
    print("Your opponent begins to rain blows on you without giving you a chance to defend. Your body falls to the floor and you're down for the count!")
    print("Game over! Please try again!")

if oppHealth <= 0:
    print("You have won Fight Night! Thanks for playing!!")