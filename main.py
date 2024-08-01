import numpy as np
import math

action_list = ['hunting','workout','picnic','dating','charity','sitdown','fishing','battleW','battleL','killing']
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
leveling_exp_list = [0, 30, 60, 100, 150, 200, 250, 300, 370, 450, 500, 650, 800, 950, 1200, 1450, 1700, 1950, 2200, 2500, 2800, 3100, 3400, 3700, 4000, 4400, 4800, 5200, 5600, 6000, 6500, 7000, 7500, 8000, 8500, 9100, 9700, 10300, 11000, 11800, 12600, 13500, 14400, 15300, 16200, 17100, 18000, 19000, 20000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000, 37000, 39000, 41000, 44000, 47000, 50000, 53000, 56000, 59000, 62000, 65000, 68000, 71000]

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
        print("Level\t:", self.level, ", TotalExp :", self.totalexp)
        print("status\t:", result)
        print("effort\t:", self.efforts)

    def action(self, dowhat : str, times=1):
        for i in range(times):
            ### get efforts
            index=action_list.index(dowhat)
            effort = effort_point[index]
            if(dowhat == "workout"):
                if (self.status[0] < self.status[6]*10):
                    effort[self.status.index(max(self.status[1:8]))] = 4
                else:
                    effort[0] = 4
            ### add efforts
            self.efforts = np.sum([self.efforts, effort], axis = 0).tolist()
            ### add to totalexp
            self.totalexp += exp_list[index]
            ###
            self.level_update()

    def level_update(self):
        while(self.totalexp >= leveling_exp_list[self.level] and self.level < 70):
            print('level up')
            self.level+=1
            ### base point
            self.status = np.sum([self.status, self.base], axis = 0).tolist()
			### floating point
            self.floating_point()
			### add val to status
            ### clean efforts
            self.efforts=[0,0,0,0,0,0,0,0,0]

    def floating_point(self):
        self.logtable()

    def logtable(self):
        bigtable=[]
        log2efforts=[0,0,0,0,0,0,0,0,0]
        log_efforts=[0,0,0,0,0,0,0,0,0]
        for j in range(1,400):
            for i in range(8):
                if(self.efforts[i] > 0):
                    log2efforts[i] = math.log2(self.efforts[i])
                else:
                    log2efforts[i] = -9999
            ### sub the max val
            result=[0,0,0,0,0,0,0,0,0]
            for i in range(8):
                log_efforts[i] = max(log2efforts)-log2efforts[i]
            ### hp
            if(log_efforts[0]>0):
                result[0]=0
            elif(log_efforts[0]==0):
                result[0]=1
            ### atk
            if(log_efforts[0]==0):
                result[1]=0
            else:
                if(log_efforts[1]>0):result[1]=0
                else:result[1]=1
            ### dfs
            if(log_efforts[0]==0 or log_efforts[1]==0):
                result[2]=0
            else:
                if(log_efforts[2]>0):result[2]=0
                else:result[2]=1
            ### str
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0):
                result[3]=0
            else:
                if(log_efforts[3]>0):result[3]=0
                else:result[3]=1
            ### dex
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0 or log_efforts[3]==0):
                result[4]=0
            else:
                if(log_efforts[4]>0):result[4]=0
                else:result[4]=1
            ### rac
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0 or log_efforts[3]==0 or log_efforts[4]==0):
                result[5]=0
            else:
                if(log_efforts[5]>0):result[5]=0
                else:result[5]=1
            ### skl
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0 or log_efforts[3]==0 or log_efforts[4]==0 or log_efforts[5]==0):
                result[6]=0
            else:
                if(log_efforts[6]>0):result[6]=0
                else:result[6]=1
            ### int
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0 or log_efforts[3]==0 or log_efforts[4]==0 or log_efforts[5]==0 or log_efforts[6]==0):
                result[7]=0
            else:
                if(log_efforts[7]>0):result[7]=0
                else:result[7]=1
            ### luk
            if(log_efforts[0]==0 or log_efforts[1]==0 or log_efforts[2]==0 or log_efforts[3]==0 or log_efforts[4]==0 or log_efforts[5]==0 or log_efforts[6]==0 or log_efforts[7]==0):
                result[8]=0
            else:
                if(log_efforts[8]>0):result[8]=0
                else:result[8]=1
            ### append to bigtable
            print(result)
            # bigtable = np.append()






### initail your kirito
val_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1] # 基礎值
val_start  = [350, 38, 33, 30, 25, 20, 32, 25, 20] # 初始值
val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,  0] # 額外值

kirito = character(val_base, val_start, val_extra)

kirito.show() 


### start your kirito
kirito.action('workout', 10)

kirito.show() 