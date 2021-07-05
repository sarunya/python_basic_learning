'''
A very simple main script
'''

from subfolder import subfile1

def mainmethod():
    '''
    A very simple main method
    '''
    print("this is main method")
    print(f"main method name is {__name__}")
    subfile1.submethod()

mainmethod()
