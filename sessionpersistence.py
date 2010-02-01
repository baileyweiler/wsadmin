usessl=['useSSL', 'false']
reqto=['requestTimeout', '5']
enctype=['encryptionType', 'NONE']
numrep=['numberOfReplicas', '1']
drssettings=[usessl, reqto, enctype, numrep]
drs=['defaultDataReplicationSettings', drssettings]
name=['name', 'testdomain']
props=[drs, name]
provid=AdminConfig.getid('/Cell:/')
AdminConfig.create('DataReplicationDomain', provid, props)
AdminConfig.save()

search = 'test'
servers = [jvm.split('(')[0] for jvm in AdminConfig.list('Server').split('\n') if jvm.split('(')[0].find(search) >= 0]
for server in servers:
  id=AdminConfig.getid('/Server:%s/' % server)
  sm=AdminConfig.list('SessionManager', id)
  datarep=['dataReplicationMode', 'BOTH']
  mbdm=['messageBrokerDomainName', 'testdomain']
  spattrs=[datarep, mbdm]
  sessionpersistence=['sessionDRSPersistence', spattrs]
  spmode=['sessionPersistenceMode', 'DATA_REPLICATION']
  spattributes=[sessionpersistence, spmode]
  AdminConfig.modify(sm, spattributes)
AdminConfig.save()

[accessSessionOnTimeout true]
[allowSerializedSessionAccess false]
[context (cells/gzcdt61wiibm/nodes/w20065/servers/w20065_connections_homepage|server.xml#WebContainer_1239911042407)]
[defaultCookieSettings "[[domain []]
[maximumAge -1]
[name SESSION_ibmcdt_connections]
[path /]
[secure false]]"]
[enable true]
[enableCookies true]
[enableProtocolSwitchRewriting false]
[enableSSLTracking false]
[enableSecurityIntegration false]
[enableUrlRewriting false]
[maxWaitTime 5]
[properties []]
[sessionDRSPersistence "[[dataReplicationMode BOTH]
[ids []]
[messageBrokerDomainName cdt_cluster_ibmconnections_m2m]
[overrideHostConnectionPoints []]
[properties []]]"]
[sessionDatabasePersistence "[[datasourceJNDIName jdbc/Sessions]
[db2RowSize ROW_SIZE_4KB]
[password *****]
[tableSpaceName []]
[userId db2admin]]"]
[sessionPersistenceMode DATA_REPLICATION]
[tuningParams "[[allowOverflow true]
[invalidationSchedule "[[firstHour 14]
[secondHour 2]]"]
[invalidationTimeout 30]
[maxInMemorySessionCount 1000]
[scheduleInvalidation false]
[usingMultiRowSchema false]
[writeContents ONLY_UPDATED_ATTRIBUTES]
[writeFrequency END_OF_SERVLET_SERVICE]
[writeInterval 10]]"]

