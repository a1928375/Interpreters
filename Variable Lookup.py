def eval_exp(tree, environment):
    
    nodetype = tree[0]
    
    if nodetype == "number":
        
        return int(tree[1])
        
    elif nodetype == "binop":
        
        left_value = eval_exp(tree[1], environment)
        operator = tree[2]
        right_value = eval_exp(tree[3], environment)
        
        if operator == "+":
            
            return left_value + right_value
            
        elif operator == "-":
            
            return left_value - right_value
            
    elif nodetype == "identifier":
        
        return env_lookup(environment,tree[1])
        
        # ("binop", ("identifier","x"), "+", ("number","2"))
        # QUIZ: (1) find the identifier name
        # (2) look it up in the environment and return it

def env_lookup(env,vname): 
        return env.get(vname,None)

environment = {"x" : 2}
tree = ("binop", ("identifier","x"), "+", ("number","2"))
print (eval_exp(tree,environment) == 4)
