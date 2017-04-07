
Output placed in the tests folder is test analysis results where parameters have been varied to test whetehr the output data is meaningful. 

As for example for feature 3 to analyze the top 10 time stamp if I carry analysis over the total input data, then the run time is long 
enough to do a quick check whether the code is producing real time analysis. Using the full input data it shows that the top 10 busiest 
time stamps are all within first few seconds; and that give me a wrong impression that the code was wrong. Actually when I run the code 
with data steps over a wide range, the results were resonably spaced over time. hours.txt in the tests folder is for datastep delta=40000.

For feature 3, I also varied number of consecutive failed attempts over 2-5 and after analysis I produced blocked.txt with 4 successive 
failed attemp over 5 sec and then further attempt would be blocked for 5 minutes from the same IP. 
