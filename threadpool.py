##
## WSADMIN Commands
##
## Grabbing ThreadPool count in a Cell
## Sample output from AdminControl.getAttributes(threadpool object) 
## '[ [growable false] [maximumSize 50] [name WebContainer] [stats ] [inactivityTimeout 3500] [minimumSize 10] ]'
#return AdminControl.getAttribute(wc_tp_list[0], 'maximumSize')

def print_report(header, data, type):
    if type!='csv':
        print_row(-30, -10, header)
    else:
        print header[0] + ',' + header[1]
    for row in data:
        if type!='csv':
	    print_row(-30, -10, row)
        else:
            print row[0] + "," + row[1]

def print_row(col1_size, col2_size, row):
    print '%(column1)-30s%(column2)-10s' % {'column1':row[0], 'column2':row[1]}

def get_threadpool_size(type=''):
    wc_tp_list = AdminControl.queryNames('name=%s,type=ThreadPool,*' % ('WebContainer')).splitlines()
    header = ('Server Name', 'ThreadPool Max')
    data = []
    for wc in wc_tp_list:
        server = wc.split('process=')[1].split(',')[0]
        if server == 'dmgr':
            continue
        tp_size = AdminControl.getAttribute(wc, 'maximumSize')
        row_tuple = (server,tp_size)
        data.append(row_tuple)
    print_report(header, data, type)

get_threadpool_size('csv')

def get_threadpool_size_51():
    wc_list = AdminConfig.list('WebContainer').split('\n')
    data = []
    header = ('Server Name', 'ThreadPool Max')
    for wc in wc_list:
        server = wc[wc.find("servers/")+8:wc.find(":")]
        tp_id = AdminConfig.showAttribute(wc, 'threadPool')
        tp_size = AdminConfig.showAttribute(tp_id, 'maximumSize')
        row_tuple = (server,tp_size)
        data.append(row_tuple)
    print_report(header, data, '')

get_threadpool_size_51()
