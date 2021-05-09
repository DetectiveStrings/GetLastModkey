# GetLastModkey
### Hello, this is my first volatility plugin, a very helpful one at least for me, helped me to detect suspicious behaviours of malware like wannacry and detect its activity in registers, hope it will be helpful for you also, (windows profile based plugin) 
#### supported in volatility 2 
#### this plugin get a list of the last modified registry keys, just give it the time you need to start listing from and it will do a good job 
#### also you can specify a range of time to search in just set the start time and end time
#### you can specify the hive file you want to search into, by default it searches NTUSER.DAT 

## usage flags 
#### -t: if you need to search from the time you set to the last key 

  getlastmodkey -t "2021-02-22 17:52:48"
  
#### -s, -e: if you will search a range of time, you must set the both together 
  
  getlastmodkey -s "2021-02-22 17:52:48" -e "2021-02-25 10:52:18"
  
#### -n: when you need to search a specific hive, by default the plugin search NTUSER.DAT , you can use it with any of the 2 types of searching 
  
  getlastmodkey -t "2021-02-22 17:52:48" -n SAM 

  getlastmodkey -s "2018-02-22 17:52:48" -e "2021-02-25 10:52:18" -n SAM
  
  
