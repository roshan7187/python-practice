#Lambda -->   lambda arguments : operations

#eg. 
var = lambda a, b : a + b
print(var(5, 10)) #15



# map() --> map(function, iterable/range) // 
# map() function applies a given function to each item of an iterable (list, tuple or range) 
# and returns a map object (which is an iterator).

#function can be a lambda function or a regular function defined using def or any built-in function.

#eg.
def square(x):
    return x ** 2
mapobject = map(square, range(1,6))
print(list(mapobject)) #[1, 4, 9, 16, 25]
print(mapobject) #<map object at 0x000001B2C9F8B430>

#filter() --> filter(function, iterable/range) //
# filter() function constructs an iterator from elements of an iterable for which a function returns true.


