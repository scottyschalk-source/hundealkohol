import streamlit as st
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

st.title("Test Titel")
#Product1
col1,_,col2,=st.columns([3,1,3])
col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg",width=400, caption="Happy Customer")
col2.write("Verwöhne deinen treuen Begleiter mit dem ersten „Rotwein“ speziell für Hunde!"
         "Unser Rottweiler Rotwein ist die perfekte, alkoholfreie Ergänzung für besondere Momente."
         "Natürlich enthält dieses Produkt 0,0 % Alkohol und ist absolut frei von Weintrauben oder anderen schädlichen Zutaten."
         ""
         "Stattdessen setzen wir auf eine gesunde Mischung aus vitaminreichem Rote-Bete-Saft, feiner Fleischbrühe und ausgewählten Kräutern, die gut für Fell und Verdauung sind."
         "Serviere den Drink einfach zimmertemperiert im Napf – für den stilvollen Feierabend zu zweit!"
         )

col1,col2,_=st.columns([4, 4, 12])
increment = col1.button("put in to cart", key="button1")
if increment:
    st.session_state.product1 +=1

increment = col2.button("Take out of cart", key="button2")
if increment and st.session_state.product1 > 0:
    st.session_state.product1 -=1

st.write(f"Sie haben {st.session_state.product1} von Product1 in ihrem wahren korb")

#Product2
col1,col2,=st.columns(2)
col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", caption="Happy Customer")
col2.write("Text für später")

col1,col2,_=st.columns([4, 4, 12])
increment = col1.button("put in to cart", key="button3")
if increment:
    st.session_state.product2 +=1

increment = col2.button("Take out of cart", key="button4")
if increment and st.session_state.product2 > 0:
    st.session_state.product2 -=1

st.write(f"Sie haben {st.session_state.product2} von Product2 in ihrem wahren korb")

#Product3
col1,col2,=st.columns(2)
col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", caption="Happy Customer")
col2.write("Text für später")

col1,col2,_=st.columns([4, 4, 12])
increment = col1.button("put in to cart", key="button5")
if increment:
    st.session_state.product3 +=1

increment = col2.button("Take out of cart", key="button6")
if increment and st.session_state.product3 > 0:
    st.session_state.product3 -=1

st.write(f"Sie haben {st.session_state.product3} von Product3 in ihrem wahren korb")

#Product4
col1,col2,=st.columns(2)
col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", caption="Happy Customer")
col2.write("Text für später")

col1,col2,_=st.columns([4, 4, 12])
increment = col1.button("put in to cart", key="button7")
if increment:
    st.session_state.product4 +=1

increment = col2.button("Take out of cart", key="button8")
if increment and st.session_state.product4 > 0:
    st.session_state.product4 -=1

st.write(f"Sie haben {st.session_state.product4} von Product4 in ihrem wahren korb")


#Product5
col1,col2,=st.columns(2)
col1.image("https://i.postimg.cc/DfjtnC1B/homepagebild1.jpg", caption="Happy Customer")
col2.write("Text für später")

col1,col2,_=st.columns([4, 4, 12])
increment = col1.button("put in to cart", key="button9")
if increment:
    st.session_state.product5 +=1

increment = col2.button("Take out of cart", key="button10")
if increment and st.session_state.product5 > 0:
    st.session_state.product5 -=1

st.write(f"Sie haben {st.session_state.product5} von Product5 in ihrem wahren korb")
