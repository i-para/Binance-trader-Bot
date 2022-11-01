###############################################################################

from datetime import datetime
from datetime import date, datetime
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import time
import pandas as pd
import numpy as np
import time
from BacktestManagement import management as backtest_management
from ExchangeManagement import management as exchange_management
from Global__init__ import backtest_set_input_ui,exchange_set_input_ui
###############################################################################
########
from functools import partial
from ttkwidgets.autocomplete import AutocompleteCombobox
import customtkinter
from tkcalendar import Calendar 
import tkinter.messagebox as mesagebox
import datetime
import datetime
from functools import partial
from tkinter import *
import customtkinter
from datetime import datetime
import pandas as pd
from ttkwidgets.autocomplete import AutocompleteCombobox
from binance.client import Client
from binance.enums import *
from tkcalendar import Calendar, DateEntry
import numpy as np
import tkinter.messagebox as mesagebox
from plyer import notification

class ui_color:
    panel_color='white'
    shaow_color='white'
    text_color='white'
    pnl_fg_color_1='white'
    pnl_fg_color_2='gray75'
    background_color='#2f3640'
    btn_hover_color='green'
    danger_hover_color='red'
    plot_backgrouand_color='white'
    upward_candle_color='green'
    downward_candle_color='red'
    chart_line_color_one='#2c82c9'
    chart_line_color_two='#2c82c9'
    stop_point_color='red'
    profits_point_color='green'
    order_point_color_1='black'
    width_full_sixe=200
    
    
    def setting(self):
        pass
    
def frm_strategy():
    
        frm_=customtkinter.CTk()
        frm_.geometry('600x370')
        frm_.title('Setting')
        customtkinter.set_appearance_mode('dark')  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
        #frm_.iconphoto(False,ImageTk.PhotoImage(file = 'botich.jpg'))
        frm_.config(bg=ui_color.background_color)
        frm_.resizable(False, False)
        pnl_main_page = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        pnl_main_page.place(relx=0.008,rely=0.1)

        frm_.mainloop()

def frm_backtest(frm_backtest=False,frm_trade=False):

        pairlist = ['BTCUSDT','ETHUSDT','DOTUSDT']
        time_frame_list = [
        '1MINUTE',
        '3MINUTE',
        '5MINUTE',
        '15MINUTE',
        '30MINUTE',
        '1HOUR',
        '2HOUR',
        '4HOUR',
        '6HOUR',
        '8HOUR',
        '1DAY'
        ]
        
        frm_=customtkinter.CTk()
        frm_.geometry('600x370')
        if frm_backtest:
            frm_.title('Backtest')
        elif frm_trade:
            frm_.title('Exchange trade')
        else:
            frm_.title('Genrate strategy')
        
        customtkinter.set_appearance_mode('dark')  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
        #frm_.iconphoto(False,ImageTk.PhotoImage(file = 'botich.jpg'))
        frm_.config(bg=ui_color.background_color)
        frm_.resizable(False, False)
        rdo_page1=customtkinter.CTkRadioButton(frm_,text='')
        rdo_page2=customtkinter.CTkRadioButton(frm_,text='')
        rdo_page3=customtkinter.CTkRadioButton(frm_,text='')
        rdo_page_0=customtkinter.CTkRadioButton(frm_,text='')
        space_left=0.45

        def trade():
            if frm_backtest: 
                try: 
                    
                    (general_dict,backtest_dc_list)=backtest_set_input_ui(server=chk_server_data.check_state, 
                                    desired_start_time=desired_start_time,
                                    desired_end_time=desired_end_time,
                                    balance=float(txt_balance.get()), 
                                    pair=str(cmb_pair.get()),
                                    time_frame=str(cmb_trading_time.get()),
                                    margin_limit=float(txt_margin_limit.get()),
                                    profit_factor=float(txt_profit_factor.get()),
                                    loss_factor=float(txt_loss_factor.get()),                                  
                                    delta_time_limit=100, 
                                    profit_limit=int(txt_profit_limit.get()),
                                    support_resistance_limit=int(txt_sr_limit.get()),
                                    change_candle_permission=chk_change.check_state,data_list_size=3)



                    backtest_management(general_dict,backtest_dc_list)
                                    
                except Exception as ex :
                         mesagebox.showerror('Error','It\'s invalied value, please fill all input ')
                         print(ex)
                

            elif frm_trade:
                try:
                    (general_dict,exchange_dc_list)=exchange_set_input_ui( 
                                        pair=str(cmb_pair.get()),
                                        time_frame=str(cmb_trading_time.get()),
                                        margin_limit=float(txt_margin_limit.get()),
                                        profit_factor=float(txt_profit_factor.get()),
                                        loss_factor=float(txt_loss_factor.get()),
                                        delta_time_limit=100, 
                                        profit_limit=int(txt_profit_limit.get()),
                                        support_resistance_limit=int(txt_sr_limit.get()),
                                        change_candle_permission=chk_change.check_state,data_list_size=3)
                    exchange_management(general_dict,exchange_dc_list)
                except Exception as ex :
                         mesagebox.showerror('Error','invalied value')
                         print(ex)

        def set_date(set_type):
            global desired_start_time, desired_end_time

            since=str(cal_since.selection_get())
            since=(since).split('-')
            print(since)
            since_up=''
            for x in since:
                since_up+=''+x+'/'
            since_up=since_up[0:-1]

            print(type(since_up),since_up)

            since= since_up+' '+txt_h.get()+':'+txt_m.get()+':0'

            
            since= datetime.strptime(since, '%Y/%m/%d %H:%M:%S')
            if set_type=='since':
                 desired_start_time = datetime(year=since.year, month=since.month, day=since.day,
                 hour=since.hour, minute=since.minute, second=59)
                 btn_start_date.set_text(str(desired_start_time))
            else:
                desired_end_time = datetime(year=since.year, month=since.month, day=since.day,
                hour=since.hour, minute=since.minute, second=59)
                btn_finish_date.set_text(str(desired_start_time))

       
        def filter_page1(page=1):
            if frm_trade: 
                if page==2:
                    if cmb_pair.get()==""or cmb_pair.get() not in pairlist:
                        lbl_error["text"]='select any index of pair list '

                    elif cmb_trading_time.get()=='' or not cmb_trading_time.get() in time_frame_list:
                        lbl_error["text"]='select any index of trading time frame list'

                    else:
                            place_page_items(page)
    
                else:
                    pass
  
            elif frm_backtest:
                    if page==2:
                        if cmb_pair.get()=="" or not cmb_pair.get()  in pairlist:
                            lbl_error["text"]='select any index of pair list '
                        elif cmb_trading_time.get()=="" or not cmb_trading_time.get()  in time_frame_list:
                            lbl_error["text"]='select any index of trading time frame list'
                        else:
                            print('s')
                            place_page_items(page)

                    elif page==3:
                       place_page_items(page)

                    else:
                        pass
                       
        def place_page_items(page=1):

            lbl_error["text"]=''
            pnl_page_1.place_forget()
            lbl_pair.place_forget()
            cmb_pair.place_forget()
            lbl_trading_time_frame.place_forget()
            cmb_trading_time.place_forget()
            btn_next_1.place_forget()
            pnl_Page2.place_forget()
            lbl_balance.place_forget()
            txt_balance.place_forget()
            lbl_margin_limit.place_forget()
            txt_margin_limit.place_forget()
            lbl_profit_limit.place_forget()
            txt_profit_limit.place_forget()
            lbl_profit_factor.place_forget()
            txt_profit_factor.place_forget()
            txt_loss_factor.place_forget()
            lbl_loss_factor.place_forget()
            lbl_sr_limit.place_forget()
            txt_sr_limit.place_forget()
            chk_change.place_forget()
            btn_next_2.place_forget()
            btn_back_2.place_forget()
            btn_start_date.place_forget()
            btn_finish_date.place_forget()
            pnl_page_3.place_forget()
            btn_next_3.place_forget()
            btn_back_3.place_forget()
            lbl_finish_dat.place_forget()
            btn_start_date.place_forget()
            lbl_start_date.place_forget()
            btn_finish_date.place_forget()
            cal_to.place_forget()
            cal_since.place_forget()
            chk_server_data.place_forget()
            rdo_page1.place_forget()
            rdo_page2.place_forget()
            rdo_page3.place_forget()
            rdo_page_0.place_forget()
            txt_h.place_forget()
            txt_m.place_forget()
            pnl_page_0 .place_forget()
            lbl_recent.place_forget()
            cmb_recent_data.place_forget()
            btn_start .place_forget()
            btn_new .place_forget()
            

            if frm_trade: 
                rdo_page1.place(relx=0.45,rely=0.015)
                rdo_page2.place(relx=0.50,rely=0.015)
                if page==0:
                    pass
                
                
                elif page==1:
                    pnl_page_1.place(relx=0.008,rely=0.1)
                    lbl_pair.place(relx=space_left,rely=0.15)
                    cmb_pair.place(relx=space_left,rely=0.22)
                    lbl_trading_time_frame.place(relx=space_left,rely=0.27)
                    cmb_trading_time.place(relx=space_left,rely=0.33)
                    btn_next_1.place(relx=0.8,rely=0.8)

                else:

                    pnl_Page2.place(relx=0.008,rely=0.1)
                    lbl_margin_limit.place(relx=space_left+0.27,rely=0.15)
                    txt_margin_limit.place(relx=space_left+0.27,rely=0.22)
                    lbl_profit_limit.place(relx=space_left,rely=0.15)
                    txt_profit_limit.place(relx=space_left,rely=0.22)
                    lbl_profit_factor.place(relx=space_left+0.27,rely=0.33)
                    txt_profit_factor.place(relx=space_left+0.27,rely=0.40)
                    lbl_loss_factor.place(relx=space_left,rely=0.33)
                    txt_loss_factor.place(relx=space_left,rely=0.40)
                    lbl_sr_limit.place(relx=space_left,rely=0.51)
                    txt_sr_limit.place(relx=space_left,rely=0.58)
                    chk_change.place(relx=space_left+0.27,rely=0.58)
                    btn_next_3.place(relx=0.8,rely=0.8)
                    btn_back_2.place(relx=-0.06,rely=0.8)

            elif frm_backtest:
                    rdo_page_0.place(relx=0.425,rely=0.015)
                    rdo_page1.place(relx=0.475,rely=0.015)
                    rdo_page2.place(relx=0.525,rely=0.015)
                    rdo_page3.place(relx=0.575,rely=0.015)
                    
                    if page==0:
                        pnl_page_0 .place(relx=0.008,rely=0.1)
                        lbl_recent.place(relx=space_left,rely=0.2)
                        cmb_recent_data.place(relx=space_left,rely=0.3)
                        btn_new .place(relx=space_left,rely=0.45)
                        btn_start .place(relx=space_left,rely=0.65)
                        
                        
                
                    elif page==1:
                        pnl_page_1.place(relx=0.008,rely=0.1)
                        lbl_pair.place(relx=space_left,rely=0.15)
                        cmb_pair.place(relx=space_left,rely=0.22)
                        lbl_trading_time_frame.place(relx=space_left,rely=0.27)
                        cmb_trading_time.place(relx=space_left,rely=0.33)
                        btn_next_1.place(relx=0.8,rely=0.8)

                    elif page==2:
                        pnl_Page2.place(relx=0.008,rely=0.1)
                        lbl_balance.place(relx=space_left,rely=0.15)
                        txt_balance.place(relx=space_left,rely=0.22)
                        lbl_margin_limit.place(relx=space_left+0.27,rely=0.15)
                        txt_margin_limit.place(relx=space_left+0.27,rely=0.22)
                        lbl_profit_limit.place(relx=space_left,rely=0.33)
                        txt_profit_limit.place(relx=space_left,rely=0.40)
                        lbl_profit_factor.place(relx=space_left+0.27,rely=0.33)
                        txt_profit_factor.place(relx=space_left+0.27,rely=0.40)
                        lbl_loss_factor.place(relx=space_left,rely=0.51)
                        txt_loss_factor.place(relx=space_left,rely=0.58)
                        lbl_sr_limit.place(relx=space_left+0.27,rely=0.51)
                        txt_sr_limit.place(relx=space_left+0.27,rely=0.58)
                        chk_change.place(relx=space_left,rely=0.69)
                        btn_next_2.place(relx=0.8,rely=0.8)
                        btn_back_2.place(relx=-0.06,rely=0.8)

                    else:
                        lbl_finish_dat.place(relx=space_left+0.42,rely=0.25)
                        btn_start_date.place(relx=space_left+0.42,rely=0.32)

                        lbl_start_date.place(relx=space_left+0.42,rely=0.43)
                        btn_finish_date.place(relx=space_left+0.42,rely=0.50)
                        pnl_page_3.place(relx=0.008,rely=0.1)
                        btn_next_3.place(relx=0.8,rely=0.8)
                        btn_back_3.place(relx=-0.06,rely=0.8)
                        cal_since.place(relx=space_left,rely=0.20)
                        cal_to.place(relx=space_left,rely=0.25)
                        chk_server_data.place(relx=space_left,rely=0.29)
                        txt_h.place(relx=space_left+0.1,rely=0.7)
                        txt_m.place(relx=space_left+0.2,rely=0.7)

        #page0
        pnl_page_0 = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        lbl_recent=customtkinter.CTkLabel(master=frm_, text='Recent Trade',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)  
        cmb_recent_data= AutocompleteCombobox(frm_, width=27,height=39,completevalues= time_frame_list)
        btn_start = customtkinter.CTkButton(frm_, text='start',width=11,command=partial(place_page_items,3),hover_color=ui_color.btn_hover_color)
        btn_new = customtkinter.CTkButton(frm_, text='+',width=11,command=partial(place_page_items,3),hover_color=ui_color.btn_hover_color)
    


        #page1
        pnl_page_1 = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        lbl_pair=customtkinter.CTkLabel(master=frm_, text='Pair',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)  
        cmb_pair = AutocompleteCombobox(frm_, width=27,height=39,completevalues=pairlist)
        lbl_trading_time_frame=customtkinter.CTkLabel(master=frm_, text='Trading time frame',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        cmb_trading_time= AutocompleteCombobox(frm_, width=27,height=39,completevalues=time_frame_list)
        btn_next_1 = customtkinter.CTkButton(frm_, text=' >> ',command=partial(filter_page1,2),hover_color=ui_color.btn_hover_color)

        #page2
        pnl_Page2 = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1,ui_color.pnl_fg_color_2 ))
        lbl_balance=customtkinter.CTkLabel(master=frm_, text='Balance',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)  
        txt_balance =customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black') 
        lbl_margin_limit=customtkinter.CTkLabel(master=frm_, text='Margin persent',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        txt_margin_limit= customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        lbl_profit_limit  =customtkinter.CTkLabel(master=frm_, text='TP count',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        txt_profit_limit =customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        lbl_profit_factor=customtkinter.CTkLabel(master=frm_, text='Between profit filter persent ',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        txt_profit_factor =customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')   
        lbl_loss_factor=customtkinter.CTkLabel(master=frm_, text='Between loss filter persent',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        txt_loss_factor =customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        lbl_sr_limit=customtkinter.CTkLabel(master=frm_, text='S/R limit',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        txt_sr_limit =customtkinter.CTkEntry(frm_, width=85, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        chk_change=customtkinter.CTkCheckBox(frm_,text='Change permision')
        btn_next_2 = customtkinter.CTkButton(frm_, text=' > ',command=partial(filter_page1,3),hover_color=ui_color.btn_hover_color)
        btn_back_2 = customtkinter.CTkButton(frm_, text=' < ',command=partial(place_page_items,1),hover_color=ui_color.btn_hover_color)
        
        #page3     
        pnl_page_3 = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        btn_next_3 = customtkinter.CTkButton(frm_, text=' Start ',command=trade,hover_color=ui_color.btn_hover_color)
        btn_back_3 = customtkinter.CTkButton(frm_, text=' < ',command=partial(place_page_items,2),hover_color=ui_color.btn_hover_color)
        btn_start_date = customtkinter.CTkButton(frm_, text='0/0/0',width=15,command=partial(set_date,'since'),hover_color=ui_color.btn_hover_color)
        btn_finish_date = customtkinter.CTkButton(frm_, text='0/0/0',width=15,command=partial(set_date,'To'),hover_color=ui_color.btn_hover_color)
        lbl_start_date=customtkinter.CTkLabel(master=frm_, text='Since',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        lbl_finish_dat=customtkinter.CTkLabel(master=frm_, text='  To  ',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)
        cal_since = DateEntry(frm_, width=20, background='darkblue',
                    foreground='white', borderwidth=2, year=2022,month=8,day=23)
        cal_to = DateEntry(frm_, width=20, background='darkblue',
                    foreground='white', borderwidth=2, year=2022,month=8,day=23)

        chk_server_data=customtkinter.CTkCheckBox(frm_,text='Exchange price')
        txt_h =customtkinter.CTkEntry(frm_, width=30, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        txt_m =customtkinter.CTkEntry(frm_, width=30, height=30, border_width=1, placeholder_text='',fg_color='white' ,text_color='black')
        lbl_error=customtkinter.CTkLabel(master=frm_, text='',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)


        
        
       
        
        place_page_items(page=0)
        lbl_error.place(relx=0.3,rely=0.8)
        frm_.mainloop()

def frm_anlize():

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams['savefig.facecolor'] = "green"
    plt.style.use('dark_background')
    #plt.style.context("seaborn-whitegrid")
    #plt.style.use('fivethirtyeight')

    fig,(price_chart,balance_chart)=plt.subplots(2,1)

    price_chart.spines['bottom'].set_color(None)
    price_chart.spines['top'].set_color(None)
    price_chart.spines['right'].set_color(None)
    price_chart.spines['left'].set_color(None)
    price_chart.patch.set_facecolor(None)


    balance_chart.spines['bottom'].set_color(None)
    balance_chart.spines['top'].set_color(None)
    balance_chart.spines['right'].set_color(None)
    balance_chart.spines['left'].set_color(None)
    balance_chart.patch.set_facecolor(None)

    def onclick(event):
        global chart_data

    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        index_value=int(event.xdata)
        finish=date_time[index_value]
        order_point_line=price_chart_data[index_value]
        finish_status=status[index_value]
        print("Status:  ",finish_status)

        fig2,(candle_stick_plt,rs_plt)=plt.subplots(2,1)
        #close open plot
        plt.close('all')
        time.sleep(1)
        start=0
        change_stop=[]
        change_profit=[]
        time_stamp=[]
    
        #find clicked info form dada base 
        for x in range(0,len(exele_fil['Position Status'])):
            if exele_fil['Date & Time'][x]==finish:
                change_profit.append(exele_fil['Profit Point'][x])
                if (exele_fil['Position Status'][x]=="Finish"):
                    time_stamp.append(exele_fil['Finish Time'][x])
                    
                    while x!=False:
                        if exele_fil['Position Status'][x]=='Start':
                            start=float(exele_fil['Date & Time'][x])
                            change_stop.append(exele_fil['Stop Point'][x])
                            change_profit.append(exele_fil['Profit Point'][x])
                            time_stamp.append(exele_fil['Date & Time'][x])
                            x=False 
                        else:
                            change_stop.append(exele_fil['Stop Point'][x])
                            change_profit.append(exele_fil['Profit Point'][x])
                            time_stamp.append(exele_fil['Date & Time'][x])
                            x-=1
                    
                    
                    
                    
                    break

                elif (exele_fil['Position Status'][x]=="Start-Finish"):
                    start=float(exele_fil['Finish Time'][x])
                    time_stamp.append(exele_fil['Finish Time'][x])
                    time_stamp.append(exele_fil['Date & Time'][x])

        print(50*'*')
        


    
        for x in range(0,len(change_profit)):
            change_profit[x]=str(change_profit[x][1:-1])
            
            change_profit [x]= str(change_profit[x]).split(",")

        for x in range(0,len(change_stop)):
            change_stop[x]=str(change_stop[x][1:-1])
            change_stop [x]= str(change_stop[x]).split(",")


        change_profit.reverse()
        time_stamp.reverse()
        change_stop.reverse()

        print(len(time_stamp)," : ",len(change_profit))
        for x in range (len(change_profit)):
            print(time_stamp[x],"  ",stop_Point[x],"   ",change_profit[x])


        #find candls from price data base
        values = pd.read_json(f'Database\\Mydata-BTCUSDT-1MINUTE-2022-01-01-2022-07-01.json')
        chart_data={"Open":[],"High":[],"Low":[],"Close":[],"Time":[]}
        for index in range(len(values["Current Time"])):
            if values["Current Time"][index]==start: 
                
                index-=10
                while  index!=False:
                    if (values["Current Time"][index]==finish): 
                        for x in range(10):
                            chart_data['Open'].append(float(values["Current Open"][index]))
                            chart_data['High'].append(float(values["Current High"][index]))
                            chart_data['Low'].append(float(values["Current Low"][index]))
                            chart_data['Close'].append(float(values["Current Close"][index]))
                            chart_data['Time'].append(values["Current Time"][index])
                            index+=1 
                        index=False    
                    else:
                        chart_data['Open'].append(float(values["Current Open"][index]))
                        chart_data['High'].append(float(values["Current High"][index]))
                        chart_data['Low'].append(float(values["Current Low"][index]))
                        chart_data['Close'].append(float(values["Current Close"][index]))
                        chart_data['Time'].append(values["Current Time"][index])

                        index+=1  

                break
                


        #set data and config into plot 
        if len(values)>0:
            stock_prices = pd.DataFrame({'close': chart_data['Close'], 'open':chart_data['Open'],
                    'low':chart_data['Low'] ,'high':chart_data['High']}
                        )
        
        plt.ylabel("BTCUSDT")
        plt.xlabel( f"Psition start time: {chart_data['Time'][10]}   Position finish time: {chart_data['Time'][-10]}")
        up = stock_prices[stock_prices.close >= stock_prices.open]
        down = stock_prices[stock_prices.close < stock_prices.open]
        col1 = 'green'
        col2 = 'red'
        width = .3
        width2 = .03
        candle_stick_plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col1)
        candle_stick_plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1)
        candle_stick_plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)
        candle_stick_plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col2)
        candle_stick_plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2)
        candle_stick_plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2,)
        plt.xticks(rotation=30, ha='right')
        candle_stick_plt.set_facecolor("#2C3333")


        #plt.set_facecolor("#ecf0f1")
        time
        color='blue'

        profit_colors_list=['#7FEB45','#00b894']
        stop_colors_list=['#c44569','#c23616']

        color_index=0
        color='red'
        

        print(chart_data['Time'])
        for change_time_stamp_index, change_time_stamp_data in enumerate(time_stamp):
            if change_time_stamp_data in chart_data['Time']:
                plt.axvline(chart_data['Time'].index(change_time_stamp_data), linestyle='--', alpha=(0.2),color=color)
                color_index=color_index+1
                if color_index==2:
                        color_index=0
                for until_chart_data_index,until_chart_data_data in enumerate(chart_data['Time']):
                    if len(time_stamp)-1>=change_time_stamp_index+1:
                        if (float(time_stamp[change_time_stamp_index+1]))==until_chart_data_data:
                            for i,draw_data in enumerate(change_profit[change_time_stamp_index]):
                                    plt.hlines(y = float(draw_data), xmin = chart_data['Time'].index(change_time_stamp_data), xmax = until_chart_data_index, color = profit_colors_list[color_index], linewidth = 0.9, label = 'linewidth = 1, default capstyle')
                            for i,draw_data in enumerate(change_stop[change_time_stamp_index]):
                                    plt.hlines(y = float(draw_data), xmin = chart_data['Time'].index(change_time_stamp_data), xmax = until_chart_data_index, color = stop_colors_list[color_index], linewidth = 0.9, label = 'linewidth = 1, default capstyle')





                                


        """color_index=color_index+1
        if color_index==2:
            color_index=0
        for x in range(len(chart_data['Time'])):
            print(x)
            if float(time_stamp[0])==chart_data['Time'][x]:
                for y in change_profit[0]:
                    plt.hlines(y = float(y), xmin = x, xmax = len(chart_data['Close'])-10, color = colors_list[color_index], linewidth = 1, label = 'linewidth = 1, default capstyle')
                break """   
        
        plt.tight_layout()
        
        plt.show()
        
    def mouse_move(event):
        global flag
        if flag==False and event.xdata !=None:
            flag=True
            price_chart.axvline(event.xdata,color="#2c82c9",markersize=20)
            balance_chart.axvline(event.xdata,color="#2c82c9",markersize=20)
            
        elif event.xdata !=None:
            price_chart.lines.pop(2)
            price_chart.axvline(event.xdata,color="#2c82c9",markersize=20)
            balance_chart.lines.pop(2)
            balance_chart.axvline(event.xdata,color="#2c82c9",markersize=20)
        elif flag==True and event.xdata ==None:
            flag=False
            price_chart.lines.pop(2)
            balance_chart.lines.pop(2)

    def show(file_name='Backtest'):
        if file_name=="Backtest":
                file_name="Excel\\Backtest\\Information\\"+cmb_backtest_list.get()
        else:
                file_name="Excel\\Exchage\\Information\\"+cmb_trade_list.get()
        
        print(file_name)
        global flag
        global balance_chart_data
        global price_chart_data
        global profits
        global stop_Point
        global exele_fil
        global date_time
        global status
        global order_point
        flag=False
        balance_chart_data=np.array([])
        price_chart_data=np.array([])
        profits=np.array([])
        stop_Point=np.array([])
        date_time=np.array([])
        status=np.array([])
        order_point=np.array([])
    
        exele_fil=pd.read_excel(file_name)
        for index in range(0,len(exele_fil['Balance'])-1):
            if exele_fil["Finish Time"][index]!='-' :
                balance_chart_data=np.append(balance_chart_data,exele_fil["Balance"][index])
                price_chart_data=np.append(price_chart_data,exele_fil["Order Point"][index])
                profits=np.append(profits,exele_fil["Profit Point"][index])
                stop_Point=np.append(stop_Point,exele_fil["Stop Point"][index])
                date_time=np.append(date_time,float(exele_fil["Date & Time"][index]))
                status=np.append(status,exele_fil["Position Status"][index])
                order_point=np.append(order_point,exele_fil["Order Point"][index])

        price_chart.set_title('Trade Result')
        price_chart.set_ylabel('Price')
        price_chart.plot(price_chart_data,color="orange")
        price_chart.set_facecolor("#2C3333")

        balance_chart.plot(balance_chart_data,color="#26a65b")
        balance_chart.set_xlabel('Date / Time')
        balance_chart.set_ylabel('Balance')
        balance_chart.set_facecolor("#2C3333")
        Cursor_price=Cursor(price_chart,horizOn=False,vertOn=False,color='green',linewidth=1.5)
        Cursor_balance=Cursor(balance_chart,horizOn=False,vertOn=False,color='green',linewidth=1.5)
        fig.canvas.mpl_connect('motion_notify_event',mouse_move)
        fig.canvas.mpl_connect('button_press_event', onclick)
        plt.tight_layout()
        plt.show()


    frm_=customtkinter.CTk()
    frm_.geometry('600x370')
    frm_.title('Setting')
    customtkinter.set_appearance_mode('dark')  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
    #frm_.iconphoto(False,ImageTk.PhotoImage(file = 'botich.jpg'))
    frm_.config(bg=ui_color.background_color)
    frm_.resizable(False, False)
    pnl_main_page = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
    import os
    analize_list = os.listdir('Excel\\Exchange\\Information')
    lbl_exchange=customtkinter.CTkLabel(master=frm_, text='Exchange data',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)  
    cmb_trade_list = AutocompleteCombobox(frm_, width=27,height=39,completevalues=analize_list)
    btn_show_trade = customtkinter.CTkButton(frm_,width=30, text=' > ',command=partial(show,'Exchange'),hover_color=ui_color.btn_hover_color)
    space_left=0.45
    backtest_list = os.listdir('Excel\\Backtest\\Information')
    lbl_backtest=customtkinter.CTkLabel(master=frm_, text='Backtest data',width=11,height=30,fg_color=('green', 'green'),corner_radius=10)  

    cmb_backtest_list = AutocompleteCombobox(frm_, width=27,height=39,completevalues=backtest_list)
    btn_show_backtest = customtkinter.CTkButton(frm_, width=30, text=' > ',command=partial(show,'Backtest'),hover_color=ui_color.btn_hover_color)
    pnl_main_page.place(relx=0.008,rely=0.1)
    lbl_exchange.place(relx=space_left,rely=0.24)
    cmb_trade_list.place(relx=space_left,rely=0.30) 
    btn_show_trade.place(relx=space_left+0.31,rely=0.30) 

    lbl_backtest.place(relx=space_left,rely=0.44)
    cmb_backtest_list.place(relx=space_left,rely=0.5)
    btn_show_backtest.place(relx=space_left+0.31,rely=0.5) 
    



    frm_.mainloop()

def _exit():
    exit()

def frm_setting():
        frm_=customtkinter.CTk()
        frm_.geometry('600x370')
        frm_.title('Setting')
        customtkinter.set_appearance_mode('dark')  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
        #frm_.iconphoto(False,ImageTk.PhotoImage(file = 'botich.jpg'))
        frm_.config(bg=ui_color.background_color)
        frm_.resizable(False, False)
        pnl_main_page = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        pnl_main_page.place(relx=0.008,rely=0.1)


        frm_.mainloop()

def frm_main():
        frm_=customtkinter.CTk()
        frm_.geometry('600x370')
        frm_.title('Main')
        customtkinter.set_appearance_mode('dark')  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
        #frm_.iconphoto(False,ImageTk.PhotoImage(file = 'botich.jpg'))
        frm_.config(bg=ui_color.background_color)
        frm_.resizable(False, False)
        pnl_main_page = customtkinter.CTkLabel(master=frm_, text='',width=590,height=300,fg_color=(ui_color.pnl_fg_color_1, ui_color.pnl_fg_color_2))
        btn_backtest = customtkinter.CTkButton(frm_, text='Backtest',width=200, height=50,command=partial(frm_backtest,frm_backtest=True),hover_color=ui_color.btn_hover_color)
        btn_trade = customtkinter.CTkButton(frm_, text='Trade',width=200, height=50,command=partial(frm_backtest,frm_trade=True),hover_color=ui_color.btn_hover_color)
        btn_exit = customtkinter.CTkButton(frm_, text=' Exit',width=200, height=50,command=_exit,hover_color=ui_color.btn_hover_color)
        btn_generate_strategy = customtkinter.CTkButton(frm_, text=' Genrate strategy ',width=200,height=50,command=frm_strategy,hover_color=ui_color.btn_hover_color)
        btn_anlize = customtkinter.CTkButton(frm_, text=' Analize ',width=200, height=50,command=frm_anlize,hover_color=ui_color.btn_hover_color)
        btn_settings = customtkinter.CTkButton(frm_, text='  Setting',width=200, height=50,command=frm_setting,hover_color=ui_color.btn_hover_color)

        pnl_main_page.place(relx=0.008,rely=0.1)
        btn_trade.place(relx=0.1,rely=0.15)
        btn_backtest.place(relx=0.5,rely=0.15)
        btn_generate_strategy.place(relx=0.1,rely=0.4)
        btn_anlize.place(relx=0.5,rely=0.4)
        btn_settings.place(relx=0.1,rely=0.65)
        btn_exit.place(relx=0.5,rely=0.65)
        frm_.mainloop()

frm_main()
