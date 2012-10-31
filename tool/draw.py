#-*- coding:utf-8 -*-
import gv
from pygraph.classes.digraph import digraph
from pygraph.readwrite.dot import write
gr = digraph()
nodes = [str(i) for i in range(56)]
gr.add_nodes(nodes)
labels = ['blank|tab|newline','letter','digit','\"','i','f','e','r','+','-','*','/',
        '>','<','=','\,',';','(',')','[',']','{','}','&']
linktonodes = ['0','1','3','5','7','11','19','27','34','35','36','37','38','41','44','47','48','49','50','51','52','53','54','55']
#print len(labels),len(linktonodes)
edges =  [[('0',linktonodes[i]),labels[i]] for i in range(len(labels))]
edges += [[('1','2'),'others'],[('1','1'),'letter']]
edges += [[('3','3'),'digit'],[('3','4'),'others']]
edges += [[('5','5'),'others'],[('5','6'),'\"']]
edges += [[('7','8'),'n'],[ ('8','9'),'t'],[('9','10'),'blank']]
edges += [[('7','17'),'f'],[('17','18'),'blank']]
edges += [[('11','12'),'l'],[('12','13'),'o'],[('13','14'),'a'],[('14','15'),'t'],[('15','16'),'blank']]
edges += [[('11','24'),'0'],[('24','25'),'r'],[('25','26'),'blank']]
edges += [[('19','20'),'l'],[('20','21'),'s'],[('21','22'),'e'],[('22','23'),'blank']]
edges += [[('27','28'),'e'],[('28','29'),'t'],[('29','30'),'u'],[('30','31'),'r'],
          [('31','32'),'n'],[('32','33'),'blank']]
edges += [[('38','38'),'blank'],[('38','39'),'='],[('38','40'),'others']]
edges += [[('41','41'),'blank'],[('41','42'),'='],[('41','43'),'others']]
edges += [[('44','45'),'='],[('44','46'),'others']]
linkto1nodes = ['7','8','9','17','11','12','13','14','15','24','25','19','20','21','22','27','28',
        '29','30','31','32']
edges += [[(node,'1'),'others'] for node in linkto1nodes]

for edge in edges:
    gr.add_edge(edge[0])
for i,edge in enumerate(edges):
    gr.set_edge_label(edge[0],edge[1])
    print edge[0],edge[1]
#gr.set_edge_label(('0','47'),'\,')



#draw as ping
dot = write(gr)
gvv = gv.readstring(dot)
gv.layout(gvv,'dot')
gv.render(gvv,'png','words.png')
