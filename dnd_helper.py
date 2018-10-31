# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:18:49 2018

@author: jancion
"""

import random


names = ['Sarai Bohnert', 'Marilou Gee', 'Cierra Blanton', 'Renetta Milan',
         'Modesta Tran', 'Lakeisha Ryles', 'Nestor Branscome', 
         'Preston Magnusson', 'Bertram Lafromboise', 'Julieta Larusso',
         'Woodrow Presswood', 'Maudie Rico', 'Terry Giorgi', 
         'Shawnna Hedgecock', 'Buddy Mizelle', 'Jayna Darcangelo',
         'Josiah Heyen', 'Ethel Eiler', 'Katherine Tanouye', 'Rena Kowal',
         'Mariah Wiesner', 'Idell Leland', 'Michal Presutti', 
         'Leatha Stickler', 'Christopher Strahan', 'Lannie Mullinax',
         'Blanch Lando', 'Sonja Lis', 'Dionne Cavalieri', 'Tanesha Ryba',
         'So Paoletti', 'Lance Seelig', 'Carina Mcveigh', 'Tracie Pung', 
         'Alissa Gamboa', 'Ignacia Kouba', 'Shery Nogueira', 'Tien Naslund',
         'Addie Kelsch', 'Genevieve Mabery', 'Keven Stengel', 'Lashon Ellisor',
         'Leo Harten', 'Clifton Cyphers', 'Mirella Legette', 'Stacy Wallen',
         'Lyndia Sletten', 'Luvenia Luster', 'Liza Bellon', 'Molly Hintz']

races = ['Human', 'Elf', 'Halfling', 'Dwarf', 'Gnome', 'Orc', 'Half-Elf', 
         'Half-Orc', 'Tiefling']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


def rand_character():
    char_name = random.choice(names)
    char_race = random.choice(races)    
    char_class = random.choice(classes)
    return 'Name: ' + char_name + '\n' + 'Race: ' +  char_race + '\n' + \
            'Class: ' + char_class
    
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
        
    






