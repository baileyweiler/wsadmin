import sys
scope = sys.argv[1] # 'gzpre61wispe'
scopeMP = [item for item in AdminConfig.list('MailProvider').split('\n') if item.split('|')[0].split('/')[-1] == scope ]
scopePP = [item for item in AdminConfig.list('ProtocolProvider').split('\n') if item.split('|')[0].split('/')[-1] == scope ]
for protocol in scopePP:
  type = AdminConfig.show(protocol, 'protocol')
  if type.find('smtp') >= 0:
     smtp = protocol
  elif type.find('pop3') >= 0:
     pop3 = protocol

name = ['name','StandardMailSession']
jndiName = ['jndiName', 'mail/StandardMailSession']
mailTransportHost = ['mailTransportHost','localhost']
mailTransportProtocol = ['mailTransportProtocol',smtp]
strict = ['strict', 'true']
mailStoreProtocol = ['mailStoreProtocol',pop3]
attrs = [ name, jndiName, mailTransportHost, mailTransportProtocol, strict, mailStoreProtocol ]
AdminConfig.create('MailSession', scopeMP[0], attrs)

