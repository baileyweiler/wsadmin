cell = AdminConfig.list('Cell').split('(')[0]
dmgr = "%s%s" % (cell, 'Manager')
def modify(id):
  current = AdminConfig.show(id, ['genericJvmArguments']).split('genericJvmArguments ')[1][1:-2]
  print "Current"
  print current
  print "New"
  new = "%s %s" % (current, "-Dsun.net.inetaddr.ttl=120")
  print AdminConfig.modify(id, [['genericJvmArguments', new]])
  print AdminConfig.show(id, ['genericJvmArguments'])
  print ""

def process(search):
  jvmlist = [server.split('(')[0] for server in AdminConfig.list('Server').split('\n') if server.find(search) > 0 ]
  [modify(AdminConfig.getid("/Server:%s/JavaProcessDef:/JavaVirtualMachine:/" % jvm)) for jvm in jvmlist]

process('wps')
process('facade')
AdminConfig.save()
syncNode = lambda x: AdminControl.invoke(AdminControl.completeObjectName('type=NodeSync,node=%s,*' % x), 'sync') 
node_list = [syncNode(node.split('(')[0]) for node in AdminConfig.list('Node').split('\n') if node.find(dmgr)!=0]



