import streamlit as st
import functions

st.title('Vanilla Option Payoff Viewer')
st.text('Enter the details of the option contract to view the payoff')

strike = st.number_input('Strike Price', min_value=0.00, step=0.01)
premium = st.number_input('Premium', min_value=0.0, step=0.01)
buy = st.radio('Long or Short', ('Long', 'Short'))
call = st.radio('Call or Put', ('Call', 'Put'))

buy_choice = True if buy == 'Long' else False
call_choice = True if call == 'Call' else False

btn = st.button('Calculate')

if btn:
    strike = round(strike, 2)
    premium = round(premium, 2)
    data = functions.premium_spread(strike, premium, buy_choice, call_choice)
    
    st.write(f'Option Value at maturity of {buy} {strike} {call} with {premium} Premium')
    st.line_chart(data.set_index('Spot'))
