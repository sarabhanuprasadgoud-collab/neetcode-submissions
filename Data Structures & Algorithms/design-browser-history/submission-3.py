class WebPageNode:
    def __init__(self, url_address: str = "", backward = None, forward = None):
        self.url_address = url_address
        self.backward = backward
        self.forward = forward

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = WebPageNode(url_address = homepage, backward = None, forward = None)

    def visit(self, url: str) -> None:
        page = WebPageNode(url_address = url, backward = self.curr, forward = None)
        self.curr.forward = page
        self.curr = page

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.backward:
            self.curr = self.curr.backward
            steps -= 1
        return self.curr.url_address
    
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.forward:
            self.curr = self.curr.forward
            steps -= 1
        return self.curr.url_address
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)