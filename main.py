import numpy as np

effort_list = ['hunting','workout','picnic','dating','charity','sitdown','fishing','battleW','battleL','killing']
exp_list    = [15,15,15,15,15,15,15,15,15,15]
effort_point = [
    [ 0, 1, 0, 2, 2, 0, 1, 1, 1],
    [ 0, 2,-1, 2, 1,-1, 2, 0,-1],
    [ 3, 1, 2, 3,-2,-2, 0,-1, 0],
    [ 0, 0, 2, 0, 0, 1, 3, 2, 0],
    [ 0, 0, 1, 1, 0, 2, 0, 2, 3],
    [ 1,-1, 1,-1, 0, 0, 1, 3, 0],
    [ 1, 2, 0, 1, 0, 3, 0, 0, 0],
    [ 0, 2, 1, 1, 2, 0, 1, 0, 0],
    [ 3,-1, 3, 1, 0, 1, 0, 2, 1],
    [-1, 3,-1,-1, 2,-1, 2, 0,-1]]

class character:
    def __init__(self,val_base,val_start,val_extra):
        self.totalexp = 0
        self.level = 1
        self.efforts=[0,0,0,0,0,0,0,0,0]
        self.base=val_base
        self.status=val_start
        self.extra=val_extra

    def show(self):
        result = np.sum([self.status, self.extra], axis = 0).tolist()
        print("Level\t:", self.level, ", Exp :", self.totalexp)
        print("status\t:", result)
        print("effort\t:", self.efforts)

    def action(self, dowhat : str, times=1):
        for i in range(times):
            # get efforts
            index=effort_list.index(dowhat)
            effort = effort_point[index]
            if(dowhat == "workout"):
                if (self.status[0] < self.status[6]*10):
                    effort[status.index(max(status[1:8]))] = 4
                else:
                    effort[0] = 4
            # add efforts
            self.efforts = np.sum([self.efforts, effort], axis = 0).tolist()
            # add to totalexp
            self.totalexp += exp_list[index]
            # self.level_check()

    def action_effort(self, dowhat):
        
        return [0,0,0,0,0,0,0,0,0]

    def level_check(self):
        if(leveluped):
			# calculate val
			# add val to status
            if(self.level<70):
                self.level+=1
            self.efforts=0


val_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1] # 基礎值
val_start  = [350, 38, 33, 30, 25, 20, 32, 25, 20] # 初始值
val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,121] # 額外值
example    = [100, 10, 10, 10, 10, 10,102,104, 10]

kirito = character(val_base, val_start, val_extra)

kirito.show() 

kirito.action('hunting', 5)

kirito.show() 