import psutil
import time
import socket
import platform
import os
import datetime
from threading import Thread
import threading

def get_process_list():
	process_list = []
        for p in psutil.process_iter():
            mem = p.memory_info()

            # psutil throws a KeyError when the uid of a process is not associated with an user.
            try:
                username = p.username()
            except KeyError:
                username = None

            proc = {
                'pid': p.pid,
                'name': p.name(),
                'user': username,
                'status': p.status(),
                'created': p.create_time(),
                'uptime': p.cpu_times()
            }
            process_list.append(proc)

        return process_list

def all_running_process():
    #Gets all RUNNING processes
    #print "Inside awake"
    #time.sleep(3)
    all_running_process_list = []
    username = get_username()
    for p in get_process_list():
        if p['user'] == "laurenkoulias":
            if p['status'] == 'running':
                p['running_time'] = time.strftime("%M:%S", time.localtime(sum(p['uptime'])))
                all_running_process_list.append(p)
    return all_running_process_list
    #print "I am here"

def all_process():
    #Gets the list of process
        #Sleeping or Running
    #time.sleep(10)
    #print "Inside Sleep"
    all_process_list = []
    username = get_username()
    for p in get_process_list():
        if p['user'] == "laurenkoulias":
        	p['running_time'] = time.strftime("%M:%S", time.localtime(sum(p['uptime'])))
        	all_process_list.append(p)
    return all_process_list

def get_sysinfo():
    uptime = int(time.time() - psutil.boot_time())
    sysinfo = {
        'uptime': uptime,
        'hostname': socket.gethostname(),
        'os': platform.platform(),
        'load_avg': os.getloadavg(),
        'num_cpus': psutil.cpu_count()
    }
    return sysinfo

def get_username():
    systemInfo = get_sysinfo()
    hostname = systemInfo['hostname']
    return hostname.split('-')[0]

#if __name__ == '__main__':
    #trial()
    #time.sleep(10)
#    print all_process()

'''    i = 0
    while i < 2:
        if threading.active_count() < 5:
            t1 = Thread(target=all_process, args=())
            t1.start()
            t2 = Thread(target=all_running_porcess, args=())
            t2.start()
            print threading.active_count()
        i = i + 1
  '''      #print "The Value of i " + str(i)
    #try:
    #thread.start_new_thread(all_process, ())
        #thread2.start_new_thread(all_running_porcess,())
    #except:
    #    print "Error: unable to start thread"
    #print get_process_list()
