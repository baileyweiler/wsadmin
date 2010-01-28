def syncer():
    for node in AdminConfig.list('Node').split('\n'):
      nodename = node.split('(')[0]
      if nodename.find('anager') < 0:
        print nodename
        sync = AdminControl.completeObjectName('type=NodeSync,node=%s,*' % nodename)
        AdminControl.invoke(sync, 'sync')


for jvm in AdminConfig.list('ProcessExecution').split('\n'):
    runAsUser=AdminConfig.showAttribute(jvm, 'runAsUser')
    runAsGroup=AdminConfig.showAttribute(jvm, 'runAsGroup')
    jvmname=jvm.split('servers/')[1].split('|')[0]
    print "%s : %s|%s" % (jvmname,runAsUser,runAsGroup) 
    if (runAsUser != 'webinst') or (runAsGroup != 'mqm') and (runAsGroup != 'apps'):
        AdminConfig.modify(jvm, [['runAsUser','webinst'],['runAsGroup','mqm']])
        runAsUser=AdminConfig.showAttribute(jvm, 'runAsUser')
        runAsGroup=AdminConfig.showAttribute(jvm, 'runAsGroup')
        print "%s : %s|%s" % (jvmname,runAsUser,runAsGroup)

AdminConfig.save()
syncer()

WebSphere:name=nodeSync,process=nodeagent,platform=common,node=at0701s,diagnosticProvider=true,version=6.1.0.13,type=NodeSync,mbeanIdentifier=nodeSync,cell=yzcdt61wiibm,spec=1.0
