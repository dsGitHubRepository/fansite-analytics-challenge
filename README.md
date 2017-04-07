# Contents
1. [Project Overview](README.md#project-overview)
2. [Feature 1](README.md#comments-on-feature-1)
3. [Feature 2](README.md#comments-on-feature-2)
4. [Feature 3](README.md#comments-on-feature-3)
5. [Feature 4](README.md#comments-on-feature-4)
6. [Summary](README.md#summary)
7. [Additional Comments](README.md#additional-comments)

# Project Overview

Four features of the data challenge has been submitted as four sepearte solutions. For feature 3 challenge since the analysis session
is to time consuming; hence tests has been carried over with steps to see whetehr the output is meaningful. For a quicker check for the solution a resonable wide steps in the input data can be chosen to satisfy the scalability of the code produced in this submission.

# Feature 1
Feature 1 analysis was pretty straight forward. It produces top 10 most active host within few minutes.

# Feature 1
For Feature 2 analysis to identify the top 10 resources taht consumes the most bandwidth on the site; avearge bytes for each resouce was calculated top resources are written in output in descending order.

# Feature 3
Feature 3 is most time consuming analysis where top 10 busiest site was identified over 60 minute time window. This analysis might be done 
only period having successfull http reply code "200"; but my analysis did not limit the computation with http reply "200"; it was done 
without this restriction.

# Feature 4
Since feature 4 analysis is related to multiple consecutive failed login attemps (e.g.; 3 or 4 attempts) over a period of few seconds ( e.g.; 5 sec or 20 sec etc.) inorder to block further attempts to reach the site from the same IP address over 5 minutes. For feature 4 analysis I have varied no of consecutive failed attemps (CFS L60) from 2 to 5 over a few seconds (timeStep L80) followed by a time block of 5 minutes (timestepBlock L94).

Above three parameters can be varied. I submitted ./log_output/blocked.txt for  4 consecutive failed attemp for 5 seconds so that it was blocked for next 5 minutes.

