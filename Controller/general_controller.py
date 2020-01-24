# -*- coding: utf-8 -*-

## Convert Decimal to String to make Member ACL Human readable
def member_acl_convert(member_acl):

    if member_acl == 10:
      member_acl_string = "GUEST_ACCESS"
    elif member_acl == 20:
      member_acl_string = "REPORTER_ACCESS"
    elif member_acl == 30:
      member_acl_string = "DEVELOPER_ACCESS"
    elif member_acl == 40:
      member_acl = "MAINTAINER_ACCESS"
    elif member_acl == 50:
      member_acl_string = "OWNER_ACCESS"
    else:
      member_acl_string = "UNRECOGNIZED ACCESS"

    return member_acl_string

def user_state_convert(user_state):

    if user_state == 'active':
      user_state_string = "Ativo"
    elif user_state == 'blocked':
      user_state_string = "Bloqueado"
    else:
      user_state_string = "UNRECOGNIZED ACCESS"

    return user_state_string