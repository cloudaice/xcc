#-*-coding:utf-8-*-
import sys
import os


#(id,value)
"""
(DIGIT,整数 )
(ID,标识符)
(STR,字符窜)
(INT,int)
(FLOAT,float)
(IF,if)
(FOR,for)
(ELSE,else)
(RETURN,return)
(+,+)
(-,-)
(*,*)
(/,/)
(>,>)
(>=,>=)
(<,<)
(<=,<=)
(==,==)
(INC,++)
(DOT,,)
(SEM,;)
(AND,&)
"""

def analysis_line(line,word_list):
    i =0
    j =0
    state =0
    while j < len(line):
        if state == 0:
            c = line[j]
            if c == '#':
                #word_list.append(line.strip())
                j += len(line)
            elif c == '\n' or c == '\t' or c== ' ':
                state = 0
                j += 1
                i += 1
            elif c.isdigit():
                state = 3
                j += 1
            elif c in ['&','\"','i','f','e','r','+','-','*','/','>','<','=',',',';','(',')','[',']','{','}']:
                render = {'"':5,'i':7,'f':11,'e':19,'r':27,'+':34,'-':35,
                        '*':36,'/':37,'>':38,'<':41,'=':44,',':47,';':48,
                        '(':49,')':50,'[':51,']':52,'{':53,'}':54,'&':55 }
                state = render[c]
                j += 1
            elif c.isalpha() or c == '_':
                state = 1
                j += 1
            else:
                print 'something error'
        elif state == 1:
            c = line[j]
            if c.isalpha() or c == '_':
                state = 1
                j += 1
            else:
                state = 2
        elif state == 2:
            word_list.append(('ID',line[i:j]))
            i = j
            state = 0
        elif  state == 3:
            c = line[j]
            if c.isdigit():
                j += 1
            else:
                state = 4
        elif  state == 4:
            word_list.append(('DIGIT',line[i:j]))
            i = j
            state = 0
        elif  state == 5:
            c = line[j]
            if c== '\"':
                state = 6
                j += 1
            else:
                j += 1
        elif  state == 6:
            word_list.append(('STR',line[i:j]))
            i = j
            state = 0
        elif  state == 7:
            c = line[j]
            if c == 'n':
                state = 8
                j += 1
            elif c == 'f':
                state = 17
                j += 1
            else:
                state = 1
        elif  state == 8:
            c = line[j]
            if c == 't':
                state = 9
                j += 1
            else:
                state = 1
        elif  state == 9:
            c = line[j]
            if c == ' ':
                state = 10
            else:
                state = 1
        elif  state == 10:
            word_list.append( ('INT',line[i:j]) )
            i = j
            state = 0
        elif  state == 11:
            c = line[j]
            if c == 'l':
                state = 12
                j += 1
            elif c == 'o':
                state = 24
                j += 1
            else:
                state = 1
        elif  state == 12:
            c = line[j]
            if c == 'o':
                state = 13
                j += 1
            else:
                state = 1
        elif  state == 13:
            c = line[j]
            if c == 'a':
                state = 14
                j += 1
            else:
                state = 1
        elif  state == 14:
            c = line[j]
            if c == 't':
                j += 1
                state = 15
            else:
                state = 1
        elif  state == 15:
            if line[j] == ' ':
                state = 16
            else:
                state = 1
        elif  state == 16:
            word_list.append( ('FLOAT',line[i:j]) )
            i = j
            state = 0
        elif  state == 17:
            if line[j] == ' ' or line[j] == '(':
                state = 18
            else:
                state = 1
        elif  state == 18:
            word_list.append(('IF',line[i:j]) )
            i = j
            state = 0
        elif  state == 19:
            if line[j] == 'l':
                state = 20
                j += 1
            else:
                state = 1
        elif  state == 20:
            if line[j] == 's':
                state = 21
                j += 1
            else:
                state = 1
        elif  state == 21:
            if line[j] == 'e':
                state = 22
                j += 1
            else:
                state = 1
        elif  state == 22:
            if line[j] == ' ':
                state = 23
            elif line[j] == '{':
                state = 23
            else:
                state = 1
        elif  state == 23:
            word_list.append(('ELSE',line[i:j]) )
            i = j
            state = 0
        elif  state == 24:
            if line[j] == 'r':
                state = 25
                j += 1
            else:
                state = 1
        elif  state == 25:
            if line[j] == ' ' or line[j] == '(':
                state = 26
            else:
                state = 1
        elif  state == 26:
            word_list.append(('FOR',line[i:j]) )
            i = j
            state = 0
        elif  state == 27:
            if line[j] == 'e':
                state = 28
                j += 1
            else:
                state = 1
        elif  state == 28:
            if line[j] == 't':
                state = 29
                j += 1
            else:
                state = 1
        elif  state == 29:
            if line[j] == 'u':
                state = 30
                j += 1
            else:
                state = 1
        elif  state == 30:
            if line[j] == 'r':
                state = 31
                j += 1
            else:
                state = 1
        elif  state == 31:
            if line[j] =='n':
                state = 32
                j += 1
            else:
                state = 1
        elif  state == 32:
            if line[j] == ' ':
                state = 33
            else:
                state = 1
        elif  state == 33:
            word_list.append(('RETURN',line[i:j]) )
            i = j
            state = 0
        elif  state == 34:
            if line[j] == '+':
                state = 57
                j += 1
            else:
                state = 56
        elif  state == 35:
            word_list.append(('-',line[i:j]))
            i = j
            state = 0
        elif  state == 36:
            word_list.append(('*',line[i:j]) )
            i = j
            state = 0
        elif  state == 37:
            word_list.append(('/',line[i:j]))
            i = j
            state = 0
        elif  state == 38:
            if line[j] == '=':
                state = 39
                j += 1
            elif line[j] == ' ':
                j += 1
            else:
                state = 40
        elif  state == 39:
            word_list.append(('>=',line[i:j]))
            i = j
            state = 0
        elif  state == 40:
            word_list.append(('>',line[i:j]))
            i = j
            state = 0
        elif  state == 41:
            if line[j] == ' ':
                j += 1
            elif line[j] == '=':
                state = 42
                j += 1
            else:
                state = 43
        elif  state == 42:
            word_list.append(('<=',line[i:j]))
            i = j
            state = 0
        elif  state == 43:
            word_list.append(('<',line[i:j]))
            i = j
            state = 0
        elif  state == 44:
            if line[j] == '=':
                state = 45
                j += 1
            else:
                state = 46
        elif  state == 45:
            word_list.append(('==',line[i:j]))
            i = j
            state = 0
        elif  state == 46:
            word_list.append(('=',line[i:j]))
            i = j
            state = 0
        elif  state == 47:
            word_list.append(('DOT',line[i:j]))
            i = j
            state = 0
        elif  state == 48:
            word_list.append(('SEM',line[i:j]))
            i = j
            state = 0
        elif  state == 49:
            word_list.append(('(',line[i:j]))
            i = j
            state = 0
        elif  state == 50:
            word_list.append((')',line[i:j]))
            i = j
            state = 0
        elif  state == 51:
            word_list.append(('[',line[i:j]))
            i = j
            state = 0
        elif  state == 52:
            word_list.append((']',line[i:j]))
            i = j
            state = 0
        elif  state == 53:
            word_list.append(('{',line[i:j]))
            i = j
            state = 0
        elif  state == 54:
            word_list.append(('}',line[i:j]))
            i = j
            state = 0
        elif state == 55:
            word_list.append(('AND',line[i:j]))
            i = j
            state = 0
        elif state == 56:
            word_list.append(('+',line[i:j]))
            i = j
            state = 0
        elif state == 57:
            word_list.append(('INC',line[i:j]))
            i = j 
            state = 0

def analysis_file(filename,word_list):
    fd = open(filename,'r')
    for line in fd.readlines():
        analysis_line(line,word_list)

def get_words_list():
    all_words = []
    analysis_file('test/test.c',all_words)
    return all_words


if __name__ == "__main__":
    all_words =[]
    filename = sys.argv[1]
    analysis_file(filename,all_words)
    ids = []
    for word in all_words:
        #ids.append(word[0])
        print word
    #line = ' '.join(ids)
    #print line

