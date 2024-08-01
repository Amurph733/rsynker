#!/usr/bin/python3
from typing import Optional
import os
import yaml

def find_rsynk_base() -> Optional[str]:
    cwd = os.getcwd()
    while True:
        potential_path = os.path.join(cwd,'.rsynk')
        if os.path.isdir(potential_path):
            return cwd
        if cwd is '/':
            return None
        cwd = os.dirname(cwd)

def main():
    print('Hello World!')

    rsynk_base = find_rsynk_base()
    if rsynk_base is None:
        print("Error: Not under an rsynk")
        exit(1)

    rsynk_dir = os.path.join(rsynk_base,'.rsynk')

    with open(os.path.join(rsynk_dir,'rsynk.yaml')) as yaml_file:
        rsynk = yaml.load(yaml_file)
        print(rsynk)

    exit(0)

if __name__=='__main__':
    main()

