for node in AdminConfig.list('Node').split('\n'):
    node = node.split('(')[0]
    print node
    object = 'type=NodeSync,node=%s,*' % node
    print object
    if node != 'gzprd60udManager':
        sync = AdminControl.completeObjectName(object)
        AdminControl.invoke(sync, 'sync')
AdminConfig.save()


node = 'v30033'
object = 'type=NodeSync,node=%s,*' % node
sync = AdminControl.completeObjectName(object)
AdminControl.invoke(sync, 'sync')
AdminConfig.save()
