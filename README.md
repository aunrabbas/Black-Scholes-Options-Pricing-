# Black-Scholes Options Pricing Calculator

An options pricing calculator that implements the Black-Scholes model from scratch and visualizes how call and put prices respond to changes in volatility and underlying stock price, displayed as side-by-side heatmaps.

<img width="1261" height="659" alt="Screenshot 2026-08-02 at 6 07 55 PM" src="https://github.com/user-attachments/assets/5c717c7f-f53d-4a07-80a3-bb55ddf76195" />


## What it does

- Takes five inputs: stock price, strike price, implied volatility, time to expiration, and risk-free rate
- Computes **d1 and d2** using the Black-Scholes formula
- Calculates **call price and put price** using the cumulative normal distribution (scipy)
- Generates a **volatility × stock price grid** — 10 volatility levels from 50% to 150% of input vol, 10 stock price levels from 80% to 120% of input price
- Renders **dual side-by-side heatmaps** — call prices on the left, put prices on the right
- Annotates each cell with the exact dollar price for that combination of inputs

## The math

```
d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 - σ√T

Call = S·N(d1) - K·e^(-rT)·N(d2)
Put  = K·e^(-rT)·N(-d2) - S·N(-d1)
```

Where N() is the cumulative standard normal distribution function.

## How to read the heatmap

- **X-axis** — stock price range (80%–120% of input price)
- **Y-axis** — implied volatility range (50%–150% of input volatility)
- **Color intensity** — brighter = more expensive option
- **Call heatmap** — prices increase moving right (stock rises toward/past strike) and down (higher volatility)
- **Put heatmap** — prices increase moving left (stock falls away from strike) and down (higher volatility)

The mirror-image relationship between the two heatmaps visually demonstrates put-call parity.

## Stack

```
scipy.stats  — cumulative normal distribution N(d1), N(d2)
numpy        — grid generation via linspace
matplotlib   — dual heatmap visualization with cell annotations
math         — log, sqrt, exp for formula components
```

## Usage

```bash
pip install scipy numpy matplotlib
python options_calculator.py
```

Enter inputs when prompted:
```
Strike price, Stock price, Implied volatility (decimal), Time (years), Risk-free rate (decimal)
```

Example: Strike 100, Stock 100, Vol 0.2, Time 1, Rate 0.05 → Call ~$10.45, Put ~$5.57

