loop = 1

while (loop < 10):
    relationship = input("Choose a relationaship (eg. father, sister..etc): " , ).upper()
    adj = input("Choose an adjective (eg. beautiful, chubby..etc): " , ).upper()
    place = input("Choose a place (eg. the market, my home...etc): " , ).upper()
    number = int(input("Choose a number: " , ))
    action = input("Choose an action (eg. cooking, running..etc): " , ).upper()
    anotherWord = input("Choose a word ending in 'ing': " , ).upper()

    print("------------------------------------------------------------------------------------------------------------------")
    print("I love" , action)
    print("But what I love more than" , action , "is" , anotherWord)
    print("See the thing is" , action , "can be done anywhere. But," , anotherWord , "can only be enjoyed in" , place)
    print("And this is what makes" , place , "a perfect destination!")
    print("The last time I recall" , action , "my" , relationship , "was" , number , "light years ago")
    print("But our" , anotherWord , "days are as old as yesterday")
    print("No wonder my joints are sore!")
    print("------------------------------------------------------------------------------------------------------------------")

    loop += 1
