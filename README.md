# aim_screennames
Simple python application to get screennames from aim.com because aim service will be shutdown Dec 15 2017

original idea came from http://dangoldin.com/2017/10/09/downloading-your-aim-buddy-list/

i modified the original code to include the actually screen name and not their context name(display name) under the file aim_get_sn.js

instructions on how to use this are provided from the original idea link

when you successfully run the code in your browser console and have gone through all the screen names, right click and save the console log.

i saved the console log file name as "raw_sns.log", but you can save to another file name want but dont forget to change the python code to use that new file name

this program will parse out the parts between each screen names and save to a seperate file, a list of only the screen names for each line. for this one please use sn_trim.py

--------------------------------------------------------------------------------------------------

i have added the aim_get_sn_n_display.js to extract screen name along with display name from aim.com

i have completed a very similiar version in which you can get the display name along with the screen name

for display name and screen name extraction, please use aim_get_sn_n_display.js and sn_n_name_trim.py
