# Solution 1, use python while
def eval_while(while_stmt, env):
    
	conditional_exp = while_stmt[1]
	
	loop_body = while_stmt[2]
	
	while eval_exp(conditional_exp, env):
	    
		eval_stmts(loop_body, env)


# # Solution 2, use Recursion
# def eval_while(while_stmt, env):

# 	conditional_exp = while_stmt[1]

# 	loop_body = while_stmt[2]

# 	if eval_exp(conditional_exp, env):

# 		eval_stmts(loop_body, env)

# 		eval_while(while_stmt, env)
