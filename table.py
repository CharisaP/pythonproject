#!/usr/bin/python
import plotly
#import plotly.plotly as py
from plotly.offline import plot
from plotly.tools import FigureFactory as FF
import plotly.graph_objs as go
from plotly.graph_objs import *
import datetime
import time
import listOfProcess as lp

stream_id = 'm09i09x89r'

stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
)

data = lp.all_running_process()
print "All running processes: "
print data

'''[{'status': 'sleeping', 'uptime': 'pcputimes(user=0.15, system=0.14)', 'name': 'init', 'created': 1459864068.03, 'pid': 1234, 'user': 'chris', 'running_time': '00:01'},
    {'status': 'sleeping', 'uptime': 'pcputimes(user=0.0, system=0.0)', 'name': 'VBoxClient', 'created': 1459864068.45, 'pid': 1315, 'user': 'chris', 'running_time': '00:02'},
    {'status': 'sleeping', 'uptime': 'pcputimes(user=0.0, system=0.0)', 'name': 'VBoxClient2', 'created': 1459864068.45, 'pid': 1316, 'user': 'chris', 'running_time': '00:03'},
    {'status': 'sleeping', 'uptime': 'pcputimes(user=0.0, system=0.0)', 'name': 'VBoxClient3', 'created': 1459864068.47, 'pid': 1325, 'user': 'chris', 'running_time': '00:04'},
    {'status': 'sleeping', 'uptime': 'pcputimes(user=0.0, system=0.0)', 'name': 'VBoxClient4', 'created': 1459864068.47, 'pid': 1326, 'user': 'chris', 'running_time': '00:05'}]
'''
internet_data_list = [19, 55, 12, 46]

counter = 0

def transform_program_data(type):
    array = ['name', 'status', 'created', 'pid', 'user', 'running_time']
    masterArrayList = [['Name', 'Status', 'Created', 'PID', 'User', 'Running Time']]
    pyProgramsData = []
    pyProgramsNames = []
    global counter
    name = ""
    for arrayIndex in data:
        arrayValues = [];
        for key in array:
            if key == 'uptime':
                pass
                #insert_value = arrayIndex[key].replace('pcputimes', '', 1)
                #insert_value = insert_value.replace('(', '', 1)
                #insert_value = insert_value.replace(')', '', 1)
                #arrayValues.append(insert_value)
            else:
                arrayValues.append(arrayIndex[key])
            if key == 'name':
                pyProgramsNames.append(arrayIndex[key])
                name = arrayIndex[key]
            if key == 'running_time':
                (mins, secs) = arrayIndex[key].split(':')
                result = int(mins)*60 + int(secs)
                if name == "VBoxClient":
                    result += counter * 2
                pyProgramsData.append(result)

        masterArrayList.append(arrayValues)

    if type == 'table':
        return masterArrayList
    if type == 'pyName':
        return pyProgramsNames
    if type == 'pyData':
        counter += 1
        return pyProgramsData

def generate():
    # Add table data
    table_data = transform_program_data('table');

    # Initialize a figure with FF.create_table(table_data)
    figure = FF.create_table(table_data, height_constant=60, index=True)



    pyChart1 = go.Pie(labels = ['facebook', 'twitter', 'pinterest', 'tumblr'],
                    values = internet_data_list,
                    name = 'Internet',
                    hole = .4,
                    domain = {'x':[0, .48], 'y':[1, .55]})

    pyChart2 = go.Pie(labels = transform_program_data('pyName'),
                    values = transform_program_data('pyData'),
                    name = 'Programs',
                    hole = .4,
                    domain = {'x':[.52, 1], 'y':[1, .55]},
                    stream=stream)

    # Add trace data to figure
    figure['data'].extend(go.Data([pyChart1]))
    figure['data'].extend(go.Data([pyChart2]))

    #Table goes at bottom of plot
    figure.layout.yaxis.update({'domain': [0, .45]})

    # Update the margins to add a title and see graph x-labels.
    figure.layout.margin.update({'t':75, 'l':50})
    figure.layout.update({'title': 'How I\'m Spending My Time'})
    figure.layout.update({'height':800, 'width':1000})


    # Plot!
    plotly.offline.plot(figure, filename='pyChartWithTable.html', auto_open=False)
    #unique_url = py.plot(figure, filename='pyChartWithTableStream')

#s = py.Stream(stream_id)

# (@) Open the stream
#s.open()
i = 0    # a counter
k = 5    # some shape parameter
N = 200  # number of points to be plotted

time.sleep(5)

while i<N:
    #help(stream)

    #s.write(dict(values = transform_program_data('pyData')))
    generate()

    i += 1
    time.sleep(5)

# (@) Close the stream when done plotting
#s.close()
