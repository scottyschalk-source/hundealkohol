import os
import streamlit as st

# Realistische Preise aus dem Tech-Shop zuweisen
price1 = 799.00   # Kamera
price2 = 349.00   # Kamera-Linse
price3 = 999.00   # Smartphone
price4 = 49.99    # Powerbank
price5 = 1249.00  # Laptop

# Session States initialisieren
if "product1" not in st.session_state: st.session_state["product1"] = 0
if "product2" not in st.session_state: st.session_state["product2"] = 0
if "product3" not in st.session_state: st.session_state["product3"] = 0
if "product4" not in st.session_state: st.session_state["product4"] = 0
if "product5" not in st.session_state: st.session_state["product5"] = 0

st.title("🛒 Dein Warenkorb & Checkout")
st.write("Überprüfe deine Auswahl und schließe deine Bestellung ab.")
st.write("---")

# ==========================================
# PRODUKT-LISTE IM WARENKORB
# ==========================================

# Spalten-Verhältnis für ein sauberes E-Commerce Layout
col_layout = [1.5, 2.5, 1, 1]

# Product 1: Kamera
if st.session_state.product1 > 0:
    col1, col2, col3, col4 = st.columns(col_layout)
    col1.image("media/product1.jpg", width=120)
    col2.metric("📸 High-End Kamera", f"{st.session_state.product1}x", f"{round(st.session_state.product1 * price1, 2)} €")
    if col3.button("➕", key="button1", use_container_width=True):
        st.session_state.product1 += 1
        st.rerun()
    if col4.button("➖", key="button2", use_container_width=True):
        st.session_state.product1 -= 1
        st.rerun()

# Product 2: Linse
if st.session_state.product2 > 0:
    col1, col2, col3, col4 = st.columns(col_layout)
    col1.image("media/product2.jpg", width=120)
    col2.metric("🔍 L-Series Prime Linse", f"{st.session_state.product2}x", f"{round(st.session_state.product2 * price2, 2)} €")
    if col3.button("➕", key="button3", use_container_width=True):
        st.session_state.product2 += 1
        st.rerun()
    if col4.button("➖", key="button4", use_container_width=True):
        st.session_state.product2 -= 1
        st.rerun()

# Product 3: Smartphone
if st.session_state.product3 > 0:
    col1, col2, col3, col4 = st.columns(col_layout)
    col1.image("media/product3.jpg", width=120)
    col2.metric("📱 Nexus X1 Smartphone", f"{st.session_state.product3}x", f"{round(st.session_state.product3 * price3, 2)} €")
    if col3.button("➕", key="button5", use_container_width=True):
        st.session_state.product3 += 1
        st.rerun()
    if col4.button("➖", key="button6", use_container_width=True):
        st.session_state.product3 -= 1
        st.rerun()

# Product 4: Powerbank
if st.session_state.product4 > 0:
    col1, col2, col3, col4 = st.columns(col_layout)
    col1.image("media/product4.jpg", width=120)
    col2.metric("⚡ VoltCharge Pro Powerbank", f"{st.session_state.product4}x", f"{round(st.session_state.product4 * price4, 2)} €")
    if col3.button("➕", key="button7", use_container_width=True):
        st.session_state.product4 += 1
        st.rerun()
    if col4.button("➖", key="button8", use_container_width=True):
        st.session_state.product4 -= 1
        st.rerun()

# Product 5: Laptop
if st.session_state.product5 > 0:
    col1, col2, col3, col4 = st.columns(col_layout)
    col1.image("media/product5.jpg", width=120)
    col2.metric("💻 AeroBook Pro Laptop", f"{st.session_state.product5}x", f"{round(st.session_state.product5 * price5, 2)} €")
    if col3.button("➕", key="button9", use_container_width=True):
        st.session_state.product5 += 1
        st.rerun()
    if col4.button("➖", key="button10", use_container_width=True):
        st.session_state.product5 -= 1
        st.rerun()

# Falls der Warenkorb komplett leer ist
if (st.session_state.product1 + st.session_state.product2 + st.session_state.product3 + st.session_state.product4 + st.session_state.product5) == 0:
    st.warning("Dein Warenkorb ist aktuell leer. Gehe zurück zum Shop, um Produkte hinzuzufügen.")

st.write("---")

# ==========================================
# BERECHNUNG & RABATT-LOGIK
# ==========================================

# Gesamtsumme berechnen
total = (st.session_state.product1 * price1 +
         st.session_state.product2 * price2 +
         st.session_state.product3 * price3 +
         st.session_state.product4 * price4 +
         st.session_state.product5 * price5)

# Rabattcode Eingabefeld
rabatq = st.text_input("🎟️ Hast du einen Rabatt-Code?", placeholder="Code hier eingeben...")

# Logik für Rabatte (Schwellenwerte an Tech-Preise angepasst)
discount_applied = 0
if rabatq == "charly5" and total > 100: # Vorher > 10
    discount_applied = 0.05
    st.success("✅ 5% Rabattcode 'charly5' erfolgreich angewendet!")
elif rabatq == "charly10" and total > 500: # Vorher > 30
    discount_applied = 0.10
    st.success("✅ 10% Rabattcode 'charly10' erfolgreich angewendet!")
elif rabatq == "charly20" and total > 1500: # Vorher > 70
    discount_applied = 0.20
    st.success("✅ 20% Rabattcode 'charly20' erfolgreich angewendet!")
elif rabatq != "":
    st.error("❌ Code ungültig oder Mindestbestellwert nicht erreicht.")

# Endsumme ermitteln
totalnew = total * (1 - discount_applied)

# Endergebnis schick präsentieren
col_sum1, col_sum2 = st.columns(2)
with col_sum1:
    st.write(f"Zwischensumme: **{round(total, 2)} €**")
    if discount_applied > 0:
        st.write(f"Abgezogener Rabatt: *-{round(total * discount_applied, 2)} €*")

with col_sum2:
    st.info(f"### 🎉 Zu zahlen: {round(totalnew, 2)} €")


# ==========================================
# EXCEL DOWNLOAD BUTTON
# ==========================================
st.write("")
try:
    relativer_pfad = os.path.join("media", "rabat_code_calc.xlsm")
    with open(relativer_pfad, "rb") as file:
        excel_daten = file.read()

    st.download_button(
        label="📊 Excel-Mappe (.xlsm) herunterladen",
        data=excel_daten,
        file_name="heruntergeladene_datei.xlsm",
        mime="application/vnd.ms-excel.sheet.macroEnabled.12",
        use_container_width=True
    )
except FileNotFoundError:
    st.caption("ℹ️ Excel-Rechner Vorlage momentan nicht verfügbar.")