#   owned exclusively by actors
#   answers requests for checks by defined functions
#   is agnostic of the asker

class AF_Attribute:
    def __init__(self, values, action_functions, name = "unnamed attribute"):
        self.action_functions = action_functions
        self.values = values
        self.name = name

    def enact(self, function_id, **kwargs):
        self.action_functions[function_id](**kwargs)



#   example **kwargs implementation
'''
def example_compete1(x):
    print("example1:", x)

def example_compete2(x,y):
    print("example2:",x,y)

a = AF_Attribute(2,[example_compete1, example_compete2])

a.enact(0,x=a.value)
a.enact(1,x=a.value, y = 4)
'''