import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    result = 0

    # Case 1 ---> All required arguments
    """
    parser.add_argument('number1', help="The first number", type=int)  # Positional argument
    parser.add_argument('number2', help="The second number", type=int)  # Positional argument
    parser.add_argument('operation', help="The operation to perform")  # Positional argument
    args = parser.parse_args()
    """

    # Case 2 ---> Using Optional and Positional arguments
    """ 
    parser.add_argument('number1', help="The first number", type=int)  # Positional argument
    parser.add_argument('number2', help="The second number", type=int)  # Positional argument
    parser.add_argument('--operation', help="The operation to perform")  # Optional argument

    Now if we don't pass operation argument then it will not throw error instead give us args.operation as None and
    eventually show Unsupported operation. We can also pass default value to operation argument so that if nothing is
    being pass be default it will perform that operation.
    # Example ==>  parser.add_argument('--operation', help="The operation to perform", default='add')  # Optional argument
    """
    # Case 3 ---> Using Optional arguments with choices. Meaning we can only pass one of the choices which developer has
    # provided other it will throw error.
    """
    parser.add_argument('number1', help="The first number", type=int)  # Positional argument
    parser.add_argument('number2', help="The second number", type=int)  # Positional argument
    parser.add_argument('--operation', help="The operation to perform",
                        choices=['add', 'subtract', 'multiply'])  # Optional argument
    """

    # Case 4 --> Using all optional arguments.
    """ 
    In this case while running the script, we need to pass them like below in any order:
   
    python3 practice.py --number1 10 --number2 20 --operation add
    python3 practice.py --number2 20 --operation subtract --number1 10

    It is kind of key value pair. Like --number1 is key and value is 10/20.
    # parser.add_argument('--number1', help="The first number", type=int)  # Optional argument
    # parser.add_argument('--number2', help="The second number", type=int)  # Optional argument
    # parser.add_argument('--operation', help="The operation to perform",
    #                     choices=['add', 'subtract', 'multiply'])  # Optional argument
    """
    # args = parser.parse_args()
    # print(args.number1, args.number2, args.operation)
    # if args.operation == 'add':
    #     result = args.number1 + args.number2
    # elif args.operation == 'subtract':
    #     result = args.number1 - args.number2
    # elif args.operation == 'multiply':
    #     result = args.number1 * args.number2
    # else:
    #     print("Unsupported operation")
    # print(result)

    # Case 5 --> Handling two arguments which are not allowed at the same time.

    group = parser.add_mutually_exclusive_group()
    # Here x and y are added to mutually_exclusive_group because we don't want them to run at the same time. Rest of the
    # options are added to the parser.
    group.add_argument('-x', '--execute', action="store",
                       help='Help text for option X')  # -x or --execute both can be used to run in CLI
    group.add_argument('-y', help='Help text for option Y', default=False)

    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())
