# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET

from testData import LoginUsers


class TestData(object):

    @staticmethod
    def GetLoginUserDetails(environment):
        # Passing the path of the
        # xml document to enable the
        # parsing process
        list_of_user = []
        users = LoginUsers()
        tree = ET.parse('../testData/LoginUsers.xml')
        try:
            root = tree.getroot()
            UserNodes = root.findall(format("UserDetails/{0}/User", environment))
            for UserNode in UserNodes:
                if UserNode.attrib['ClientId'] != None:
                    users.ClientId = UserNode.Attributes["ClientId"].Value
                if UserNode.attrib['UserName'] != None:
                    users.ClientId = UserNode.Attributes["UserName"].Value
                if UserNode.attrib['Password'] != None:
                    users.ClientId = UserNode.Attributes["Password"].Value
                if UserNode.attrib['Role'] != None:
                    users.ClientId = UserNode.Attributes["Role"].Value
                list_of_user.append(users)
        except:
            pass
        return list_of_user
