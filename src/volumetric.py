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
    print("Executed successfully")
    
    # results compare by two dates data
    dates = utility._get_today_yesterday_dates_()    
    file1 = resultfileprefix + dates[0] + "_requests.csv"
    file2 = resultfileprefix + dates[1] + "_requests.csv"
    # print(file1 , file2)
    requestData = utility._result_compare_(resultsDir, file1, file2)
    fileutils.write_data(resultsDir + "/requests_" + dates[0] + "_" + dates[1] + "_compared_results.json", requestData)
    
    
    try: 
        plotgraph._plot_graph_(resultsDir, file1, file2)
    except Exception as e:
        print(" Exception occurred while plotting : " + str(e))
    
if __name__ == "__main__":
    main()