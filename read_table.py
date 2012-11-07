#-*-coding:utf-8 -*-
actionfd = open('lib/action','r')
action = {}
for line in actionfd.readlines():
    line = line.strip().split(':')
    k1,k2 = line[0].split(' ')
    try:
        action[k1][k2] = line[1]
    except:
        action[k1] = {}
        action[k1][k2] = line[1]
gotofd = open('lib/goto','r')
goto = {}
for line in gotofd.readlines():
    line = line.strip().split(':')
    k1,k2 = line[0].split(' ')
    try:
        goto[k1][k2] = line[1]
    except:
        goto[k1] = {}
        goto[k1][k2] = line[1]

#print action['2']['ID']
#print action['52']['INT']
#print goto['0']['expression_list']
#print goto['6']['expression_list']
