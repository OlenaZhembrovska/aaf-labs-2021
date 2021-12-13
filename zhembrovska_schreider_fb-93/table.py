#from main import 

class Table:
    titles = []
    elements = []



    def separation(n):
        print("-" * n)

    def print_dblarr(mas):
        for x in range(0, len(mas)): 
            for y in range(0, len(mas[x])):
                print('|    ' + mas[x][y], end = '    ')
            print( ' |') 

    def add_new_title(titles, new_title):
       
        #for i in range(number_of_lines):
        #elem_mas.append(list(map(str , input("Enter elements: ").split(','))))
        #new_title = input("Print new title:  ")
        titles.append(new_title)

    def delete_title(arr):
                delete_index = int(input("Which title do you want to delete? \n"))
                del arr[delete_index]



    def print_table(self, titles_arr, elements_mas):
        print("|    "+('    |    '.join(titles_arr)) + '    |')
        #separation(40)
        print("-" * 40)
        self.print_dblarr(elements_mas)
        
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