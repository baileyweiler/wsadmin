import string,sys
search = sys.arg[0]
server_list = AdminConfig.list('Server').split('\n')
shortname = [server.split('(')[0] for server in server_list if server.find(search) >= 0]
for server in shortname:
    server_id = AdminConfig.getid('/Server:%s/' % server)
    print server_id
    tc = AdminConfig.list('TraceService', server_id)
    AdminConfig.modify(tc, [['startupTraceSpecification', '*=info']])

for node in AdminConfig.list('Node').split('\n'):
    node = node.split('(')[0]
    print node
    object = 'type=NodeSync,node=%s,*' % node
    print object
    if node.endswith('Manager') == 'False':
        sync = AdminControl.completeObjectName(object)
        AdminControl.invoke(sync, 'sync')

AdminConfig.save()

#AdminConfig.modify(tc, [['startupTraceSpecification', '*=info']])
#AdminConfig.modify(tc, [['startupTraceSpecification', 'com.ibm.websphere.management.*=all=enabled:com.ibm.ws.management.*=all=enabled:com.ibm.ws.runtime.*=all=enabled']])

# getid output
# server1(cells/gzcdt60wispe/nodes/w20031/servers/server1|server.xml#Server_1216663052306)
# TraceService object
# (cells/gzcdt60wispe/nodes/w20031/servers/server1|server.xml#TraceService_1216663052311)
