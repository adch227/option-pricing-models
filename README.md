# Option Valuation

## Introduction to repository

The repository contains a web app with a purpose of calculating European option prices. It was created using open-source framework "Streamlit"

## Option Pricing Models

### 1. Black-Scholes-Merton  Model
Developed in 1970s by Fischer Black, Myron Scholes, and Robert Merton. The
model has had a huge influence on the way that traders price and hedge derivatives. In
1997, the importance of the model was recognized when Robert Merton and Myron
Scholes were awarded the Nobel prize for economics. Unfortuantely, Fischer Black died in 1995,
otherwise he too would undoubtedly have been one of the recipients of this prize.

**The Black–Scholes–Merton** differential equation is an equation that must be satisfied
by the price of any derivative dependent on a non-dividend-paying stock.

$$ \frac{\partial f}{\partial t} + r S \frac{\partial f}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 f}{\partial S^2} = r f $$

Above Equation is a Black–Scholes–Merton differential equation. It has many
solutions, corresponding to all the different derivatives that can be defined with S as
the underlying variable. The particular derivative that is obtained when the equation is
solved depends on the boundary conditions that are used. These specify the values of the
derivative at the boundaries of possible values of S and t. In the case of a European call
option, the key boundary condition is f = max(S - K, 0) when t = T

#### Assumptions

The assumptions that were used to derive the Black–Scholes–Merton differential equation are
as follows:
1. The stock price follows the process of **geometric brownian motion** with drift and volatility constant.
2. The short selling of securities with full use of proceeds is permitted.
3. There are no transaction costs or taxes. All securities are perfectly divisible.
4. There are no dividends during the life of the derivative.
5. There are no riskless arbitrage opportunities.
6. Security trading is continuous.
7. The risk-free rate of interest, r, is constant and the same for all maturities.

To price a derivative with a dividend-paying underlying asset, we have to make a few adjustments.

### 2. Black's Model

The Commodity Futures Trading Commission in the U.S. authorized the trading of
options on futures on an experimental basis in 1982. Permanent trading was approved
in 1987, and since then the popularity of the contract has grown very fast.
In 1976, Fischer Black proposed a model, now known as Black’s model, for valuing
European options on futures. The model has proved to be an
important alternative to the Black–Scholes–Merton model for valuing a wide range of
European spot options.
