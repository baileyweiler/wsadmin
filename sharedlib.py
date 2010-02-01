Usage: /usr/WebSphere61/AppServer/bin/wsadmin.sh -lang jython -f thisthingdownbelow.py

# Make sure that libraries path pastes as 1 line

nodelist = ['v10037', 'v10038', 'v20037', 'v20038', 'v30037', 'v30038']
wpsLibrary=('WPSlib','/projects/spe_gz_ha_shared_61/lib;/projects/spe_gz_ha_shared_61/properties;/projects/spe_gz_ha_wps_61/lib;/projects/spe_gz_ha_wps_61/lib/ecc;/projects/spe_gz_ha_wps_61/lib/webidentity;/projects/spe_gz_ha_wps_61/properties/shared;/projects/spe_gz_ha_wps_61/properties/spe;/projects/spe_gz_ha_wps_61/properties/spe/add_portlet;/projects/spe_gz_ha_wps_61/properties/spe/generic_list;/projects/spe_gz_ha_wps_61/properties/spe/home;/projects/spe_gz_ha_wps_61/properties/spe/machine_translation_selector;/projects/spe_gz_ha_wps_61/properties/spe/merchandising;/projects/spe_gz_ha_wps_61/properties/spe/nojavascriptproductselector;/projects/spe_gz_ha_wps_61/properties/spe/page_title;/projects/spe_gz_ha_wps_61/properties/spe/product_selector;/projects/spe_gz_ha_wps_61/properties/spe/returnlink;/projects/spe_gz_ha_wps_61/properties/spe/search;/projects/spe_gz_ha_wps_61/properties/spe/search_by_doc_type;/projects/spe_gz_ha_wps_61/properties/spe/shared;/projects/spe_gz_ha_wps_61/properties/spe/sign_in_reminder;/projects/spe_gz_ha_wps_61/properties/spe/spe_content_palette;/projects/spe_gz_ha_wps_61/properties/spe_notification;/projects/spe_gz_ha_wps_61/properties/spe/support_feedback;/projects/spe_gz_ha_wps_61/properties/spe/system_availability;/projects/spe_gz_ha_wps_61/properties/upr;/projects/spe_gz_ha_wps_61/properties/sss/crs;/projects/spe_gz_ha_wps_61/properties/sss/DocDisplay;/projects/spe_gz_ha_wps_61/properties/sss/warranty;/projects/spe_gz_ha_wps_61/properties/sss/DynamicMatrixPortlet;/projects/spe_gz_ha_wps_61/properties/ecc;/projects/spe_gz_ha_wps_61/properties/esa;/projects/spe_gz_ha_wps_61/properties/sr;${USER_INSTALL_ROOT}/PortalServer/config;${WPS_HOME}/shared/app;${USER_INSTALL_ROOT}/PortalServer/config/contentLib;${WPS_HOME}/base/wp.script/shared/app/scripting/wp.link.jar;${WPS_HOME}/base/wp.ai.api/script/shared/app/scripting/wp.ai.api.script.jar;${WPS_HOME}/base/wp.ai.io.impl/script/shared/app/scripting/wp.ai.io.impl.script.jar;${WPS_HOME}/shared/app/scripting/wp.link.jar;/usr/WebSphere61/PortalServer/wcm/shared/app')
facLibrary=('spe_gz_ha_session_facade_61_library','/projects/spe_gz_ha_session_facade_61/lib;/projects/spe_gz_ha_session_facade_61/properties;/projects/spe_gz_ha_session_facade_61/lib/fix;/projects/spe_gz_ha_session_facade_61/properties/fix;/projects/spe_gz_ha_shared_61/lib;/projects/spe_gz_ha_shared_61/properties;/projects/spe_gz_ha_wps_61/lib/ecc;/projects/spe_gz_ha_wps_61/properties/ecc;/projects/spe_gz_ha_wps_61/lib/Mediator.jar')

wpslib = [lib for lib in AdminConfig.list('Library').split('\n') if lib.find('WPSlib') == 0]
faclib = [lib for lib in AdminConfig.list('Library').split('\n') if lib.find('spe_gz_ha_session_facade_61_library') == 0]
for lib in wpslib:
    name, newcp = wpsLibrary
# Modifying the shared library seems to only work when it is emptied first
    AdminConfig.modify(lib, [['classPath', '']]) 
    AdminConfig.modify(lib, [['classPath', newcp]])
for lib in faclib:
    name, newcp = facLibrary
# Modifying the shared library seems to only work when it is emptied first
    AdminConfig.modify(lib, [['classPath', '']])
    AdminConfig.modify(lib, [['classPath', newcp]])
AdminConfig.save()

for node in nodelist:
  sync = AdminControl.completeObjectName('type=NodeSync,node=%s,*' % node)
  AdminControl.invoke(sync, 'sync')

Usage: /usr/WebSphere61/AppServer/bin/wsadmin.sh -lang jython -f thisthingdownbelow.py

cell='gzprd61wispe'
cellid=AdminConfig.getid('/Cell:%s/' % cell)
libraries=('spe_gz_ha_session_facade_library','Library for the session facade EAR','/projects/spe_gz_ha_session_facade_61/properties;/projects/spe_gz_ha_shared_61/properties;/projects/spe_gz_ha_wps_61/lib/ecc;/projects/spe_gz_ha_wps_61/properties/ecc;/projects/spe_gz_ha_wps_61/lib/Mediator.jar')
name, desc, classpath = libraries
print name, classpath, desc
AdminConfig.create('Library', cellid, [['name', name], ['classPath', classpath], ['description', desc]])


node_list = [node.split('(')[0] for node in AdminConfig.list('Node').split('\n') if node.find(cell)!=0]
for node in node_list:
    print node
    object = 'type=NodeSync,node=%s,*' % node
    print object
    sync = AdminControl.completeObjectName(object)
    AdminControl.invoke(sync, 'sync')
AdminConfig.save()

wpslib = [lib for lib in AdminConfig.list('Library').split('\n') if lib.find('WPSlib') == 0]
faclib = [lib for lib in AdminConfig.list('Library').split('\n') if lib.find('spe_gz_ha_session_facade_61_library') == 0]
showCP = lambda x: AdminConfig.show(x, ['classPath'])
modCP = lambda x,y: AdminConfig.modify(x, [['classPath', y]])

newfacLP = "/projects/spe_gz_ha_session_facade_61/properties;/projects/spe_gz_ha_shared_61/properties;/projects/spe_gz_ha_wps_61/lib/ecc;/projects/spe_gz_ha_wps_61/properties/ecc;/projects/spe_gz_ha_wps_61/lib/Mediator.jar"

newwpsLP = "/projects/spe_gz_ha_shared_61/properties;/projects/spe_gz_ha_wps_61/lib;/projects/spe_gz_ha_wps_61/lib/ecc;/projects/spe_gz_ha_wps_61/lib/webidentity;/projects/spe_gz_ha_wps_61/properties/shared;/projects/spe_gz_ha_wps_61/properties/spe;/projects/spe_gz_ha_wps_61/properties/spe/add_portlet;/projects/spe_gz_ha_wps_61/properties/spe/generic_list;/projects/spe_gz_ha_wps_61/properties/spe/home;/projects/spe_gz_ha_wps_61/properties/spe/machine_translation_selector;/projects/spe_gz_ha_wps_61/properties/spe/merchandising;/projects/spe_gz_ha_wps_61/properties/spe/page_title;/projects/spe_gz_ha_wps_61/properties/spe/product_selector;/projects/spe_gz_ha_wps_61/properties/spe/search;/projects/spe_gz_ha_wps_61/properties/spe/search_by_doc_type;/projects/spe_gz_ha_wps_61/properties/spe/shared;/projects/spe_gz_ha_wps_61/properties/spe/sign_in_reminder;/projects/spe_gz_ha_wps_61/properties/spe/spe_content_palette;/projects/spe_gz_ha_wps_61/properties/spe_notification;/projects/spe_gz_ha_wps_61/properties/spe/support_feedback;/projects/spe_gz_ha_wps_61/properties/spe/system_availability;/projects/spe_gz_ha_wps_61/properties/upr;/projects/spe_gz_ha_wps_61/properties/sss/crs;/projects/spe_gz_ha_wps_61/properties/sss/DocDisplay;/projects/spe_gz_ha_wps_61/properties/sss/warranty;/projects/spe_gz_ha_wps_61/properties/sss/DynamicMatrixPortlet;/projects/spe_gz_ha_wps_61/properties/ecc;/projects/spe_gz_ha_wps_61/properties/esa;/projects/spe_gz_ha_wps_61/properties/sr;${USER_INSTALL_ROOT}/PortalServer/config;${WPS_HOME}/shared/app;${USER_INSTALL_ROOT}/PortalServer/config/contentLib;${WPS_HOME}/base/wp.script/shared/app/scripting/wp.link.jar;${WPS_HOME}/base/wp.ai.api/script/shared/app/scripting/wp.ai.api.script.jar;${WPS_HOME}/base/wp.ai.io.impl/script/shared/app/scripting/wp.ai.io.impl.script.jar;${WPS_HOME}/shared/app/scripting/wp.link.jar;/usr/WebSphere61/PortalServer/wcm/shared/app"

def display(cp):
  for item in cp.split(';'):
    print item
  
def modify(lib,newcp):
  cp = showCP(lib).split(' ')[1][:-1]
  print "Old paths for : %s" % lib
  print ""
  display(cp)
  print ""
  modCP(lib,newcp)
  cp = showCP(lib).split(' ')[1][:-1]
  print "New Paths for : %s" % lib
  print ""
  display(cp)

for lib in wpslib:
  modify(lib, newwpsLP)

for lib in faclib:
  modify(lib, newfacLP)
