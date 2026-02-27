def func1(arg):
    print(f'arg = {arg}')
    def func2():
        arg()

    return func2
@func1
class sample:
    def __init__(self):
        print('Inside Constructor')
print(f'sample = {sample}')
obj1 = sample()
obj2 = sample()



# The control flow will be 
# @func1 decorator will take sample class address to arg of func1 --> func1(sample)

#then print arg and return func2 to class sample                     arg = <class '__main__.sample'>
# now class sample has func2                                         sample = <function func1.<locals>.func2 at 0x0000027BDA078860>
# sample is printed which has func2 so address of func2 printed     
#when we create obj1 = sample() it calls the fuc2 as sample has func2
# inside function2 arg() it contains sample location so sample class called
# contructor will be called and Inside constructor printed 
# same process for obj2