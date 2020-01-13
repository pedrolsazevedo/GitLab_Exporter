# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from Controller.generalController import memberACLConvert
from Controller.filesController import reportCleanUp

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# File management
## Cleanup old files
reportCleanUp()

## Prepare new files and open the connection
### Create and open the project file for amend
projectListFile = open("list\\projects.csv", "a")

### Project list Header
projectListFile.write('\"project_ID\";\"project_Name\";\"project_Desc\";\"project_Namespace\";\n')

## Create and open the member file for amend
membersListFile = open("list\\members.csv", "a")
## Members list Header
membersListFile.write('\"project_ID\";\"project_Name\";\"project_Desc\";\"project_Namespace\";\"member_Reg\";\"member_Name\";\"member_ACL\";\"member_ACL_DESC\";\n')

dtnow = datetime.now()

projects = gl.projects.list(all=True)

for project in projects:
  projectID = project.id
  projectName = project.name
  projectNamespace = project.name_with_namespace
  projectDesc = project.description

  ## File amend write
  projectListFile.write('\"%s\";\"%s\";\"%s\";\"%s\";\n'% (projectID, projectName, projectDesc, projectNamespace))
  members = project.members.list()

  for member in members:
    memberName = member.name
    memberUsr = member.username
    memberACL = member.access_level

    memberACLString = memberACLConvert(memberACL)

    membersListFile.write('\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";%s;\"%s\";\n'% (projectID, projectName, projectDesc, projectNamespace, memberUsr, memberName, memberACL, memberACLString))
membersListFile.write('\"Report Date:\";\"%s\"\n'% (dtnow))
