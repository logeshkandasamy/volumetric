# This file is used for global declaration
import os

from util.readconfig import read_config ,ConfigSectionMap

PROPS_PAYER_PAYLOAD = "payer.properties"
PROPS_PAYLOAD = "payload.properties"
PROPS_CONFIG = "environ.properties"
PROPS_APPLICATION = "application.properties"
RESOURCES_FOLDER = "resources"
env = None
resultfileprefix = None
timeframe = None
csvresultfileformat = None
resultsDir = None
locustusers = None
locusthatchrate = None
host = None
runtime = None

# S3 Bucket
bucket_name = None
bucket_path = None

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print("project root is ", project_root)
output_path = os.path.join(project_root, 'output')
print("output_path root is ", output_path)



def init():
    print(" -- init -----")
     # merge all into one config dictionary
    config = read_config([os.path.join(project_root, RESOURCES_FOLDER, PROPS_APPLICATION), os.path.join(project_root, RESOURCES_FOLDER, PROPS_CONFIG)])
    
    # if(config == None):
    #   return 
    global resultsDir, bucket_name, bucket_path, locust_taskset_min_wait_time, locust_taskset_max_wait_time
    global env, runtime, host, locusthatchrate, locustusers, timeframe, resultfileprefix, csvresultfileformat,logOutputDirectory
    # get the current branch (from local.properties)
    env=ConfigSectionMap("branch")['env'] 
    timeframe =ConfigSectionMap("global")['timeframe']      
    resultfileprefix = config.get('global', 'csvresultfile_prefix')
   
    #csvresultfileformat = config.get('global', 'csvresultfileformat')
    csvresultfileformat = ConfigSectionMap('global')['csvresultfileformat']
    
    #Locust related configuration propertiess
    locustusers =ConfigSectionMap(env + ".locust")['no_of_users']
    locusthatchrate =ConfigSectionMap(env + ".locust")['no_of_hatchrate']
    host =ConfigSectionMap (env + ".locust")['host']
    runtime =ConfigSectionMap(env + ".locust")['run-time']
    locust_taskset_min_wait_time=ConfigSectionMap(env + ".locust")['min_wait_time']
    locust_taskset_max_wait_time=ConfigSectionMap(env + ".locust")['max_wait_time']
    
    resultsDir = config.get('global', 'resultsDir')
  
    logOutputDirectory=ConfigSectionMap(env+".log")['log_output_directory']
    print("logOutputDirectory ==> ",logOutputDirectory)
    
    
init()
