# Custom Error Code
ERROR_CODE = -1

# Custom Exception Class
class MyCustomException(Exception):
    pass

def split_ticket(amount, npeople):
    if npeople == 0:
        raise ValueError("Dividing by Zero.")
    return amount/npeople

#def split_ticket(amount, npeople):
#    return amount/npeople

if __name__ == "__main__":
    try:
        split_ticket(1000,0)
    except ZeroDivisionError as e:
        print(e)
    except Exception:
        print("Error message")

    else:
        pass
    finally:
        pass

    '''
    USING IF STATEMENTS 

    val = split_ticket(1000,0)  # cannot divide by zero
    if val == ERROR_CODE:
        print("Cannot divide by zero")
    else:
        print(val)
    '''