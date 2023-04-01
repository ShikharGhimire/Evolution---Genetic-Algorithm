import random

class organism():
    def __init__(self,setting,wih = None,who = None,name = None):
        self.x = random.uniform(setting['x_min'],setting['x_max']) # x position
        self.y = random.uniform(setting['y_min'],setting['y_max']) # y position

        self.r  = random.uniform(0,360) # rotation
        self.v = random.uniform(0,setting['v_max']) # velocity
        self.dv = random.uniform(-setting['dv_max'],setting['dv_max']) # velocity change

        self.d_food = 1000 # distance to food
        self.r_food = 0 # angle to food
        self.fitness = 0 # fitness

        self.wih = wih # input to hidden weights
        self.who = who # hidden to output weights

        self.name = name # name of organism


        #Neural Network

