from datetime import time

import requests

import Driver


# @pytest.mark.usefixtures("setup")


class BaseTest:

    @staticmethod
    def go_to_url(url):
        print(".............Launching Application URL : " + url)
        # Driver.Instance.get(url)
        Driver.Instance.get(url)

    @staticmethod
    def maximize_window_size():
        print("..............Maximizing browser window..............")
        Driver.Instance.maximize_window()

    @staticmethod
    def refresh_browser():
        print("..............Refreshing browser window..............")
        Driver.Instance.refresh()

    @staticmethod
    def SwitchToDefaultContent():
        print(".............switching to default content..........")
        Driver.Instance.SwitchTo().DefaultContent()

    @staticmethod
    def switch_to_active_window():
        # get current window handle
        p = Driver.Instance.current_window_handle

        # get first child window
        chwd = Driver.Instance.window_handles

        for w in chwd:
            # switch focus to child window
            if (w != p):
                Driver.Instance.switch_to.window(w)
                break
        time.sleep(5000)
        print("Child window title: " + Driver.Instance.title)
        # try Driver.Instance.window_handles[1] or [2]

    @staticmethod
    def switch_to_first_child_window():
        # prints parent window title
        print("Parent window title: " + Driver.Instance.title)

        # get current window handle
        p = Driver.Instance.current_window_handle

        # get first child window
        chwd = Driver.Instance.window_handles

        for w in chwd:
            # switch focus to child window
            if (w != p):
                Driver.Instance.switch_to.window(w)
                break
        time.sleep(5)
        print("Child window title: " + Driver.Instance.title)

    @staticmethod
    def CloseCurrentWindow():
        Driver.Instance.close()

    @staticmethod
    def CheckStatusCode():
        pass

    @staticmethod
    def get_page_status_code(PageUrl):
        response = requests.Response
        return response.status_code

    @staticmethod
    def IsPageURLCorrect(expected_url):
        print("verifying browser page url")
        Driver.WaitTillPageURLContains(expected_url)
        actual_url = Driver.Instance.current_url
        print("Actual URL : " + actual_url)
        print("Expected URL : " + expected_url)

    @staticmethod
    def CheckPageTitleStatus():
        pass
        if ("404 Error Page" in Driver.Instance.title) or ("Can???t reach this page" in Driver.Instance.title) or (
                "403" in Driver.Instance.title):
            return True

    @staticmethod
    def GetPageStatusCode(page_url):
        response = requests.get(page_url)
        return response.status_code

    @staticmethod
    def IsCorrectPageStatusCode(page_url):
        print("...Checking Page Status Code is correct...")
        http_status_code = BaseTest.GetPageStatusCode(page_url)
        flag = None
        if "InternalServerError" in http_status_code:
            flag = False
        elif "NotFound" in http_status_code:
            flag = False
        elif "ServiceUnavailable" in http_status_code:
            flag = False
        elif "Forbidden" in http_status_code:
            flag = False
        # when no internet connection
        elif "site can???t be reached" in http_status_code:
            flag = False
        # when VPN switch happens
        elif "connection was interrupted" in http_status_code:
            flag = False
        else:
            flag = True

        if not flag:
            print("The url: " + page_url + " is broken. Http status code : " + http_status_code)
        else:
            print("The url: " + page_url + " is Correct. Http status code : " + http_status_code)

    @staticmethod
    def check_http_status_code_page(page_url):
        print("check http page status code")
        try:
            js = '''
            let callback = arguments[0];
            let xhr = new XMLHttpRequest();
            xhr.open('GET', 'https://stackoverflow.com/', true);
            xhr.onload = function () {
                if (this.readyState === 4) {
                    callback(this.status);
                }
            };
            xhr.onerror = function () {
                callback('error');
            };
            xhr.send(null);
            '''

            status_code = Driver.Instance.execute_async_script(js)
            print(status_code)  # 200
            return status_code

        except Exception as ex:
            print("page status not found : "+ex)