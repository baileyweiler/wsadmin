#!/usr/bin/bash
#
# Port Listing Script
#
# Requirements:
#
#   Requires the getPorts.py script 
#     - Modify ports_script variable to reflect location
#
# Description:
#   When run from a Deployment Manager server, it will print the ports being
# utilized by each jvm.  If multiple Deployment Managers exist, each one
# will be parsed as part of the output.
# Supports: WAS 5.1, 6.0 and 6.1
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
#  ./portreport.sh
#
# Authors:
# 
#   Marvin Gjoni <mgjoni@us.ibm.com> Thad Hinz <thadhinz@us.ibm.com>
#
# Date Created:
#
#   06/08/2008
#
was51='/usr/WebSphere51/DeploymentManager'
was60='/usr/WebSphere60/AppServer'
was61='/usr/WebSphere61/AppServer'
ports_script='./getPorts.py'
hostname=`hostname`
roles=`lssys $hostname |grep role | awk '{$1 = ""; $2 = ""; print $0}' | awk '{ 
z=split($0,flds,"; ")
for(i=1;i<=z;i++){
rolename=flds[i]
print rolename}}
'`
#echo $roles
function was51ports
{
  was51='/usr/WebSphere51/DeploymentManager/config/cells/'
  celldir=$(ls -d ${was51}*/)
  for file in $celldir; do
    was51config=${file}'nodes/'
    nodes=$(ls $was51config)
    for node in ${nodes}; do
      nodedir=$was51config$node
      $ports_script $nodedir/serverindex.xml
#/usr/WebSphere51/DeploymentManager/config/cells/yzt51ud/nodes/at0701j/servers/at0701j_ibmtest_dynamicnav
      httpdir=$(ls $nodedir/servers/ | grep -v nodeagent) 
      for http in $httpdir; do
        transportdir=$nodedir/servers/$http/server.xml
        #echo $transportdir
        $ports_script $nodedir/servers/$http/server.xml $http
      done
    done
  done 
}

function was6xports
{
  was6x=${version}/profiles/
  profiledir=$(ls -d ${was6x}*/)
  for profile in $profiledir; do
    celldir=$(ls -d ${profile}config/cells/*/)
    for file in $celldir; do
      was6xconfig=$(ls -d ${file}nodes/*/)
      for node in $was6xconfig; do 
        $ports_script ${node}serverindex.xml
      done
    done
  done  
}

#if [ -d $was51 ]
#  then
#    was51ports
#fi

for role in $roles
do
  if echo $role | grep DM |grep -q 51
  then
    was51ports
  fi
  if echo $role | grep DM |grep -q 60
  then
    version=$was60
    was6xports $version
  fi
  if echo $role | grep DM |grep -q 61
  then
    version=$was61
    was6xports $version
  fi
done
