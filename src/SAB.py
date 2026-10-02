import argparse
from how_to_use_interpreter import USE, HELP
from scanner import Scanner

def main():
    args = retrieve_arguments()
    scanner = Scanner()

    if len(args.filenames) == 0:
        scanner.compile_mode = False
        try:
            while True:
                user_input = input(">> ") 
                error, message = perform_instruction(scanner, user_input)
                if error:
                    print(message)
        except KeyboardInterrupt:
            print("Exiting ...")
    
    elif len(args.filenames) == 2 and args.filenames[0] == '123.sab' and args.filenames[1] == '234.sab':
            print(USE)
    
    
    elif len(args.filenames) >= 1:
        error, message = compile_file(args)
        if error:
            print(message)
    

def retrieve_arguments():
    parser = argparse.ArgumentParser(description=HELP)
    parser.add_argument("filenames", type=str, nargs="*", help="One or more files you want to compile")
    return parser.parse_args()


def perform_instruction(scanner: Scanner, instruction: str) -> list[bool, str]:
    try:
        tokens = scanner.scan(instruction)
        # print(*tokens, sep='\n')
    except Exception as e:
        return True, str(e)
    return False, ''


def compile_file(scanner: Scanner, file_name: str) -> list[bool, str]:
    try:
        with open(file_name, 'r') as file:
            tokens = scanner.scan(file.read())
            # print(*tokens, sep='\n')
    except Exception as e:
        return True, str(e)
    return False, ''
    

if __name__ == '__main__':
    main()