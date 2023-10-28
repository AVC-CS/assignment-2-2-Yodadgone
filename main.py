def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius= int(input('enter your tempurature in celsius'))
    fahrenheit = 9/5* celsius + 32 

    print(f'converted tempurature fahrenheit {fahrenheit:.1f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################  
    """
    return celsius, fahrenheit

if __name__ == '__main__':
    main()
