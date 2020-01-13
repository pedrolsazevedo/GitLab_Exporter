# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from Controller.generalController import memberACLConvert, userStateConvert
from Controller.filesController import reportCleanUp

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# File management
## Cleanup old files
reportCleanUp()

## Prepare new files and open the connection
### Create and open the project file for amend
userListFile = open("list\\users.csv", "a")
userListFile.write('\"ID\";\"Registro\";\"Nome\";\"Status\";\n')

users = gl.users.list(all=True)

for user in users:
    userID = user.id;
    userName = user.name
    userReg = user.username;
    userState = userStateConvert(user.state);

    ## File amend write
    userListFile.write('\"%s\";\"%s\";\"%s\";\"%s\";\n'% (userID, userReg, userName, userState));