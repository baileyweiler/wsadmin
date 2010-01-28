vhost = 'cnp_wps60_host'
cell = AdminConfig.list('Cell').split('(')[0]
dmgr = "%s%s" % (cell, 'Manager')
for ear in AdminApp.list().split('\n'):
    webmodules = [module for module in AdminApp.listModules(ear).split('\n') if module.find("web.xml") > -1]
    for web in webmodules:
        temp = web.split('#')[1]
        war, xml = temp.split('+')
        application = "/usr/WebSphere60/AppServer/profiles/%s/config/cells/%s/applications/%s.ear/deployments/%s/%s/WEB-INF/web.xml" % (dmgr, cell, ear, ear, war)
        xmlfile = open(application, 'r')
        webxml = xmlfile.read()
        xmlfile.close()
        chunk = webxml.split("<display-name>")[1]
        name = chunk.split("</display-name>")[0]
        print name
	if name.find('cii') < 0:
          AdminApp.edit(ear, "[-MapWebModToVH [[\"%s\" %s,%s %s]]]]" % (name, war, xml, vhost))
AdminConfig.save()
node_list = [node.split('(')[0] for node in AdminConfig.list('Node').split('\n') if node.find(dmgr)!= 0]
for node in node_list:
    sync = AdminControl.completeObjectName('type=NodeSync,node=%s,*' % node)
    AdminControl.invoke(sync, 'sync')

