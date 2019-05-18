

#Program requirements
#The program needs python in your desktop or  python supported server. An IDE like IDLE or PyCharm to run this module.

#Compiling instructions
# The program requires user to enter 2 arguments for the unification.
# The program will ask for first argument and second argument.
# Depending on the argument entered first, the answer may change.
# It is necessary to follow the instructions for entering the input.
# The user must not enter input other than alpha characters or ")",",","(". The program will not accept the other characters. If characters other than mentioned are entered , the program will print no.
# Standard for function - small letters only  and make sure there is a ")" at the end.
# Standard for variables - Capital letters only.
# Standard for constant - small letters only.

def check_syntax(temp):
    incr =0
    br =0
    for i in temp:
        if i=="(":
            br =br+1
        elif i==")":
            br =br-1        
        if i.isupper()and incr ==0:
            return "error"
        if i!=")"and incr ==len(temp):
            return "error"
        incr = incr+1
    if br!=0:
        return "error"
    else:
        return "passed"

def check_const_var(temp):
    for i in temp:
        if i.islower():
             # Returns constant if input is a small letter
            return "constant"
        else:
            # Returns variable if input is a capital letter
            return "variable"
    

def check_type(temp):
    # Function to check the type whether the input entered is a function, constant, variable or input error
    if temp.isalpha()or "(" in temp or ")" in temp or "," in temp:
        # first valid condition to check only alpha and acceptable characters are allowed for the input
        if "(" in temp:
            if ")" in temp:
                # if the input contains both ")" and "(" , it will return function
                if check_syntax(temp)=="error":
                    return "input error"
                else:
                    return "function"                
            else:
                return "input error"
            
        if "(" not in temp and ")" not in temp and "," not in temp:
            # if no ")" and "(" it will return variable or constant
            checktyp =check_const_var(temp)
            return checktyp            
    else:
        # Return input erro for unacceptable characters
        return "input error"
    
def check_numarg (temparg):
    #Function to get the number of arguments in the function
    br=0 # initiate the bracket as 0
    co=0 # initiate the comma as 0
    for i in temparg:
        # Check if input contains "(" and ")" increament br if "(" and decrement br if ")"
        if i =="(":
            br=br+1
        elif i == ")":
            br=br-1
        # If input = "," and br =0 then only increase the number of commas
        if i=="," and br==1:
            co=co+1
    if br==0:
        # check at the end if br ==0 return co+ 1 as the number of arguments
        return co+1
    else:
        # Return input error if br !=0 
        return "input error"

def check_funname (temparg):
    #function to get the name of the function
    funname = "" # initiate the function name as an empty string
    for i in temparg:        
        if i =="(":
           break # Once the function finds the first "(". The loop will end.
        funname = funname + i # Append i to function until the i==","        
    return funname # Return Function name


def ret_arg (temparg):
    #function to return the number of arguments in a "function"
    arguments = [] # initiate the arguments list as an empty list 
    
    actual = "" # actual is a variable storing variables in a format such that if temparg = f(a,b) , actual = a,b
    br=0 # initiate the bracket count as 0
    co=0 # initiate the comma count as 0
    inc ="" #initiate the argument value as an empty string
    first =0 #Status flag to check the first "(" 
    
    for j in temparg:
        if first ==1: # if the first value is 1, then append the entire rest of the input to the actual
            actual =actual +j
        if j=="(":
            first =1
            
    actual = actual[:-1] # remove the last ")"
    
    for i in actual:
        if i=="," and br==0:# check for the commas and bracket value as 0
            co=co+1 # incrrease the number of commas
            arguments.append(inc)# if a comma is found then the argument value in inc should be appended in argument list
            inc ="" # initiate the inc again to empty string if a comma is found
        else:
            inc = inc + i # if no comma is found then append i to the inc
        if i =="(": # count the bracket values
            br=br+1 
        elif i == ")":
            br=br-1

    if co==0:
        # if number of commas are 0 the the whole input is the only argument and the actual value is appended to the argument list
        arguments.append(actual)
    else:
        # append the last argument in the list
        arguments.append(inc)
    # return argument list to the process fucntion   
    return (arguments)

def subst(v,l):
    # function to substitite the value of variables in another variables.
    for i in range(len(v)):
        if l[0][0] in v[i][1]:
            v[i][1]= v[i][1].replace(l[0][0],l[0][1])
    

def process(tempa,tempb,v,l):
    var = "top"
    # Process function  process the unification according to some conditions
    a1 = check_type(tempa) # Check the type of input tempa and store value in a1
    a2 = check_type(tempb) # Check the type of input tempb and store value in a2
    # tempa and tempb are temporary variables inputed from the call method. The process function is a recursive function which will be called with different values of temp and tempb
    
    if a1 == "input error" or a2 == "input error": # if the input type a1 or a2 is input error then the Process function returns input error
        return "input error"
    
    if a1 == "function" or a2 =="function": # if the input type a1 or a2 is fucntion then the multiple conditions are required to be checked
        if a1== "constant" or a2 == "constant": # Check if either of the two input is a constant
            return "no" # If either of the input have constant value then return no as constant and funcayion cannotbe unified.
        else:
            if a1=="variable" and a2 =="function": # check for variable and fucntion case
                if tempa in tempb: # check if temp a contains tempb 
                    return "no" # return no as f(X) and X cannot be unified
                else:                                                        
                    l.append([tempa,tempb])# append variable value to the last added variable list l 
                    if v!=[]:# check if the variable list is empty
                        subst(v,l)#If the variable list is not empty call substitution
                    v.append([tempa,tempb])# append variable to the variable list    
                    return "top"#return top to replace the value of variable in the given input fucntion
            elif a2=="variable" and a1 =="function": # check for variable and fucntion case
                if tempb in tempa:# check if tempb contains tempa 
                    return "no" # return no as f(X) and X cannot be unified
                else:   
                    l.append([tempb,tempa])# append variable value to the last added variable list l
                    if v!=[]:# check if the variable list is empty
                        subst(v,l)#If the variable list is not empty call substitution
                    v.append([tempb,tempa])# append variable to the variable list     
                    return "top"#return top to replace the value of variable in the given input fucntion
            else: #function and function case
                f1 = check_funname(tempa) # check function name for first input
                f2 = check_funname(tempb)# check function name for second input
                t1= check_numarg(tempa) # check the number of arguments for first input
                t2 = check_numarg(tempb)# check the number of arguments for first input
                
                if t1 =="input error" or t2 =="input error": # check if the number of arguments is returned input error
                    return "input error" # return input error to the main function
                
                if f1 ==f2 and t1==t2:# check if the function name and number of arguments in both functions are same 
                    count = 0; # initiate count pointer as 0
                    arg1 = ret_arg(tempa) # get arguments for function1 in arg1
                    arg2 = ret_arg(tempb) # get arguments for function2 in arg2
                    while count< t1: # Loop until the count value equals the number of arguments
                        var ="top" 
                        var = process(arg1[count],arg2[count],v,l)# process the process function again 
                        if var =="top": # if the value returned from function is top then return top to the main function
                            return "top"
                        elif var =="no":# if the value returned from function is no then return no to the  function
                            return "no"
                        elif var =="input error":# if the value returned from function is input error then return input error to the  function
                            return "input error"
                        elif var =="True" and count==(t1-1):# if the value returned from function is True and it is the last argument of the function then return True to the main function
                            count =count +1
                            return "True"
                        else: # if the value returned from function is True and it is not the last argument of the function then move to the next argument
                            count=count+1
                else:
                    return "no" # Return no as number of arguments or function name are not same
                
    elif a1== "constant" and a2 =="constant": # if a1 and a2 both are constants
        if tempa==tempb: # We need to check if value of the two constant inputs are same or  not.
            #Returns no as two constant input have same input value
            return "True"
        else:
            #Returns no as two constant input have two different values
            return "no"

    elif a1 =="variable" or a2=="variable": # if a1 or a2 is a variable   
        if a1 =="variable": # check if a1 is variable
            if a2 == "variable": # check if input two is variable
                if tempa==tempb: # if two inputs have same value then it is unified.
                    return "True" # Return True if two variable inputs have same value
                else:                    
                    l.append([tempa,tempb])# append variable value to the last added variable list l
                    if v!=[]:#check if the variable list is empty
                        subst(v,l) # If the variable list is not empty call substitution
                    v.append([tempa,tempb])# append variable to the variable list
                    return "top" #return top to replace the value of variable in the given input fucntion
            else:
                l.append([tempa,tempb]) # append variable value to the last added variable list l
                if v!=[]:#check if the variable list is empty
                    subst(v,l) # If the variable list is not empty call substitution
                v.append([tempa,tempb])# append variable to the variable list
                return "top" #return top to replace the value of variable in the given input fucntion
        else:
            l.append([tempb,tempa]) # append variable value to the last added variable list l
            if v!=[]: # check if the variable list is empty
                subst(v,l)#If the variable list is not empty call substitution
            v.append([tempb,tempa])# append variable to the variable list                    
            return "top"#return top to replace the value of variable in the given input fucntion
				
			
def main():
    # Main Function
    a = raw_input("Enter first argument ") # Enter First argument for the unification algorithm
    b = raw_input("Enter second argument ") # Enter Second argument for unification algorithm
    v  = [] # Initiate variable list  as empty for appending the variable value, if the program finds any variable in the program
    l  = [] # l stores the last variable appended to varibale list
    var ="top" # var is a status variable, It is initiated as top.
    # var = top means processing of unification is not completed.
    # var = "no" means the two inputs cannot be unified
    # var = "input error" means error in inputs
    # var = "True" means the two inputs are unified.
    
    while var =="top":
        # Program runs until the value of var is returned as top from the inner function.
        if len(l)==0:
            #if there is no variable in the v list, then process the unification
            var = process(a,b,v,l)# process the function again -- Call the Process function            
        else:
            # if there is a variable in the v list, substitute the variable values and then process the unification            
            a=a.replace(l[0][0], l[0][1]) #substitute variable value in input a
            b=b.replace(l[0][0], l[0][1])# substitute varibale value in input b
            l =[] # empty the previously added variable from the l list
            var = process(a,b,v,l)# process the function again -- Call the Process function
            
    if var == "no":
        # if the value is returned no, then print "no"
        print "no"
        v=[]
    elif var == "input error":
        # if the value is returned input error, then print "input error"
        print "input error"
        v=[]   
    elif var == "True":
        # if the value is returned True, then print "yes" and print the variables with its values
        print "Yes"
        for i in range(len(v)):
            print(v[i][0] + "-->" + v[i][1])
    
if __name__== "__main__":
    main()
  
