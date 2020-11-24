import _CORE as c
import random as r

class F_Attribute(c.AF_Attribute):
    def __init__(self,values, functions, _id):
        super().__init__(values = values,action_functions=functions, id = _id)

    def basic_check(self, index_of_value):
        if self.values[index_of_value] < 1:
            return c.E.INVALID_INTERACTION
        roll = r.randint(1,6)
        ret = 0
        for i in range(self.values[index_of_value]):
            if roll > 4:
                ret+=1
        return True, ret


'''
a = F_Attribute([1],[F_Attribute.basic_check])
b = F_Attribute([1],[F_Attribute.basic_check])
print(a.action_functions[0](b))
#print(a.enact(0))
'''