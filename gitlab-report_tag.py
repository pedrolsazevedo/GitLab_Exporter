# -*- coding: utf-8 -*-
import gitlab
from datetime import datetime
from controller.general_controller import member_acl_convert
from controller.files_controller import report_cleanup

## Start a connection with GitLab instance
gl = gitlab.Gitlab.from_config('PRD', ['config\\.python-gitlab.cfg'])

# Get a project by ID
## Inser the project ID here:
project_id = 000
project = gl.projects.get(project_id)

tags = project.tags.list(all=True)

for tag in tags:
  tag_name = tag.name
  tag_message = tag.message
  tag_release = tag.release.get('description')
  print("Tag Name:" + tag_name + "\n" + "Tag Message:" + tag_message  + "\n" + tag_release)