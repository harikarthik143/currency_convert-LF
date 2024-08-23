import tkinter as tk
import requests #pip install requests
from tkinter import *
from tkinter import ttk

#function 
def convert():
    from_=select1.get()
    to_=select2.get()
    a=x.get()
    b=y.get()
    try:
        res = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_}')
        res.raise_for_status()  # Raises HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error with request: {e}")
        return
    
    data=res.json()
    if 'rates' not in data:
        print("Error: 'rates' not found in API response")
        return
    exchange_rate=data['rates'][to_]
    if exchange_rate is None:
        print("Error: Target currency not found in 'rates'")
        return

    amount=float(a)
    result=amount*exchange_rate
    result=format(result,'.4f')
    y.set(result)
        
window=tk.Tk()
window.title("Currency Convertor")
window.geometry("329x230")

# Set the background color of the window
window.configure(bg='#e9d7fe')

x=IntVar()
y=IntVar()
select1=StringVar()
select1.set("INR")
select2=StringVar()
select2.set("USD")

label1=tk.Label(window,text="Currency Convertor ",font=("Eras Bold ITC",18,"bold"), bg='#e9d7fe')
label1.grid(row=0,columnspan=2,padx=10,pady=10)

#entry box
entry1=tk.Entry(window,textvariable=x,width=20, font=("Eras Bold ITC", 12))
entry1.grid(row=2,column=1,padx=5)
entry2=tk.Entry(window,textvariable=y,width=20, font=("Eras Bold ITC", 12))
entry2.grid(row=3,column=1,padx=5)

combo1=ttk.Combobox(window,width=8,textvariable=select1, font=("Eras Bold ITC", 11))
combo1['values']=('CAD','HKD','ISK','PHP','DKK','HUF','CZK','GBP','RON','SEK','IDR','INR','BRL','RUB','HRK','JPY',
'THB','CHF','EUR','MYR','BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','SGD','AUD','ILS','KRW','PLN')
combo1.grid(row=2,column=0,padx=5, pady=10)

combo2=ttk.Combobox(window,width=8,textvariable=select2, font=("Eras Bold ITC", 11))
combo2['values']=('CAD','HKD','ISK','PHP','DKK','HUF','CZK','GBP','RON','SEK','IDR','INR','BRL','RUB','HRK','JPY',
'THB','CHF','EUR','MYR','BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','SGD','AUD','ILS','KRW','PLN')
combo2.grid(row=3,column=0,padx=5, pady=10)

button=tk.Button(window,command=convert,text="Convert",font=("Eras Bold ITC",13,"bold"),bg="#f4ebff")
button.grid(row=6,columnspan=2,pady=10)
window.mainloop()