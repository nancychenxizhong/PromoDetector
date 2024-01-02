import streamlit as st
import pandas as pd

#from price_fetching import googleShoppingSearch
from price_fetching import find_promo



st.title('Promo Search by Product and Named Shops')
product_name = st.text_input('Enter the product name')

all_shops = ['chemist warehouse', 'coles', 'woolworths', 'priceline']
shops = st.multiselect('Select shops to search', all_shops, default=all_shops)

if st.button('Search'):
    result_df = find_promo(product_name=product_name, shops=shops)
    st.dataframe(result_df)
