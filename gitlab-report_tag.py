# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from Controller.generalController import memberACLConvert
from Controller.filesController import reportCleanUp

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# Get a project by ID
## Inser the project ID here:
project_id = 000
project = gl.projects.get(project_id)

tags = project.tags.list(all=True)

for tag in tags:
  tagName = tag.name
  tagMessage = tag.message
  tagRelease = tag.release.get('description')
  print("Tag Name:" + tagName + "\n" + "Tag Message:" + tagMessage  + "\n" + tagRelease)