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
            ### base point
            self.status = np.sum([self.status, self.base], axis = 0).tolist()
            ### getting floatpoint? 
            point=self.floating_point_gain()
			### floating point calculation
            if(point!=0):
                self.floating_point(point)
			### add val to status
            ### reset efforts & update level
            self.efforts=[0,0,0,0,0,0,0,0,0]
            self.level+=1

    def floating_point_gain(self):
        currentlevel=self.level
        finishlevel=currentlevel+1
        point_gain = math.floor((finishlevel+1)/7) * (finishlevel+1-math.floor((finishlevel+1)/7)*7/2-7/2) - math.floor((currentlevel+1)/7) * (currentlevel+1-math.floor((currentlevel+1)/7)*7/2-7/2)
        return point_gain

    def floating_point(self, point:int):
        inttable=[[]]
        logtable=[[]]
        for j in range(1,400):
            log2efforts=[0,0,0,0,0,0,0,0,0]
            tmp_efforts=[0,0,0,0,0,0,0,0,0]
            for i in range(9):
                if(j==1):
                    if(self.efforts[i] > 0):
                        log2efforts[i] = math.log2(self.efforts[i])
                    else:
                        log2efforts[i] = -9999
                else:
                    log2efforts[i] = logtable[j-1][i] - inttable[j-1][i]
            ### append logtable
            logtable.append(log2efforts)
            ### sub the max val
            result_effort=[0,0,0,0,0,0,0,0,0]
            for i in range(9):
                tmp_efforts[i] = max(log2efforts)-log2efforts[i]
            ### hp
            if(tmp_efforts[0]>0):
                result_effort[0]=0
            elif(tmp_efforts[0]==0):
                result_effort[0]=1
            ### atk
            if(tmp_efforts[0]==0):
                result_effort[1]=0
            else:
                if(tmp_efforts[1]>0):result_effort[1]=0
                else:result_effort[1]=1
            ### dfs
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0):
                result_effort[2]=0
            else:
                if(tmp_efforts[2]>0):result_effort[2]=0
                else:result_effort[2]=1
            ### str
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0):
                result_effort[3]=0
            else:
                if(tmp_efforts[3]>0):result_effort[3]=0
                else:result_effort[3]=1
            ### dex
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0 or tmp_efforts[3]==0):
                result_effort[4]=0
            else:
                if(tmp_efforts[4]>0):result_effort[4]=0
                else:result_effort[4]=1
            ### rac
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0 or tmp_efforts[3]==0 or tmp_efforts[4]==0):
                result_effort[5]=0
            else:
                if(tmp_efforts[5]>0):result_effort[5]=0
                else:result_effort[5]=1
            ### skl
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0 or tmp_efforts[3]==0 or tmp_efforts[4]==0 or tmp_efforts[5]==0):
                result_effort[6]=0
            else:
                if(tmp_efforts[6]>0):result_effort[6]=0
                else:result_effort[6]=1
            ### int
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0 or tmp_efforts[3]==0 or tmp_efforts[4]==0 or tmp_efforts[5]==0 or tmp_efforts[6]==0):
                result_effort[7]=0
            else:
                if(tmp_efforts[7]>0):result_effort[7]=0
                else:result_effort[7]=1
            ### luk
            if(tmp_efforts[0]==0 or tmp_efforts[1]==0 or tmp_efforts[2]==0 or tmp_efforts[3]==0 or tmp_efforts[4]==0 or tmp_efforts[5]==0 or tmp_efforts[6]==0 or tmp_efforts[7]==0):
                result_effort[8]=0
            else:
                if(tmp_efforts[8]>0):result_effort[8]=0
                else:result_effort[8]=1
            ### append to inttable
            inttable.append(result_effort)
        ### sum of the inttable






### initail your kirito
val_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1] # 基礎值
val_start  = [350, 38, 33, 30, 25, 20, 32, 25, 20] # 初始值
val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,  0] # 額外值

kirito = character(val_base, val_start, val_extra)

kirito.show() 


# ### start your kirito
# kirito.action('workout', 18)

# kirito.show() 

### test level 6 to 7
kirito.level=6
kirito.totalexp = 245
kirito.action('workout', 1)
kirito.show()