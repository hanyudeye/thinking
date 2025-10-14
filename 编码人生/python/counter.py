"""_summary_
    class reposible for counting words for different files:
        - Reduce redundant code 精简冗余代码
        - Easier code management/debugging
        - Code readability
"""

class Counter:
    def __init__(self, text: str) -> None:
        self.text = text
        self.count_lower = 0
        self.count_upper = 0
        self.count()

    def count(self) -> None:
        for char in self.text:
            if char.islower():
                self.count_lower += 1
            elif char.isupper():
                self.count_upper += 1

    def get_total_lower(self) -> int:
        return self.count_lower

    def get_total_upper(self) -> int:
        return self.count_upper

    def get_total(self) -> int:
        return self.count_lower + self.count_upper