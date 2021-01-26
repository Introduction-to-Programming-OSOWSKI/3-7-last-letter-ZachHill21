
def lastLetter(a): 
    a = a + " "
    for i in range(len(a)): 
        if a[i] == ' ': 
            print(a[i - 1], end = " ") 
  
a = "a"
lastLetter(a) 