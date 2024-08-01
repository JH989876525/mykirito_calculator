import numpy as np

class status:
    def __init__(self, start):
        self.summary = start

    def __call__(self, addon):
        self.summary = np.sum([self.summary, addon], axis = 0).tolist()

class effort:
    def __init__(self):
        self.summary = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def __call__(self, addon):
        self.summary = np.sum([self.summary, addon], axis = 0).tolist()

class action:
    hunting = [ 0, 1, 0, 2, 2, 0, 1, 1, 1]
    workout = [ 0, 2,-1, 2, 1,-1, 2, 0,-1] # base line, changed base on status
    picnic  = [ 3, 1, 2, 3,-2,-2, 0,-1, 0]
    dating  = [ 0, 0, 2, 0, 0, 1, 3, 2, 0]
    charity = [ 0, 0, 1, 1, 0, 2, 0, 2, 3]
    sitdown = [ 1,-1, 1,-1, 0, 0, 1, 3, 0]
    fishing = [ 1, 2, 0, 1, 0, 3, 0, 0, 0]
    battleW = [ 0, 2, 1, 1, 2, 0, 1, 0, 0]
    battleL = [ 3,-1, 3, 1, 0, 1, 0, 2, 1]
    killing = [-1, 3,-1,-1, 2,-1, 2, 0,-1]

    def __init__(self, status):
        if (status[0] < 10*status[6]):
            self.workout[status.index(max(status[1:8]))] = 4
        else:
            self.workout[0] = 4

class character:
    def __init__(self, base, extra):
        self.status = status(base)
        self.extra = extra
        self.effort = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def show(self):
        print("effort\t:", self.effort)
        print("status\t:", self.status.summary)
        print("extra\t:", self.extra)
        self.result = np.sum([self.status.summary, self.extra], axis = 0).tolist()
        print("summary\t:", self.result)

    def action(self, action, times):
        for i in range(times):
            print('aa')


list_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1] # 基礎值
list_start  = [350, 38, 33, 30, 25, 20, 32, 25, 20] # 初始值
list_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,121] # 額外值
list_exp    = [100, 10, 10, 10, 10, 10,102,104, 10]

kirito = character(list_start, list_extra) # create a character

kirito.show() # show character status
