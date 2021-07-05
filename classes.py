class SampleClass():

  ##class object attribute
  # same for all objects
  constval = "CONSTANT"

  def __init__(self, arr=[]):
    self.arr = arr

  def push(self, val):
    self.arr.append(val)

  def pop(self):
    print(self.arr.pop())

  def peek(self):
    if len(self.arr)==0:
      print("Peek not possible")
    else:
      print(self.arr[len(self.arr)-1])
  


sample = SampleClass([1])
sample.push(5)
sample.peek()
sample.push(1)
sample.peek()
sample.push(2)
sample.peek()
sample.push(3)
sample.peek()
sample.push(6)
sample.pop()
sample.peek()
print(SampleClass.constval)
print(sample.constval)
SampleClass.constval = "sarunya"
print(SampleClass.constval)
print(f"{sample.constval} is sample")