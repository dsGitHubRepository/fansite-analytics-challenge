#!/bin/bash

python ./src/process_logQ1.py ./log_input/log.txt ./log_output/hosts.txt

python ./src/process_logQ2.py ./log_input/log.txt ./log_output/resources.txt

python ./src/process_logQ3.py ./log_input/log.txt ./log_output/hours.txt 

python ./src/process_logQ4.py ./log_input/log.txt ./log_output/blocked.txt


