
def lastLetter(string): 
    string = string + " "
    for i in range(len(string)): 
        if string[i] == ' ': 
            print(string[i - 1], end = " ") 
  
string = "minnesota"
lastLetter(string) 