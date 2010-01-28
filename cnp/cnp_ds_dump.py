def dump_ds_full(ds_list):
    for ds in ds_list:
        dsname = ds.split('(')[0]
        size = len(dsname)
        format = size + 6
        print '*' * format
        print '** ' + dsname + ' **'
        print '*' * format
        print AdminConfig.attribute('databaseName')
        print '\n'
    
if __name___ == '__main__':
    was40ds_list = AdminConfig.list('WAS40DataSource').split('\n')
    jt400_dapi_list = [was40 for was40 in was40ds_list if AdminConfig.showAttribute(was40, 'provider').find("JT400 for DAPI")>=0]
    dump_ds_full(jt400_dapi_list)
