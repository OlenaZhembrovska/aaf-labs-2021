def separation(n):
        print("-" * n)

def add_new_title(arr):
            new_title = input("Print new title:  ")
            arr.append(new_title)

def delete_title(arr):
            i = int(input("Which title do you want to delete? \n"))
            del arr[i]
    
def print_table(arr, mas):
    print("|    "+('    |    '.join(arr)) + '    |')
    separation(40)
    print_dblarr(mas)
    
    
def add_line_to_dbl_arr(mas):
    for i in range(a):
        mas.append(list(map(str , input("Enter elements: ").split(','))))

def print_dblarr(mas):
    for x in range(0, len(mas)):
        
        for y in range(0, len(mas[x])):
            
            print('|    ' + mas[x][y], end = '    ')
        print( ' |')

def menu(title_arr, elem_mas, command):
        b = input('  a - Add new title name?  \n  d - Delete one title name?    \n  l - Add new table line?  \n  t - Print table   \n  x - Exit \n')
        command = b
        for i in 'a d l t x':
            if b == "a":
                add_new_title(title_arr)
                break
            elif b == "d":
                delete_title(title_arr)
                break
            elif b == "l":
                add_line_to_dbl_arr(elem_mas)
                break
            elif b == "t":
                print_table(title_arr,elem_mas)
                #print_dblarr(mas) 
                break
            elif b == "x":
                return 'x'
            else:
                print("Uncorrect enter !!! \n")
                break
#.............................................................................
a = input("CREATE TABLE y/n \n")
if a == "y":
 
    table_name = input("Enter table name:  ")
    title_arr = input("Enter titles: ").split(',')

    a = 1 #int(input())
    elem_mas = []
    for i in range(a):
        elem_mas.append(list(map(str , input("Enter elements: ").split(','))))
    
    
    command = ' '
    while command != 'x':
        command = menu(title_arr, elem_mas, command)
         

    print_table(title_arr, elem_mas)


       
   


