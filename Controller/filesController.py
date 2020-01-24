# -*- coding: utf-8 -*-
import os

## Cleanup last report to create the new one
def reportCleanUp():
    ## Cleanup old reportFiles
    ### Remove project old files
    projectFileListExists = os.path.isfile('list\\projects.csv')
    if projectFileListExists:
      os.remove("list\\projects.csv")
    ### Remove members old files
    projectFileListExists = os.path.isfile('list\\members.csv')
    if projectFileListExists:
      os.remove("list\\members.csv")
    ### Remove users old files
    projectFileListExists = os.path.isfile('list\\users.csv')
    if projectFileListExists:
      os.remove("list\\users.csv")