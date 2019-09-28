import graphics

def interpret(trees): # Hello, friend

    for tree in trees: # Hello,
    
        # ("word-element","Hello")
        nodetype=tree[0] # "word-element"
        
        if nodetype == "word-element":
            
            graphics.word(tree[1]) 
            
        elif nodetype == "tag-element":
            
            # <b>Strong text</b>
            tagname = tree[1] # b
            tagargs = tree[2] # []
            subtrees = tree[3] # ...Strong Text!...
            closetagname = tree[4] # b
        
            if tagname != closetagname:
            
                graphics.warning("mismatched tag")
            
            else:
                
                graphics.begintag(tagname,tagname)
                interpret(subtrees)
                graphics.endtag()


graphics.initialize() # Enables display of output.\
interpret([("word-element","Hello")])
graphics.finalize() # Enables display of output.
