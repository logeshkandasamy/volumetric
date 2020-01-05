#!/usr/bin/python
import os
import sys
import time
import plot.volumetricplotgraph as plotgraph
from util.constants import *
import util.fileutils as fileutils
import util.util as utility
from util.readconfig import read_config

def today():
    print('yes ')

def main():
    print(" results directory is ", resultsDir)
    #payerresult.non_recursive_iteration()
    path = os.path.dirname(os.path.realpath(__file__))
    
    # print(path)  
    
    # By Default ,we are running the tests daily.
    #timestr = time.strftime("%Y%m%d")
    
    timestr = time.strftime("%Y-%m-%d_%H_%M")
    
    if(timeframe == 'daily'):
        timestr = time.strftime(csvresultfileformat)
        print('Todays file name is ', resultfileprefix + timestr)
        
    if(timeframe == 'hourly'):
        print('hourly')
        timestr = time.strftime("%Y%m%d-%H%M%S")
    
    if not os.path.exists(resultsDir):
        os.makedirs(resultsDir)
    logOutputDirectory="../log"
    if not os.path.exists(logOutputDirectory):
        os.makedirs(logOutputDirectory)
    
    #os.system("locust -f locust.py --host=http://localhost:8080  --csv=sample  --no-web -c 100 -r 1 -t 1m  ")
    
    #host="http://localhost:8080"
    os.system("locust -f locust.py --host=" + host + " --csv=" + resultsDir + resultfileprefix + timestr + " --no-web -c " + locustusers + " -r " + locusthatchrate + " -t " + runtime + "  --only-summary > ../log/locustTest.log ")
    
    
if __name__ == "__main__":
    main()