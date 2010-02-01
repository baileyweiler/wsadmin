def setAdminRefs(adminTuple):
    global AdminConfig, AdminControl, AdminTask, AdminApp
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

def getNodeIDList(**search):
    try:
        node = search['node']
    except:
        node = ''
    node_list = wsadminToList(AdminConfig.getid('/Node:'+node+'/'))
    return node_list

def getNodeList(nodeid_list):
    nodename_list = [AdminConfig.showAttribute(node, 'name') for node in nodeid_list]
    return nodename_list

def getScopeIDList(nodename_list):
    scopeid_list = [AdminConfig.getid("/Node:%s/" %(node)) for node in nodename_list]
    return scopeid_list

def getServerEntryIDList(scopeid_list):
    serverentryid_list = []
    for server_entry in scopeid_list:
        tmplist = AdminConfig.list("ServerEntry", server_entry).split('\n')
        serverentryid_list += tmplist
    return serverentryid_list

def getServerInfoFromID(serverentry):
    server_name, server_info = se.split('(')[0], se.split('(')[1]
    cell_name, node_name = server_info.split('/')[1], server_info.split('/')[3].split('|')[0] 
    return specialendpoints_list

def getEndPointList(serverentryid_list):
    serverPorts = {}
    reservedPorts = []
    for se in serverentryid_list:
        serverPorts = {}
        server_name, cell_name, node_name = getServerInfoFromID(se)
        eps = AdminConfig.showAttribute(se, "specialEndpoints").split()
        for ep in eps:
            if ep.find('[') == 0:
                ep = ep[1:]
            if ep.find(']') > 0:
                ep = ep[:ep.find(']')]
            epName = AdminConfig.showAttribute(ep, "endPointName" )
            epVal = AdminConfig.showAttribute(ep, "endPoint" )
            portNumb = AdminConfig.showAttribute(epVal, "port" )
            portname = cell_name, node_name, server_name, epName, portNumb
            reservedPorts.append(portname)
    return reservedPorts

def getPortList(nodename):
    nodeid_list = getNodeIDList(node=nodename)
    nodename_list = getNodeList(nodeid_list)
    scopeid_list = getScopeIDList(nodename_list)
    serverentryid_list = getServerEntryIDList(scopeid_list)
    port_list = getEndPointList(serverentryid_list)
    return port_list 

if __name__ == "main":
    port_list = getPortList('w30038')
    for port in port_list:
        print '%s,%s,%s,%s,%s' % port

