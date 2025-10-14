    """_summary_
    class reposible for counting words for different files:
        - Reduce redundant code 精简冗余代码
        - Easier code management/debugging
        - Code readability
    """

class Counter:
    def __init__(self,text: str) ->None:
        self.text = text

        #Define the initial count of the lower and upper case
        self.count_lower = 0