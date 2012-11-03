#-*-coding:utf-8 -*-
import read_table
import words
import string

action_table = read_table.action
goto_table = read_table.goto
words =  words.get_words_list()

expressions = []
#ids = [ word[0] for word in words]
#ids.append('$')
#stream =  ids
stream = [list(word) for word in words]
stream.append(['$',])
state_stack = ['0']
words_stack = []
f_table = {}
index = 0
f_table['addr'] = 0
f_table['label'] = 0
f_table['tmp'] = 0
out_strings = []

outputstr = []

while True:
    word = stream[index][0]
    acter = action_table[state_stack[-1]][word]
    act = acter.strip().split(' ')
    if act[0] == 'shift':
        state_stack.append(act[1])
        words_stack.append({'name':stream[index][0],'value':stream[index][1]})
        index += 1
    elif act[0] == 'reduce':
        act = ' '.join(act[1:])
        expression = act.strip()
        act = act.strip().split('->')
        act[0] = act[0].strip()
        act[1] = act[1].strip()
        act[1] = act[1].split(' ')
        right_exp = []
        while act[1]:
            act[1].pop()
            #print words_stack[-1]['name'],words_stack[-1]['value']
            right_exp.append(words_stack.pop())
            state_stack.pop()
        right_exp.reverse()
        if expression == "type -> INT":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':'int'})

        elif expression == "declarator -> ID [ DIGIT ]":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'], \
                    'size':right_exp[2]['value'],'type':'array'})

        elif expression == "digit_list -> DIGIT":
            words_stack.append({'name':act[0],'value':[right_exp[0]['value'],],'type':'digit_list'})

        elif expression == "digit_list -> digit_list DOT DIGIT":
            #print right_exp[0],right_exp[2]
            words_stack.append({'name':act[0],'value':right_exp[0]['value'] + \
                    [right_exp[2]['value'],],'type':'digit_list'})
            #print words_stack[-1]

        elif expression == "declarator_e -> type declarator = { digit_list } SEM":
            words_stack.append({'name':act[0],'value':'type declarator = { digit_list } SEM'})
            #print right_exp[4]
            if right_exp[0]['value'] == 'int' or right_exp[0]['value'] == 'float':
                mem_size = 4 * int(right_exp[1]['size'])
                f_table['addr'] = f_table['addr'] + mem_size
                f_table[right_exp[1]['value']] = f_table['addr']
                #print 'mem_size',mem_size
                #print 'subl $' + str(mem_size) + ',%esp'
                outputstr.append('subl $' + str(mem_size) + ',%esp')
                for i in range(int(right_exp[1]['size'])):
                    #print 'movl $'+ str(i) +',%ebx'
                    outputstr.append('movl $'+ str(i) +',%ebx')
                    #print 'movl $'+ right_exp[4]['value'][i] + ', -' + str(f_table['addr']) + '(%ebp,%ebx,4)'
                    outputstr.append('movl $'+ right_exp[4]['value'][i] + ', -' + \
                            str(f_table['addr']) + '(%ebp,%ebx,4)')

        elif expression == "expression -> declarator_e":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "expression_list -> expression":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "expression_list -> expression_list expression":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "declarator -> ID":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':'id'})

        elif expression == "declarator_list -> declarator":
            words_stack.append({'name':act[0],'value':[right_exp[0]['value'],],'type':'id_list'})

        elif expression == "declarator_e -> type declarator_list SEM":
            words_stack.append({'name':act[0],'value':'type declarator_list SEM'})
            #print right_exp[1]
            if right_exp[0]['value'] == 'int' or right_exp[0]['value'] == 'float':
                num_len = len(right_exp[1]['value'])
                for i in range(num_len):
                    #print 'subl $4,%esp'
                    outputstr.append('subl $4,%esp')
                    f_table['addr'] = f_table['addr'] + 4
                    f_table[right_exp[1]['value'][i]] = f_table['addr']

        elif expression == "type -> FLOAT":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':'float'})

        elif expression == "declarator_list -> declarator_list DOT declarator":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'] + [right_exp[2]['value'],],\
                    'type':'id_list'})

        elif expression == "func_e -> ID ( STR ) SEM":
            words_stack.append({'name':act[0]})
            if right_exp[0]['value'] == 'printf':
                #print 'LC' + str(f_table['label']) + ':\n.string ' + right_exp[2]['value']
                out_strings.append('LC' + str(f_table['label']) + ': .string ' + right_exp[2]['value'])
                #print 'pushl $LC' + str(f_table['label'])
                outputstr.append('pushl $LC' + str(f_table['label']))
                f_table['label'] += 1
                #print 'call printf'
                outputstr.append('call printf')
                #print 'addl $4,%esp'
                outputstr.append('addl $4,%esp')

        elif expression == "expression -> func_e":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "func_e -> ID ( STR DOT AND ID ) SEM":
            words_stack.append({'name':act[0]})
            if right_exp[0]['value'] == 'scanf':
                #print 'leal -' + str(f_table[right_exp[5]['value']])+'(%ebp),%eax'
                outputstr.append('leal -' + str(f_table[right_exp[5]['value']])+'(%ebp),%eax')
                #print 'pushl %eax'
                outputstr.append('pushl %eax')
                #print 'LC' + str(f_table['label']) + ':\n.string ' + right_exp[2]['value']
                out_strings.append('LC' + str(f_table['label']) + ': .string ' + right_exp[2]['value'])
                #print 'pushl $LC' + str(f_table['label'])
                outputstr.append('pushl $LC' + str(f_table['label']))
                f_table['label'] += 1
                #print 'call scanf'
                outputstr.append('call scanf')
                #print 'addl $8,%esp'
                outputstr.append('addl $8,%esp')

        elif expression == "cast_e -> DIGIT":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':'digit'})

        elif expression == "multi_e -> cast_e":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':right_exp[0]['type']})

        elif expression == "add_e -> multi_e":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':right_exp[0]['type']})

        elif expression == "assignment_e -> declarator = add_e SEM":
            words_stack.append({'name':act[0]})
            if right_exp[2]['type'] == 'digit':
                #print 'movl $' + right_exp[2]['value'] + ',-' + str(f_table[right_exp[0]['value']]) + '(%ebp)'
                outputstr.append('movl $' + right_exp[2]['value'] + ',-' + str(f_table[right_exp[0]['value']]) + '(%ebp)')
            elif right_exp[2]['type'] == 'array':
                #print 'movl ' + f_table[right_exp[2]['value']] + ',-' + str(f_table[right_exp[0]['value']]) + '(%ebp)'
                outputstr.append('movl ' + f_table[right_exp[2]['value']] + ',%eax')
                outputstr.append('movl %eax,' + '-' + str(f_table[right_exp[0]['value']]) + '(%ebp)')
            else:
                print 'error'

        elif expression == "expression -> assignment_e":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "cast_e -> declarator":
            words_stack.append({'name':act[0],'value':right_exp[0]['value'],'type':right_exp[0]['type']})

        elif expression == "bool_e -> cast_e < cast_e":
            #print  words_stack[-1],words_stack[-2],words_stack[-3]
            #print 'start_for:'
            outputstr.append('start_for:')
            #print 'movl -' + str(f_table[right_exp[0]['value']]) + '(%ebp), %eax'
            outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) + '(%ebp), %eax')
            #print 'movl $'+right_exp[2]['value'] + ',%ebx'
            outputstr.append('movl $'+right_exp[2]['value'] + ',%ebx')
            #print 'cmp %ebx,%eax'
            outputstr.append('cmp %ebx,%eax')
            #print 'jae end_for'
            outputstr.append('jae end_for')
            words_stack.append({'name':act[0]})

        elif expression == "inc_e -> ID INC":
            #print 'addl $1,-' + str(f_table[right_exp[0]['value']]) + '(%ebp)'
            words_stack.append({'name':act[0],'value':'addl $1,-' + \
                str(f_table[right_exp[0]['value']]) + '(%ebp)' })

        elif expression == "cast_e -> ID [ ID ]":
            words_stack.append({'name':act[0],'value':right_exp[0]['value']+right_exp[1]['value'] + \
                    right_exp[2]['value'] + right_exp[3]['value'],'type':'array'
                    })
            #print 'movl -' + str(f_table[right_exp[2]['value']]) + '(%ebp),%edx'
            outputstr.append('movl -' + str(f_table[right_exp[2]['value']]) + '(%ebp),%edx')
            #print 'movl -' + str(f_table[right_exp[0]['value']]) + '(%ebp,%edx,4), %eax'
            outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) + '(%ebp,%edx,4), %eax')
            #print 'movl %eax, tmp' + str(f_table['tmp'])
            outputstr.append('movl %eax, tmp' + str(f_table['tmp']))

            f_table[words_stack[-1]['value']] = 'tmp' + str(f_table['tmp'])
            f_table['tmp']+= 1

        elif expression == "multi_e -> multi_e * cast_e":
            #print right_exp[0]['value'],right_exp[2]['value']
            #print 'movl ' + str(f_table[right_exp[0]['value']]) + ',%eax'
            outputstr.append('movl ' + str(f_table[right_exp[0]['value']]) + ',%eax')
            #print 'movl ' + str(f_table[right_exp[2]['value']]) + ',%ebx'
            outputstr.append('movl ' + str(f_table[right_exp[2]['value']]) + ',%ebx')
            #print 'mull %ebx'
            outputstr.append('mull %ebx')
            #print 'movl %eax,' + 'tmp' + str(f_table['tmp'])
            outputstr.append('movl %eax,' + 'tmp' + str(f_table['tmp']))
            words_stack.append({'name':act[0],'value':'multi_e'})
            f_table['multi_e'] = 'tmp' + str(f_table['tmp'])
            f_table['tmp'] += 1

        elif expression == "add_e -> add_e + multi_e":
            #print 'movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)'  + ',%eax'
            outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)'  + ',%eax')
            #print 'movl '  + str(f_table[right_exp[2]['value']]) + ',%ebx'
            outputstr.append('movl '  + str(f_table[right_exp[2]['value']]) + ',%ebx')
            #print 'addl %ebx,%eax'
            outputstr.append('addl %ebx,%eax')
            #print 'movl %eax,' + 'tmp' + str(f_table['tmp'])
            outputstr.append('movl %eax,' + 'tmp' + str(f_table['tmp']))
            f_table['add_e'] = 'tmp' + str(f_table['tmp']);
            f_table['tmp'] += 1
            words_stack.append({'name':act[0],'value':'add_e','type':'array'})

        elif expression == "iterator_e -> FOR ( assignment_e bool_e SEM inc_e ) { expression_list }":
            #print right_exp[5]['value']
            outputstr.append(right_exp[5]['value'])
            #print 'jmp start_for'
            outputstr.append('jmp start_for')
            #print 'end_for:'
            outputstr.append('end_for:')
            words_stack.append({'name':act[0]})

        elif expression == "expression -> iterator_e":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "multi_e -> multi_e / cast_e":
            #print 'movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)' + ',%eax'
            outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)' + ',%eax')
            #print 'movl -' + str(f_table[right_exp[2]['value']]) +'(%ebp)' + ',%ebx'
            outputstr.append('movl -' + str(f_table[right_exp[2]['value']]) +'(%ebp)' + ',%ebx')
            #print 'divl %ebx'
            outputstr.append('divl %ebx')
            #print 'movl %eax,' + 'tmp' + str(f_table['tmp'])
            outputstr.append('movl %eax,' + 'tmp' + str(f_table['tmp']))
            words_stack.append({'name':act[0],'value':'multi_e','type':'array'})
            f_table['multi_e'] = 'tmp' + str(f_table['tmp'])
            f_table['tmp'] += 1


        elif expression == "bool_e -> cast_e >= cast_e":
            #print 'movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)' + ',%eax'
            outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)' + ',%eax')
            #print 'movl $' + right_exp[2]['value'] + ', %ebx'
            outputstr.append('movl $' + right_exp[2]['value'] + ', %ebx')
            #print 'cmp %ebx, %eax'
            outputstr.append('cmp %ebx, %eax')
            #print 'jb else'
            outputstr.append('jb else')
            words_stack.append({'name':act[0]})

        elif expression == "add_e -> add_e - multi_e":
            if right_exp[0]['type'] == 'digit':
                #print 'movl $' + right_exp[0]['value'] + ',%eax'
                outputstr.append('movl $' + right_exp[0]['value'] + ',%eax')
                #print 'movl -' + str(f_table[right_exp[2]['value']]) +'(%ebp)'  + ',%ebx'
                outputstr.append('movl -' + str(f_table[right_exp[2]['value']]) +'(%ebp)'  + ',%ebx')
            else:
                #print 'movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)'  + ',%eax'
                outputstr.append('movl -' + str(f_table[right_exp[0]['value']]) +'(%ebp)'  + ',%eax')
                #print 'movl $' + right_exp[2]['value'] + ',%ebx'
                outputstr.append('movl $' + right_exp[2]['value'] + ',%ebx')
            #print 'subl %ebx,%eax'
            outputstr.append('subl %ebx,%eax')
            #print 'movl %eax,' + 'tmp' + str(f_table['tmp'])
            outputstr.append('movl %eax,' + 'tmp' + str(f_table['tmp']))
            f_table['add_e'] = 'tmp' + str(f_table['tmp']);
            f_table['tmp'] += 1
            words_stack.append({'name':act[0],'value':'add_e','type':'array'})

        elif expression == "func_e -> ID ( STR DOT declarator_list ) SEM":
            #print right_exp[4]
            for v in right_exp[4]['value']:
                #print 'pushl -' + str(f_table[v]) +'(%ebp)'
                outputstr.append('pushl -' + str(f_table[v]) +'(%ebp)')
            count = len(right_exp[4]['value']) + 1
            #print 'LC' + str(f_table['label']) + ':\n.string ' + right_exp[2]['value']
            out_strings.append('LC' + str(f_table['label']) + ': .string ' + right_exp[2]['value'])
            #print 'pushl LC' + str(f_table['label'])
            outputstr.append('pushl $LC' + str(f_table['label']))
            f_table['label'] += 1
            #print 'call printf'
            outputstr.append('call printf')
            #print 'addl $' + str(count * 4) + ',%esp'
            outputstr.append('addl $' + str(count * 4) + ',%esp')
            #print 'jmp end'
            outputstr.append('jmp end')
            words_stack.append({'name':act[0]})
            #print words_stack[-1],words_stack[-2],words_stack[-3],words_stack[-4]
            if words_stack[-4]['name'] != 'ELSE':
                #print 'else:'
                outputstr.append('else:')

        elif expression == "select_e -> IF ( bool_e ) { expression_list } ELSE { expression_list }":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "expression -> select_e":
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        elif expression == "expression -> RETURN DIGIT SEM":
            #print 'end:'
            outputstr.append('end:')
            #print 'movl $1, %eax'
            outputstr.append('movl $1, %eax')
            #print 'movl $0, %ebx'
            outputstr.append('movl $0, %ebx')
            words_stack.append({'name':act[0]})

        elif expression == "p -> INT ID ( ) { expression_list }":
            #print 'int $0x80'
            outputstr.append('int $0x80')
            #print expression,len(right_exp)
            words_stack.append({'name':act[0]})

        else:
            print 'error no this expression'
        if goto_table[state_stack[-1]][words_stack[-1]['name']] == 'error':
            print 'goto error'
            exit()
        goto_state = goto_table[state_stack[-1]][words_stack[-1]['name']]
        state_stack.append(goto_state)
        expressions.append(expression)
    elif act[0] == 'accept':
        print 'accept'
        break
    elif act[0] == 'error':
        print 'action error'
        print act
        exit()
    else:
        print 'unkown error'
        print act
        exit()

startstr= ['.section .data']
for i in range(f_table['tmp']):
    startstr.append('tmp'+str(i) + ': .int 0')
startstr.append('.section .text')
startstr.append('.globl main')
startstr += ['main:','pushl %ebp','movl %esp, %ebp']
for v in startstr:
    print v
for v in outputstr:
    print v
for s in out_strings:
    print s
result = startstr + outputstr + out_strings
fd = open('out.s','a')
for v in result:
    fd.write(v + '\n')
#for k,v in f_table.items():
#    print k,v
#for v in expressions:
#    print v

"""
ex = []
for v in expressions:
    if v not in ex:
        print '\"'+v+'\":lambda'
    ex.append(v)
"""
