import sys
import random
import os
import getopt
import csv
import glob
import time
import subprocess


def check_path():
    if os.path.exists('/usr/local/bin/obabel') == False:
        error_obabel_path = '''
        Sorry, Dockpipes requires that you have Dockpipes installed in your PATH.
        To do so you can go here: https://openbabel.org/docs/dev/Installation/install.html
        You can then verify if it is installed by entering obabel -h
        '''
        sys.exit(error_obabel_path)


WD = '/Users/Alexis/PycharmProjects/First/'
WD_CSV = '/Users/Alexis/PycharmProjects/First/*csv'

check_path()

argv = sys.argv[1:]
    #print(argv)

try:
        opts, args = getopt.getopt(argv, "f:g:h")
        #print(opts)
except getopt.GetoptError as err:
        print()
        opts = []

input_file = None
output_file = None

for opt, arg in opts:
        if opt in ['-g']:
            header_a = '''
                ====================================================
                Here are the interesting CSV  file in your directory
                ====================================================
                
                '''
            header_b = '''
            
                ====================================================
                '''
            print(header_a)
        for filename in glob.glob(arg):
                print(filename)
                print(header_b)
        if opt in ['-h']:
                help = '''
                        /$$$$$$$                      /$$       /$$$$$$$  /$$                              
                       | $$__  $$                    | $$      | $$__  $$|__/                              
                       | $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$| $$  \ $$ /$$  /$$$$$$   /$$$$$$   /$$$$$$$
                       | $$  | $$ /$$__  $$ /$$_____/| $$  /$$/| $$$$$$$/| $$ /$$__  $$ /$$__  $$ /$$_____/
                       | $$  | $$| $$  \ $$| $$      | $$$$$$/ | $$____/ | $$| $$  \ $$| $$$$$$$$|  $$$$$$ 
                       | $$  | $$| $$  | $$| $$      | $$_  $$ | $$      | $$| $$  | $$| $$_____/ \____  $$
                       | $$$$$$$/|  $$$$$$/|  $$$$$$$| $$ \  $$| $$      | $$| $$$$$$$/|  $$$$$$$ /$$$$$$$/
                       |_______/  \______/  \_______/|__/  \__/|__/      |__/| $$____/  \_______/|_______/                                                         
                                                                             | $$                          
                                                                             |__/                          
                                                                                    
                       
                       Arguments
                       
                       -f <foo> : function will find the relevant files in the current directory
                       
                       -h       : shows this help page                                                           
                                                                               
                '''
                print(help)
        if opt in ['-f']:
                 if os.path.isfile(args):
                     input_file = args
                 else:
                     err = '''
                     Your file seems to be inaccessible for DockPipes.
                     Please very that it is in the current directory
                     if not use the option -f to find it.
                     '''
                     print(err)
        if opt in  ['-o']:
                 output_file = args

