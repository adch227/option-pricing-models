import streamlit as st
from enum import Enum
from option_pricing_models import BSM_Model, Black_Model
import json


class UNDERLYING_ASSETS(Enum):
    STOCK = "Stock"
    FUTURE_CONTRACT = "Futures contract"
class PRICING_MODELS(Enum):
    BSM = "Black-Scholes-Merton"
    BLACK = "Black Model"

MODEL_MAP = {
    UNDERLYING_ASSETS.STOCK.value: PRICING_MODELS.BSM,
    UNDERLYING_ASSETS.FUTURE_CONTRACT.value: PRICING_MODELS.BLACK}

st.title("Option pricing")
st.sidebar.markdown("# Model Summary")

underlying_asset = st.selectbox("Select the option's underlying asset:", [i.value for i in UNDERLYING_ASSETS])


if underlying_asset:
    availaible_models = MODEL_MAP[underlying_asset].value
    pricing_model = st.selectbox("Select the pricing model:", availaible_models)

st.subheader(f"Pricing model: {pricing_model}")

if pricing_model == PRICING_MODELS.BSM.value and underlying_asset == UNDERLYING_ASSETS.STOCK.value:
    st.sidebar.markdown("### 📘 Black Scholes Merton Model Formulas")
    st.sidebar.latex(r"C = S_0 N(d_1) - K e^{-rT} N(d_2)")
    st.sidebar.latex(r"P = K e^{-rT} N(-d_2) - S_0 N(-d_1)")
    dividend_checkbox = st.checkbox("Dividend-paying stock?", value=False)
    if dividend_checkbox:
        dividend_yield = st.slider("Dividend yield (%):", min_value=0.0, max_value=100.0, value=2.0, step=0.1) / 100

if pricing_model:
    with st.form("Option input"):
        if pricing_model == PRICING_MODELS.BSM.value:
            spot_price = st.number_input("Spot price:", min_value=0.01, value=100.0)
        elif pricing_model == PRICING_MODELS.BLACK.value:
           st.sidebar.markdown("### 📘 Black's Model Formulas")
           st.sidebar.latex(r"C = e^{-rT} [F_0N(d_1) - KN(d_2)]")
           st.sidebar.latex(r"P = e^{-rT} [KN(-d_2) - F_0 N(-d_1)]")
           #instead of spot price, we use futures price 
           f_price = st.number_input("Futures price:", min_value=0.01, value=100.0)

        strike_price = st.number_input("Strike price:", min_value=0.01, value=100.0)
        days_to_expiry = st.number_input("Days to expiry:", min_value=1, value=30)
        risk_free_rate = st.slider("Risk-free rate (%):", min_value=0.0, max_value=100.0, value=5.0, step=0.1) / 100
        volatility = st.slider("Volatility (%):", min_value=0.0, max_value=100.0, value=20.0, step=0.1) / 100

        



        submit_button = st.form_submit_button("Calculate Option Price")


    if submit_button:
        if pricing_model == PRICING_MODELS.BSM.value:
            model = BSM_Model(spot_price, strike_price, days_to_expiry, risk_free_rate, volatility)
            if underlying_asset == UNDERLYING_ASSETS.STOCK.value and dividend_checkbox:
                call_price = model.call_price_dividend(dividend_yield)
                put_price = model.put_price_dividend(dividend_yield)
            else:
                call_price = model.call_price()
                put_price = model.put_price()
        elif pricing_model == PRICING_MODELS.BLACK.value:
            model = Black_Model(f_price, strike_price, days_to_expiry, risk_free_rate, volatility)

        st.subheader(f"Call Price: {call_price:.2f}")
        st.subheader(f"Put Price: {put_price:.2f}")





       
    




    




