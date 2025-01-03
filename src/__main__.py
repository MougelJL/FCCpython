import argparse

def main():
    #crea el parser origen
    parser = argparse.ArgumentParser(prog="calculator")
    #parser.add_argument('--help', '-h', action='help')
    subparsers = parser.add_subparsers(dest= 'command', help='subcommand help')

    #crea el sub-parser de suma
    parser_sum = subparsers.add_parser('add', help='Add two numbers together')
    parser_sum.add_argument('summands',nargs=2, type=int, help='Numbers to be summed')

    args = parser.parse_args()

    match args.command:
        case 'add':
            print(sum(args.summands))

if __name__ == '__main__':
    main()