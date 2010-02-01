print AdminConfig.list('VariableMap')

ds_list = [ds for ds in AdminConfig.list('WAS40DataSource').split('\n') if ds.find('support_electronic_itsdapiDS')>=0]
${OS400_TOOLBOX_JDBC_DRIVER_PATH}/jt400.jar

ds = AdminConfig.getid('/WAS40DataSource:support_electronic_itsdapiDS/')
AdminControl.testConnection(ds)
rchasa51.rchland.ibm.com
esvcas01a.boulder.ibm.com

Custom properties
esvcas01a

ds_list = [ds for ds in AdminConfig.list('WAS40DataSource').split('\n')  if ds.find('support_electronic_itsdapi')==0 and ds.find('clusters/p1')>=0]
print AdminConfig.attributes('WAS40DataSource')
#category String
#connectionPool WAS40ConnectionPool
#databaseName String
#defaultPassword String
#defaultUser String
#description String
#jndiName String
#name String
#propertySet J2EEResourcePropertySet
#provider J2EEResourceProvider@
#providerType String
sys.exit(1)
prop_dict = {'databaseName':'rchasa51', 'serverName':'rchasa51.rchland.ibm.com'}
def find_prop(cp, prop_dict):
    found = [prop for prop in prop_dict.keys() if cp.find(prop)==0]
    return len(found)
      
def modify_cp(mod, prop_dict):
    for prop in prop_dict.keys(): 
        print 'AdminConfig.modify %s %s' % (mod, prop_dict[prop])
        AdminConfig.modify(mod, [['value', prop_dict[prop]]])

ds_list = [ds for ds in AdminConfig.list('WAS40DataSource').split('\n')  if ds.find('support_electronic_itsdapi')==0 and ds.find('clusters/p1')>=0]

for ds in ds_list:
    AdminConfig.modify(ds_list[0], [['databaseName', 'rchasa51.rchland.ibm.com']])
    ds_props = AdminConfig.showAttribute(ds_list[0],'propertySet')
    props = AdminConfig.showAttribute(ds_props, 'resourceProperties')[1:-1]
    cp_list = props.split(' ')
    mod_list = [cp for cp in cp_list if find_prop(cp, prop_dict)]
    [modify_cp(mod, prop_dict) for mod in mod_list]

AdminConfig.save()
cluster_id = [cluster for cluster in AdminConfig.list('ServerCluster').split('\n') if cluster.find('p1_prod_cluster_cnp_support_electronic_itsdapi')==0]
cluster_members = AdminConfig.showAttribute(cluster_id[0], 'members')[1:-1].split(' ')
node_list = [AdminConfig.showAttribute(cluster, 'nodeName') for cluster in cluster_members]
sync_list = [AdminControl.completeObjectName('type=NodeSync,node=' + node + ',*') for node in node_list]
synced = [AdminControl.invoke(sync,'sync') for sync in sync_list]
