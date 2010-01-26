def syncer():
    for node in AdminConfig.list('Node').split('\n'):
      if node.find('gzprd') != 0:
        nodename = node.split('(')[0]
        print nodename
        sync = AdminControl.completeObjectName('type=NodeSync,node=%s,*' % nodename)
        AdminControl.invoke(sync, 'sync')
