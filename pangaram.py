def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
m =input()
if(ispangram(m) == True): 
    print("yes") 
else: 
    print("no")
