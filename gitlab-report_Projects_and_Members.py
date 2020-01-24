# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from controller.general_controller import member_acl_convert
from controller.files_controller import report_cleanup

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# File management
## Cleanup old files
report_cleanup()

## Prepare new files and open the connection
### Create and open the project file for amend
projectListFile = open("list\\projects.csv", "a")

### Project list Header
projectListFile.write('\"project_ID\";\"project_Name\";\"project_Desc\";\"project_Namespace\";\n')

## Create and open the member file for amend
members_list_file = open("list\\members.csv", "a")
## Members list Header
members_list_file.write('\"project_ID\";\"project_Name\";\"project_Desc\";\"project_Namespace\";\"member_Reg\";\"member_Name\";\"member_ACL\";\"member_ACL_DESC\";\n')

dtnow = datetime.now()

projects = gl.projects.list(all=True)

for project in projects:
  project_id = project.id
  project_name = project.name
  project_namespace = project.name_with_namespace
  project_desc = project.description

  ## File amend write
  projectListFile.write('\"%s\";\"%s\";\"%s\";\"%s\";\n'% (project_id, project_name, project_desc, project_namespace))
  members = project.members.list()

  for member in members:
    member_name = member.name
    member_usr = member.username
    member_acl = member.access_level

    member_acl_string = member_acl_convert(member_acl)

    members_list_file.write('\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";%s;\"%s\";\n'% (project_id, project_name, project_desc, project_namespace, member_usr, member_name, member_acl, member_acl_string))
members_list_file.write('\"Report Date:\";\"%s\"\n'% (dtnow))
