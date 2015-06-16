#!/usr/bin/env python2
from __future__ import print_function, with_statement, division, generators
import socialism.benevolant_dictator as bd
import socket

if __name__ == "__main__": 
    bd.launch(
        script_path="/home/julesgm/task/files/client.py", 
        project_name="jvb-000-aa", 
        walltime=10, 
        number_of_nodes=4, 
        number_of_gpus=4, 
        job_name="experims"
        )

