def evaluate(ast):
    
    env = {}
    
    finished = False
    
    while not finished:
        
        finished = True
        
        for elt in ast:
            
            who = elt[0]
            
            elttype = elt[1]
            
            if elttype == "has":
                
                env[who] = elt[2]
                
                finished = False
                
                elt[1] = "skip"
            
            elif elttype == "buy":
                
                what = elt[2]
                howmuch = elt[3]
                
                for i in range(len(ast)):
                    
                    if ast[i][1]  == "sell" and ast[i][2] == what and env[who]>=howmuch and ast[i][3] == howmuch:
                        
                        elt[1] = "skip"
                        ast[i][1] = "skip"
                        env[who] = env[who] - howmuch
                        env[ast[i][0]] = env[ast[i][0]]+howmuch
                        finished = False
    
    return env                    


# In test1, exactly one sell happens. Even though klaus still has 25 money left over, a "buy"/"sell" only happens once per time it is listed. 
test1 = [ ["klaus","has",50] ,
          ["wrede","has",80] ,
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , ] 

print (evaluate(test1) == {'klaus': 25, 'wrede': 105})

# In test2, klaus does not have enough money, so no transactions take place.
test2 = [ ["klaus","has",5] ,
          ["wrede","has",80] ,
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , ] 

print (evaluate(test2) == {'klaus': 5, 'wrede': 80})

# Wishful thinking, klaus! Although you want to buy sheep for 5 money and you even have 5 money, no one is selling sheep for 5 money. So no transactions happen.
test2b = [ ["klaus","has",5] ,
           ["wrede","has",80] ,
           ["klaus","buy","sheep", 5] ,
           ["wrede","sell","sheep", 25] , ] 

print (evaluate(test2b) == {'klaus': 5, 'wrede': 80})

# In test3, wrede does not have the 75 required to buy the wheat from andreas until after wrede sells the sheep to klaus. 
test3 = [ ["klaus","has",50] ,
          ["wrede","has",50] ,
          ["andreas","has",50] ,
          ["wrede","buy","wheat", 75] ,
          ["andreas","sell","wheat", 75] , 
          ["klaus","buy","sheep", 25] ,
          ["wrede","sell","sheep", 25] , 
          ] 
print (evaluate(test3 ) == {'andreas': 125, 'klaus': 25, 'wrede': 0})
