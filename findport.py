def setAdminRefs(adminTuple):
    global AdminConfig, AdminControl
    global AdminTask, AdminApp
    (AdminConfig, AdminControl, AdminTask, AdminApp) = adminTuple

def wsadminToList(inStr):
    outList=[]
    if (len(inStr)>0 and inStr[0]=='[' and inStr[-1]==']'):
        tmpList = inStr[1:-1].split() #splits space-separated lists,
    else:
        tmpList = inStr.split("\n")   #splits for Windows or Linux
    for item in tmpList:
        item = item.rstrip();         #removes any Windows "\r"
        if (len(item)>0):
            outList.append(item)
    return outList

def id_to_name(id):
    return id.split('(')[0]

def get_id_list(scope, search='None'):
    scope_name = "/" + scope.capitalize() + ":/"
    if search == 'None':
        scope_id_list = wsadminToList(AdminConfig.getid(scope_name))
    else:
        scope_id_list = [scope_id for scope_id in wsadminToList(AdminConfig.getid(scope_name)) if scope_id.find(search)>=0]
    return scope_id_list

def get_server_entry_list(node):
    node_id = get_id_list('Node', node)[0]
    return wsadminToList(AdminConfig.list("ServerEntry", node_id))

def get_ports_list(server_entry,port='all'):
    # Test if server_entry parameter is a list or a string
    if type(server_entry) == type([]): # Check if it is a list
        for se in server_entry:
            ep_list = wsadmintToList(AdminConfig.showAttribute(se, "specialEndpoints"))
'''
    # insert function per server_entry
    for se in server_entry_list:
        eps = wsadminToList(AdminConfig.showAttribute(se, "specialEndpoints"))
        epName = AdminConfig.showAttribute(eps, "endPointName" )
        epVal = AdminConfig.showAttribute(eps, "endPoint" )
        portNumb = AdminConfig.showAttribute(epVal, "port" )
        keyName = epName
        serverPorts[keyName] = portNumb
        if server_name != 'nodeagent':
            for key in serverPorts:
                if serverPorts[key].find('90')==0:
                                portname = serverPorts[key],server_name,key
                                reservedPorts.append(portname)
    reservedPorts.sort()
    for port in reservedPorts:
        print '%-20s %-30s %s' % (port[0],port[1],port[2])
'''

server_entry_list = get_server_entry_list('w30037')
