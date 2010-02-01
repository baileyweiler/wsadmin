#!/usr/bin/python
#
# serverindex.xml Parser script
#
# Description:
#
#   XML Parser specifically geared towards extracting port
# information from serverindex.xml and server.xml (for
# WAS 51 HTTP Transports).
# 
# Output:
#   Script output will be as follows:
#
#     <cell>,<node>,<jvm>,<portname>,<port>
#
#     yzcdt61udibm,at0701k,at0701k_ibm_taxonomy,WC_defaulthost_secure,9059
#
# Usage:
#
#  Current requirement is to use the wrapper script, portreport.sh
#
# Authors:
#
#   Marvin Gjoni <mgjoni@us.ibm.com>
#
# Date Created:
#
#   06/08/2008
#
import sys, string
from xml.sax import handler, make_parser
class ServerIndexHandler(handler.ContentHandler):             
    def __init__(self, outfile, **serverinfo):                   
        self.outfile = outfile
        self.server_name = serverinfo['server']
        self.port_name = ''
        self.port = ''
        self.node_name = serverinfo['node']
        self.cell = serverinfo['cell']
        self.count = 0
        self.transport_count = 0
    def startElement(self, name, attrs):                      
        self.count += 1
        if name=='serverEntries':
            self.server_name = attrs['serverName']
        if name=='specialEndpoints':
            self.port_name = attrs['endPointName']
        if name=='endPoint':
            self.port = attrs['port']
        if name=='transports':
            self.transport_count = self.count
            self.transport_ssl = attrs['sslEnabled']
        if name=='address' and self.transport_count == self.count - 1:
            if self.transport_ssl == "true":
                self.port_name = "HTTPS Transport"
            else:
                self.port_name = "HTTP Transport"
            self.port = attrs['port']
    def endElement(self, name):                              
        if name=='endPoint' or name=='address':
            self.outfile.write('%s,%s,%s,%s,%s\n' % (self.cell, self.node_name, self.server_name, self.port_name, self.port))
        if name=='serverEntries':
            self.reset_vars()
    def reset_vars(self):
        self.server_name = ''
        self.port_name = ''
        self.port = ''

def test(inFileName, cell, node, server):
    outFile = sys.stdout
    handler = ServerIndexHandler(outFile, cell=cell, node=node, server=server)
    parser = make_parser()
    parser.setContentHandler(handler)
    inFile = open(inFileName, 'r')
    parser.parse(inFile)                                   
    inFile.close()

def main():
    args = sys.argv[1:]
    if len(args) > 2:
        print 'usage: python test.py infile.xml (servername)'
        sys.exit(-1)
    info = args[0].split('/cells/')[1]
    cell = info.split('/')[0]
    node = info.split('/')[2]
    server = ''
    try:
        server = args[1]
    except:
        server = ''
    test(args[0], cell, node, server)

if __name__ == '__main__':
    main()

