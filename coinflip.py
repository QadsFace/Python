import random
def coinflip():
    return random.choice(("Heads", "Tails"))

def multi_flip(num):
    heads = 0
    tails = 0

    for x in range(num):
        flip = coinflip()
        if (flip == "Heads"):
            heads = heads + 1
        else:
            tails = tails + 1
    print("You flipped " + str(heads) + "heads and " + str(tails) + "tails")
    print("Precentage of Heads " + str(100 + heads / num) + "%")
    print("Precentage of Tails " + str(100 + tails / num) + "%")
    if (heads == tails):
        print("You flipped the same number of heads and tails")
    elif(heads > tails):
        print("You flipped more heads than tails")
    elif(tails > heads):
        print("You flipped more tails than heads")



