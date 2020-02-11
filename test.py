print("hello")

list1 = ["test1","test2","test3", "test4"]

for element in list1:
    print(element)
    print("testing")

def function(number1, number2):
    """ 
                                    * This is from autoDocstring
    Arguments:  
        number1 {integer} -- [This should be an integer]
        number2 {integer} -- [This should be another number]
    
    Returns:
        [integer] -- [Returns the lesser of number1 and number2]
    """
    if number1 < number2:
        return number1
    else:
        return number2

# * These are from Better Comments
""" 
 * Highlights
 ! Alerts
 ? Queries
 TODO: Todos
 
"""