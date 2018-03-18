
# -*- coding: UTF-8 -*-
'''
Created on 2018年03月19日
@author: banrieen
'''


class People:

    def __init__(self,people_name,people_age):
        self.name = people_name
        self.age = people_age

    def getName(self):
        return self.name
    def getName(self):
        return self.age

def HiHello():
    print ("Hello ,It is a fine !")

if __name__ == '__main__':
    people_name = input("Please input the people`s name: ")
    people_age = input("Please input the people`s age (int): ")

    P = People(people_name,people_age)
    print(P.getName, P.getAge())
