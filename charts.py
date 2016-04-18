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
import re

file_contents = ""
# stream_id = 'm09i09x89r'
#
# stream = Stream(
#     token=stream_id,  # (!) link stream id to 'token' key
# )

internet_data_list = [1, 1, 1, 1]

def transform_program_data(type):
    array = ['name', 'status', 'created', 'pid', 'user', 'running_time']
    masterArrayList = [['Name', 'Status', 'Time Created', 'CPU Percentage', 'User', 'Running Time']]
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
                #if name == "VBoxClient":
                    #result += counter * 2
                pyProgramsData.append(result)

        masterArrayList.append(arrayValues)

    if type == 'table':
        return masterArrayList
    if type == 'pyName':
        return pyProgramsNames
    if type == 'pyData':
        #counter += 1
        return pyProgramsData

def generate():
    # Add table data

    global data
    global internet_data_list
    data = lp.all_running_process()
    #print data
    table_data = transform_program_data('table')

    # Initialize a figure with FF.create_table(table_data)
    figure = FF.create_table(table_data, height_constant=60, index=True)



    pyChart1 = go.Pie(labels = ['tumblr', 'twitter', 'facebook', 'pinterest'],
                    values = internet_data_list,
                    name = 'Internet',
                    hole = .4,
                    domain = {'x':[0, .48], 'y':[1, .55]})

    pyChart2 = go.Pie(labels = transform_program_data('pyName'),
                    values = transform_program_data('pyData'),
                    name = 'Programs',
                    hole = .4,
                    domain = {'x':[.52, 1], 'y':[1, .55]})

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


if __name__ == "__main__":
    data = lp.all_running_process()
    #print "All running processes: "
    #print data

    i = 0    # a counter
    N = 200  # number of points to be plotted

    time.sleep(5)

    while i<N:
        #help(stream)
        fo = open("charisa_output.txt", "r")
        #s.write(dict(values = transform_program_data('pyData')))


        #file_contents = fo.read()
        temp = fo.read()
        fo.close()
        if len(temp) != 0:
            file_contents = temp
        time_list = re.findall("\d+\.\d+", file_contents)
        print "file contents: "
        print file_contents
        print time_list
        global internet_data_list
        internet_data_list = time_list
        generate()
        i += 1
        time.sleep(5)
