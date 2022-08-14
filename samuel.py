intro = ("You are walking through the forest when you come to a fork in the road." 
"\nDo you take the dark scary path on the right or the other dark scary path on the left?")
print (intro)
prompt = "Press 1 to go left, 2 to go right "
userInput = input(prompt)
if(userInput == "1"): 
    print("A big bat comes and bites your head off")
else:
    print("A giant dragon burns you to a crisp")