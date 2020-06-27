"""def my_for(iterable):
     iterator = iter(iterable)
     while True:
          try:
               print(next(iterator))
          except StopIteration:
               break
my_for([2,23,4,5,6])"""


def my_li(iterable,func):
    iterator = iter(iterable)
    while True:
          try:
              thing = next(iterator)
          except StopIteration:
              break
          else:
              func(thing)

def square(x):
     print(pow(x,2))
print(my_li([1,2,3,4,5],square))


