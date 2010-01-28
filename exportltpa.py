import java.lang.String as jstr
import java.util.Properties as jprops
import java.io as jio       
import javax.management as jmgmt
import sys                  
                            
def printUsage():           
    print ""                
    print "Usage:  <was_install_dir>/bin/wsadmin -lang jython [-user <was_user>] [-password <was_password>] -f exportLTPAKeys.py <ltpaKeyFile>"
    print "   where <was_install_dir>   is your WAS directory"
    print "         <was_user>          is WAS user"
    print "         <was_password>      is WAS user password"
    print "         <ltpaKeyFile>       is the file the LTPA keys will be exported to"
    print ""                
    print "Sample:"         
    print "===================================================================="
    print "wsadmin -lang jython -user tipadmin -password admin123" 
    print " -f \"c:\\Documents and Settings\\rkunapuli\\Desktop\\exportLTPAKeys.py\""
    print " \"c:\\\\Documents and Settings\\\\rkunapuli\\\\Desktop\\\\ltpakeys.txt\""
    print "===================================================================="
    print ""                
                            
# Verify the correct number or parameters were passed in
if not (len(sys.argv) == 1):
   sys.stderr.write("Invalid number of arguments\n")
   printUsage()             
   sys.exit(101)            

ltpaKeyFile=sys.argv[0]     
security=AdminControl.queryNames('*:*,name=SecurityAdmin,process=dmgr')
securityON=jmgmt.ObjectName(security)
params=[]                   
signature=[]                
                            
ltpaKeys=AdminControl.invoke_jmx(securityON,'exportLTPAKeys', params, signature)
                            
fout=jio.FileOutputStream(ltpaKeyFile)
ltpaKeys.store(fout,'')     
fout.close()

