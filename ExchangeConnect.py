###############################################################################

from binance.client import Client
from binance.enums import *
from RoundFloor import round_floor
from EmailConnect import EMAIL_ACCOUNT
import time
import os

###############################################################################

class ExchangeConnect:
    def __init__(self, api_key, api_secret):
        # Clients
        self.api_key = api_key
        self.api_secret = api_secret
        self.secret_client = Client(self.api_key, self.api_secret)

        '''fees = self.secret_client.get_trade_fee(symbol='ETHUSDT')
        print(fees)'''

        # Connect to account on exchange
        asset_info = self.secret_client.get_asset_balance('USDT')
        print("Asset Type: ", asset_info['asset'],"\nFree Balance: ", asset_info['free'], "\nLocked Balance: ", asset_info['locked'])
        EMAIL_ACCOUNT.send_email(subject="Connection successfully", my_message=f"Bot is ONLINE.\n\nAsset Type: {asset_info['asset']}\nFree Balance: {asset_info['free']}\nLocked Balance: {asset_info['locked']} (USDT)")

    def check_open_orders(self, pair):
        profit_status_list = []
        profit_point_list = []
        loss_margin_list = []
        gain_margin_list = []
        margin_list = []
        trail_stop_point_list = []
        orderId = None
        stop_point = None
        order_point = None
        start = False
        position = False
        previous_candle_status = "None"
        open_orders_status = self.secret_client.get_open_orders(symbol=pair)
        if len(open_orders_status)>0:
            position = True
            all_orders = self.secret_client.get_all_orders(symbol=pair)
            all_orders.reverse()

            for item in all_orders:
                if item['type'] == 'LIMIT':
                    if item['status'] == 'FILLED' or item['status'] == 'NEW':
                        order_point = round_floor(float(item['price']),2)
                        if item['side'] == 'BUY':
                            previous_candle_status = "Upward_Candle"
                        elif item['side'] == 'SELL': 
                            previous_candle_status = "Downward_Candle" 
                        break

            for order in open_orders_status:
                if order['type'] == 'LIMIT_MAKER':
                    print("open order append PROFIT")
                    margin_list.append(round_floor(round_floor(float(order['origQty']),5)*order_point,8))
                    gain_margin_list.append(round_floor(round_floor(float(order['origQty']),5)*round_floor(float(order['price']),2),8))
                    profit_status_list.append(order)
                    profit_point_list.append(round_floor(float(order['price']),2))
                    start = True
                elif order['type'] == 'STOP_LOSS_LIMIT':
                    print("open order append STOP")
                    loss_margin_list.append(round_floor(round_floor(float(order['origQty']),5)*round_floor(float(order['price']),2),8))
                    stop_point = round_floor(float(order['price']),2)
                    start = True
                elif order['type'] == 'LIMIT':
                    print("open buy order append")
                    orderId = order['orderId']    

            if start:
                trail_stop_point_list += profit_point_list
                trail_stop_point_list.append(order_point)
                trail_stop_point_list.reverse()
                #trail_stop_point_list.append(stop_point)
                EMAIL_ACCOUNT.send_email(subject="Open Order Status", my_message=f"Order price:{order_point}\nStop price: {str(stop_point)}\nProfit price: {str(profit_point_list)}")
            else:
                EMAIL_ACCOUNT.send_email(subject="Open Order Status", my_message=f"Order not started yet\nOrder price:{order_point}")
        return profit_status_list, orderId, start, position, order_point, stop_point, profit_point_list, previous_candle_status, loss_margin_list, gain_margin_list, margin_list, trail_stop_point_list 
    
    def get_balance(self, asset_type):
        print("Get Balance")
        time.sleep(0.2)
        asset = self.secret_client.get_asset_balance(asset_type)
        balance = float(asset['free'])
        print(f"Balance({asset_type}) is : {balance}")
        return balance

    def get_locked_balance(self, asset_type):
        print("Get Balance")
        time.sleep(0.2)
        asset = self.secret_client.get_asset_balance(asset_type)
        locked_balance = float(asset['locked'])
        print(f"Balance({asset_type}) is : {locked_balance}")
        return locked_balance

    def check_asset(self):
        print("Check asset")
        if self.get_balance(asset_type='USDT') <= 11:
            print("Low asset!")
            EMAIL_ACCOUNT.send_email(subject="Low asset!", my_message="Your asset is lower than 11 (USDT)")
            return False
        else:
            print("Check asset is successfully")
            return True

    def get_order_info(self, pair, orderId):
        #print("Get order info")
        return self.secret_client.get_order(symbol=pair, orderId=orderId)

    def send_order_limit_buy(self, pair, margin_limit, order_point):
        print("Send order limit buy")
        balance = (self.get_balance(asset_type='USDT') - margin_limit)
        quantity = round_floor(balance/order_point,5)
        print("Quantity: ", quantity)
        margin = round_floor(quantity*order_point,8)
        print("Margin: ", margin)
        order_limit_buy_info = self.secret_client.order_limit_buy(
            symbol=pair, quantity=quantity, price=order_point)
        orderId = order_limit_buy_info['orderId']
        EMAIL_ACCOUNT.send_email(subject="Order Send", my_message=f"Order price:{order_point}\nBalance: {self.get_balance(asset_type='USDT')}\nMargin: {str(margin)}\nQuantity :{str(quantity)}")
        print("Order limit buy sending is successfully")
        return orderId, balance , quantity

    def send_order_cancel(self, pair, orderId):
        self.secret_client.cancel_order(symbol=pair, orderId=orderId)
        print("Order canceling is successfully")

    def send_oco_order(self, pair, stop_point, profit_point_list, quantity, order_point):
        print("Send OCO order")
        profit_status_list = []
        loss_margin_list = []
        gain_margin_list = []
        margin_list = []
        quantity = round_floor(quantity/len(profit_point_list),5)
        stop_point=round_floor((stop_point-(stop_point*0.00001)), 2)
        oco_profit_point_list=profit_point_list.copy()
        oco_profit_point_list.reverse()
        for profit in oco_profit_point_list[:]:
            if profit == oco_profit_point_list[-1]:
                print("Last quantity")
                quantity = round_floor(self.get_balance('BTC'),5)
            print('profit price: ',profit)
            print("stop price: ",stop_point)
            print("Quantity: ",quantity)
            margin_list.append(round_floor(quantity*order_point,8))
            loss_margin_list.append(round_floor(stop_point*quantity,8))
            gain_margin_list.append(round_floor(profit*quantity,8))
            create_oco_order_info = self.secret_client.create_oco_order(symbol=pair,
                                                                            side=SIDE_SELL,
                                                                            stopLimitTimeInForce=TIME_IN_FORCE_GTC,
                                                                            quantity=quantity,
                                                                            stopPrice=stop_point,
                                                                            stopLimitPrice=stop_point,    
                                                                            price=profit)
            for i in range(0,2):
                order = create_oco_order_info['orderReports'][i]
                if order['type'] == 'LIMIT_MAKER':
                    profit_status_list.append(order)
                    #print("order id:",profit_status_list)
        #margin_list.reverse()
        #gain_margin_list.reverse()
        #loss_margin_list.reverse()
        #print("Balance(USDT): ",self.get_balance(asset_type='USDT')," --- Balance(BTC): ",self.get_balance(asset_type='BTC'))
        #print("Profit status list: ",profit_status_list)

        profit_status_list.reverse()
        gain_margin_list.reverse()
        loss_margin_list.reverse()
        margin_list.reverse()
        print("Margin List: ",margin_list)
        print("Gain Margin List: ",gain_margin_list)
        print("Loss Margin List: ",loss_margin_list)
        print("OCO order sending is successfully")
        return profit_status_list, loss_margin_list, gain_margin_list, margin_list

###############################################################################
        
# Exchange Accounts:
EXCHANGE_ACCOUNT = ExchangeConnect(api_key=os.environ.get('API_Key'), api_secret=os.environ.get('API_Secret'))