import random
def fortune_cookie():
    fortunes = ["Help! I'm being held prisoner in a Chinese bakery!", "The fortune you search for is in another cookie.", "Your heart will skip a beat.", "Don't just think. Act!", "Someone in your life needs a letter from you.", "The early bird gets the worm, but the second mouse gets the cheese.", "All things are difficult before they are easy.", "Don't pursue happiness – create it."]
    print(fortunes[random.randint(0,7)])

fortune_cookie()
fortune_cookie()
fortune_cookie()
