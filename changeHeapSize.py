filter = 'facade'
newheap = '1024'
heap = ['maximumHeapSize', newheap]
jvmattrs = [heap]
modify = lambda x: AdminConfig.modify(AdminConfig.list('JavaVirtualMachine',x) , jvmattrs)
jvms = [ modify(jvm) for jvm in AdminConfig.list('Server').split('\n') if jvm.find(filter) >= 0 ]
sync = lambda x: AdminControl.completeObjectName('type=NodeSync,node=%s,*' % x)
AdminConfig.save()
nodesync = [ sync(node) for node in AdminConfig.list('Node').split('\n') if node.find('Manager') < 0 ]
