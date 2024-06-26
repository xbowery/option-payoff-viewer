import streamlit as st
import functions


st.set_page_config(page_title="Multiple Separate Vanilla Options Payoff Viewer", page_icon="📈")

st.title('Multiple Separate Vanilla Options Payoff Viewer')
st.sidebar.header("Multiple Separate Vanilla Options Payoff Viewer")

if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

def disable():
    st.session_state["disabled"] = True

no_contracts = st.number_input('Enter the number of option contracts', step=1, disabled=st.session_state.disabled)
st.button('Enter', on_click=disable)

if st.session_state.disabled:
    st.text('Enter the details of the option contracts to view the payoff')
    strikes, premiums, buys, calls = [], [], [], []
    for i in range(no_contracts):
        strikes.append(st.number_input(f'Contract {i + 1} Strike Price', min_value=0.00, step=0.01))
        premiums.append(st.number_input(f'Contract {i + 1} Premium', min_value=0.0, step=0.01))
        buys.append(st.radio(f'Contract {i + 1} Long or Short', ('Long', 'Short')))
        calls.append(st.radio(f'Contract {i + 1} Call or Put', ('Call', 'Put')))

    buy_choices = [True if buy == 'Long' else False for buy in buys]
    call_choices = [True if call == 'Call' else False for call in calls]

    btn = st.button('Calculate')

    if btn:
        strikes = [round(strike, 2) for strike in strikes]
        premiums = [round(premium, 2) for premium in premiums]
        data = [functions.premium_spread(strike, premium, buy, call) for strike, premium, buy, call in zip(strikes, premiums, buy_choices, call_choices)]

        for i in range(no_contracts):
            st.write(f'Option Value at maturity of {buys[i]} {strikes[i]} {calls[i]} with {premiums[i]} Premium')
            st.line_chart(data[i].set_index('Spot'))

    re_run = st.button('Re-run')
    if re_run:
        st.session_state.disabled = False
        st.experimental_rerun()
