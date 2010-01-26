list = [auth for auth in AdminConfig.list('JAASAuthData').split('\n')]
authdict = {}
for item in list:
    authdict[AdminConfig.showAttribute(item, 'alias')] = AdminConfig.showAttribute(item, 'userId')

def dump_ds_full40(ds_list):
    for ds in ds_list:
        dsname,scope = ds.split('(')[0], ds.split('(')[1]
        print '%s : %s : %s : %s' % (scope.split('|')[0],AdminConfig.showAttribute(ds,'defaultUser'),dsname,AdminConfig.showAttribute(ds,'databaseName'))

def dump_ds_full(ds_list):
    for ds in ds_list:
        ps = AdminConfig.showAttribute(ds, 'propertySet')
        rps = AdminConfig.showAttribute(ps, 'resourceProperties')
        rpslist = [attr for attr in rps[1:len(rps)-1].split(' ') if attr.find('serverName')==0]
        sn=rpslist[0]
        authAlias=AdminConfig.showAttribute(ds, 'authDataAlias')
        if (authAlias):
            user = authdict[authAlias]
        else:
            userlist = [attr for attr in rps[1:len(rps)-1].split(' ') if attr.find('user')==0]
            un=userlist[0]
            user = AdminConfig.showAttribute(un,'value')
        dsname,scope = ds.split('(')[0], ds.split('(')[1]
        print '%s : %s : %s : %s' % (scope.split('|')[0],dsname, AdminConfig.showAttribute(sn,'value'),user)

jt400_dapi_list = AdminConfig.list('WAS40DataSource').split('\n')
#size = len(jt400_dapi_list)
#jt400_dapi_list = [was40 for was40 in was40ds_list if AdminConfig.showAttribute(was40, 'provider').find("JT400 for DAPI")>=0]
if (size > 0):
    print "Datasources (V4)"
    dump_ds_full40(jt400_dapi_list)
wasds_list = [ds for ds in AdminConfig.list('DataSource').split('\n') if ds.find('DefaultEJBTimer')<0]
print "Datasources"
dump_ds_full(wasds_list)

