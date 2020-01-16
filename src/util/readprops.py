import os.path
from util.hdsconstants import *
import json
from collections import defaultdict
#Global Declarations
appl_props= {}
payload_props = {}
separator = "="
keys = {}


s=[]
d = defaultdict(list)

def loadPayloadProps():
    print(os.path.join(project_root,RESOURCES_FOLDER,PROPS_PAYLOAD))    
    with open(os.path.join(project_root,RESOURCES_FOLDER,PROPS_PAYLOAD)) as fp:
        lines = fp.read().split("\n")
    #path_list = []
    #print(lines)
    counter=0;
    for nodeAndPayload in lines:
        node, payload = nodeAndPayload.split(separator, 1)
        #p = payload.split("=")
        #print("dict is :: "+node)
        #print("dict is :: "+payload)
        payload_props[node] = payload
        
    print("payload properties")
    print(payload_props)
    return payload_props

def getPayloadProps():
#     city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
# 
#     cities_by_state = defaultdict(list)
#     for state, city in city_list:
#         cities_by_state[state].append(city)
#     print(cities_by_state)
#     for state, cities in cities_by_state.items():
#         print( state, ', '.join(cities))
        
    print(os.path.join(project_root,RESOURCES_FOLDER,PROPS_PAYLOAD))    
    with open(os.path.join(project_root,RESOURCES_FOLDER,PROPS_PAYLOAD)) as fp:
        lines = fp.read().split("\n")
    #path_list = []
    tempList=[]
    for nodeAndPayload in lines:
        if not nodeAndPayload:
            continue
        node, payload = nodeAndPayload.split(separator, 1)
        #p = payload.split("=")
        print("dict is :: "+node)
        print("dict is :: "+payload)
        payload_props[node] = payload
        tempList.append((node,payload))
    #print(tempList)
    test_dict = defaultdict(list)
    for state, city in tempList:
        test_dict[state].append(city)
    #print("Dictionary testing ")
    #print(test_dict)
    
#     for node, requestPayeload in test_dict.items():
#         print(len(requestPayeload))
        
    return test_dict

def getApplicationProperty(key):
    return appl_props.get(key)

def getPayloadProperty(key):
    return payload_props.get(key)


#main
if __name__ == '__main__':
    #loadApplicationProps()
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print("project root is ", project_root)
    #loadPayloadProps(project_root,"resources","payload.properties")
    getPayloadProps()