cell='gzpre61wispe'
scope = 'Cell'
objectCacheID = AdminConfig.getid('/%s:%s/CacheProvider:/' % (scope, cell))
cacheSize = ['cacheSize', '2000']
jndi = ['jndiName', 'services/cache/spe/parameters']
description = ['description', '']
enableCacheReplication = ['enableCacheReplication', 'true']
messageBrokerDomainName = ['messageBrokerDomainName', cluster]
replicationType = ['replicationType', 'PUSH_PULL']
name = ['name', 'speUserContextCacheInstance']
attrs = [ cacheSize, jndi, description, enableCacheReplication, name, replicationType ]
id=AdminConfig.create('ObjectCacheInstance', objectCacheID, attrs)
AdminConfig.modify(id, [['disableDependencyId', 'true']])
AdminConfig.modify(id, attrs)
