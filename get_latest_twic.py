#!/usr/bin/env python3

import urllib.request
import datetime
import sys

original_issue_number = None
with open('/home/myname/Chess/Backups/TWIC/twic_information.txt', 'r') as twic_info:
    original_issue_number = twic_info.readline().strip()

error_message = None
if not original_issue_number:
    error_message = "Nothing found in twic_information file"
elif not original_issue_number.isdigit():
    error_message = "Value found in twic_information is not a number: " + original_issue_number
if error_message:
    error_message = str(datetime.datetime.now()) + "     " + error_message + "\n"
    with open('/home/myname/Chess/Backups/TWIC/twic_update_log.txt', 'a') as error_log:
        error_log.write(error_message)
        sys.exit()

original_issue_number = int(original_issue_number)
last_successful_issue_number = original_issue_number
url_start = "https://www.theweekinchess.com/zips/twic"
url_end = "g.zip"
while True:
    next_issue_number = last_successful_issue_number + 1
    next_url = url_start + str(next_issue_number) + url_end
    next_file_name = "/home/myname/Chess/Backups/TWIC/twic" + str(next_issue_number) + "g.zip"
    try:
        urllib.request.urlretrieve(next_url, next_file_name)
    except Exception as e:
        error_message = str(datetime.datetime.now()) + "     " + str(e) + "\n"
        with open('/home/myname/Chess/Backups/TWIC/twic_update_log.txt', 'a') as error_log:
            error_log.write(error_message)
        break
    last_successful_issue_number = next_issue_number

if last_successful_issue_number > original_issue_number:
    with open('/home/myname/Chess/Backups/TWIC/twic_information.txt', 'w') as twic_info:
        twic_info.write(str(last_successful_issue_number))
    log_message = str(datetime.datetime.now()) + "     successfully updated from issue " + str(original_issue_number) + " to issue " + str(last_successful_issue_number) + "\n"
    with open('/home/myname/Chess/Backups/TWIC/twic_update_log.txt', 'a') as twic_log:
        twic_log.write(log_message)
