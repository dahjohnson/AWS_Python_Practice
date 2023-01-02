from random import choice
from csv import writer
from os import getcwd

def select_department():
    
    print('\nPlease enter the Name of the Department you would like to generate an EC2 name for.\n')
    print('Choose from the following: ')
    print('1) Marketing')
    print('2) Accounting')
    print('3) FinOps\n')

    dep_choice = input('Enter Department Name: ')

    match dep_choice:
        case 'Marketing':
            return 'Marketing'
        case 'Accounting':
            return 'Accounting'
        case 'FinOps':
            return 'FinOps'
        case _:
            print('\nYou\'ve entered the wrong option! Please try again or contact the System Administrator.\n')
            return select_department()

def select_count():
    try:
        count_choice = int(input('Please enter the number of instances you would like to generate a name for: '))
        return count_choice
    except ValueError:
        print('\nYou must enter an interger value!')
        print('Example:  1, 4, 10, etc.\n')
        return select_count()

def ec2_name_gen(ec2_count, department):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    char_list = []
    csv_list = []
    zip_csv_list = zip(csv_list)
    csv_name = 'ec2-instance-names.csv'
    cwd = getcwd()
    
    print('\nHere are the Names for your EC2 Instance(s):')

    for count in range(ec2_count):
        for x in range(7):
            char_list.append(choice(characters))
        join_list = ''.join(char_list)
        string = department + r'-' + join_list
        print(string)
        csv_list.append(string)
        char_list = []

    zip_csv_list = zip(csv_list)
    try:
        with open(csv_name, 'w', newline= '') as csv_file:
            w = writer(csv_file)
            for name in zip_csv_list:
                w.writerow(name)
            csv_file.close()
    except PermissionError:
        print(f'\nPermission Error:')
        print(f'Unable to export name(s) to {csv_name} in {cwd}')
        print(f'Verify that the file, {csv_name}, is closed OR that you have permissions to create a file in {cwd}')
    else:
        print(f'\nNames have also been exported to \'{csv_name}\' in {cwd}\n')

print('\nWelcome to the EC2 Random Name Generator!')

department = select_department()
ec2_count = select_count()

ec2_name_gen(ec2_count, department)