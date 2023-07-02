'''variables=['Western Australia','Northern Territory','South Australia','Queensland','New south wales','Victoria','Tasmania']
assigned_colors=['','','','','','','']
available_colors=['Red','Green','Blue']
assignment=[]
Australia_map=[
    [0,1,1,0,0,0,0],
    [1,0,1,1,0,0,0],
    [1,1,0,1,1,1,0],
    [0,1,1,0,1,0,0],
    [0,0,1,1,0,1,0],
    [0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0]]
'''

n=int(input('Enter no. of cities:'))
variables=input('Enter cities:').split()
available_colors=input('Enter available colors:').split()
print('Enter map in graph format')
assigned_colors=[]
Australia_map=[]
for i in range(n):
    assigned_colors.append('')
    l=[int(x) for x in input().split(',')]
    Australia_map.append(l)
assignment=[]


def check_constraint(city_index,color):
    adjacent_cities=[x for x in range(len(Australia_map[city_index])) if Australia_map[city_index][x]==1]
    
    for city in adjacent_cities:
        if assigned_colors[city]==color:
           return False
    return True
def assign_color():
    
    if '' not in assigned_colors:
        return assigned_colors

    pending_cities=[variables[i] for i in range(len(variables)) if assigned_colors[i]=='']

    for city in pending_cities:
        
        for color in available_colors:
            city_index=variables.index(city)
            if not check_constraint(city_index,color):
                continue
            assignment.append( (city,color))
            assigned_colors[city_index]=color 
            print(city,' assigned with ',color)
            
            result= assign_color()
            if result!='failure':
                return result
            
        else:
            return 'failure'
            



coloured_map=assign_color() 
if coloured_map=='failure':
    print('Coloring not possible with available colors.')
else:
    print(coloured_map)


