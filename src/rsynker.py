#!/usr/bin/python3
from typing import Optional
import subprocess
import os
import yaml

def find_rsynk_base() -> Optional[str]:
    """Get the base directory to copy"""
    cwd = os.getcwd()
    while True:
        potential_path = os.path.join(cwd,'.rsynk.yaml')
        if os.path.isfile(potential_path):
            # Remove trailing slash 
            cwd = cwd [:-1]
            return cwd
        if cwd is '/':
            return None
        cwd = os.path.dirname(cwd)

def main():
    print('Hello World!')

    rsynk_base = find_rsynk_base()
    if rsynk_base is None:
        print("Error: Not under an rsynk")
        exit(1)

    rsynk_file = os.path.join(rsynk_base,'.rsynk.yaml')

    with open(rsynk_file) as yaml_file:
        rsynk = yaml.load(yaml_file)

    if rsynk is None:
        print('Error: Failed to parse rsynk.yaml file.')
        exit(1)

    print(rsynk)

    where = "{}@{}".format(rsynk['user'], rsynk['host'])
    if where == '@':
        where = rsynk['location']
    else:
        where = "{}:{}".format(where, rsynk['location'])
    
    cmd = [
        'rsync',
        '-r',
        rsynk_base,
        where
    ]

    print(" ".join(cmd))

    # subprocess.run()

    exit(0)

if __name__=='__main__':
    main()

