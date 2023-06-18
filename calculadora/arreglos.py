import numpy as np

class Vector:
    def __init__(self, coord):
        self.coord = np.array(coord)

    def get_coord(self):
        return self.coord
        
    def nuevo_objeto(self, coord):
        return Vector(coord)

    def __str__(self):
        return str(self.coord)
    
    def __getitem__(self, index):
        return self.coord[index]

    def __add__(self, vector):
        result = self.coord  + vector.coord  
        return self.nuevo_objeto(result)
    
    def __sub__(self, vector):
        result = self.coord - vector.coord
        return self.nuevo_objeto(result)

    def __mul__(self, obj):
        #producto punto, o multiplicacion por escalar
        if type(obj) == Vector:
            result = sum(self.coord * obj.coord)
            return result
        else:
            result = obj*self.coord
        return self.nuevo_objeto(result)
    
    def __rmul__(self, obj):
        return self.__mul__(obj)
    
    def __truediv__(self, escalar):
        result = self.coord / escalar
        return self.nuevo_objeto(result)

