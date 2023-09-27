#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        # self._condition = ""


    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):  
        brand._self = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition
    
 
    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")
   

stan_smith = Shoe("Adidas", 9)
print(stan_smith.brand)
print(stan_smith.size)
print(stan_smith.cobble())
print(stan_smith.condition)

