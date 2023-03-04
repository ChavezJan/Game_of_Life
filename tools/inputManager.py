"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
def inputManager(e,expected):
    try:
        if(e in expected):
            return e
    except AssertionError:
        print("ERROR: The input is different")
        exit()