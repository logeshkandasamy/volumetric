import csv, os
import datetime

from util.constants import *
import util.fileutils as fileutils


def _get_today_yesterday_dates_():
    # folder = "E:\writable\Results\Results3"
    # listOfFiles = os.listdir(folder)
    today = str(datetime.date.today())
    yesterday = str(datetime.date.today() + datetime.timedelta(days=-1))
    dates = [yesterday, today]
    # print(dates)
    return dates


def _get_dict_(filename):
    # print("test method")
    print(filename)


def jsoncomp(arg1, arg2):
    if arg1 < arg2:
        # print ("arg1 is smaller");
        return 1
    elif arg1 > arg2:
        # print ("arg2 is smaller");
        return -1
    else:
        # print ("both equal");
        return 0

# jsoncomp(2,5);


def isrequest_type(file_name_to_check):
    global cols_to_filter
    global rows_to_filter
    if file_name_to_check.find("requests") == -1 :
    # rows_to_filter=prop_container_object.get('rows')
    # if ("request") in file_name_to_check:
        # cols_to_filter=prop_container_object.get('Request_cols')
        return False
    else:
        # cols_to_filter=prop_container_object.get('Distribution_cols')
        return True

        
def genarate_telemetry_details(folder, file_name1, file_name2):
    print("Generating the Telemetry data for files : ", file_name1, " and ", file_name2)
    # total_payload_count=request_count=failure_count=0
    row_container_obj = {}
    file_name_obj = {}
    container_obj = {}
    # list_of_files=[]
    # median_resp_time=0
    # avg_resp_time=0      
    isrequest = isrequest_type(file_name1)
    list_of_files = [file_name1, file_name2]
    print("list of files", list_of_files)         
    # len_cols_to_filter=len(cols_to_filter)
    # len_rows_to_filter=len(rows_to_filter)
    # print(cols_to_filter)
    dictUrl = {}
    for file_name in list_of_files:       
        entry = file_name.split("_")
        # print(entry)
        # full_file_name=re.sub("\D","",file_name)
        # print("full file name is ",full_file_name)
        full_file_name = entry[1]
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r') as _filehandler:
            total = 0
            num_requests = 0
            num_failures = 0
            filename_date = file_path.split("_")[1]
            csv_file_reader = csv.DictReader(_filehandler)
            for row, line in enumerate(csv_file_reader):                
            # for row,line in csv_file_reader:
                isNone = 'line[{}] = {}'.format(row, line[csv_file_reader.fieldnames[0]])
                if isNone.find("None") == -1:                 
                    # col_container_obj={}
                    method = line[csv_file_reader.fieldnames[0]]
                    url = line[csv_file_reader.fieldnames[1]]
                    num_requests = num_requests + int(line[csv_file_reader.fieldnames[2]])
                    num_failures = num_failures + int(line[csv_file_reader.fieldnames[3]])
                    total = num_requests + num_failures            
                    dictUrlDetails = {"method":method, "url":url, "num_requests":int(line[csv_file_reader.fieldnames[2]]), "num_failures":int(line[csv_file_reader.fieldnames[3]])}
                    print("dictUrlDetails ==> ", dictUrlDetails)
                    if filename_date in dictUrl:
                        tmp = dictUrl.get(filename_date)
                        # print(dictUrl," is available \t " , tmp)
                        if total not in tmp:
                            tmp.update({"total":total})
                        if url not in tmp:
                           # print("am here -> ",url)
                           tmp.update({url:dictUrlDetails})
                           # print(tmp)
                        else:
                            tmp.update({url:dictUrlDetails})
                            
                        dictUrl.update({filename_date :tmp})
                        # print("dictUrl #### ==> ",dictUrl)
                    else:
                        dictUrl.update({filename_date :{"total":total, "requests":num_requests , "failures":num_failures, url:dictUrlDetails}})
                    # if (((len_rows_to_filter)>0) and (not(line.get('Name') in rows_to_filter)) or (("Total") in line.get('Name'))):
                    #    continue
                    # print("key =",key)
                    # for key in line:
                        # if ((len_cols_to_filter) > 0) and not(key in cols_to_filter):
                        #    continue
                        # print("key =",key)
                        # col_container_obj[key]=line.get(key)
#                         if (isrequest):
#                             request_count=int(line.get("# requests"))
#                             failure_count=int(line.get("# failures"))
#                             print("req ==> ",request_count, "failures ==> ",failure_count)
#                             total_payload_count=total_payload_count+int(line.get("# requests"))+int(line.get("# failures"))
#                             print("total_payload_count ==> ",total_payload_count)
#                         
#                     row_name=line.get('Name') 
#                      
#                     if (isrequest):
#                         row_container_obj["total"]=total_payload_count
#                         row_container_obj["total_requests"]=request_count
#                         row_container_obj["total_failures"]=failure_count
#                     row_container_obj[row_name]=col_container_obj
                        
            file_name_obj[full_file_name] = row_container_obj
            # total_payload_count=request_count=failure_count=0  
            if (isrequest):
                container_obj['requests'] = dictUrl
            else:
                container_obj['distribution'] = dictUrl
        # print(container_obj)
    return container_obj


def _get_Dict_Value_(tempDict, key):
    if key in tempDict :
        return tempDict.get(key)


def _get_Dict_Value_By_List(tempDict, keysList, key):
    tempList = []
    # tempList.clear()
    for s in keysList:
        # print("s is ",s)
        dateResults1 = tempDict.get(s)
        if key in dateResults1 :
            # print("am here ")
            v1 = (_get_Dict_Value_(dateResults1, key))
            tempList.append(v1)
    return tempList

def _time_duration(elapsedTime):
    if elapsedTime <= 1.00:
       #print (elapsedTime)
       return True
    else:
       #print ("The elapsedTime is lesser than 1 sec",elapsedTime)
       return False
    

def _results_compare_plot_(folder, file1, file2):
    ###########################################
    files_path = [x for x in os.listdir(folder) if x.endswith(".json") and "_telemetry_" in x]  #
    # print("filtered f=" , files_path)
    
    for f in files_path:
        # print("filtered f= ", f)
        arr = f.split("_")
#         print(len(arr))
#         print()
    ###########################################
    myDict = genarate_telemetry_details(folder, file1, file2)
    isrequest = isrequest_type(file1)
    
    val1 = None
    if isrequest :
        dates = _get_today_yesterday_dates_()
        fileutils.write_data(folder + "/requests_" + dates[0] + "_" + dates[1] + "_telemetry_results.json", myDict)
        val1 = myDict.get("requests")
    else :
        val1 = myDict.get("distribution")
    myList = val1.keys()
    print("myList is ", myList)
    tmp = {}
    if isrequest :
        requestsDict = _get_Dict_Value_(myDict, "requests")
        for k, v in requestsDict.items():
            print("key = ", k, "value =" , v)
            tot = _get_Dict_Value_(v, "total")
            req = _get_Dict_Value_(v, "requests")
            fails = _get_Dict_Value_(v, "failures")
            if k in tmp:
                print("key is map " , k)
            else:
                if not tmp:
                    # print("Dict is Empty")
                    tmp = {k:{"total":tot, "requests":req, "failures":fails}}
                else:
                    tmp.update({k:{"total":tot, "requests":req, "failures":fails}})
    
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("tmp => " , tmp)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    return tmp


def _result_compare_(folder, file1, file2):
    n_file1 = os.path.join(folder, file1)
    if not os.path.exists(n_file1):
        fileutils.read_write_csv(folder,file2, file1)
        # print("The File s% it's not created "%file1)
        # os.touch(file1)
        print("The file s% has been Created ..." % file1)
      
    myDict = genarate_telemetry_details(folder, file1, file2)
    print("telemetry results is \n", myDict)
    # requestData = _result_compare_(resultsDir,file1,file2)
    
    isrequest = isrequest_type(file1)
    val1 = None
    if isrequest :
        dates = _get_today_yesterday_dates_()
        fileutils.write_data(folder + "/requests_" + dates[0] + "_" + dates[1] + "_telemetry_results.json", myDict)
        val1 = myDict.get("requests")
    else :
        val1 = myDict.get("distribution")
    myList = val1.keys()
    print("myList is ", myList)
    outDict = {}
    tempDict = {}
    if isrequest :
        tempDict = {"total":_get_Dict_Value_By_List(val1, myList, 'total')}
        tempDict.update({"requests":_get_Dict_Value_By_List(val1, myList, 'requests')})
        tempDict.update({"failures":_get_Dict_Value_By_List(val1, myList, 'failures')})
        
    # print(tempDict)
    else:
        print("do nothing ..")
        return
    
    for k, v in tempDict.items():
        # print(k, "length of list is ",len(v))
        if len(v) >= 2:
            value = jsoncomp(v[0], v[1])
            # print(value)
            isIncreased = False
            isDecreased = False
            if value >= 1 :
                isIncreased = True 
                isDecreased = False
            elif value <= -1 :
                isIncreased = False
                isDecreased = True
            else :
                isIncreased = False
                isDecreased = False
            outDict.update({k:{"Increased":"isIncreased", "Decreased":"", "oldvalue":v[0], "newvalue":v[1]}})

    print(outDict)    
    return outDict


if __name__ == '__main__':
    _get_today_yesterday_dates_()
    file1 = "imnresults_2018-09-19_requests.csv"
    file2 = "imnresults_2018-09-18_requests.csv"
    print(_results_compare_plot_("../output/", file1, file2))
