nodes = [node.split('(')[0] for node in AdminConfig.list('Node').split('\n')]
for node in nodes:
  servers = [jvm for jvm in AdminConfig.list('JavaVirtualMachine').split('\n') if jvm.split('nodes/')[1].find(node) == 0]
  totalmem = 0
  for jvm in servers:
    mem = float(AdminConfig.showAttribute(jvm, "maximumHeapSize"))
    name = jvm.split('servers/')[1].split('|')[0]
    print "%s : %.0fM" % (name, mem)
    totalmem = totalmem + mem
  print "Total for node %s : %.2fG" % (node, totalmem/1024)
