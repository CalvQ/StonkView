import sys
import yfinance as yf
import plotext as plt

from constants import *

if len(sys.argv) < 2:
    print("Usage: python main.py [$symbol...]")
    sys.exit()

tick = yf.Ticker("GME")

while(True):
    tickH = tick.history(period="1d", interval="1m")
    y = list((tickH["Open"] + tickH["Close"])/2)
    x = range(tickH.shape[0])

    plt.clp()
    plt.clt()
    plt.plot(x,y)
    plt.canvas_color("none")
    plt.axes_color("none")
    plt.ticks_color("teal")
    plt.figsize(150, 45)
    plt.sleep(0.1)
    print(yel_s(sys.argv[1]))
    plt.show()