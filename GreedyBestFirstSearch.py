
map={'Arab':[('Zerind',75),('Sibiu',140),('Timisoara',118)],
     'Zerind':[('Arab',75),('Oradea',71)],
     'Oradea':[('Zerind',71),('Sibiu',151)],
      'Sibiu':[('Arab',140),('Oradea',151),('Fagaras',99),('Rimnicu Vilcea',80)],
       'Timisoara':[('Arab',118),('Lugoj',111)],
        'Lugoj':[('Timisoara',111),('Mehadia',70)],
         'Mehadia':[('Lugoj',70),('Drobeta',75)],
        'Drobeta':[('Mehadia',75),( 'Craiova',120)],
         'Craiova':[('Drobeta',120),('Pitesi',138),('Rimnicu Vilcea',146)],
          'Rimnicu Vilcea':[('Craiova',146),('Pitesi',97),('Sibiu',80)],
         'Fagaras':[('Sibiu',99),('Bucharest',211)],
          'Pitesi':[('Rimnicu Vilcea',97),('Craiova',138),('Bucharest',101)],
           'Bucharest':[('Pitesi',101),('Fagaras',211),('Giurgiu',90),('Urziceni',85)],
           'Giurgiu':[('Bucharest',90)],
           'Urziceni':[('Bucharest',85),('Hirsova',98),('Vaului',142)],
           'Hirsova':[('Urziceni',98),('Eforie',86)],
           'Eforie':[('Hirsova',86)],
         'Vaslui':[('Urziceni',142),('Iasi',92)],
          'Iasi':[('Vaslui',92),('Neampt',87)],
          'Neampt':[('Iasi',87)] }
heuristic={'Arab':366,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
          'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
           'Mehadia':241,'Neampt':234,'Oradea':380,'Pitesi':100,'Rimnicu Vilcea':193,
            'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
def minimum(d):
    node=d[0][0]
    m=heuristic[node]
    for i in range(1,len(d)):
        if heuristic[d[i][0]]<m:
            m=heuristic[d[i][0]]
            node=d[i][0]
    return node 
            
node=input('Enter Starting city:')
goal=input('Enter Goal city:')
path=node+"-->"
while node!=goal:
    d=map[node]
    node=minimum(d)
    path+=node+"-->"
print(path[:-3])
    
