
class RSI:
    def __init__(self,window_length=14,buy_signal=30,sell_signal=70) -> None:
        
        self.window_length = window_length
        self.buy_signal=buy_signal
        self.sell_signal=sell_signal
        self.prev_avg_gain = None
        self.prev_avg_loss = None
        self.rsi_data = []
        self.gains = []
        self.losses = []
        self.window = []
        self.rsi_signal = 0
        

    def set_data(self, value):
        self.rsi_data.append(value)
        self.pruduct_signal()
        #print(self.rsi_signal)

    def get_signal(self):
        return self.rsi_signal

    def get_rsi_buy_strategy(self,value):
            self.set_data(value)
            return True if self.rsi_signal < self.buy_signal else False

    def get_rsi_sell_strategy(self):
            return True if self.rsi_signal > self.sell_signal else False      
            
    def pruduct_signal(self):
        self.gains = []
        self.losses = []
        self.window = []
        self.rsi_signal = 0
        self.prev_avg_gain = None
        self.prev_avg_loss = None
        if len(self.rsi_data) > self.window_length:
            for i, price in enumerate(self.rsi_data):
                if i == 0:
                    self.window.append(price)
                    continue
                difference = round(
                    float(self.rsi_data[i]) - float(self.rsi_data[i - 1]), 2)
                if difference > 0:
                    gain = difference
                    loss = 0
                elif difference < 0:
                    gain = 0
                    loss = abs(difference)
                else:
                    gain = 0
                    loss = 0
                self.gains.append(gain)
                self.losses.append(loss)
                if i < self.window_length:
                    self.window.append(price)
                    continue
                if i == self.window_length:
                    avg_gain = sum(self.gains) / len(self.gains)
                    avg_loss = sum(self.losses) / len(self.losses)
                else:
                    avg_gain = (
                        self.prev_avg_gain * (self.window_length - 1) + gain) / self.window_length
                    avg_loss = (
                        self.prev_avg_loss * (self.window_length - 1) + loss) / self.window_length
                self.prev_avg_gain = avg_gain
                self.prev_avg_loss = avg_loss
                avg_gain = round(avg_gain, 2)
                avg_loss = round(avg_loss, 2)
                self.prev_avg_gain = round(self.prev_avg_gain, 2)
                self.prev_avg_loss = round(self.prev_avg_loss, 2)
                if avg_loss==0:
                    rs=0
                else:
                    rs = round(avg_gain / avg_loss, 2)
                self.rsi_signal = round(100 - (100 / (1 + rs)), 2)
                self.window.append(price)
                self.window.pop(0)
                self.gains.pop(0)
                self.losses.pop(0)
            self.rsi_data.pop(0)


