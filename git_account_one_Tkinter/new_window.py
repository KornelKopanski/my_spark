
class Windows:

    def __init__(self,tk,root):

        self.tk = tk
        self.root = root


    def create_window(self):

        window_two = self.tk.Frame(self.root)
        window_two.pack()