from yahoo_fin import stock_info 
from tkinter import *
from main_script import create_order, get_account
import warnings
import numpy as np
warnings.filterwarnings("ignore")

ACCOUNT = get_account()
PORTFOLIO_VALUE = ACCOUNT['portfolio_value']


#funcs
def stock_price(): 
  
    price = stock_info.get_live_price(e1.get()) 
    Current_stock.set(price) 
  
def portfolio():
    return PORTFOLIO_VALUE


def insertitem(item):
    listbox.insert(0, item)
    

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func




master = Tk() 
master.geometry("600x400")
Current_stock = StringVar() 
  
Label(master, text="Company Symbol : ").grid(row=0, sticky=W) 
Label(master, text="Stock Result:").grid(row=3, sticky=W) 
  
result2 = Label(master, text="", textvariable=Current_stock, 
                ).grid(row=3, column=1, sticky=W) 
  
e1 = Entry(master) 
e1.grid(row=0, column=1) 


b = Button(master, text="Show", command=stock_price) 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5) 
  
#portfolio value
value = Label(master, text = str(PORTFOLIO_VALUE)).grid(row = 9, column = 1, sticky = W)


Label(master, text = 'Total Profit :').grid(row = 5, sticky = W)
Label(master, text = 'Total Loss: ').grid(row = 7, sticky = W)
Label(master, text = 'Day Profit :').grid(row = 5, column = 2, sticky = W)
Label(master, textvariable = profit()).grid(row = 5, column = 3, sticky = W)
Label(master, text = 'Day Loss :').grid(row = 7, column = 2, sticky = W)
Label(master, text = 'PORTFOLIO VALUE :').grid(row = 9, column = 0, sticky = W)
Label(master, text = 'CREATE ORDER (SYM, #): ').grid(row = 11, column = 0, sticky = W)

stepTwo = LabelFrame(master, text="ORDERS: ")
stepTwo.grid(rowspan=10, columnspan=10, sticky='nsew', 
             padx=5, pady=5, ipadx=5, ipady=5)



listbox = Listbox(stepTwo)
listbox.pack(fill = 'both', expand = True)


#create order
def place_order():
    create_order(o1.get(), o2.get(), 'buy', 'market', 'day')

def submit_data():
    content = o1.get()
    price_stock = stock_info.get_live_price(o1.get())
    rounded = np.round(price_stock, 3)
    insertitem(content + ': ' + str(rounded))



o1 = Entry(master)
o1.grid(row = 11, column = 1)
o2 = Entry(master)
o2.grid(row = 11, column = 2)

b1 = Button(master, text = 'ORDER', command = combine_funcs(place_order, submit_data))
b1.grid(row=11, column=3, columnspan=2, rowspan=2, padx=5, pady=5) 

mainloop() 