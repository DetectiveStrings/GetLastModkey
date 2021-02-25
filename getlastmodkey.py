import volatility.plugins.common as common
import volatility.plugins.registry.registryapi as registryapi
import volatility.utils as utils
import volatility.win32 as win32
import time
import datetime 

class GetLastModKey(common.AbstractWindowsCommand):
    """ Regitery keys last modefication """
    def __init__(self, config, *args, **kwargs):
    
        common.AbstractWindowsCommand.__init__(self, config, *args, **kwargs)
        self._config.add_option('SatrtToEnd', short_option = 't', default = None, help = 'set start time , end time is set to last edit key', action = 'store')
        self._config.add_option('StartOfRange', short_option = 's', default = None, help = 'set range start time ', action = 'store')
        self._config.add_option('EndOfRange', short_option = 'e', default = None, help = 'set range end time ', action = 'store')
        self._config.add_option('HiveName', short_option = 'n', default = "NTUSER.DAT", help = 'specify the hive name , the default is NTUSER.DAT ', action = 'store')
    def calculate(self):
        
        T = self._config.SatrtToEnd
        S = self._config.StartOfRange
        E = self._config.EndOfRange
        Hi = self._config.HiveName
        return T , S , E , Hi
    
    def render_text(self, outfd, data):
        regapi = registryapi.RegistryApi(self._config)
        T , S , E , Hi  = data
        regapi.set_current(hive_name = Hi , user = "administrator")
        count = 0
        stop_time = 0
        if T :
            try : 
                stop_time = time.mktime(datetime.datetime.strptime(T, "%Y-%m-%d %H:%M:%S").timetuple())
                count = 10000000000
                for t , k in regapi.reg_get_last_modified(hive_name = Hi  , count = count ):
                    if stop_time != 0 :
                        cop_time_hand = str(t).split(" UTC") 
                        cop_time = cop_time_hand[0]
                        end_time = time.mktime(datetime.datetime.strptime(cop_time, "%Y-%m-%d %H:%M:%S").timetuple())
                        if stop_time > end_time :
                            break
                    #k = k.replace("CMI-CreateHive{D43B12B8-09B5-40DB-B4F6-F6DFEB78DAEC}\\", "")
                        print t , k
            except : 
                print "an error happend , plz inter a correct format of time ,  Y-m-d H:M:S  , like the form of start and end processes "
        
        elif S : 
            try : 
                start_time = time.mktime(datetime.datetime.strptime(S, "%Y-%m-%d %H:%M:%S").timetuple())
                stop_time = time.mktime(datetime.datetime.strptime(E, "%Y-%m-%d %H:%M:%S").timetuple())
                count = 10000000000
                for t , k in regapi.reg_get_last_modified(hive_name = Hi  , count = count ):
                    cop_time_hand = str(t).split(" UTC")
                    cop_time = cop_time_hand[0]
                    cop_time = time.mktime(datetime.datetime.strptime(cop_time, "%Y-%m-%d %H:%M:%S").timetuple())
                    if cop_time <= stop_time and cop_time >= start_time :
                        print t , k
                    elif cop_time < start_time : 
                        break
            except : 
                print "an error happend , plz inter a correct format of time , Y-m-d H:M:S  , like the form of start and end processes , also make sure you interd the start and end time , the start time must be less than the end time "

