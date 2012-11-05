#! /usr/python2.7
#-*-coding:utf-8-*-
import os
import sys
import grammar

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
        try:
            grammar.do_grammar(sourcefile,resultfile)
        except:
            print 'file error'
            exit()
    elif sys.argv[2] == '-o':
        sourcefile = sys.argv[1]
        resultfile = sys.argv[3]
        try:
            os.system('gcc ' + sourcefile + ' -o ' + resultfile)
        except:
            print 'file error'
            exit()
