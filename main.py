import numpy as np
import math
import pygal
from pygal.style import Style

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
        self.float=[0,0,0,0,0,0,0,0,0]

    def show(self, show:bool=True):
        result=[0,0,0,0,0,0,0,0,0]
        for i in range(9):
            if (i == 0):
                result[i] = self.status[i] + self.extra[i]*10 + self.float[i]*10
            else:
                result[i] = self.status[i] + self.extra[i] + self.float[i]

        if show :
            print("Level\t:", self.level, ", TotalExp :", self.totalexp)
            print("extra\t:", self.extra)
            print("float\t:", self.float)
            print("status\t:", result)
            print("efforts\t:", self.efforts)

        return result

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
            ### update level & add status
            self.level_update()
            if self.level >= 70:
                break

    def level_update(self):
        while self.totalexp >= leveling_exp_list[self.level]:
            ### base point
            self.status = np.sum([self.status, self.base], axis = 0).tolist()
            ### getting floatpoint? 
            point_add=self.floating_point_gain()
			### floating point calculation
            if point_add!=0:
                float_neg = self.floating_point_sub()
                point_sub=0
                for i in range(9):
                    if float_neg[i]<0:
                        point_sub+=float_neg[i]
                float_pos = self.floating_point_add(point_add - point_sub)
                float_sum = [0,0,0,0,0,0,0,0,0]
                for i in range(9):
                    if self.efforts[i]>0:
                        float_sum[i]=float_pos[i]
                    else:
                        float_sum[i]=float_neg[i]
                ### add to float
                # print('level:', self.level, point_add-point_sub, self.efforts, float_pos, float_neg, float_sum)
                self.float = np.sum([self.float, float_sum], axis = 0).tolist()
            ### reset efforts & update level at the end of this function
            self.efforts=[0,0,0,0,0,0,0,0,0]
            self.level+=1
            if self.level >= 70:
                break

    def floating_point_gain(self):
        currentlevel=self.level
        finishlevel=currentlevel+1
        point_gain = math.trunc((finishlevel+1)/7) * (finishlevel+1-math.trunc((finishlevel+1)/7)*7/2-7/2) - math.trunc((currentlevel+1)/7) * (currentlevel+1-math.trunc((currentlevel+1)/7)*7/2-7/2)
        return point_gain

    def floating_point_sub(self):
        float_sum=[0,0,0,0,0,0,0,0,0]
        currentlevel=self.level
        finishlevel=currentlevel+1
        levelupped=finishlevel-currentlevel
        tmpa = 6-currentlevel if(6-currentlevel>0) else 0
        tmpb = 6-finishlevel if(6-finishlevel>0) else 0
        unsubbale= tmpa-tmpb
        for i in range(9):
            if(i==0):
                if(math.trunc(self.efforts[i]/10)+self.base[i]*levelupped > unsubbale*self.base[i]):
                    float_sum[i] = math.trunc(self.efforts[i]/10)
                else:
                    float_sum[i] = (unsubbale-levelupped)*math.trunc(self.base[i]/10)
            else:
                if(math.trunc(self.efforts[i]/10)+self.base[i] > unsubbale*self.base[i]):
                    float_sum[i] = math.trunc(self.efforts[i]/10)
                else:
                    float_sum[i] = unsubbale*self.base[i] - self.base[i]
        return float_sum

    def floating_point_add(self, point:int):
        inttable=[[]]
        logtable=[[]]
        sumtable=[[]]
        float_sum=[0,0,0,0,0,0,0,0,0]
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
            ### recore sum of float point
            if(point+0.5>j):
                sumtable.append(result_effort)
                float_sum = np.sum([float_sum, result_effort], axis = 0).tolist()
        ### sum of the inttable
        return float_sum

    def radar_chart(self,max:int=500):
        ### get vals
        feature=['攻擊', '防禦', '體力', '敏捷', '反應', '技巧', '智力', '幸運']
        result_sum=[0,0,0,0,0,0,0,0]
        result_default=[0,0,0,0,0,0,0,0]
        result_float=[0,0,0,0,0,0,0,0]
        result_hp = self.status[0] + self.extra[0]*10 + self.float[0]*10
        for i in range(8):
            result_sum[i] = self.status[i+1] + self.float[i+1] + self.extra[i+1]
            result_float[i] = self.status[i+1] + self.float[i+1] 
            result_default[i] = self.status[i+1]

        ### setting up the radar_chart
        custom_style = Style(
            background='white',
            plot_background='white',
            foreground='#000000',
            foreground_strong='#000000',
            foreground_subtle='#630C0D',
            colors=('#0800E8CC', '#9BC850CC', '#FAB243CC', '#404040CC', '#E853A0CC', '#E8537ACC')
        )
        radar_chart = pygal.Radar(fill = True, range=(0,max), style=custom_style)
        radar_chart.title = 'HP:' + str(result_hp) + '=' + str(self.status[0]) + '+' + str(self.float[0]*10) + '+' + str(self.extra[0]*10)
        radar_chart.x_labels = feature

        ### draw
        radar_chart.add('sum', result_sum)
        radar_chart.add('float', result_float)
        radar_chart.add('default', result_default)

        ### save
        radar_chart.render_to_file('radar_chart.svg')


def ut_kirito_sitdown_1400():
    ### initial
    val_base   = [ 25,  3,  2,  2,  3,  6,  2,  1,  1]
    val_start  = [250, 27, 22, 23, 35, 42, 30, 25, 15]
    val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,121]
    kirito = character(val_base, val_start, val_extra)

    ### actions & calculate result
    kirito.action('sitdown', 1400)
    result=kirito.show(False)
    
    ### assert result
    assert result == [2255, 84,182,51,182,336,179,204,185], 'kirito sitdown to 50 level calculation failed'

def ut_xmascirika_charity_300():
    ### initial
    val_base   = [ 55,  1,  3,  3,  3,  2,  3,  1,  5] # 基礎值
    val_start  = [450, 12, 28, 30, 32, 25, 20, 25, 35] # 初始值
    val_extra  = [  0,  0,  0,  0,  0,  0,  0,  0,121] # 額外值
    xmascirika = character(val_base, val_start, val_extra)

    ### actions & calculate result
    xmascirika.action('charity',300)
    result=xmascirika.show(False)

    ### assert result
    assert result == [1825, 37, 103, 105, 107, 88, 95, 56, 301], 'kirito charity to 26 level calculation failed'

def unittest():
    ut_kirito_sitdown_1400()
    ut_xmascirika_charity_300()


### start your kirito here
if __name__ == "__main__":
    print("リンクスタート！")
    unittest()