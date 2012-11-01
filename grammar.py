#-*-coding:utf-8 -*-
import read_table
import words

action_table = read_table.action
goto_table = read_table.goto
words =  words.get_words_list()


expressions = []
ids = [ word[0] for word in words]
ids.append('$')
stream =  ids
state_stack = ['0']
words_stack = []


index = 0
while True:
    word = stream[index]
    acter = action_table[state_stack[-1]][word]
    act = acter.strip().split(' ')
    if act[0] == 'shift':
        state_stack.append(act[1])
        words_stack.append(word)
        index += 1
    elif act[0] == 'reduce':
        act = ' '.join(act[1:])
        expression = act.strip()
        act = act.strip().split('->')
        act[0] = act[0].strip()  
        act[1] = act[1].strip()
        act[1] = act[1].split(' ')
        while act[1]:
            act[1].pop()
            words_stack.pop()
            state_stack.pop()
        words_stack.append(act[0])
        if goto_table[state_stack[-1]][words_stack[-1]] == 'error':
            print 'goto error'
            exit()
        goto_state = goto_table[state_stack[-1]][words_stack[-1]]
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

for v in expressions:
    print v
