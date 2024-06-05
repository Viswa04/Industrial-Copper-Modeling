import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu

def predict_status(ctry, itmty, app, wth, prref, qtl, cslg, thlg, splg, itmdt, itmm, itmy, dldt, dldm, dldy):

    # Changing Datatypes
    itdd= int(itmdt)
    itdm= int(itmm)
    itdy= int(itmy)

    dydd= int(dldt)
    dydm= int(dldm)
    dydy= int(dldy)

    # Classification Model
    with open ("C:/Users/user/Desktop/Guvi/Visual studio code/Industrial Copper/Classification_model.pkl", 'rb') as f:
        model_class = pickle.load(f)
    
    user_data= np.array([[ctry, itmty, app, wth, prref, qtl, cslg, thlg, splg, itdd, itdm, itdy, dydd, dydm, dydy]])

    y_pred = model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry, sts, itmty, app, wth, prref, qtl, cslg, thlg, itmdt, itmm, itmy, dldt, dldm, dldy):
    # Changing Datatypes
    itdd= int(itmdt)
    itdm= int(itmm)
    itdy= int(itmy)

    dydd= int(dldt)
    dydm= int(dldm)
    dydy= int(dldy)

    # Regression Model
    with open("C:/Users/user/Desktop/Guvi/Visual studio code/Industrial Copper/Regression_Model.pkl", "rb") as f:
        model_regress = pickle.load(f)
    
    user_data = np.array([[ctry, sts, itmty, app, wth, prref, qtl, cslg, thlg, itdd, itdm, itdy, dydd, dydm, dydy]])

    y_pred = model_regress.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred

# Streamlit Page
st.set_page_config(layout="wide")

st.title(":red[*INDUSTRIAL COPPER MODELING*]")

options = option_menu('', ["PREDICT SELLING PRICE", "PREDICT STATUS"], icons=["bar-chart-fill", "front"], default_index=0, orientation='horizontal')

if options == "PREDICT STATUS":
    
    st.header(":blue[**PREDICT STATUS (WON / LOSE)**]")
    st.write('------------------')
    st.write('')

    col1, col2 = st.columns(2)
    
    with col1:
        country= st.selectbox(":green[*Select the Country*]",("25.","26.","27.","28.","30.","32.","38.","39.","40.","77.","78.","79.","80.","84.","89.","107.","113."))
        item_type= st.selectbox(":green[*Select the Item_Type*]",("0.","1.","2.","3.","4.","5.","6."))
        application= st.selectbox(":green[*Select the Application*]",("2.",  "3.",  "4.",  "5.", "10.", "15.", "19.", "20.", "22.", "25.", "26.", "27.", "28.", "29.", "38.", "39.", "40.", "41.", "42.", "56.", "58.", "59.", "65.", "66.", "67.", "68.", "69.", "70.", "79.", "99."))
        width= st.number_input(label=":green[*Enter the Value for WIDTH*/ Min:700.0, Max:1980.0]")
        product_ref= st.number_input(label=":green[*Enter the Value for PRODUCT_REF*/ Min:611728, Max:1722207579]")
        quantity_tons_log= st.number_input(label=":green[*Enter the Value for QUANTITY_TONS (Log Value)*/ Min:-0.322, Max:6.924]", format="%0.15f")
        customer_log= st.number_input(label=":green[*Enter the Value for CUSTOMER (Log Value)*/ Min:17.21910, Max:17.23015]",format="%0.15f")
        thickness_log= st.number_input(label=":green[*Enter the Value for THICKNESS (Log Value)*/ Min:-1.71479, Max:3.28154]",format="%0.15f")
    
    with col2:
        selling_price_log= st.number_input(label=":green[*Enter the Value for SELLING PRICE (Log Value)*/ Min:5.97503, Max:7.39036]",format="%0.15f")
        item_date_day= st.selectbox(":green[*Select the Day for ITEM DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox(":green[*Select the Month for ITEM DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox(":green[*Select the Year for ITEM DATE*]",("2020","2021"))
        delivery_date_day= st.selectbox(":green[*Select the Day for DELIVERY DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox(":green[*Select the Month for DELIVERY DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox(":green[*Select the Year for DELIVERY DATE*]",("2020","2021","2022"))

    st.write('---')
    st.write('')
    st.write('')
    st.write('')
    button = st.button(":orange[***PREDICT THE STATUS***]", use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,selling_price_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        if status == 1:
            st.write("## :blue[*Status* : ]:green[ *WON*]")
        else:
            st.write("## :blue[*Status* : ]:red[ *LOSE*]")

if options == "PREDICT SELLING PRICE":
    st.header(":blue[**PREDICT SELLING PRICE**]")
    st.write('------------------')
    st.write('')

    col1, col2 = st.columns(2)

    with col1:
        country= st.selectbox(":green[*Select the Country*]",("25.","26.","27.","28.","30.","32.","38.","39.","40.","77.","78.","79.","80.","84.","89.","107.","113."))
        status= st.selectbox(":green[*Select the Status*]",("0","1","2","3","4","5","6","7","8"))
        item_type= st.selectbox(":green[*Select the Item_Type*]",("0.","1.","2.","3.","4.","5.","6."))
        application= st.selectbox(":green[*Select the Application*]",("2.",  "3.",  "4.",  "5.", "10.", "15.", "19.", "20.", "22.", "25.", "26.", "27.", "28.", "29.", "38.", "39.", "40.", "41.", "42.", "56.", "58.", "59.", "65.", "66.", "67.", "68.", "69.", "70.", "79.", "99."))
        width= st.number_input(label=":green[*Enter the Value for WIDTH*/ Min:700.0, Max:1980.0]")
        product_ref= st.number_input(label=":green[*Enter the Value for PRODUCT_REF*/ Min:611728, Max:1722207579]")
        quantity_tons_log= st.number_input(label=":green[*Enter the Value for QUANTITY_TONS (Log Value)*/ Min:-0.322, Max:6.924]", format="%0.15f")
        customer_log= st.number_input(label=":green[*Enter the Value for CUSTOMER (Log Value)*/ Min:17.21910, Max:17.23015]",format="%0.15f")
    
    with col2:
        thickness_log= st.number_input(label=":green[*Enter the Value for THICKNESS (Log Value)*]/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
        item_date_day= st.selectbox(":green[*Select the Day for ITEM DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox(":green[*Select the Month for ITEM DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox(":green[*Select the Year for ITEM DATE*]",("2020","2021"))
        delivery_date_day= st.selectbox(":green[*Select the Day for DELIVERY DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox(":green[*Select the Month for DELIVERY DATE*]",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox(":greeen[*Select the Year for DELIVERY DATE*]",("2020","2021","2022"))

    st.write('---')
    st.write('')
    st.write('')
    st.write('')

    button = st.button(":orange[***PREDICT THE SELLING PRICE***]", use_container_width=True)

    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        st.write("## :blue[*The Selling Price is :*]",price)
