from enum import Enum


class FindBy(Enum):
    ID = 1
    CLASS_NAME = 2
    CSS_SELECTOR = 3
    LINK_TEXT = 4
    NAME = 5
    TAG_NAME = 6
    XPATH = 7
    PARTIAL_LINK_TEXT=8
