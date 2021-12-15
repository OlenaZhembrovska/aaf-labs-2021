import re
from table import Table

def separation(n):
            print("-" * n)

def menu(title_arr, elem_mas, command):
        menu_choice = input("""
        - Create_table
        - Add title  
        - Add element
        - Delete title  
        - Delete line
        - Delete element
        - Print
        - Exit
    """)
        alpf ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        command = menu_choice
        
        for i in alpf :
                word_mas = re.findall(r'\w+', menu_choice)
                if re.match(r'^[Cc][Rr][Ee][Aa][Tt][Ee][_][Tt][Aa][Bb][Ll][Ee]', word_mas[0]):
                    table_name = word_mas[1]
                    tab.print_name(table_name)
                    break
                elif re.match(r'^[Aa][Dd][Dd]', word_mas[0]):
                    if re.match(r'^[Tt][Ii][Tt][Ll][Ee]', word_mas[1]):
                        new_title = word_mas[2]
                        
                        tab.add_new_title(title_arr, new_title)
                        break
                    elif re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        new_line = word_mas[2]
                        print(new_line)
                        tab.add_elem_line(elem_mas, new_line)
                        break 
                    elif re.match(r'^[Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[1]):
                        new_element = word_mas[2]
                        tab.change_element(elem_mas,new_element)
                        break    
                elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee]', word_mas[0]):
                    if re.match(r'^[Tt][Ii][Tt][Ll][Ee]', word_mas[1]):
                        tab.delete_title(title_arr)
                        break
                    elif re.match(r'^[Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[1]):
                        tab.delete_element(elem_mas)
                        break
                    elif re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        tab.delete_elem_line(elem_mas)
                        break
                elif re.match(r'^[Ss][Ee][Ll][Ee][Cc][Tt]', word_mas[0]):
                    element = word_mas[1]
                    #tab.print_table(tab, title_arr,elem_mas)
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
tab.name = 'friends'
tab.titles = ['№','name ','surname','birth']
tab.elements = [['1','Aseya','Sernova','19.12'],
                ['2','Lesha','Siedykh', '02.03'],
                ['3','Vadym','Atamank', '12.05'],
                ['4','Gulia','Klassna', '06.01'],
                ['5','Tanya','Malanya', '03.01'],
                ['6','Vicky','Leshena', '21.11'],
                ['7','Aleks','Murguls', '19.11']] 

command = ' '
while command != 'x':
    command = menu(tab.titles, tab.elements, command)
    separation(60)

                        


 