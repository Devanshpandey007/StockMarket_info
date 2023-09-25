import tkinter as tk
class News_box:
    def __init__(self,win):
        LIGHT_CYAN = '#E4F1FF'
        self.win  = win
        self.box = tk.Entry(win,width=20)
        self.box.place(x=10,y=320)
        self.box2 = tk.Entry(win,width=20)
        self.box2.place(x=150,y=320)
        # fetch_news = tk.Button(win,width=10)
        self.listbox = tk.Listbox(win,width=105,height=23,font=('arial',11),bg=LIGHT_CYAN)
        self.listbox.place(x=7,y=350)
        scroll = tk.Scrollbar(win,orient= tk.VERTICAL)
        scroll.place(x=860,y=380,height=300, width=30)
        scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scroll.set)
    def get_info(self):
        self.box1_data = self.box.get()
        self.box2_data = self.box.get()


