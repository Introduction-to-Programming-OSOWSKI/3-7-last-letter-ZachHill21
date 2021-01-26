
def lastLetter(w): 
    w = w + " "
    for i in range(len(w)): 
        if w[i] == ' ': 
            print(w[i - 1], end = " ") 
  

lastLetter("minnesota") 