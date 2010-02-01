import sys
try:
  search = sys.argv[0]
except:
  print "Please specify a search filter for the LDAPUserRegistry"
  sys.exit()

def delete(host):
  print "\nDeleting %s : %s\n" % (getHost(host), host)
  AdminConfig.remove(host)

def getHostList(search):
  return [hostid for hostid in AdminConfig.showAttribute(ldap, 'hosts')[1:-1].split(' ') if getHost(hostid).find(search) >= 0]

getHost = lambda x: AdminConfig.showAttribute(x, 'host')
getPort = lambda x: AdminConfig.showAttribute(x, 'port')

ldap=AdminConfig.list("LDAPUserRegistry")
hostList=getHostList(search)

for host in hostList:
  name = "%s:%s" % (getHost(host), getPort(host))
  print "LDAPUserRegistry: %s \nLDAPServer: %s" % (host, name)
  answer = raw_input("Delete this host? (y/n) ")
  if answer == 'y':
    delete(host)

saveYN = raw_input("Save configuration? (y/n) ")
if saveYN == 'y':
  AdminConfig.save()

