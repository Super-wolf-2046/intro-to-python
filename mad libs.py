x=0
while x==0:
    print("""Hello and welcome to another game of Madlibs. If you are new to this our rules are simple you will be asked to give diffrent nouns and verbs, they can be funy or serious. Lets begin!""")
    Plural_noun = raw_input("A Plural noun is required here")
    Noun1 = raw_input("noun is needed")
    Noun2 = raw_input("how about another noun")
    Verb1 =raw_input("how about a verb")
    Verb2 = raw_input("a verb is being requested")
    Book = raw_input("The name of a book please")
    Tv = raw_input("The name of a show please") 

    Madlibs=("""The art of learning how to code may seem like a challenge but here is a few tips what and what not to do 1. Do make sure your work please is clean and to shut off your phone so you don't keep getting calls from %s. 2. Make sure your %s is with you at all times. 3. If you get frustrated don't throw your %s just calm down and %s.  4. Kept trying and don't %s no matter what. 5. Do not get distracted and start reading %s. 6.Do not give up and start watching %s instead if you do you will never complete anything. I hope these tips help you with goal.""")
    print(Madlibs %(Plural_noun,Noun1,Noun2,Verb1,Verb2,Book,Tv))
    print ("thanks for playing")
    user= raw_input("Would you like to play again")
    if user == "no":
        break
