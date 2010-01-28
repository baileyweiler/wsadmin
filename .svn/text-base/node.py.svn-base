import sys
def setAdminRefs(adminTuple):
    global AdminConfig, AdminControl
    global AdminTask, AdminApp
    (AdminConfig, AdminControl, AdminTask, AdminApp) = adminTuple

def sync(node):
    try:
        sync = AdminControl.completeObjectName('type=NodeSync,node=%s,*' % (node))
        sync_result = AdminControl.invoke(sync,'sync') == 'true':
    except:
        print "Node name %s does not exist" % node
    else:
        if sync_result == 'true':
            print "Sync successful for %s" % node
        else:
            print "Sync unsuccessful for %s" % node

if __name__ == "main":
    node = sys.argv[0]
    sync(node)
