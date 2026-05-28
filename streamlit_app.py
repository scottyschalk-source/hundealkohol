import streamlit as st
col1,col2 = st.columns(2)
with col1:
    st.title("Die A35 flash")
with col1:
    st.image("media/product1.jpg", caption="Perfekte Schärfe")
with col2:
    st.markdown(
        """
    # 📸 Halte deine Momente fest!

    Egal ob atemberaubende Landschaften, spontane Schnappschüsse mit Freunden oder professionelle Content-Creation: Die neue **[Kamera-Modellname]** ist dein perfekter Begleiter.

    Bring deine Fotografie aufs nächste Level und halte Erinnerungen so fest, wie sie es verdienen.
    """
    )

    # 2. Teil: Der "Read more" / Ausklapp-Bereich für die Details
    with st.expander("📖 Mehr anzeigen...", expanded=False):
        st.markdown(
            """
        ### ✨ Warum du sie lieben wirst:
        * **🎯 Kristallklare Details:** Dank des *[24 Megapixel / 4K-Video]* Sensors entgeht dir kein einziges Detail mehr.
        * **⚡ Blitzschneller Autofokus:** Halte die Action genau im richtigen Moment fest.
        * **🎒 Kompakt & Robust:** Leicht genug für jede Tasche, aber bereit für jedes Abenteuer.
        * **📲 Einfach teilen:** Mit der integrierten *[Wi-Fi / Bluetooth]* Funktion landen deine Meisterwerke sofort auf dem Smartphone.

        ---

        > **💡 Mach Schluss mit unscharfen Handy-Fotos.**
        """
        )

col1, col2 = st.columns(2)
with col1:
    st.title("Die L-Series Prime")
with col1:
    st.image("media/product2.jpg", caption="Perfekte Schärfe")

with col2:
    st.markdown(
        """
    # 🔍 Bring deine Details ganz groß raus!

    Egal ob professionelle Porträts mit wunderschönem, unscharfem Hintergrund, beeindruckende Street-Fotografie oder kristallklare Nahaufnahmen: Die neue **L-Series Prime Linse** holt das Beste aus deiner Kamera heraus.

    Erweitere deinen kreativen Spielraum und fange das Licht so ein, wie du es noch nie gesehen hast.
    """
    )

    # 2. Teil: Der "Read more" / Ausklapp-Bereich für die Linsen-Details
    with st.expander("📖 Mehr anzeigen...", expanded=False):
        st.markdown(
            """
        ### ✨ Warum du diese Linse lieben wirst:
        * **🌌 Extreme Lichtstärke:** Dank einer großen Offenblende von *[z. B. F/1.8]* gelingen dir selbst bei Dämmerung gestochen scharfe Bilder ohne Bildrauschen.
        * **🌸 Traumhaftes Bokeh:** Setze dein Motiv perfekt in Szene mit einem seidenweichen, kinoreifen Hintergrund.
        * **💎 Premium-Verarbeitung:** Hochwertig geschliffene Glaselemente minimieren Verzerrungen und sorgen für maximale Farbtreue.
        * **⚡ Lautloser Fokusmotor:** Ideal auch für Videoaufnahmen, da der Autofokus absolut geräuschlos und blitzschnell arbeitet.

        ---

        > **💡 Das wichtigste Upgrade für deine Kamera.** Ein Gehäuse ist nur so gut wie das Glas davor. Investiere in deine Bildqualität!
        """
        )

col1, col2 = st.columns(2)
with col1:
    st.title("Das Nexus X1")
with col1:
    st.image("media/product3.jpg", caption="Dein täglicher Begleiter")

with col2:
    st.markdown(
        """
    # 📱 Erlebe die Zukunft in deiner Hand!

    Egal ob blitzschnelles Multitasking im Alltag, grafikintensives Gaming oder das Streamen deiner Lieblingsserien in Kinoqualität: Das neue **Nexus X1** vereint maximale Power mit einem eleganten Design.

    Mach keine Kompromisse mehr und hol dir den perfekten Allrounder, der hält, was er verspricht.
    """
    )

    # 2. Teil: Der "Read more" / Ausklapp-Bereich für die Smartphone-Details
    with st.expander("📖 Mehr anzeigen...", expanded=False):
        st.markdown(
            """
        ### ✨ Warum du dieses Smartphone lieben wirst:
        * **🚀 Flaggschiff-Performance:** Der neueste Prozessor sorgt für absolut flüssige Bedienung, extrem kurze Ladezeiten und müheloses App-Switching.
        * **📺 Atemberaubendes Display:** Ein *[z. B. 120 Hz OLED]* Display liefert kinoreife Farben, tiefe Kontraste und eine butterweiche Darstellung.
        * **🔋 Akku ohne Ende:** Bringt dich dank intelligenter Energieverwaltung locker durch den intensivsten Tag – und ist per *[z. B. Super-Fast-Charge]* im Handumdrehen wieder voll.
        * **🛡️ Robust & Sicher:** Kratzfestes Glas und modernste Sicherheitsfeatures wie Gesichtserkennung oder Fingerabdruck-Sensor schützen deine Daten optimal.

        ---

        > **💡 Dein Upgrade für den Alltag.** Mehr als nur ein Telefon – deine Steuerzentrale für Arbeit, Freizeit und Entertainment, die perfekt in jede Tasche passt.
        """
        )

col1, col2 = st.columns(2)
with col1:
    st.title("Die VoltCharge Pro")
with col1:
    st.image("media/product4.jpg", caption="Nie wieder leerer Akku")

with col2:
    st.markdown(
        """
    # ⚡ Volle Power, egal wo du gerade bist!

    Kennst du das Gefühl, wenn im wichtigsten Moment der Akku versagt? Mit der neuen **VoltCharge Pro Powerbank** gehört diese Sorge der Vergangenheit an. Sie ist dein unsichtbares Sicherheitsnetz für lange Tage, Reisen und Outdoor-Abenteuer.

    Bleib flexibel, bleib erreichbar und lade deine Geräte überall blitzschnell wieder auf.
    """
    )

    # 2. Teil: Der "Read more" / Ausklapp-Bereich für die Powerbank-Details
    with st.expander("📖 Mehr anzeigen...", expanded=False):
        st.markdown(
            """
        ### ✨ Warum du diese Powerbank lieben wirst:
        * **🔋 Gewaltige Kapazität:** Mit *[z. B. 20.000 mAh]* Kapazität lädst du dein Smartphone mehrfach komplett auf, bevor die Powerbank selbst an die Steckdose muss.
        * **🚀 High-Speed Charging:** Dank modernster *[z. B. Power Delivery (PD) & Quick Charge]* Technologie werden deine Geräte bis zu 4x schneller geladen als mit Standard-Netzteilen.
        * **🔌 Multi-Device Laden:** Lade Smartphone, Tablet und Kopfhörer gleichzeitig – dank flexibler USB-C und USB-A Anschlüsse für die ganze Familie.
        * **🛡️ Intelligenter Schutz:** Ein integriertes Sicherheitssystem schützt deine wertvollen Geräte zuverlässig vor Überladung, Überhitzung und Kurzschlüssen.

        ---

        > **💡 Dein treuer Begleiter für unterwegs.** Kompakt genug für jeden Rucksack, aber stark genug, um selbst dein Laptop im Notfall mit neuer Energie zu versorgen.
        """
        )

col1, col2 = st.columns(2)
with col1:
    st.title("Das AeroBook Pro")
with col1:
    st.image("media/product5.jpg", caption="Produktivität ohne Grenzen")

with col2:
    st.markdown(
        """
    # 💻 Maximale Power für Arbeit, Freizeit und Kreativität!

    Egal ob du komplexe Projekte im Homeoffice stemmst, hochauflösende Videos schneidest oder einfach entspannt deine Lieblingsserien streamst: Das neue **AeroBook Pro** kombiniert kompromisslose Leistung mit ultraleichtem Design.

    Verwandle jeden Ort in deinen perfekten Arbeitsplatz und erlebe Performance, die mit deinem Tempo mithält.
    """
    )

    # 2. Teil: Der "Read more" / Ausklapp-Bereich für die Laptop-Details
    with st.expander("📖 Mehr anzeigen...", expanded=False):
        st.markdown(
            """
        ### ✨ Warum du diesen Laptop lieben wirst:
        * **🚀 Blitzschnelle Performance:** Ausgestattet mit einem High-End Prozessor und *[z. B. 16 GB RAM]* starten Apps ohne Verzögerung und Multitasking wird zum Kinderspiel.
        * **🎨 Brillantes Display:** Das hochauflösende *[z. B. Quad-HD IPS]* Display sorgt für messerscharfe Texte, lebendige Farben und ein augenschonendes Arbeiten – auch bei direktem Sonnenlicht.
        * **🔋 Akku für den ganzen Tag:** Dank der extrem effizienten Architektur hält der Akku bis zu *[z. B. 12 Stunden]* durch. Dein Ladekabel kann also getrost zu Hause bleiben.
        * **🪶 Ultraleicht & Elegant:** Das schlanke Gehäuse aus Premium-Aluminium wiegt fast nichts und passt perfekt in jede Tasche, ohne dich zu beschweren.

        ---

        > **💡 Deine Schaltzentrale für die Zukunft.** Ein Laptop, der keine Wünsche offenlässt – elegant im Design, kompromisslos in der Leistung und bereit für all deine Ideen.
        """
        )






















