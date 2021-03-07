import random

jokes = ["The adjective for metal is metallic, but not so for iron, which is ironic." , "DO NOT TOUCH must be one of the most terrifying things to read in braille" , "My wife asked me to put ketchup on the shopping list that I was making and now, I can’t read anything." , "If there's one thing that makes me throw up, it's a dart board on a ceiling." , "Together, I can beat schizophrenia." , "The thief who stole my iPhone could face time." , "I, for one, like Roman Numerals" , "Chameleons are supposed to blend well, but I think it's ruined this smoothie." , "Gravity is one of the most fundamental forces in the universe, but if you remove it, you get gravy." , "My cocaine is so white, the police let it go with a warning" , "I was gonna tell a time travelling joke but you guys didn't like it" , "People who buy sex dolls are fucking dummies" , "My girlfriend confided in me she loves when I blow air on her when she's hot, but honestly, I’m not a fan." , "Justice is a dish best served cold, if it were served warm, it would be justwater." , "Oral sex in the morning is a great way to get a head start." , "If your Tesla gets stolen, is it called an Edison now?" , "Every day is a D-Day, if you're a stutterer."]

print("Type: Tell me a joke")
request = input().upper()

print("---------------------------------------------------------------------")

if request == "TELL ME A JOKE":
    print(random.choice(jokes))

print("---------------------------------------------------------------------")
