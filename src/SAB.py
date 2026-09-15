import argparse
from how_to_use_interpreter import USE, HELP

def main():
    args = retrieve_arguments()

    if len(args.filenames) == 0:
        try:
            while True:
                user_input = input(">> ") 
                error, message = perform_instruction(user_input)
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


def perform_instruction(instruction: str) -> list[bool, str]:
    try:
        raise NotImplementedError("Scanner Not Implemented")
    except Exception as e:
        return True, str(e)
    return False, ''


def compile_file(file: str) -> list[bool, str]:
    try:
        raise NotImplementedError("Scanner Not Implemented")
    except Exception as e:
        return True, str(e)
    return False, ''
    

if __name__ == '__main__':
    main()