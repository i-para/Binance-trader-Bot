# Load the data via Python's CSV module
import csv
from multiprocessing.sharedctypes import Value
from binance.client import Client
client = Client()
values = client.get_historical_klines(
    "BTCUSDT", client.KLINE_INTERVAL_1MINUTE, "2022-9-5 07:27","2022-9-7 10:12")
data=[]
for x in range(0,(len(values)-1)):
    data.append(values[x][2])

print(data)




window_length = 14
gains = []
losses = []
window = []

prev_avg_gain = None
prev_avg_loss = None
output = [['date', 'close', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rsi']]
wilder_data=data

for i, price in enumerate(wilder_data):
    if i == 0:
        window.append(price)
        output.append([i+1, price, 0, 0, 0, 0, 0])
        continue
    difference = round(float(wilder_data[i]) - float(wilder_data[i - 1]), 2)
    if difference > 0:
        gain = difference
        loss = 0

    elif difference < 0:
        gain = 0
        loss = abs(difference)

    else:
        gain = 0
        loss = 0

    gains.append(gain)
    losses.append(loss)

    if i < window_length:
        window.append(price)
        output.append([i+1, price, gain, loss, 0, 0, 0])
        continue

    if i == window_length:
        avg_gain = sum(gains) / len(gains)
        avg_loss = sum(losses) / len(losses)

    else:
        avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
        avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length

    prev_avg_gain = avg_gain
    prev_avg_loss = avg_loss

    avg_gain = round(avg_gain, 2)
    avg_loss = round(avg_loss, 2)
    prev_avg_gain = round(prev_avg_gain, 2)
    prev_avg_loss = round(prev_avg_loss, 2)
    rs = round(avg_gain / avg_loss, 2)

    rsi = round(100 - (100 / (1 + rs)), 2)

    window.append(price)
    window.pop(0)
    gains.pop(0)
    losses.pop(0)

    # Save Data
    output.append([i+1, price, gain, loss, avg_gain, avg_loss, rsi])


for x in output[:]:
    
        print(x[6])

