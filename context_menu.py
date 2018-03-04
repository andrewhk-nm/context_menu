import sys
import os
import glob
import re
from functools import namedtuple

#print('hello context_menu\nsys.argv={}'.format(sys.argv))

def add_prefix(filename, prefix):
    """ Add a prefix to the file name, return the new filename.
    """
    return prefix + filename

def process_changes(post_path_fn):
    """ Rename the original file name to the modified filename.
    """
    # TODO: probably have a temporary name change operation to avoid
    #       collisions.
    #print(post_path_fn)
    #print(post_path_fn[0])
    #print(post_path_fn[0][0])
    #print(post_path_fn[0][0][0])
    #input('<enter> to continue')
    for elem in post_path_fn:
        os.renames(os.path.join(elem[0][0], elem[0][1]),
                   os.path.join(elem[1][0], elem[1][1]))
    
    

if __name__ == '__main__':
    #print('__main__')
    args = sys.argv[0:]
    print('args={}'.format(args))
    input('<enter> to continue')
    # Parse the input arguements, find the '-f' arg which means a list of
    # files will come next.
##    args.index('-f')
##    pattern = '^-[a-z]'
##    re.search(pattern, '-e')

    for c in range(args.index('-f'), len(args)):
        print(args[c])

    input('<enter> to continue')
        
    #args_f = args[args.index('-f'):

    
    # For the first run through, the original and modiifed parts are the same
    PathFilename = namedtuple('PathFilename', ['path', 'filename'])
    path_fn = {PathFilename(os.path.split(arg)): PathFilename(os.path.split(arg)) for arg in args}
    #print(path_fn)

    #FncTupleType = namedtuple('FncTupleTyple', ['org', 'mod'])
    
    prefix = input('What prefix would you like to add to the filename? ')
    post_path_fn = [(original, (modified[0], add_prefix(modified[1], prefix))) for original, modified in path_fn]
    #print('post_fn={}'.format(post_path_fn))

    r = input('Apply changes? ')
    if r == 'y':
        process_changes(post_path_fn)
    print('Done!')
else:
    print('__name__={}'.format(__name__))

input('<enter> to continue')
