# generate random string
# generate random number
# generate date
import string
import random


class Other_Utilities:

    @staticmethod
    def generate_random_string():
        # using random.choices()
        # generating random strings
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=10))
        return res

    @staticmethod
    def get_project_root_path():
        import os
        ROOT_DIR = os.path.abspath(os.curdir)
        return ROOT_DIR
