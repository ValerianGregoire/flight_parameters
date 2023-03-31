from sympy import Symbol

def find_root(func,result,**kwargs):
    
    # Define the variables as sympy symbols
    variables = {}
    for key in kwargs:
        variables.update({f'{key}':Symbol(f'{key}')})
    # print('Declared variables:',kwargs)
    
    try:
        
        # Find the variable to search
        var_idx = list(kwargs.values()).index(None)
        var = list(kwargs.keys())[var_idx]
        
        # print('Unknown variable:',var)
        # print(f'Use of Newton-Raphson method to find {var}')
    
        # Define the function to work with
        f = func(variables)-result
        # print('Function to study:',f)
    
    
        # Try a first guess of the final value for the variable to find
        c0 = 0
        
        # Get the derivative of the study function
        f_prime = f.diff(var)
        # print(f'Derivative of the function with respect to {var}:',f_prime)
        
        # Setpoint where the computation is precise enough
        tolerance = 1e-6
        
        # Declare an arbitrary c1
        c1 = c0 + 1
        
        # Verify that the difference between the two values is low enough
        while abs(c1 - c0) > tolerance:
            
            # Update the arguments given to the function
            values_dic = kwargs
            
            # Replacing the unknown var with the current estimation
            values_dic[var] = c1
            
            # Keep the estimation in memory
            c0 = c1
            
            # Compute a new estimation
            c1 = c0 - f.evalf(subs = values_dic) /   \
                f_prime.evalf(subs = values_dic)
        
        c1 = round(c1,3)
        # print(f'{var} = {c1}')
        
        return c1
     
    
    # If all variables have a value, we look for the basic result
    except ValueError:
        # print('Basic computation of the answer')
        f = func(variables)
        solution = round(f.evalf(subs = kwargs),3)
        # print(f'{func.__name__}{kwargs} = {solution}')
        return solution