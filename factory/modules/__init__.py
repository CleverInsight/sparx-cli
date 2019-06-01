# python
import os
import sys
import math
import click
import requests
import tarfile
from tqdm import tqdm



def check_if_app_exist(app_name):
    '''
    Check if app_name matches with any folder in home dir
    '''
    return os.path.exists(os.path.join(os.path.join(\
        os.path.abspath('..'), 'sparx-io'), app_name))
    
    

def download(url, app_name):
    '''
    Download the app skeleton from the repository
    '''
    if check_if_app_exist(app_name) :
        sys.exit(app_name + " already exists")

    # download the tar.gz file using request module
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0));
    block_size, wrote = 1024, 0
    destination_path = os.path.join(os.path.abspath('..'), 'sparx-io')

    # dowload the tar.gz file into the given destination
    with open(os.path.join(destination_path, app_name+'.tar.gz'), 'wb') as f:
        for data in tqdm(response.iter_content(block_size), total = math.ceil(total_size//block_size), unit='KB', unit_scale=True, ascii=True):
            wrote = wrote  + len(data)
            f.write(data)
        print "craft created!!"

    if total_size != 0 and wrote != total_size:
        print "ERROR, something went wrong"
    
    # Make app directory 
    os.mkdir(os.path.join(destination_path, app_name))
    tf = tarfile.open(app_name + '.tar.gz')
    tf.extractall(path=os.path.join(destination_path, app_name))


    # remove the downloaded tarfile after extraction
    os.remove(os.path.join(destination_path, app_name+'.tar.gz'))
     
