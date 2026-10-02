from typing import List

def read_integers() -> List[int]:
    read_line = input()
    list_of_integers = read_line.split(",")
    return [int(i) for i in list_of_integers]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
