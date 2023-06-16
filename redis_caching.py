'''
author: tkucherera

Purpose:
This is a caching module for 
    1. caching results of processes that might be expensive to keep doing for every api call 
    2. storing results of periodic tasks 
'''

import redis
import subprocess

class Cache:
    def __init__(self, connection=None):
        self.server = self.check_server_running()
        if self.server and not connection:
            self.connection  = redis.Redis(host='localhost', port='6379', decode_responses=True)
            self.authenticated = True


    def check_server_running(self):
        try: 
            r = redis.Redis(host='localhost', socket_connect_timeout=10)
            r.ping()           
        except redis.ConnectionError:
            return self.__start_redis()
        
        return True
                
    
    def __start_redis(self):
       response = subprocess.run(['service', 'redis-server', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stderr = response.stderr
       if stderr:
           return 1

    def read(self, key):
        if not self.authenticated:
            raise Exception("NotConnected")
        return self.connection.get(key)
    

    def write(self, key, value):
        if not self.authenticated:
            raise Exception("NotConnected")
        return(self.connection.set(key, value))
    

