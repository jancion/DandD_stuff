"""
Julian Ancion
Trap generator for DND
"""

def trapper(level, *argv):
    trap_list = ['gas', 'pit', 'monster', 'spikes', 'boulder', 'magic', 'arrow', 'room']
    gases = ['poison', 'sleeping', 'burning']
    monsters = ['small', 'medium', 'large']
    numbers = ['few', 'some', 'many']
    depths = ['shallow', ]
  
    if argv:
        for i in trap_list:
            if argv[0] == i:
                trap = i
    else:
        print 'trap not in list'
        print 'assign random trap'        
        trap = random.choice(trap_list)
    
    if trap == 'gas':
        flavor = random.choice(gases)
        severity = random.randint(1, 5) * level
        result = trap, flavor, severity
    elif trap == 'pit':
        depth = random.randint(10,20) * level
        result = trap, depth
    elif trap == 'monster':
        result = 'monster'        
    elif trap == 'spikes':
        damage = random.randrange(1, 5) * level
        result = 'spikes', damage
    elif trap == 'boulder':
        result = 'boulder'
    elif trap == 'magic':
        result = 'magic'
    elif trap == 'arrow':
        result = 'arrow'
    elif trap == 'room':
        result = 'room'
    else:
        result = 'null'
    return result
