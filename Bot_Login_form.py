from binance import Client
from ttkwidgets.autocomplete import AutocompleteCombobox
from email.mime import image
from tkinter import *
import tkinter.messagebox as mesagebox
import os
from webbrowser import get
from PIL import ImageTk, Image
from functools import partial
import tkinter as tk
from tkinter import ttk
from plyer import notification
from PIL import ImageTk, Image

all_pair_info={}
client = Client()
info = client.get_all_tickers()
pairlist = []
for x in info:
    pairlist.append(x['symbol'])


whatching_list=[]
all_pair_info={}
limt_input_margin=100.0
def add_Monitor():
    value=cmb_monitor_timeframe.get()
    if value in cmb_monitor_timeframe["values"]:
        if value in whatching_list:
            mesagebox.showerror('Error','It\'s repetitive value')
        else:
            whatching_list.append(value)
            selected_values()
            mesagebox.showinfo(f"{str(value)} added to watch list","َadded")
    else:
        mesagebox.showerror('Error','It\'s invalied value, please select index of box')

def selected_values(n=None):
    lbl_chosen_pair['text']=cmb_pair.get()
    lbl_chosen_trading_timeframe['text']=cmb_trading_time.get()
    lbl_chosen_monitors_time_frame['text']='' 
    a=1
    confirm=[]   
    for items in whatching_list:
        lbl_chosen_monitors_time_frame['text']+= " - " + str(items)
        confirm.append(a)
        a+=1
        cmb_confirmation_number['values']=confirm
    lbl_chosen_confirmation_number['text']=cmb_confirmation_number.get()
    if txt_risk.get() !="" and txt_riward.get()!="":
        lbl_chosen_r_r['text']=str(txt_risk.get())+'/'+str(txt_riward.get())
    lbl_chosen_margin['text']=txt_margin.get()

a=0
def add_pair():
    global a
    global whatching_list


    if (lbl_chosen_pair['text']=='' or
        lbl_chosen_trading_timeframe['text']==''or
        lbl_chosen_monitors_time_frame['text']==''or
        lbl_chosen_confirmation_number['text']==''or
        lbl_chosen_r_r['text']==''or
        lbl_chosen_margin['text']==''):
        mesagebox.showerror('Error','Please fill all fields')
        
    elif(len(all_pair_info)==0):
        all_pair_info[a]={}
        all_pair_info[a]["Pair Name"]=str(lbl_chosen_pair['text'])
        all_pair_info[a]["Trading Time Frame"]=str(lbl_chosen_trading_timeframe['text'])
        all_pair_info[a]["Monitors Time Frame"]=whatching_list
        all_pair_info[a]["Confirmation Number"]=str(lbl_chosen_confirmation_number['text'])
        all_pair_info[a]["Risk"]=int(txt_risk.get())
        all_pair_info[a]["Riward"]=int(txt_riward.get())
        all_pair_info[a]["Margin"]=int(lbl_chosen_margin['text'])
        whatching_list=[]
        cmb_pair.set('')
        lbl_chosen_pair['text']=''
        cmb_trading_time.set('')
        lbl_chosen_trading_timeframe['text']=''
        cmb_monitor_timeframe.set('')
        lbl_chosen_monitors_time_frame['text']=''
        cmb_confirmation_number.set('')
        lbl_chosen_confirmation_number['text']=''
        txt_risk.delete(0, END)
        txt_riward.delete(0, END)
        lbl_chosen_r_r['text']=''
        txt_margin.delete(0, END)
        lbl_chosen_margin['text']=''
        print(all_pair_info)
        a+=1
        notification.notify(title = "successfully"
        ,message=f"Added successfully  {all_pair_info[a-1]['Pair Name']}  pair",
        app_icon = "bot.ico",
        timeout=2)  

    else:    
        for x in range(len(all_pair_info)):
            if (all_pair_info[x]["Pair Name"]==str(lbl_chosen_pair['text']) and
                (all_pair_info[x]["Trading Time Frame"]==str(lbl_chosen_trading_timeframe['text']))):
                 mesagebox.showerror('Error','The selected trading timeframe and currency have already been added')
                
            else:
                    all_pair_info[a]={}
                    all_pair_info[a]["Pair Name"]=str(lbl_chosen_pair['text'])
                    all_pair_info[a]["Trading Time Frame"]=str(lbl_chosen_trading_timeframe['text'])
                    all_pair_info[a]["Monitors Time Frame"]=whatching_list
                    all_pair_info[a]["Confirmation Number"]=str(lbl_chosen_confirmation_number['text'])
                    all_pair_info[a]["Risk"]=int(txt_risk.get())
                    all_pair_info[a]["Riward"]=int(txt_riward.get())
                    all_pair_info[a]["Margin"]=int(lbl_chosen_margin['text'])
                    whatching_list=[]
                    cmb_pair.set('')
                    lbl_chosen_pair['text']=''
                    cmb_trading_time.set('')
                    lbl_chosen_trading_timeframe['text']=''
                    cmb_monitor_timeframe.set('')
                    lbl_chosen_monitors_time_frame['text']=''
                    cmb_confirmation_number.set('')
                    lbl_chosen_confirmation_number['text']=''
                    txt_risk.delete(0, END)
                    txt_riward.delete(0, END)
                    lbl_chosen_r_r['text']=''
                    txt_margin.delete(0, END)
                    lbl_chosen_margin['text']=''
                    print(all_pair_info)
                    a+=1
                    notification.notify(title = "successfully"
                    ,message=f"Added successfully  {all_pair_info[a-1]['Pair Name']}  pair",
                    app_icon = "bot.ico",
                    timeout=2)  
                    # displaying time
                    break
        

#Form
register = Tk()
register.geometry('590x400')
register.title('Botich')
register.iconphoto(False,ImageTk.PhotoImage(file = 'bot.ico'))
register.config(bg='#2f3640')

# tools
lbl_pair = Label(register, text="Pair", bg='#2f3640',foreground='green', font='25')
cmb_pair = AutocompleteCombobox(register, width=27,completevalues=pairlist)
lbl_chosen_pair = Label(register, text="", bg='#2f3640',foreground='#d35400', font='25')
lbl_trading_timeframe = Label(register, text="Trading time Frame ", bg='#2f3640', foreground='green', font='25')
cmb_trading_time= AutocompleteCombobox(register, width=27,completevalues=[' 1m', ' 3m', ' 5m', ' 15m','30m', '1h', '2h', '4h', '6h', '8h','1d', '3d', '1w', '1M'])
lbl_chosen_trading_timeframe = Label(register, text="", bg='#2f3640', foreground='#d35400', font='25')
lbl_watching_time_frame= Label( register, text="Monitors time frame", bg='#2f3640', foreground='green', font='25')
cmb_monitor_timeframe= AutocompleteCombobox(register, width=27,completevalues= [' 1m', ' 3m', ' 5m', ' 15m','30m', '1h', '2h', '4h', '6h', '8h','1d', '3d', '1w', '1M'])
lbl_chosen_monitors_time_frame= Label( register, text="", bg='#2f3640', foreground='#d35400', font='25')
btn_add_watch_time = tk.Button (register, width=25,padx=1, pady=1,text="Add",command = add_Monitor)
lbl_confirmation_number = Label(register, text="Confirmation number", bg='#2f3640', foreground='green', font='25')
cmb_confirmation_number = AutocompleteCombobox(register, width=27,completevalues=['0'])
lbl_chosen_confirmation_number= Label( register, text="", bg='#2f3640', foreground='#d35400', font='25')
btn_start = tk.Button (register, width=25,padx=1, pady=1,text="Add to trade list",command=add_pair)
lbl_r_r = Label(register, text="Risck/Riward",   bg='#2f3640', foreground='green', font='25')
txt_risk = Entry(register, width=30)
txt_riward = Entry(register, width=15)
lbl_chosen_r_r = Label(register, text="",   bg='#2f3640', foreground='#d35400', font='25')
txt_margin = Entry(register, width=30)
lbl_margin= Label(register, text="Margin",   bg='#2f3640', foreground='green', font='25')
lbl_chosen_margin= Label(register, text="",   bg='#2f3640', foreground='#d35400', font='25')

#Tools grid
lbl_pair.grid(row=1, column=0, padx=50, pady=10, sticky='ew')
cmb_pair.grid( row=1,column=1,padx=10, pady=10)
lbl_chosen_pair.grid(row=1, column=2, padx=50, pady=10, sticky='ew')
lbl_trading_timeframe.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
cmb_trading_time.grid(row=3,column=1,padx=10, pady=10 )
lbl_chosen_trading_timeframe.grid(row=3,column=2,padx=10, pady=10 )
lbl_watching_time_frame.grid(row=5, column=0, padx=10, pady=10, sticky='ew')
cmb_monitor_timeframe.grid(row=5,column=1 ,padx=10, pady=10)
lbl_chosen_monitors_time_frame.grid(row=5,column=2 ,padx=10, pady=10)
btn_add_watch_time.grid( row=7,column=1 ,padx=10, pady=10)
lbl_confirmation_number.grid(row=9, column=0, padx=10, pady=10, sticky='ew')
cmb_confirmation_number.grid( row=9,column=1,padx=10, pady=10)
lbl_chosen_confirmation_number.grid(row=9, column=2, padx=10, pady=10, sticky='ew')
lbl_r_r.grid(row=11, column=0, padx=10, pady=10, sticky='ew')
txt_risk.grid( row=11,column=1,padx=10, pady=10)
txt_riward.grid(row=11,column=1, ipadx="10")
lbl_chosen_r_r.grid( row=11,column=2,padx=10, pady=10)
lbl_margin.grid( row=13,column=0,padx=10, pady=10)
txt_margin.grid(row=13,column=1,padx=10, pady=10)
lbl_chosen_margin.grid( row=13,column=2,padx=10, pady=10)
btn_start.grid(row=15,column=1, padx=10, pady=10)
cmb_pair.bind('<<ComboboxSelected>>',selected_values)
cmb_trading_time.bind('<<ComboboxSelected>>',selected_values)
txt_risk.bind('<Key>',selected_values)
txt_riward.bind('<Key>',selected_values)
txt_margin.bind('<Key>',selected_values)
cmb_monitor_timeframe.bind('<<ComboboxSelected>>',selected_values)
cmb_confirmation_number.bind('<<ComboboxSelected>>',selected_values)
#packing
cmb_pair.current()
cmb_trading_time.current()
cmb_monitor_timeframe.current()
cmb_confirmation_number.current()
register.mainloop()
