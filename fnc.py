import sys

# -f ["Space Separated list of path+filenames"] [] []
# -o [Output Subfolder] e.g. 'tmp' will put the output in a tmp subfolder of
#                             it's original path


ARGS = ['-f', '-o']

def main()
    """ This function will be the central control.
        It will call the function to parse the command line args
        then pass those to the correct functions.
    """

    # Get the command line args
    args = sys.argv[1:]
    # make them into a dictionary of the option as the key and the
    # value as the list of things that follow. None for no value.

    start = 0
    for c in ARGS:
        index = args.index(c, start)
        args_dict[c] = args[start:index]
    
    
    
    
    


if __name__ == '__main__':
    main()
