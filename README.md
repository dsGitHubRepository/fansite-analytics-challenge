# Contents
1. [Project Overview](README.md#project-overview)
2. [Feature 1](README.md#comments-on-feature-1)
3. [Feature 2](README.md#comments-on-feature-2)
4. [Feature 3](README.md#comments-on-feature-3)
5. [Feature 4](README.md#comments-on-feature-4)

# Project Overview

Four features of the data challenge has been submitted as four sepearte solution. Feature 3 analysis has been carried over with data steps to check whether the output is meaningful to real time analysis of server log data. For a quicker check for the solution a resonable wide steps in the input data can be chosen to satisfy the scalability of the code produced in this submission.

# Feature 1

Feature 1 analysis was implemented and tested to sort out the top 10 most active hosts in descending order.

# Feature 2

Feature 2 analysis to identify the top 10 resources that consumes the most bandwidth on the site; avearge bandwidth for individual resources was calculated to sort out the top 10 in descending order. 

# Feature 3

Feature 3 is the most time consuming analysis where top 10 busiest 60 minutes period was identified and reported as ./log_output/hours.txt. Since analysis was lengthy in time consideration, so output file is reported with datastep delta=200. This analysis might be done only for periods having successfull http reply code "200"; but submitted analysis did not limit the computation with http reply "200"; it was done without this restriction.

# Feature 4

Since feature 4 analysis is related to multiple consecutive failed login attemps (e.g.; 3 or 4 attempts) over a period of few seconds ( e.g.; 5 sec or 20 sec etc.) inorder to block further attempts to reach the site from the same IP address over 5 minutes. For feature 4 analysis was carried over 4 consecutive failed login attemps (CFS L60) for  5 seconds (timeStep L80) followed by a time block of 5 minutes (timestepBlock L94).

Above three parameters can be varied to check the pattern. 




