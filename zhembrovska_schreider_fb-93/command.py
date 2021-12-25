import re
from table import Table
import main

tab = Table

def menu(title_arr, elem_mas, command):  

        menu_choice = input("""
        - Create_table
        - Add title ..  
        - Add element .. to line .. column ..
        - Add line ..,..,..,.. 
        - Select line with ..
        - Delete element from line .. column ..
        - Delete title  
        - Delete line ..
        - Print line ..
        - Print table
        - Exit
    """)
        alpf ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        command = menu_choice
        
        for i in alpf :
                word_mas = re.findall(r'[0-9A-Za-z.]+', menu_choice)
                if re.match(r'^[Cc][Rr][Ee][Aa][Tt][Ee]', word_mas[0]):
                  if re.match(r'^[Tt][Aa][Bb][Ll][Ee]', word_mas[1]):  
                    table_name = word_mas[2]
                    if re.match(r'^[Ww][Ii][Tt][Hh]', word_mas[3]):
                        #tab.print_name(table_name)
                        colums = word_mas[4:]
                        print(table_name)
                        print(colums)
                        break
                elif re.match(r'^[Aa][Dd][Dd]', word_mas[0]):
                    if re.match(r'^[Tt][Ii][Tt][Ll][Ee]', word_mas[1]):
                        new_title = word_mas[2]
                        tab.add_new_title(title_arr, new_title)
                        break
                    elif re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        new_line = word_mas[2:]
                        tab.add_elem_line(elem_mas, new_line)
                        break 
                    elif re.match(r'^[Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[1]):
                        new_element = word_mas[2]
                        if re.match(r'^[Tt][Oo]', word_mas[3]):
                            if re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[4]):
                                line_number = word_mas[5]
                                if re.match(r'^[Cc][Oo][Ll][Uu][Mm][Nn]', word_mas[6]):
                                    column_index = word_mas[7]
                                    tab.change_element(elem_mas,new_element,line_number, column_index)
                                    break    
                elif re.match(r'^[Dd][Ee][Ll][Ee][Tt][Ee]', word_mas[0]):
                    if re.match(r'^[Tt][Ii][Tt][Ll][Ee]', word_mas[1]):
                        title_index = word_mas[2]
                        tab.delete_title(title_arr, title_index)
                        break
                    elif re.match(r'^[Ee][Ll][Ee][Mm][Ee][Nn][Tt]', word_mas[1]):
                        new_element = '_____'
                        if re.match(r'^[Ff][Rr][Oo][Mm]', word_mas[2]):
                            if re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[3]):
                                line_number = word_mas[4]
                                if re.match(r'^[Cc][Oo][Ll][Uu][Mm][Nn]', word_mas[5]):
                                    column_index = word_mas[6]
                                    tab.change_element(elem_mas,new_element,line_number, column_index)
                                    break    
                        break
                    elif re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        delete_line_number = word_mas[2]
                        tab.delete_elem_line(elem_mas, delete_line_number)
                        break
                elif re.match(r'^[Ss][Ee][Ll][Ee][Cc][Tt]', word_mas[0]):
                    if re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        if re.match(r'^[Ww][Ii][Tt][Hh]', word_mas[2]):
                            element = word_mas[3]
                            tab.compare(tab, elem_mas, element)
                            break    
                elif re.match(r'^[Pp][Rr][Ii][Nn][Tt]', word_mas[0]):
                    if re.match(r'^[Tt][Aa][Bb][Ll][Ee]', word_mas[1]):
                        tab.print_table(tab, title_arr,elem_mas)
                        break
                    elif re.match(r'^[Ll][Ii][Nn][Ee]', word_mas[1]):
                        line_numb = word_mas[2]
                        number = int(line_numb) - 1
                        tab.print_line(elem_mas, number)
                        break
                elif re.match(r'^[Ee][Xx][Ii][Tt]', word_mas[0]):
                    return 'x'
                else:
                    print("Uncorrect enter !!! \n")
                    break