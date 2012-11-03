#! /usr/python2.7
#-*-coding:utf-8-*-
import os
import sys

if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv != 4 or (sys.argv[2] != '-S' and sys.argv[2] != '-o'):
        #print len_argv,sys.argv[2],sys.argv[2]
        print """useage:
            ./xcc.py source_file -S result_file
            ./xcc.py source_file -o result_file
            """
        exit()
    elif sys.argv[2] == '-S':
        sourcefile = sys.argv[1]
        resultfile = sys.argv[3]
        print sourcefile,resultfile,sys.argv[2]
        os.popen('python grammar.py ' + sourcefile + ' '+ resultfile)
    elif sys.argv[2] == '-o':
        sourcefile = sys.argv[1]
        resultfile = sys.argv[3]
        print sourcefile,resultfile,sys.argv[2]
    tmp = os.popen('ls *.py')
