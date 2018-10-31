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
    
