# -*- coding: utf-8 -*-

## Convert Decimal to String to make Member ACL Human readable
def memberACLConvert(memberACL):

    if memberACL == 10:
      memberStringACL = "GUEST_ACCESS"
    elif memberACL == 20:
      memberStringACL = "REPORTER_ACCESS"
    elif memberACL == 30:
      memberStringACL = "DEVELOPER_ACCESS"
    elif memberACL == 40:
      memberStringACL = "MAINTAINER_ACCESS"
    elif memberACL == 50:
      memberStringACL = "OWNER_ACCESS"
    else:
      memberStringACL = "UNRECOGNIZED ACCESS"

    return memberStringACL

def userStateConvert(userState):

    if userState == 'active':
      userStateString = "Ativo"
    elif userState == 'blocked':
      userStateString = "Bloqueado"
    else:
      userStateString = "UNRECOGNIZED ACCESS"

    return userStateString