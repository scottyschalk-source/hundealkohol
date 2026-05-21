import os
import streamlit as st
price1 = 3
price2 = 5
price3 = 7
price4 = 8
price5 = 21

if "product1" not in st.session_state:
    st.session_state["product1"] = 0
if "product2" not in st.session_state:
    st.session_state["product2"] = 0
if "product3" not in st.session_state:
    st.session_state["product3"] = 0
if "product4" not in st.session_state:
    st.session_state["product4"] = 0
if "product5" not in st.session_state:
    st.session_state["product5"] = 0
if "rabatq" not in st.session_state:
    st.session_state["rabatq"] = 0
if "rabat" not in st.session_state:
    st.session_state["rabat"] = 0
if "total" not in st.session_state:
    st.session_state["total"] = 0
if "totalnew" not in st.session_state:
    st.session_state["totalnew"] = 0

st.title("Test Titel")
#Product1
col1, col2, col3, col4 = st.columns(4)
increment = col3.button("put in to cart", key="button1")
if increment:
    st.session_state.product1 +=1

increment = col4.button("Take out of cart", key="button2")
if increment and st.session_state.product1 > 0:
    st.session_state.product1 -=1

col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", width=150, caption="Vorschaubild")
col2.write(f"Sie Kaufen {st.session_state.product1} von product1 das macht {st.session_state.product1 * price1}€")


#Product2
col1, col2, col3, col4 = st.columns(4)
increment = col3.button("put in to cart", key="button3")
if increment:
    st.session_state.product2 +=1

increment = col4.button("Take out of cart", key="button4")
if increment and st.session_state.product2 > 0:
    st.session_state.product2 -=1

col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", width=150, caption="Vorschaubild")
col2.write(f"Sie Kaufen {st.session_state.product2} von product2 das macht {st.session_state.product2 * price2}€")

#Product3
col1, col2, col3, col4 = st.columns(4)
increment = col3.button("put in to cart", key="button5")
if increment:
    st.session_state.product3 +=1

increment = col4.button("Take out of cart", key="button6")
if increment and st.session_state.product3 > 0:
    st.session_state.product3 -=1

col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", width=150, caption="Vorschaubild")
col2.write(f"Sie Kaufen {st.session_state.product3} von product3 das macht {st.session_state.product3 * price3}€")

#Product4
col1, col2, col3, col4 = st.columns(4)
increment = col3.button("put in to cart", key="button7")
if increment:
    st.session_state.product4 +=1

increment = col4.button("Take out of cart", key="button8")
if increment and st.session_state.product4 > 0:
    st.session_state.product4 -=1

col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", width=150, caption="Vorschaubild")
col2.write(f"Sie Kaufen {st.session_state.product4} von product4 das macht {st.session_state.product4 * price4}€")

#Product5
col1, col2, col3, col4 = st.columns(4)
increment = col3.button("put in to cart", key="button9")
if increment:
    st.session_state.product5 +=1

increment = col4.button("Take out of cart", key="button10")
if increment and st.session_state.product5 > 0:
    st.session_state.product5 -=1

col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", width=150, caption="Vorschaubild")
col2.write(f"Sie Kaufen {st.session_state.product5} von product5 das macht {st.session_state.product5 * price5}€")

#calc total
st.session_state.total = st.session_state.product1*price1+st.session_state.product2*price2+st.session_state.product3*price3+st.session_state.product4*price4+st.session_state.product5*price5
st.write(f"Sie zahlen {st.session_state.total}€")

#Rabat code eingabe
rabatq = st.text_input(
    "Rabat Code"
)


if rabatq == "charly5" and st.session_state.total > 10:
    st.session_state.totalnew = st.session_state.total * 0.95
    st.write(f"Sie zahlen {round(st.session_state.totalnew,2)}€")
elif rabatq == "charly10" and st.session_state.total > 30:
    st.session_state.totalnew = st.session_state.total * 0.90
    st.write(f"Sie zahlen {round(st.session_state.totalnew, 2)}€")
elif rabatq == "charly20" and st.session_state.total > 70:
    st.session_state.totalnew = st.session_state.total * 0.80
    st.write(f"Sie zahlen {round(st.session_state.totalnew, 2)}€")
else:
    st.write(f"Sie zahlen {st.session_state.total}€")
