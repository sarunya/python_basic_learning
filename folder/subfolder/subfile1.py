'''
A very simple importable script
'''

def submethod():
  '''
  This helps to learn the import and __name__ varaible
  '''
  print("this is submethod")
  print(f"submethod name is {__name__}")

if __name__ == "__main__":
  submethod()