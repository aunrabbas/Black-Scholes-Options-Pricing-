import yfinance as yf
from scipy.stats import norm 
import matplotlib.pyplot as plt 
import math as math 
import numpy as np


strike = int(input("What Strike Price?: "))
stock = int(input("What's Stock Price?: "))
vol =  float(input("What's implied volatility?(Decimal): "))
time = int(input("How long till option expiry? (Years)"))
rate = float(input("What is Risk Free Interest rate? (Decimal): "))




def call_calculate(strike, stock, vol, time, rate):
    d1 = (math.log(stock/strike) + (rate + (vol**2)/2)*time)/vol*math.sqrt(time)
    d2 = d1 - vol*(math.sqrt(time))
    call = norm.cdf(d1)*stock - (norm.cdf(d2)*(strike)*(math.e**(-rate*time)))
    return call 

def put_calculate(strike, stock, vol, time, rate):
    d1 = (math.log(stock/strike) + (rate + (vol**2)/2)*time)/vol*math.sqrt(time)
    d2 = d1 - vol*(math.sqrt(time))
    put = (norm.cdf(-d2)*(strike)*(math.e**(-rate*time))) - norm.cdf(-d1)*stock
    return put


vol_values = np.linspace(0.5*vol, 1.5*vol, 10).round(2)
sto_values = np.linspace(0.8*stock, 1.2*stock, 10).round(2)
call_heatmap = []
put_heatmap = []

for v in range(len(vol_values)):
    call_list = []
    put_list = []
    for s in range(len(sto_values)):
        call_list.append(call_calculate(strike, sto_values[s], vol_values[v], time, rate).round(2))
        put_list.append(put_calculate(strike, sto_values[s], vol_values[v], time, rate).round(2))
    call_heatmap.append(call_list)
    put_heatmap.append(put_list)




fig, ax = plt.subplots(1,2,figsize = (13,6.75))

# for calls 
ax[0].imshow(call_heatmap)
ax[0].set_xticks(range(len(sto_values)), sto_values)
ax[0].set_yticks(range(len(vol_values)), vol_values)
ax[0].set_xlabel = "Stock Price"
ax[0].set_title("Call", fontweight= 700)

for i in range(len(vol_values)):
    for j in range(len(sto_values)):
        text = ax[0].text(j, i, call_heatmap[i][j],
                       ha="center", va="center", color="w")
        

# # for puts 

ax[1].imshow(put_heatmap)
ax[1].set_xticks(range(len(sto_values)), sto_values)
ax[1].set_yticks(range(len(vol_values)), vol_values)
ax[1].set_xlabel = "Stock Price"
ax[1].set_title("Put", fontweight= 700 )

for i in range(len(vol_values)):
    for j in range(len(sto_values)):
        text = ax[1].text(j, i, put_heatmap[i][j],
                       ha="center", va="center", color="w")
        


fig.suptitle("Black Scholes Options Calculator", fontweight='bold')
plt.tight_layout()
plt.show()