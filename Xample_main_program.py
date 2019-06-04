# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 12:13:33 2017

@author: JohannesMHeinrich
"""


from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- to use the scheduler for the execution of jobs

import math # ------------------------------------------------------------------------- python math module
import random # ----------------------------------------------------------------------- python random number generator

from time import localtime, strftime # ------------------------------------------------ for the right format of time values
import datetime # --------------------------------------------------------------------- for the monitoring





########################################################################################################
########################################################################################################
########################################################################################################
################                                                            ############################
################               THE MAIN PROGRAMM                            ############################
################                                                            ############################
########################################################################################################
########################################################################################################
########################################################################################################

# starts the scheduler for our program -----------------------------------------------------------------
program_scheduler = QtScheduler()
program_scheduler.start()



class c_program:
    def __init__(self):

        #----- values which are part of the object program and can be accessed easily from the outside -#
        self.add_value_01 = 0.0 # for the addition
        self.add_value_02 = 0.0 # for the addition
        
        self.mult_value_01 = 0.0 # for the multiplication
        self.mult_value_02 = 0.0 # for the multiplication

        # save start time of program
        self.time_start = int(strftime("%Y", localtime())),int(strftime("%m", localtime())),int(strftime("%d", localtime())),int(strftime("%H", localtime())),int(strftime("%M", localtime())),int(strftime("%S", localtime()))
        self.time_start_datetime = datetime.datetime(int(self.time_start[0]),int(self.time_start[1]),int(self.time_start[2]),int(self.time_start[3]),int(self.time_start[4]),int(self.time_start[5]))
        
        # this value will be updated
        self.time_now = int(strftime("%Y", localtime())),int(strftime("%m", localtime())),int(strftime("%d", localtime())),int(strftime("%H", localtime())),int(strftime("%M", localtime())),int(strftime("%S", localtime()))
        
        # lists for the displayed data
        self.random_data_x = []
        self.random_data_y = []
        #-----------------------------------------------------------------------------------------------#




        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        
        #++ scheduled jobs + scheduled jobs + scheduled jobs + scheduled jobs + scheduled jobs +++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
        #++ scheduled job, updates each 0.1 seconds the time self.time_now +++++++++++++++++++++++++++++#          
        program_scheduler.add_job(self.set_time_now, 'interval', seconds=0.1, id='set_time_now_id')
        
        #++ scheduled job, saves each 0.1 seconds a new dataset into self.random_data_x/y ++++++++++++++#
        program_scheduler.add_job(self.generate_random_data, 'interval', seconds=0.1, id='gen_rand_data_id')
        

         
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ FUNCTIONS OF THE MAIN PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    #~~ function: add_two_numbers, takes num1 and num2 and gives sum ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#      
    def add_two_numbers(self,num1,num2):     
        result = num1+num2
        
        return result
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
     
     
    #~~ function: multiply_two_numbers, takes num1 and num2 and gives product ~~~~~~~~~~~~~~~~~~~~~~~~~#
    def multiply_two_numbers(self,num1,num2):
        result = num1*num2
        
        return result
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        

    #~~ function: updates the time saved in self.time_now with the current time ~~~~~~~~~~~~~~~~~~~~~~~#   
    def set_time_now(self):
        
        self.time_now = [int(strftime("%Y", localtime())),int(strftime("%m", localtime())),int(strftime("%d", localtime())),int(strftime("%H", localtime())),int(strftime("%M", localtime())),int(strftime("%S", localtime()))]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function: generates a set of random data when called ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def generate_random_data(self):
        
        timestamp = (datetime.datetime.now() - self.time_start_datetime).total_seconds()
            
        self.random_data_x.append(timestamp)
        
        
        value = math.sin(2*math.pi*(self.time_now[5])*6/360)
        noise = random.random()*0.5 - 0.25
        
        val = float(value+noise)
        
        self.random_data_y.append(val)     
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#