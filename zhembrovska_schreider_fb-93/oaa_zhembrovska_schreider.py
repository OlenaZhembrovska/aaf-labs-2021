import re

def separation(n):
        print("-" * n)

def print_dblarr(mas):
    for x in range(0, len(mas)): 
        for y in range(0, len(mas[x])):
            
            print('|    ' + mas[x][y], end = '    ')
        print( ' |') 

def add_new_title(new_title):
    #for i in range(number_of_lines):
    #elem_mas.append(list(map(str , input("Enter elements: ").split(','))))
    #new_title = input("Print new title:  ")
    titles.append(new_title)

def delete_title(arr):
            delete_index = int(input("Which title do you want to delete? \n"))
            del arr[delete_index]
    
def print_table(titles_arr, elements_mas):
    print("|    "+('    |    '.join(titles_arr)) + '    |')
    separation(40)
    print_dblarr(elements_mas)
    
def add_elem_line(elements_mas):

    #for i in range(number_of_lines):
    elements_mas.append(list(map(str , input("Enter elements: ").split(','))))

def delete_elem_line(elements_mas):
    delete_line = int(input("Which line do you want to delete? \n"))
    del elements_mas[delete_line]

def change_element(elements_mas):
    line = int(input("Which line is the element you want to delete? \n"))
    index= int(input("Which index have the element you want to delete? \n"))
    elements_mas[line][index] = input('Enter new element:  ')

def delete_element(elements_mas):
    delete_line = int(input("Which line is the element you want to delete? \n"))
    delete_index= int(input("Which index have the element you want to delete? \n"))
    elements_mas[delete_line][delete_index] = '____'

def menu(title_arr, elem_mas, command):
    
    #title_arr = input("Enter titles: ").split(',')

    menu_choice = input("""
    - Create_table
    - Add_title  
    - Delete_title 
    - Add_line 
    - Delete_line
    - Change_element
    - Delete_element
    - Print
    - Exit
""")
    alpf ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    command = menu_choice
    
    for i in alpf :
            word_mas = re.findall(r'\w+', menu_choice)
            if re.match(r'^[Cc][Rr][Ee][Aa][Tt][Ee][_][Tt][Aa][Bb][Ll][Ee]', word_mas[0]):
                table_name = word_mas[1]
                print('table name: ' + table_name)
                break
            elif re.match(r'^[Aa][Dd][Dd][_][Tt][Ii][Tt][Ll][Ee]', word_mas[0]):
                new_title = word_mas[1]
                print(new_title)
                add_new_title(new_title)
                break
            elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Tt][Ii][Tt][Ll][Ee]', word_mas[0]):
                delete_title(title_arr)
                break
            elif re.match(r'^[Aa][Dd][Dd][_][Ll][Ii][Nn][Ee]', word_mas[0]):
                add_elem_line(elem_mas)
                break 
            elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Ll][Ii][Nn][Ee]', word_mas[0]):
                delete_elem_line(elem_mas)
                break
            elif re.match(r'^[Cc][Hh][Aa][Nn][Gg][Ee][_][Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[0]):
                change_element(elem_mas)
                break
            elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[0]):
                delete_element(elem_mas)
                break    
            elif re.match(r'^[Pp][Rr][Ii][Nn][Tt]', word_mas[0]):
                print_table(title_arr,elem_mas)
                break
            elif re.match(r'^[Ee][Xx][Ii][Tt]', word_mas[0]):
                return 'x'
            else:
                print("Uncorrect enter !!! \n")
                break
#.............................................................................

titles = []
elements = []

                    
command = ' '
while command != 'x':
    command = menu(titles, elements, command)
    separation(40)

                        


