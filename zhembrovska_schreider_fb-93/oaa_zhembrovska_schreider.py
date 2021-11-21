def separation(n):
        print("-" * n)

def add_new_title(arr):
            new_title = input("Print new title:  ")
            arr.append(new_title)

def delete_title(arr):
            delete_index = int(input("Which title do you want to delete? \n"))
            del arr[delete_index]
    
def print_table(titles_arr, elements_mas):
    print("|    "+('    |    '.join(titles_arr)) + '    |')
    separation(40)
    print_dblarr(elements_mas)
    
    
def add_line_to_dbl_arr(elements_mas):
    for i in range(number_of_lines):
        elements_mas.append(list(map(str , input("Enter elements: ").split(','))))
        separation(40)

def delete_elem_line(elements_mas):
            delete_line = int(input("Which line do you want to delete? \n"))
            del elements_mas[delete_line]

def delete_element(elements_mas):
            delete_line = int(input("Which line is the element you want to delete? \n"))
            delete_index= int(input("Which index have the element you want to delete? \n"))
            elements_mas[delete_line][delete_index] = '____'


def print_dblarr(mas):
    for x in range(0, len(mas)): 
        for y in range(0, len(mas[x])):
            
            print('|    ' + mas[x][y], end = '    ')
        print( ' |')

def menu(title_arr, elem_mas, command):
        menu_choice = input("""
        1 - Add new title name  
        2 - Delete one title name 
        3 - Add new table line 
        4 - Delete one element from table  
        5 - Delete one line from table 
        6 - Print table
        x - Exit
         """)
        command = menu_choice
        for i in '1 2 3 4 5 6 x':
            if menu_choice == "1":
                add_new_title(title_arr)
                break
            elif menu_choice == "2":
                delete_title(title_arr)
                break
            elif menu_choice == "3":
                add_line_to_dbl_arr(elem_mas)
                break 
            elif menu_choice == "4":
                delete_element(elem_mas)
                break
            elif menu_choice == "5":
                delete_elem_line(elem_mas)
                break
            elif menu_choice == "6":
                print_table(title_arr,elem_mas)
                break
            elif menu_choice == "x":
                return 'x'
            else:
                print("Uncorrect enter !!! \n")
                break
#.............................................................................
create_table = input("CREATE TABLE y/n \n")
if create_table == "y":
 
    table_name = input("Enter table name:  ")
    title_arr = input("Enter titles: ").split(',')

    number_of_lines = 1 #int(input())
    elem_mas = []
    for i in range(number_of_lines):
        elem_mas.append(list(map(str , input("Enter elements: ").split(','))))
    
    
    command = ' '
    while command != 'x':
        command = menu(title_arr, elem_mas, command)
        separation(40)

    print_table(title_arr, elem_mas)




       
   


