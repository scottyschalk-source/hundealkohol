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

# Shop-Überschrift (Gibt der Seite einen klaren E-Commerce-Vibe)
st.title("🛍️ Unser Hardware & Tech Shop")
st.subheader("Entdecke erstklassiges Equipment für dein Setup")
st.write("---")

# Neugestaltung: Produkte in interaktive Tabs aufteilen statt untereinander zu scrollen
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📸 Kamera",
    "🔍 Linse",
    "📱 Smartphone",
    "⚡ Powerbank",
    "💻 Laptop"
])

# ==========================================
# TAB 1: KAMERA
# ==========================================
with tab1:
    col1, _, col2 = st.columns([3, 0.5, 3])
    with col1:
        st.image("media/product1.jpg", use_container_width=True)
        # Zusätzliches E-Commerce Element: Statusanzeige
        st.caption("🟢 Auf Lager | Lieferung in 1-2 Werktagen")

    with col2:
        st.markdown("# 📸 High-End Kamera")
        st.markdown("### **799,00 €**")  # Preis-Highlight
        st.write(
            "Egal ob atemberaubende Landschaften, spontane Schnappschüsse mit Freunden "
            "oder professionelle Content-Creation: Diese Kamera ist dein perfekter Begleiter."
        )

        with st.expander("⚙️ Technische Details einblenden", expanded=False):
            st.markdown(
                """
            * **🎯 Details:** 24 Megapixel / 4K-Video Sensor.
            * **⚡ Fokus:** Blitzschneller Autofokus ohne Verzögerung.
            * **🎒 Design:** Kompakt, robust und leicht zu transportieren.
            * **📲 Konnektivität:** Integrierte Wi-Fi & Bluetooth Funktion.
            """
            )

        st.write("")
        # Modernere Warenkorb-Anzeige direkt beim Produkt
        st.metric("Im Warenkorb", f"{st.session_state.product1} Stk.")

        col1_btn, col2_btn = st.columns(2)
        if col1_btn.button("🛒 Hinzufügen", key="button1", use_container_width=True):
            st.session_state.product1 += 1
            st.rerun()
        if col2_btn.button("❌ Entfernen", key="button2", use_container_width=True):
            if st.session_state.product1 > 0:
                st.session_state.product1 -= 1
                st.rerun()

# ==========================================
# TAB 2: KAMERA-LINSE
# ==========================================
with tab2:
    col1, _, col2 = st.columns([3, 0.5, 3])
    with col1:
        st.image("media/product2.jpg", use_container_width=True)
        st.caption("🟢 Auf Lager | Kostenloser Versand")

    with col2:
        st.markdown("# 🔍 L-Series Prime Linse")
        st.markdown("### **349,00 €**")
        st.write(
            "Erweitere deinen kreativen Spielraum. Egal ob professionelle Porträts mit "
            "wunderschönem Bokeh oder kristallklare Nahaufnahmen: Diese Linse holt das Beste heraus."
        )

        with st.expander("⚙️ Technische Details einblenden", expanded=False):
            st.markdown(
                """
            * **🌌 Lichtstärke:** Extreme Offenblende von F/1.8 für Aufnahmen bei Dämmerung.
            * **🌸 Bokeh:** Seidenweicher, kinoreifer Hintergrund.
            * **💎 Glas:** Hochwertig geschliffene Elemente minimieren Verzerrungen.
            * **⚡ Motor:** Absolut lautloser Fokusmotor – ideal für Videos.
            """
            )

        st.write("")
        st.metric("Im Warenkorb", f"{st.session_state.product2} Stk.")

        col1_btn, col2_btn = st.columns(2)
        if col1_btn.button("🛒 Hinzufügen", key="button3", use_container_width=True):
            st.session_state.product2 += 1
            st.rerun()
        if col2_btn.button("❌ Entfernen", key="button4", use_container_width=True):
            if st.session_state.product2 > 0:
                st.session_state.product2 -= 1
                st.rerun()

# ==========================================
# TAB 3: SMARTPHONE
# ==========================================
with tab3:
    col1, _, col2 = st.columns([3, 0.5, 3])
    with col1:
        st.image("media/product3.jpg", use_container_width=True)
        st.caption("🟡 Nur noch wenige verfügbar")

    with col2:
        st.markdown("# 📱 Nexus X1 Smartphone")
        st.markdown("### **999,00 €**")
        st.write(
            "Erlebe die Zukunft in deiner Hand. Blitzschnelles Multitasking, "
            "grafikintensives Gaming und ein Display, das dich staunen lässt."
        )

        with st.expander("⚙️ Technische Details einblenden", expanded=False):
            st.markdown(
                """
            * **🚀 Prozessor:** Flaggschiff-Performance für absolut flüssige Bedienung.
            * **📺 Display:** 120 Hz OLED-Display für kinoreife Farben.
            * **🔋 Akku:** Intelligente Energieverwaltung für lange Tage.
            * **🛡️ Schutz:** Kratzfestes Glas und modernste Sicherheitsfeatures.
            """
            )

        st.write("")
        st.metric("Im Warenkorb", f"{st.session_state.product3} Stk.")

        col1_btn, col2_btn = st.columns(2)
        if col1_btn.button("🛒 Hinzufügen", key="button5", use_container_width=True):
            st.session_state.product3 += 1
            st.rerun()
        if col2_btn.button("❌ Entfernen", key="button6", use_container_width=True):
            if st.session_state.product3 > 0:
                st.session_state.product3 -= 1
                st.rerun()

# ==========================================
# TAB 4: POWERBANK
# ==========================================
with tab4:
    col1, _, col2 = st.columns([3, 0.5, 3])
    with col1:
        st.image("media/product4.jpg", use_container_width=True)
        st.caption("🟢 Auf Lager | Sofort versandfertig")

    with col2:
        st.markdown("# ⚡ VoltCharge Pro Powerbank")
        st.markdown("### **49,99 €**")
        st.write(
            "Volle Power, egal wo du gerade bist. Dein unsichtbares Sicherheitsnetz "
            "für lange Tage, Reisen und Outdoor-Abenteuer. Lade deine Gadgets blitzschnell."
        )

        with st.expander("⚙️ Technische Details einblenden", expanded=False):
            st.markdown(
                """
            * **🔋 Kapazität:** Gewaltige 20.000 mAh für Mehrfachladungen.
            * **🚀 Speed:** Power Delivery (PD) lädt bis zu 4x schneller.
            * **🔌 Anschlüsse:** Multi-Device Laden über USB-C und USB-A parallel.
            * **🛡️ Sicherheit:** Integrierter Schutz vor Überhitzung und Überladung.
            """
            )

        st.write("")
        st.metric("Im Warenkorb", f"{st.session_state.product4} Stk.")

        col1_btn, col2_btn = st.columns(2)
        if col1_btn.button("🛒 Hinzufügen", key="button7", use_container_width=True):
            st.session_state.product4 += 1
            st.rerun()
        if col2_btn.button("❌ Entfernen", key="button8", use_container_width=True):
            if st.session_state.product4 > 0:
                st.session_state.product4 -= 1
                st.rerun()

# ==========================================
# TAB 5: LAPTOP
# ==========================================
with tab5:
    col1, _, col2 = st.columns([3, 0.5, 3])
    with col1:
        st.image("media/product5.jpg", use_container_width=True)
        st.caption("🟢 Auf Lager | Expressversand möglich")

    with col2:
        st.markdown("# 💻 AeroBook Pro Laptop")
        st.markdown("### **1.249,00 €**")
        st.write(
            "Maximale Power für Arbeit, Freizeit und Kreativität. Ein extrem "
            "schlankes Alugehäuse trifft auf kompromisslose Rechenleistung für unterwegs."
        )

        with st.expander("⚙️ Technische Details einblenden", expanded=False):
            st.markdown(
                """
            * **🚀 Hardware:** High-End Prozessor und 16 GB RAM für Multitasking.
            * **🎨 Bildschirm:** Hochauflösendes Quad-HD IPS-Display.
            * **🔋 Laufzeit:** Effizienter Akku für bis zu 12 Stunden arbeiten.
            * **🪶 Gehäuse:** Ultraleichtes Premium-Aluminium, das in jede Tasche passt.
            """
            )

        st.write("")
        st.metric("Im Warenkorb", f"{st.session_state.product5} Stk.")

        col1_btn, col2_btn = st.columns(2)
        if col1_btn.button("🛒 Hinzufügen", key="button9", use_container_width=True):
            st.session_state.product5 += 1
            st.rerun()
        if col2_btn.button("❌ Entfernen", key="button10", use_container_width=True):
            if st.session_state.product5 > 0:
                st.session_state.product5 -= 1
                st.rerun()

# Fußzeile des Shops
st.write("---")
st.caption("💡 Tipp: Nutze die Tabs oben, um schnell zwischen den Produkten zu wechseln.")