import random
import numpy as np

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
    def brain(self):
        activation = lambda x : np.tanh(x) #activation function
        h1 = activation(np.dot(self.wih,self.r_food)) # hidden layer
        out = activation(np.dot(self.who,h1)) # output

        #Updating dv and dr with MLP response
        self.nn_dv = float(out[0]) # velocity change
        self.nn_dr = float(out[1]) # rotation change

    #Update heading
    def update_r(self,setting):
        self.r += self.nn_dr * setting['dr_max']*setting['dt']
        self.r = self.r % 360
        return self.r
            
    #Update velocity
    def update_velocity(self,setting):
        self.v+=self.nn_dv*setting['dv_max']*setting['dt']               
        if self.v < 0: 
            self.v = 0
        if self.v>setting['v_max']:
            self.v = setting['v_max']

    #Update position
    def update_position(self,setting):
        dx += self.v * np.cos(self.r*np.pi/180) * setting['dt']
        dy += self.v * np.sin(self.r*np.pi/180) * setting['dt']
        self.x+=dx
        self.y+=dy

class food():
    def __init__(self, settings):
        self.x = random.uniform(settings['x_min'], settings['x_max'])
        self.y = random.uniform(settings['y_min'], settings['y_max'])
        self.energy = 1

    def respawn(self,settings):
        self.x = random.uniform(settings['x_min'], settings['x_max'])
        self.y = random.uniform(settings['y_min'], settings['y_max'])
        self.energy = 1


            
