# Interpreters

(1) Writing an Interpreter:  Your function should display HTML according to a given parse tree. graphics.warning(msg) displays an error message. Upon encountering mismatched tags, use graphics.warning to display the error message: "mismatched tag". To display a tag, use graphics.begintag(tag,args) at the start and graphics.endtag() at the end of the tag.

(2) Variable Lookup:  Adding variable lookup to the interpreter.

(3) Evaluating Statements

(4) Frames:  Return will throw an excception. Function Calls: new environments, catch return values.

(5) I Could Wile Away The Hours:  Although our HTML and JavaScript interpreters are not yet integrated into a single browser, we can still extend our JavaScript interpreter independently. We already have support for recursive functions and "if" statements, but it would be nice to add support for "while". Consider the following two JavaScript fragments:

    var i = 0;
    while (i <= 5) {
      document.write(i); 
      i = i + 2;
    };

And: 

    function myloop(i) {
      if (i <= 5) {
         document.write(i);
         myloop(i + 2);
      } ;
    }
    myloop(0);

They both have the same effect: they both write 0, 2 and 4 to the webpage. (In fact, while loops and recursion are equally powerful! You
really only need one in your language, but it is very convenient to have them both.

We can extend our lexer to recognize 'while' as a keyword. We can extend our parser with a new statement rule like this: 

    def p_stmt_while(p):
        'stmt : WHILE exp compoundstmt'
         p[0] = ("while",p[2],p[3])

Now we just need to extend our interpreter to handle while loops. The meaning of a while loop is: 

       1. First, evaluate the conditional expression in the current
       environment. If it evaluates to false, stop.

       2. Evaluate the body statements in the current environment. 

       3. Go to step 1. 

Recall that our JavaScript interpreter might have functions like:

       eval_stmts(stmts,env)
       eval_stmt(stmt,env)
       eval_exp(exp,env) 

For this assignment, you should write a procedure:

       eval_while(while_stmt,evn) 

Your procedure can (and should!) call those other procedures. Here is how our interpreter will call your new eval_while(): 
 
     def eval_stmt(stmt,env): 
         stype = stmt[0] 
         if stype == "if-then":
                 cexp = stmt[1]
                 then_branch = stmt[2] 
                 if eval_exp(cexp,env):
                         eval_stmts(then_branch,env) 
         elif stype == "while":
                 eval_while(stmt,env) 
         elif stype == "if-then-else":
                 ...

    Hint 1: We have structured this problem so that it is difficult for you to test (e.g., because we have not provided you the entire 
    JavaScript interpreter framework). Thus, you should think carefully about how to write the code correctly. Part of the puzzle of 
    this exercise is to reason to the correct answer without "guess and check" testing.

    Hint 2: It is totally legal to define JavaScript's while using a Python while statement. (Remember, an interpreter is like a 
    translator.) You could also define JavaScript's while using recursion in Python.

    Hint 3: Extract the conditional expression and while loop body statements from while_stmt first.

(6) JavaScripts Big Bang:  In class we saw one way to integrate our HTML Interpreter and our JavaScript interpreter to make a web browser. Our JavaScript interpreter returned a string, which was then rendered unchanged on the webpage.

In practice, however, JavaScript output may include HTML tags and should be lexed, parsed and interpreted again. For example, on modern web browsers the following webpage ...

     <html>
     <script type="text/javascript">
     document.write("Tags in <i>my</i> output should be processed.");
     </script>
     </html>

Does not output the literal string "Tags in <i>my</i> output should be processed." Instead, the <i> tags are lexed, parsed and interpreted again, and the web page contains "Tags in my output should be processed." with the word "my" drawn in italics. This sort of recursive dependence -- in which intepreted HTML contains JavaScript which runs and creates new HTML which is then interpreted, and so on, is the heart of JavaScript's power. You can visualize it like a snake eating its own tail: http://en.wikipedia.org/wiki/Ouroboros. In this assignment you will extend our web browser so that the string produced by JavaScript is not merely passed to the graphics library as a word, but is instead lexed, parsed and interpreted as HTML. (For the purposes of this assignment, if JavaScript creates HTML, it must created only well-balanced tags.) Below is the top-level HTML Interpreter code for the web browser. You will not need to change any lexer definitions, token definitions, or anything about the JavaScript interpreter. Hint: The required extension can be made by changin as few as three lines (because you already know so much about this topic)! It does require you to understand how lexers, parser and interpreters all fit together. 
