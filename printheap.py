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

                     nodeagent : 256M
         v30065_ibm_search_csa : 512M
        v30065_ibm_search_csqs : 512M
             v30065_ibmcom_m2m : 512M
                  Total v30065 : 1.75G

                     nodeagent : 0M
         v30066_ibm_search_csa : 512M
        v30066_ibm_search_csqs : 512M
             v30066_ibmcom_m2m : 512M
                  Total v30066 : 1.50G
nodes = [node.split('(')[0] for node in AdminConfig.list('Node').split('\n')]
for node in nodes:
  servers = [jvm for jvm in AdminConfig.list('JavaVirtualMachine').split('\n') if jvm.split('nodes/')[1].find(node) == 0]
  totalmem = 0
  for jvm in servers:
    mem = float(AdminConfig.showAttribute(jvm, "maximumHeapSize"))
    name = jvm.split('servers/')[1].split('|')[0]
    print "%30s : %.0fM" % (name, mem)
    totalmem = totalmem + mem
  print "%30s : %.2fG" % ("Total " + node, totalmem/1024)
  print ""
