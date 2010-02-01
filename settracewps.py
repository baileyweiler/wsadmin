import sys
tracespec=sys.argv[1]
serverstring=sys.argv[0]

servers = [server.split('(')[0] for server in AdminConfig.list('Server').split('\n') if server.find(serverstring)>0]
for server in servers:
  ts = AdminControl.completeObjectName('type=TraceService,process=%s,*' % server)
  print "Current trace for %s: %s" % (server, AdminControl.getAttribute(ts, 'traceSpecification'))
  AdminControl.setAttribute(ts, 'traceSpecification', tracespec)
  print "New trace for %s: %s" % (server, AdminControl.getAttribute(ts, 'traceSpecification'))

