def do_stuff(num1):
    try:
        return num1 + 4
    except ValueError as err:
        raise err
   