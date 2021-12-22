#from main 
import re

class Table:
    name = ''
    titles = []
    elements = []

    def compare(self, element_mas, element):
        for x in range(0, len(element_mas)): 
            for y in range(0, len(element_mas[x])): 
                if element == element_mas[x][y]:
                    self.print_line(element_mas, x)
                


    def print_name(table_name):
        name = table_name
        print(table_name)

    def add_new_title(titles, new_title):
        titles.append(new_title)

    def delete_title(arr, index):
        delete_index = int(index) + 1
        arr[delete_index] = '____'

    def print_colums(titles_arr, element_mas, name_colums):
        x = int(name_colums) - 1
        

    def print_line(mas, x):
        for y in range(0, len(mas[x])):  
            print('|    ' + mas[x][y], end = '    ')
        print( ' |')

    def print_dblarr(mas):       
        for x in range(0, len(mas)):
            print( x+1 , end = ' ' )    
            for y in range(0, len(mas[x])): 
                print('|    ' + mas[x][y], end = '    ')
            print( ' |') 

    def print_table(self, titles_arr, elements_mas):
        print("№ |    "+('    |    '.join(titles_arr)) + '    |')
        #self.separation(40)
        print("-" * 60)
        self.print_dblarr(elements_mas)
        
    def add_elem_line(elements_mas, line):
        elements_mas.append(line)


    def delete_elem_line(elements_mas, delete_index):
        x = int(delete_index) - 1
        if x in range(0,len(elements_mas)):    
            del elements_mas[x]
        else: 
         print('No line with № ' + delete_index)    

    def change_element(elements_mas, element, line, index):
        x = int(line) - 1
        y = int(index) - 1
        elements_mas[x][y] = element
