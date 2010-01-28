import sys
tracespec=sys.argv[0]
AdminControl.completeObjectName('type=TraceService,node=mynode,process=server1,*')

servers = [server.split('(')[0] for server in AdminConfig.list('Server').split('\n') if server.find('wps')>0]
for server in servers:
  ts = AdminControl.completeObjectName('type=TraceService,process=%s,*' % server)
  AdminControl.setAttribute(ts, 'traceSpecification', tracespec)

