class effort:
    status  = ['hp','atk','dfs','str','dex','rac','skl','int','luk']
    def __init__(self, action, multiper):
        self.action = action

class action:
    hunting = [ 0, 1, 0, 2, 2, 0, 1, 1, 1]
    workout = [ 0, 2,-1, 2, 1,-1, 2, 0,-1] # base line, set to 4 based on status
    picnic  = [ 3, 1, 2, 3,-2,-2, 0,-1, 0]
    dating  = [ 0, 0, 2, 0, 0, 1, 3, 2, 0]
    charity = [ 0, 0, 1, 1, 0, 2, 0, 2, 3]
    sitdown = [ 1,-1, 1,-1, 0, 0, 1, 3, 0]
    fishing = [ 1, 2, 0, 1, 0, 3, 0, 0, 0]
    battleW = [ 0, 2, 1, 1, 2, 0, 1, 0, 0]
    battleL = [ 3,-1, 3, 1, 0, 1, 0, 2, 1]
    killW   = [-1, 3,-1,-1, 2,-1, 2, 0,-1]

    def __init__(self, status):
        if (status[0] < 10*status[6]):
            self.workout[status.index(max(status[1:8]))] = 4
        else:
            self.workout[0] = 4

kirito = [100,10,10,10,10,10,102,1002,10]

efforts = action(kirito).workout

print(efforts)