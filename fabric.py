#!/usr/bin/env python
# coding:utf-8
import sys
from fabric.api import *

env.roledefs = {
'docker1': ['root@123.56.220.57:22',],
'docker2': ['root@39.107.116.132:22',]
'docker3': ['root@39.96.9.16:22', ]
}
jen = ["","",""]
d1 = []
d2 = []
d3 = []
env.password = 'm-clinical'
filename='sys.argv[1]'
filepath='target'
jarname='m-eSafety-1.0-SNAPSHOT.jar'

def localcp():
    local('cp /data/jenkins/workspace/'+jarname+'/'+filepath+'/'+jarname+' /data/app/')

def localdeploy():
    local('ps -ef |grep 'jarname' |grep jar | grep -v grep | awk '{print $2}'| xargs kill -9')
    local('nohup java -jar /data/app/'jarname' >> /data/logs/nohup.log 2>&1 &')

@roles(docker1)    
def deploy():
    run('ps -ef |grep 'jarname' |grep jar | grep -v grep | awk '{print $2}'| xargs kill -9')
    run('nohup java -jar /data/app/'jarname' >> /data/logs/nohup.log 2>&1 &')

def main():
    if filename in jen:
    execute(localcp)
    execute(deploy)
    else:
    execute(localcp)
    execute(localdeploy)