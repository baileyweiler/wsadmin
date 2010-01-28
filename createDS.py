import sys
dslist = (('GCSDS','jdbc/GcsDB','GCS database for SPE','10','100'),('Quest','jdbc/QuestDB','Quest database for SPE','10','100'),('speDS','jdbc/SPEDB','SPE database for SPE','10','100'))
dmgr=sys.argv[1] # 'gzpre61wispeManager'
jdbcName='speJDBC_db2'
cell=dmgr.split('Manager')[0]
scope = AdminConfig.getid('/Cell:%s/' % cell)

jdbc_classpath=['classpath','${WP_DB2_JDBC_DRIVER_CLASSPATH_1};${WP_DB2_JDBC_DRIVER_CLASSPATH_11}']
jdbc_description=['description','For SPE Datasources']
jdbc_implementationClassName=['implementationClassName','com.ibm.db2.jcc.DB2XADataSource']
jdbc_name=['name',jdbcName]
jdbc_nativepath=['nativepath','${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH}']
jdbc_providerType=['providerType','DB2 Universal JDBC Driver Provider (XA)']
jdbc_xa=['xa','true']
jdbc_attrs=[jdbc_classpath, jdbc_description, jdbc_nativepath, jdbc_implementationClassName, jdbc_name, jdbc_providerType, jdbc_xa]

jdbc=AdminConfig.create('JDBCProvider', scope, jdbc_attrs)
for ds in dslist:
        name, jndi, desc, min, max = ds
        dsAttrs = [['name', name],['jndiName', jndi],['description', desc]]
        AdminConfig.create('DataSource', jdbc, dsAttrs)
        dsid = AdminConfig.getid('/DataSource:%s/' % name)
        cpid = AdminConfig.showAttribute(dsid, 'connectionPool')
        cpAttrs = [['minConnections', min], ['maxConnections', max]]
        AdminConfig.modify(cpid, cpAttrs)

for node in AdminConfig.list('Node').split('\n'):
    node = node.split('(')[0]
    object = 'type=NodeSync,node=%s,*' % node
    if node != dmgr:
        sync = AdminControl.completeObjectName(object)
        AdminControl.invoke(sync, 'sync')
        
AdminConfig.save()
