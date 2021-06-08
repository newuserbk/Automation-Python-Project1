from testbase import BaseTest


class JavaScriptUIActions(BaseTest):

    def ScrollToElement(self,element):
        Driver.Instance.execute_script("arguments[0].scrollIntoView();", element)
        pass

    def FindElement(self,javaScript):
        return Driver.Instance.execute_script(javaScript)
        pass

    def ClickElement(self,javaScript):
        link = self.FindElement(javaScript)
        link.click()
        #element = Driver.Instance.find_element_by_id("myid")
        #Driver.Instance.execute_script("arguments[0].click();", element)

