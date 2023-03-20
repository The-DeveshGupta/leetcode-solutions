class BrowserHistory:

    def __init__(self, homepage: str):
        self.page_list = [homepage]
        self.pointer = 0


    def visit(self, url: str) -> None:
        self.page_list = self.page_list[:self.pointer+1]
        self.page_list.append(url)
        self.pointer += 1


    def back(self, steps: int) -> str:
        self.pointer = 0 if self.pointer < steps else self.pointer - steps
        return self.page_list[self.pointer]


    def forward(self, steps: int) -> str:
        self.pointer = len(self.page_list) - 1 if len(self.page_list) - 1 < self.pointer + steps else self.pointer + steps
        return self.page_list[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)