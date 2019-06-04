# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 12:14:27 2017

@author: JohannesMHeinrich
"""


# import python classes --------------------------------------------------------------------------------
import sys # -------------------------------------------------------------------------- import for stuff i guess? i don't really know... 
from PyQt5 import QtCore, QtGui, QtWidgets # ------------------------------------------ imports for the GUI
 
import time # ------------------------------------------------------------------------- time

from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- similar to above

import pyqtgraph as pg # -------------------------------------------------------------- for the plots

# import custom classes --------------------------------------------------------------------------------
from Xample_gui import Ui_Xample_gui # ------------------------------------------------ import the layout generated with QtDesigner
from Xample_main_program import c_program # ------------------------------------------- the program which collects the controll over all the devices



## global style options for the plots -------------------------------------------------------------------
brush_background = (255,255,255,255) #------------------------------------------------- background
brush_red = (212,70,78,255) #---------------------------------------------------------- red for measured values
redPen = pg.mkPen(color=brush_red, width=2) #------------------------------------------ same like brush_red
labelStyle_l = {'color': '#000', 'font-size': '12pt'} #-------------------------------- big label





########################################################################################################
########################################################################################################
########################################################################################################
################                                                            ############################
################       THE WINDOW CLASS                                     ############################
################                                                            ############################
########################################################################################################
########################################################################################################
########################################################################################################



starttime=time.time()
scheduler = QtScheduler()
scheduler.start()


 
class window(Ui_Xample_gui):
    def __init__(self, dialog_A, the_program):
        Ui_Xample_gui.__init__(self)
        self.setupUi(dialog_A)
        
########################################################################################################
########################################################################################################
########################################################################################################
################# the first part of the class sets up the layout of the program.   #####################
################# the PLOTS are placed and the PUSH BUTTONS are connected with the #####################
################# functions which are defined further below in the class           #####################
########################################################################################################
########################################################################################################        
########################################################################################################        
        
        ################################################################################################        
        ### CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB# ##
        ################################################################################################        
        
        #---------------- PLOT for camera temperature -----------------------------------------------------#
        self.plot_random_stuff = pg.PlotWidget(name='PlotRandomStuff')  
        self.plot_random_stuff.setBackground(background=brush_background)
        self.plot_random_stuff.setLabel('left', 'random', **labelStyle_l)   
        self.plot_random_stuff.showGrid(x=True,y=True)
        self.plot_random_stuff.setRange(yRange=(-1.25, 1.25)) 
        self.horizontalLayout_plot_random_stuff.addWidget(self.plot_random_stuff) 
        #--------------------------------------------------------------------------------------------------#

        
        #================ PUSH BUTTONS for camera tab =====================================================#  
        self.pushButton_add.clicked.connect(self.do_addition)
              
        self.pushButton_multiply.clicked.connect(self.do_multiplication)
        #==================================================================================================#
            
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        
        #++ timer + timer + timer + timer + timer + timer + timer + timer + timer + timer + timer ++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#             
        #++ timer for the update of all plots +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#   
        self.timer_t_dependent_plots = QtCore.QTimer()
        self.timer_t_dependent_plots.setInterval(100)
        self.timer_t_dependent_plots.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_t_dependent_plots.timeout.connect(self.t_dependent_updates)
        self.timer_t_dependent_plots.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ the second part of the class contains all the FUNCTIONS which are  ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ triggerered when the different push buttons are pressed. there are ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ more functions dedicated to permanet monitoring and backgroundjobs ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    def do_addition(self):
        the_program.add_value_01 = self.doubleSpinBox_add_01.value()
        the_program.add_value_02 = self.doubleSpinBox_add_02.value()
        
        res = the_program.add_two_numbers(the_program.add_value_01,the_program.add_value_02)
        
        self.label_result_1.setText(str(res))
        

  
    def do_multiplication(self):
        the_program.mult_value_01 = self.doubleSpinBox_mult_01.value()
        the_program.mult_value_02 = self.doubleSpinBox_mult_02.value()
        
        res = the_program.multiply_two_numbers(the_program.mult_value_01,the_program.mult_value_02)
        
        self.label_result_2.setText(str(res))



    def t_dependent_updates(self):
        
        hours = the_program.time_now[3]
        minutes = "{:02d}".format(the_program.time_now[4])
        seconds = "{:02d}".format(the_program.time_now[5])
        
        self.label_time.setText(str(hours) + ":" + str(minutes) + ":" + str(seconds))

        self.plot_of_randomnes = self.plot_random_stuff.plot(the_program.random_data_x,the_program.random_data_y, pen=redPen, symbol='o', symbolBrush = brush_red, name = 'pressure', clear = True)
        
        
        
        
        
########################################################################################################
########################################################################################################
########################################################################################################
################                                                             ###########################
################        STARTING THE MAIN LOOP                               ###########################
################                                                             ###########################
########################################################################################################
########################################################################################################
########################################################################################################



if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    # create instance of parameters 
    the_program = c_program()
        
    # set up window   
    dialog_sequ = QtWidgets.QMainWindow()
    prog_sequ = window(dialog_sequ,the_program)    
    dialog_sequ.show()

 
    sys.exit(app.exec_())
