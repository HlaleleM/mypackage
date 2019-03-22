def sum_array(array):
    '''
     Return sum of all items in array
    Args :
        array(np.array): array items of the same type
    Returns :
        a sum of all elements in an array
    Examples :
        >>> sum_array(array([2,4,6,8,10]))
            30
        >>> sum_array(array(['E','D','S','A']))
            'ASDE'
    '''
    if len(array) == 1:
        return array[0]
    else :
        return array[len(array)-1] + sum_array(array[:len(array)-1] )

def fibonacci(tn):
    """
    Calculate nth term in fibonacci sequence
    Args:
        tn (int): nth term in fibonacci sequence to calculate
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if tn <= 1:
        return tn
    else:
        return fibonacci(tn - 1) + fibonacci(tn - 2)

def factorial(value):
    '''
    Return n!
    Args:
        value (int) : number to solve factorial for
    Return :
        return value! (int) : factorial for value
    Example :
        >>> factorial(0)
            1
        >>> factorial(2)
            2
        >>> factorial(3)
        6
    '''
    if value <= 1 :
        return 1
    else :
        return value * factorial(value-1)

def reverse(word):
    '''
    Reverses the word
    arg :
        word(str) : string of alphabets
    Return :
        gives the word in reverse from last element to the first element
    Example :
        >>> reverse('EDSA')
            'ASDE'
    '''
    if len(word) == 1 :
        return word
    else:
        return word[len(word)-1] + reverse(word[:len(word)-1])
