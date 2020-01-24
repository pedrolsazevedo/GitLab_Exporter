# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from controller.general_controller import member_acl_convert, user_state_convert
from controller.files_controller import report_cleanup

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# File management
## Cleanup old files
report_cleanup()

## Prepare new files and open the connection
### Create and open the project file for amend
user_list_file = open("list\\users.csv", "a")
user_list_file.write('\"ID\";\"Registro\";\"Nome\";\"Status\";\n')

users = gl.users.list(all=True)

for user in users:
    user_id = user.id
    user_name = user.name
    user_reg = user.username
    user_state = user_state_convert(user.state)

    ## File amend write
    user_list_file.write('\"%s\";\"%s\";\"%s\";\"%s\";\n'% (user_id, user_reg, user_name, user_state))