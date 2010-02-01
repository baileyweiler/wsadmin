import sys
def usage:
  print "Usage:"
  print "  sudo ./wsadmin.sh -lang jython -f genJvmArgs.py <add | remove> <jvm search> <partial arg or full (if adding)> [save]"
  print ""
  print "Example:"
  print "  sudo ./wsadmin.sh -lang jython -f genJvmArgs.py add wps -Xmx1024m"
  print ""
  print "Note: Changes will only be saved if 'save' is specified."


if len(sys.argv)<3:
  usage()
  sys.exit(1)
try:
  argSearch=sys.argv[2]
  jvmSearch=sys.argv[1]
  operation=sys.argv[0]
except:
  usage()

try:
  save=sys.argv[3]
except:
  save=None

getJvmArguments = lambda x: AdminConfig.show(x, ['genericJvmArguments']).split('genericJvmArguments ')[1][1:-2]

jvmList = [AdminConfig.getid("/Server:%s/JavaProcessDef:/JavaVirtualMachine:/" % jvm.split('(')[0]) for jvm in AdminConfig.list('Server').splitlines() if jvm.find(jvmSearch)>=0 ]
sync = map(lambda x: AdminControl.invoke(AdminControl.completeObjectName('type=NodeSync,node=%s,*' % x), 'sync'), filter(lambda y: y.find('Manager') == -1, AdminConfig.list('Node').splitlines()))

def addArgs(newArg, jvm, save):
  node = jvm.split('nodes/')[1].split('/')[0]
  newArg = newArg.replace('%HOST%', node) 
  argList = getJvmArguments(jvm)
  if argList.find(newArg) >= 0:
    print "%s already exists : %s" % (newArg, argList)
    sys.exit(1)
  else:
    new = "%s %s" % (argList, newArg)
    AdminConfig.modify(jvm, [['genericJvmArguments', new]])
    if save:
      AdminConfig.save()
      sync()

def removeArgs(argSearch, jvm, save):
  argList = getJvmArguments(jvm)
  newArgList = ' '.join([arg for arg in argList.split(' ') if arg.find(argSearch) < 0])
  jvmDisplayName = jvm.split('servers/')[1].split('|')[0]
  print jvmDisplayName
  print "%s %s" % ('Current',argList)
  AdminConfig.modify(jvm, [['genericJvmArguments', newArgList]])
  print "%s %s" % ('New',getJvmArguments(jvm))
  if save:
    AdminConfig.save()
    sync()

if __name__ == "main":
  if operation == 'add':
    map(lambda x: addArgs(argSearch, x, save), jvmList)
  elif operation == 'remove':
    map(lambda x: removeArgs(argSearch, x, save), jvmList)
