import sys
argSearch=sys.argv[2]
jvmSearch=sys.argv[1]
operation=sys.argv[0]
try:
  save=sys.argv[3]
except:
  save=None

getJvmArguments = lambda x: AdminConfig.show(x, ['genericJvmArguments']).split('genericJvmArguments ')[1][1:-2]

jvmList = [AdminConfig.getid("/Server:%s/JavaProcessDef:/JavaVirtualMachine:/" % jvm.split('(')[0]) for jvm in AdminConfig.list('Server').splitlines() if jvm.find(jvmSearch)>=0 ]

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
       print "save"

def removeArgs(argSearch, jvm, save):
  argList = getJvmArguments(jvm)
  newArgList = ' '.join([arg for arg in argList.split(' ') if arg.find(argSearch) < 0])
  jvmDisplayName = jvm.split('servers/')[1].split('|')[0]
  print jvmDisplayName
  print "%s %s" % ('Current',argList)
  AdminConfig.modify(jvm, [['genericJvmArguments', newArgList]])
  print "%s %s" % ('New',getJvmArguments(jvm))
  if save:
    print "save"

if __name__ == "main":
  if operation == 'add':
    map(lambda x: addArgs(argSearch, x, save), jvmList)
  elif operation == 'remove':
    map(lambda x: removeArgs(argSearch, x, save), jvmList)
