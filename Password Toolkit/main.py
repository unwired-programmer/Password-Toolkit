#DO-YOU-AGEEE--------------------------------------------------------------------------------------
qaz=input("(yes/no) IF YOU AGREE TO THIS, YOU ARE RESPONSIBLE FOR ANY DAMAGES CAUSED BY THE USE OR ALTERATION OF THE CODE. \nREFUSAL WILL MAKE THE PROGRAM UNUSEABLE. \n:")
if qaz == "yes":
    print("")
else:
    while True:
        print("")

def menu():

#RANDOM-------------------------------------------------------------------------------------------
    import random

#CHARACTERS---------------------------------------------------------------------------------------
    Lletters=("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m")
    Cletters=("Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M")
    numbers=("1","2","3","4","5","6","7","8","9","0")
    symbols=("!""@""#""$""%""^""&""*""("")""_""+""{""[""\"|"":"";""?""<"">"","".""]""}")

#CHARACTHER-CHOICER-------------------------------------------------------------------------------
    z=random.choices(Lletters)
    x=random.choices(Cletters)
    c=random.choices(numbers)
    v=random.choices(symbols)

    a=random.choices(Lletters)
    s=random.choices(Cletters)
    d=random.choices(numbers)
    f=random.choices(symbols)

    q=random.choices(Lletters)
    w=random.choices(Cletters)
    e=random.choices(numbers)
    r=random.choices(symbols)

    tipes=(f"{z}{v}{d}{c}{r}{w}{a}{f}{d}{c}{v}{r}{z}{q}{z}{x}{c}{x}",f"{v}{x}{x}{s}{x}{a}{v}{w}{v}{f}{x}{s}{z}{r}{x}{d}{z}{c}",f"{z}{x}{q}{w}{s}{v}{d}{c}{x}{f}{q}{x}{e}{w}{x}{s}{z}{v}",f"{z}{w}{x}{d}{x}{z}{c}{d}{f}{w}{x}{e}{v}{z}{r}{x}{a}{v}",f"{v}{x}{s}{f}{q}{r}{x}{a}{z}{z}{v}{d}{q}{z}{s}{z}{d}{v}",f"{e}{a}{v}{a}{d}{r}{w}{s}{x}{s}{e}{w}{c}{q}{r}{d}{c}{v}",f"{s}{f}{x}{z}{q}{s}{d}{c}{v}{a}{r}{w}{q}{s}{d}{d}{x}{v}",f"{f}{s}{q}{x}{c}{z}{d}{a}{e}{w}{s}{a}{c}{f}{a}{x}{w}{v}",f"{e}{d}{w}{x}{a}{f}{s}{x}{w}{q}{x}{v}{d}{q}{x}{z}{v}{q}",f"{f}{d}{w}{q}{c}{f}{e}{r}{x}{a}{f}{z}{e}{d}{a}{q}{c}{d}")
    tp=random.choices(tipes)
#ATTEMPTS------------------------------------------------------------------------------------------
    attempts = 0

#PASSLIST-----------------------------------------------------------------------------------------
    pas_list=["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","qwertyuiop","123321","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","william","corvette","hello","martin","heather","secret","merlin","diamond"]
# PASSWORDS FROM (https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords)  FEEL FREE TO ADD MORE!

#MAIN-MENU---------------------------------------------------------------------------------------

    print("                                        ")
    print("                                        ")
    print("       ![-Password toolkit-]!           ")
    print("-----------------------------------------")     
    print("|-(1)Brute force password.              |")
    print("|-(2)Manual.                            |")
    print("|-(3)How strong is my password?         |")
    print("|-(4)How do i protect my passwords?     |")
    print("|-(5)Password generator.                |-This program was made for educational purposes.-")
    print("-----------------------------------------            *WARNING: BAD ENGLISH")

#CHOICES------------------------------------------------------------------------------------------
    cho = input("/[NUMBER]/: ")
    if cho == "2":

    #MANUAL-------------------------------------------------------------------------------------
        print("\n\n\n|Welcome to The Password toolkit|\n|Password toolkit is a list of tools, you can use on passwords.|\n")
        print("1.Brute force tester: simulates a brute force atack. (does not work like a real brute force atack)")
        print("2.Manual: View info about the tools in PTK. ")
        print("3.How strong is my password: Tells you, how strong your password is.")
        print("4.How do i protect my passwords: Tips, on protecting your passwords.")
        print("5.Password generator: generates a random password.")
        print("\n--Q&A--\nQ: Is it safe to put my passwords here ? ")
        print("A: Password Toolkit does not store your passwords.")
        print("Q: How can i support the project.")
        print("A: Share the project with EVERYONE!")
        print("Q: Are the generated passwords strong ?")
        print("A: According to Bitwarden, our passwords are strong and can take centuries to be cracked.")
        input("Press enter to exit: ")
        menu()

    if cho == "1":

    #PASSWORD-CRACKING----------------------------------------------------------------------------
        passs = input("---[PASSWORD]: ")
        while True:
            choice=random.choice(pas_list)
            if choice == passs:
                attempts += 1
                print(f"[ATTEMPTS]: {attempts}. [PASSWORD-FOUND]:-----{choice}--------------------------------------------------------------------------------------|")
                input("Press enter to exit: ")
                menu()
                break
            else:
                attempts += 1
                print(f"[ATTEMPTS]: {attempts}. [PASSWORD-NOT-FOUND]:-{choice}| ")

    if cho == "3":

    #HOW-STRONG-IS-YOUR-PASSWORD------------------------------------------------------------------
        print("   [How strong is your password?]   ")
        print("------------------------------------")
        print("---Does your password have: ")
        q=input("-[y/n]Symbols-:")
        qq=input("-[y/n]Numbers-:")
        qqq=input("-[y/n]Lowercase Letters-:")
        qqqq=input("-[y/n]Upercase Letters-:")
        qqqqq=input("-[y/n]8-16 or more Characters-:")
        if qqq == "y" and qqqq == "y" and qqqqq == "y":
            print("-You have a (STRONG) password!")
            input("Press enter to exit.")
            menu()
        else:
            print("-You have a (WEAK) password!")
            input("Press enter to exit.")
            menu()

    if cho == "4":

    #TIPS-----------------------------------------------------------------------------------------
        print("----                           [PASSWORD PROTECTION TIPS]                          ----")
        print("---------------------------------------------------------------------------------------")
        print("|1.NEVER share your passwords with anyone.")
        print("|2.Use a strong open-source password manager.")
        print("|3.Never enter your passwords on a password testing website. (they can be stored in a database).")
        print("|4.Make strong passwords, with lowercase and upercase letters, numbers, symbols, that is at least 16 characthers long. ")
        print("|5.Try making passphrases like: MYd0g1$cut3. These are easy to remember and hard to crack.")
        print("|6.Change your passwords frequently.")
        print("|7.You can try to hide your passwords in your home, on a pice of paper.")
        input("---press enter to exit.")
        menu()

    if cho == "5":

    #PASSWORD-GENERATOR---------------------------------------------------------------------------
        print("\n!----|[Password generator]|----!\n")
        print(f"{tp}\n")
        input("Press enter to exit.")
        menu()
menu()