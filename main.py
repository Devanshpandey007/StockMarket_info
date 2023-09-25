from News_space import News_box
from tkinter import *
from Stock_price import stock_data
from srch_company import *
from daily_news import News
class Body:
    def __init__(self):
        LIGHTBLUE = '#AED2FF'
        LIGHTCYAN = '#E4F1FF'
        self.window = Tk()
        self.window.geometry("900x750")
        self.window.config(bg=LIGHTBLUE)
        self.lst_box = Listbox(self.window, height=13, width=65, font=('Arial', 12),bg=LIGHTCYAN)
        self.lst_box.place(x=260, y=6)
        scrollbar = Scrollbar(self.window, orient=VERTICAL)
        scrollbar.place(x=860, y=5, height=310, width=30)
        self.lst_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lst_box.yview)
        self.selected_company = Text(self.window,height=1,width=25)
        self.selected_company.place(x=25,y=230)


        self.srch_obj = Serch_box(self.window)
        self.stock_obj = stock_data()
        self.news_box_instance = News_box(self.window)
        # Create Buttons
        less_day_Button = Button(self.window, width=20, text="10 Days Data", command=self.less_DData)
        less_day_Button.place(x=370, y=270)
        more_day_button = Button(self.window, width=20, text="30 Days Data", command=self.more_Ddata)
        more_day_button.place(x=570, y=270)
        news_button = Button(self.window, width=20, text="Get News", command = self.open_news )
        news_button.place(x=300,y=318)


        self.window.mainloop()
    def open_news(self):
        self.news_box_instance.get_info()
        news_obj = News(self.news_box_instance.box1_data, self.news_box_instance.box2_data)
        self.news_box_instance.listbox.delete(0, END)
        for i in range(10):
            self.news_box_instance.listbox.insert(END, f"Title: {news_obj.r_json['articles'][i]['title']}")
            # self.news_box_instance.listbox.insert(END, f"{news_obj.r_json['articles'][i]['description']}")

    def more_Ddata(self):
        self.stock_obj.update_company_data(self.srch_obj.x)
        self.stock_obj.fetch_stock_data()
        self.lst_box.delete(0, END)
        for i in range(len(self.stock_obj.extacted_data)):
            self.lst_box.insert(END, f" {self.stock_obj.extacted_data[i][0]}            Opening Price --> {self.stock_obj.extacted_data[i][1]['1. open']}            Closing Price --> {self.stock_obj.extacted_data[i][1]['4. close']}")

    def less_DData(self):
        self.stock_obj.update_company_data(self.srch_obj.x)
        self.stock_obj.fetch_stock_data()
        self.lst_box.delete(0, END)
        for i in range(10):
            self.lst_box.insert(END, f" {self.stock_obj.extacted_data[i][0]}            Opening Price --> {self.stock_obj.extacted_data[i][1]['1. open']}            Closing Price --> {self.stock_obj.extacted_data[i][1]['4. close']}")

obj = Body()



