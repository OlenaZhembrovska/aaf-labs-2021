import re
from table import Table


def separation(n):
            print("-" * n)

def menu(title_arr, elem_mas, command):
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
                    tab.add_new_title(title_arr, new_title)
                    break
                elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Tt][Ii][Tt][Ll][Ee]', word_mas[0]):
                    tab.delete_title(title_arr)
                    break
                elif re.match(r'^[Aa][Dd][Dd][_][Ll][Ii][Nn][Ee]', word_mas[0]):
                    tab.add_elem_line(elem_mas)
                    break 
                elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Ll][Ii][Nn][Ee]', word_mas[0]):
                    tab.delete_elem_line(elem_mas)
                    break
                elif re.match(r'^[Cc][Hh][Aa][Nn][Gg][Ee][_][Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[0]):
                    tab.change_element(elem_mas)
                    break
                elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee][_][Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[0]):
                    tab.delete_element(elem_mas)
                    break    
                elif re.match(r'^[Pp][Rr][Ii][Nn][Tt]', word_mas[0]):
                    tab.print_table(tab, title_arr,elem_mas)
                    break
                elif re.match(r'^[Ee][Xx][Ii][Tt]', word_mas[0]):
                    return 'x'
                else:
                    print("Uncorrect enter !!! \n")
                    break
#.............................................................................
tab = Table
tab.titles = []
tab.elements = []
                   
command = ' '
while command != 'x':
    command = menu(tab.titles, tab.elements, command)
    separation(40)

                        


