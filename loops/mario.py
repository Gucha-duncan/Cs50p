def main():
    print_column(5)
    print_row(7)
    
    
def print_row(width):
     for _ in range (width):
         print('#', end='')

def print_column(height):
     for _ in range (height):
         print('# \n', end='')
    
main()