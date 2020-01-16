from datetime import timedelta, date, datetime
import os

import matplotlib

import matplotlib.pyplot as plt
import util.util as utility, util.fileutils as fileutils


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

        
def _plot_graph_(resultsDir, file1, file2):
    requestData = utility._results_compare_plot_(resultsDir, file1, file2)
    dates = utility._get_today_yesterday_dates_()    
    files_path = [x for x in os.listdir(resultsDir) if x.endswith(".json")]
    fileutils.write_data(resultsDir + "/requests_" + dates[0] + "_" + dates[1] + "_compared_results.json", requestData)
    file_path = resultsDir + "/requests_" + dates[0] + "_" + dates[1] + "_compared_results.json"
    # #print(" file path ",file_path)
    isrequest = utility.isrequest_type(file1)
    mydictionary = fileutils._read_json_data_(file_path)
    xaxis = []
    yaxis_total = []
    yaxis_requests = []
    yaxis_failures = []
    # myDic = SortedDict(mydictionary)
    for key in mydictionary:
        # #print( "key: %s , value: %s" % (key, mydictionary[key]))
        value = mydictionary[key]
        xaxis.append(key)
        for k, v in value.items():
            # #print("k= ",k,"value = ",v)
            if k == "total" :
                yaxis_total.append(v)
            elif k == "requests":
                yaxis_requests.append(v)
                # #print("k.find('requests')" , yaxis_total)
            elif k == "failures":
                yaxis_failures.append(v)
                # #print("k.find('failres')" , yaxis_total)
    # find last 7 days in the xaxis
    #xaxis.sort()
    #yaxis_total.sort()
    #yaxis_requests.sort()
    #yaxis_failures.sort()
    
    start_dt = datetime.strptime(xaxis[-1], '%Y-%m-%d').date()
    # print(start_dt)
    last7days = start_dt - timedelta(days=7)
    # print(last7days) 
    end_dt = last7days
    end_dt = datetime.strptime(last7days.strftime("%Y-%m-%d"), '%Y-%m-%d').date()
    plt.figure(num='HDS Volume Testing Metrics')
    # plt.plot(xaxis,yaxis_total)
    plt.plot(xaxis, yaxis_requests)
    plt.plot(xaxis, yaxis_failures)
    # plt.gca().set_color_cycle(['blue','green','yellow'])
    # plt.legend(['Total Requests','Passed','Failures'], loc='upper right')
    plt.legend(['Passed', 'Failures'], loc='upper right')
    plt.xlabel('Date')
    plt.ylabel('No. of Requests')
    # plt.title('Date Vs Volumetric Tests')
    plt.grid(True)
    plt.suptitle("Volume Test")    
    plt.show()
    
    
if __name__ == '__main__':
    file1 = "imnresults_2018-09-19_requests.csv"
    file2 = "imnresults_2018-09-18_requests.csv"
    # print(_plot_graph_("../output/",file1,file2))

