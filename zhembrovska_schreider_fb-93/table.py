#from main import 

class Table:
    name = ''
    titles = []
    elements = []

    def print_name(table_name):
        name = table_name
        print(table_name)

    def print_dblarr(mas):
        for x in range(0, len(mas)): 
            for y in range(0, len(mas[x])):
                print('|    ' + mas[x][y], end = '    ')
            print( ' |') 

    def add_new_title(titles, new_title):
        titles.append(new_title)

    def delete_title(arr):
        delete_index = int(input("Which title do you want to delete? \n"))
        arr[delete_index] = '____'



    def print_table(self, titles_arr, elements_mas):
        print("|    "+('    |    '.join(titles_arr)) + '    |')
        #self.separation(40)
        print("-" * 60)
        self.print_dblarr(elements_mas)
        
    def add_elem_line(elements_mas, line):
        print(line)
        elements_mas.append(list(map(str , line.split(','))))


    def delete_elem_line(elements_mas):
        delete_line = int(input("Which line do you want to delete? \n"))
        del elements_mas[delete_line]

    def change_element(elements_mas, element):
        line = int(input("Which line is the element you want to delete? \n"))
        index= int(input("Which index have the element you want to delete? \n"))
        elements_mas[line][index] = element

    def delete_element(elements_mas):
        delete_line = int(input("Which line is the element you want to delete? \n"))
        delete_index= int(input("Which index have the element you want to delete? \n"))
        elements_mas[delete_line][delete_index] = '____'