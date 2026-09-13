# python log analyser

a simple python program that analyses login logs and identifies potentially suspicious activity.

## features

* counts successful login attempts
* counts failed login attempts
* extracts IP addresses from log entries
* counts how many attempts were made from each IP address
* identifies IP addresses with multiple login attempts
* handles missing log files

## how it works

the program reads a text-based log file line by line.

it searches each line for successful and failed login attempts and extracts the IP address associated with the entry.

the IP addresses are stored and counted. if an IP address makes more than three attempts, the program flags it as potentially suspicious.

## technologies used

* python
* file handling
* dictionaries

## what i learned

this project helped me practise file handling, iteration, selection, functions and dictionaries in python.

i also learned how log files can be analysed to identify patterns in login activity and how repeated attempts from the same IP address could be used as an indicator of suspicious activity.

## how to run

1. download or clone this repository
2. open `log_analyser.py`
3. create or use a text log file containing login entries
4. run the program using python
5. enter the name of the log file when prompted
6. the program will display the login statistics and any potentially suspicious IP addresses

## example

```text
enter the log file name: login_log.txt

===== log analyser =====
successful logins: 4
failed logins: 8

ip addresses:
192.168.1.10 - 2 attempts
192.168.1.20 - 6 attempts

ip addresses with multiple attempts:
192.168.1.20 - 6 attempts
```

## disclaimer

this project is for educational purposes and demonstrates basic log-analysis techniques. the results should not be treated as proof of malicious activity.
