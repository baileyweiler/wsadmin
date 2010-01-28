import sys
jvmfilter = sys.argv[0]
cookiename = sys.argv[1]
sessionmanagers = [jvm for jvm in AdminConfig.list('SessionManager').split('\n') if jvm.find('connections') > 0 ]
cookies = ['name', cookiename]
cAttrs = [cookies]
for sm in sessionmanagers:
  cookie = AdminConfig.showAttribute(sm, 'defaultCookieSettings')
  AdminConfig.modify(cookie, cAttrs)
AdminConfig.save()
