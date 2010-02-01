for ds in AdminConfig.list('DataSource').split('\n'):
  dsname = ds.split('(')[0]
  if dsname.find('DefaultEJBTimerDataSource') == 0:
    continue
  dsid = AdminConfig.getid('/DataSource:%s/' % dsname)
  print '%s: %s' % (dsname, AdminControl.testConnection(dsid))
