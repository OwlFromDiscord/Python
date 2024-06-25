numeral_input = input("Enter the Roman Numerals you want to convert: ") #asks for user input to determine
def rom_to_int(numeral): #function to convert                            what gets translated
    fin_ans = 0
    #Solution to scenarios where numerals need to subtract instead of add.
    if "CM" in numeral:
        fin_ans += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        fin_ans += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        fin_ans =+ 90
        numeral = numeral.replace ("XC", "")
    if "XL" in numeral:
        fin_ans += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        fin_ans += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        fin_ans += 4
        numeral = numeral.replace("IV", "")
    for i in numeral:
        if i == "M":
            fin_ans += 1000
        elif i == "D":
            fin_ans += 500
        elif i == "C":
            fin_ans += 100
        elif i == "L":
            fin_ans += 50
        elif i == "X":
            fin_ans += 10
        elif i == "V":
            fin_ans += 5
        elif i == "I":
            fin_ans += 1
    print("The roman numerals provided equate to: " + str(fin_ans) + "!") #Prints final output
rom_to_int(numeral_input) #Actually runs the function we just made