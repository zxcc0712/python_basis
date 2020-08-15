import  sys,shelve

def store_person(db):
    '''
    让用户输入的数据并存储在shelf对象中
    '''
    pid = input('Enter unique ID number:')
    person = {}
    person['name'] = input('Enter name:')
    person['age'] = input('Enter age:')
    person['phone'] = input('Enter phone:')
    db[pid] = person

def lookup_person(db):

    pid = input('Enter ID number:')
    field = input('what would you like to know?(name,age,phone)')
    field = field.strip().lower()

    print(field.capitalize()+':',db[pid][field])

def print_help():
    print('''
    sdsadasddasdad
    ''')

def enter_command():
    cmd = input()
    cmd = cmd.strip().lower()
    return cmd

