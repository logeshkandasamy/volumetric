import csv, collections, os
import json


def write_data(file_path, data):
    path = file_path.split("/")
    # length=len(path)
    # print("length = ",len(path) ," last element =",path[length-1])
    if path[-1].endswith(".json"):
        with open(file_path, 'w') as outfile:  
            json.dump(data, outfile)
    else:
        with open(file_path, 'w') as file:
            file.write(str(data))
    print('File successfully written!!!')


def _read_json_data_(file_path):
    with open(file_path) as json_file:  
        data = json.load(json_file)
        print(data)
        return data
    

def read_write_csv(folder,file, newfile):
    n_file1 = os.path.join(folder, file)
    csvlines = []
    with open(n_file1, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
        row_count = len(data)
        print("No. of rows in ", row_count)
        line_count = 0
        colCount = 0;
        for row in data:
            if line_count == 0:
                colCount = len(row)                
                print(len(row))
                print(f'Column names are {", ".join(row)}')                
                rowkeys = collections.OrderedDict(row.items()).keys()
                keysList = list(rowkeys)
                # csvlines[keysList]
                print("header is ", keysList)
                # headerData=",".join(keysList)
                headerFormat = "\"%s\", \"%s\",\"%s\", \"%s\",\"%s\", \"%s\",\"%s\", \"%s\",\"%s\", \"%s\"" % tuple(keysList)
                csvlines.append(headerFormat)
                print("headerFormat is ", headerFormat)
                line_count += 1
            lineFormat = "\"%s\", \"%s\",%d,%d,%d,%d,%d,%d,%d,%.2f" % (row["Method"], row["Name"], 0, 0, 0, 0, 0, 0, 0, 0.00)
            print("line format is ", lineFormat)
            lineCSV = lineFormat  # ("\""+row["Method"]+"\"")+str(",")+(row["Name"])+str(",0,0,0,0,0,0,0,")+str(float(0.00))
            print(f'\t{row["Method"]} works in the {row["Name"]} ')            
            print(f'Processed {line_count} lines.')
            csvlines.append(lineCSV)
            line_count += 1
    
    print(csvlines)
    n_file2 = os.path.join(folder, newfile)
    with open( n_file2, "w") as output:
        # output.write(str(values))
        for line in csvlines:
            output.write("".join([str(i) for i in line]))
            output.write("\n")
                
# read_write_csv("E:\\writable\\Users\\lkandasamy.CORPORATE\\git\\hds_volume_defect_fix\\volumetest\\output\\imnresults_2018-10-24_requests.csv","E:\\writable\\Users\\lkandasamy.CORPORATE\\git\\hds_volume_defect_fix\\volumetest\\output\\imnresults_2018-10-25_requests.csv")
