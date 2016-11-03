#!/usr/bin/python

import sys,getopt
from sys import argv


def main(argv):
    inputfile=''
    outputfile=''
    helpline=__file__+ "-i <inputfile> -o <outputfile>"
    
    try:
        opts, args=getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print helpline
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpline
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
        elif opt in ("-o","--ofile"):
            outputfile= arg
    print 'Input file is"',inputfile
    print 'Output file is"',outputfile
    
    
if __name__=="__main__":
    main(sys.argv[1:])
    
        