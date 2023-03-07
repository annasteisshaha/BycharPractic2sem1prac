#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os 

def change_directory(new_directory = ''):
        try:
            os.chdir('C:\\Users\\Анастасия\\STUDY\\PRAK\\Programming patterns' + '\\' + new_directory)
        except FileNotFoundError:
            print('Такая папка не существует')
            
def create_folder(name):
    try:
        os.mkdir('C:\\Users\\Анастасия\\STUDY\\PRAK\\Programming patterns\\Departments' + '\\' + name)
    except FileExistsError:
        print ('Папка с таким именем уже есть') 
        
def create_file(name, text = None):
    with open(os.getcwd() + '\\' + name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)  
            
def move_file(name_file, name_dir):
    try:
        os.replace(os.getcwd() + '\\' + name_file, 'C:\\Users\\Анастасия\\STUDY\\PRAK\\Programming patterns\\Departments' + '\\' + name_dir + '\\' + name_file)
    except FileNotFoundError:
        print('Папки или файла не существует')


# In[ ]:




