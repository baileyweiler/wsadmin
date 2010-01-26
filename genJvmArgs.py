import sys
argSearch=sys.argv[2]
jvmSearch=sys.argv[1]
operation=sys.argv[0]
#newwpsargs=sys.argv[1]
try:
  save=sys.argv[3]
except:
  save=''
#jvms = {}

getJvmArguments = lambda x: AdminConfig.show(x, ['genericJvmArguments']).split('genericJvmArguments ')[1][1:-2]

jvmList = [AdminConfig.getid("/Server:%s/JavaProcessDef:/JavaVirtualMachine:/" % jvm.split('(')[0]) for jvm in AdminConfig.list('Server').splitlines() if jvm.find(jvmSearch)>=0 ]
#map(lambda x: displayGJA(x), jvmList)

def addArgs(newArg, jvm, save):
  node = jvm.split('nodes/')[1].split('/')[0]
  newArg = newArg.replace('%HOST%', node) 
  argList = getJvmArguments(jvm)
  if argList.find(newArg) >= 0:
    print "%s already exists : %s" % (newArg, argList)
    sys.exit(1)
  else:
    new = "%s %s" % (argList, newArg)
    AdminConfig.modify(id, [['genericJvmArguments', new]])

def printCols(item1,item2):
  firstCol = 10 - len(item1)
  print "%(buffer)-2s %( )s %(gen)s" % {'buffer': item1, ' ': ' '*firstCol, 'gen':item2}

def removeArgs(argSearch, jvm, save):
  argList = getJvmArguments(jvm)
  newArgList = ' '.join([arg for arg in argList.split(' ') if arg.find(argSearch) < 0])
  jvmDisplayName = jvm.split('servers/')[1].split('|')[0]
  if (save != 'save'):
    print jvmDisplayName
    printCols("Current",argList)
    printCols("New",newArgList)
  else:
    print jvmDisplayName
    AdminConfig.modify(jvm, [['genericJvmArguments', newArgList]])
    print getJvmArguments(jvm)

if operation == 'add':
  map(lambda x: addArgs(argSearch, x, save), jvmList)
elif operation == 'remove':
  map(lambda x: removeArgs(argSearch, x, save), jvmList)
