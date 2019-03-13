import configparser
import cowsay
import os
import numpy as np
paramfile = "data_param.ini"
if not os.path.isfile(paramfile):
    cowsay.cow(paramfile + ' does not exist \n quitting now \n dumbass')
    quit()
Config = configparser.ConfigParser()
# cowsay.cow(Config.sections())
print(np.tile(tuple(range(3))),5)