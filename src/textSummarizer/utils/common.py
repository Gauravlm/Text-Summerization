'''
Adding function which can freqently use in main code
so mention it into utils or common folder/files
'''
from textSummarizer.logging import logger
import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    """
    read yaml file and return
    
    Args:
        path_to_yaml(str)--> path like input
    Raise:
        valueError:- If yaml file is empty
    Returns:
        configBox: ConfigBox type/object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f'ymal file:{path_to_yaml} load successfully') 
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError('Ymal file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directory:list, verbose=True):
    '''
    Create list of directories
    Args: 
        path_to_directory (list): get list path for directory
    '''
    for path in path_to_directory:
        os.makedirs(path)
        if verbose:
            logger.info(f'Created directory at: {path}')



@ensure_annotations
def get_size(path:Path)->str:
    '''
    Get size in KB
    Args:
        path(Path)- path of the file
    Returns:
        str: size in KB
    '''
    size_in_kb= round(os.path.getsize(path)/1024)
    return f'~{size_in_kb} KB'