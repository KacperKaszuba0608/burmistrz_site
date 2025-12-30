import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Artur Gaik na Burmistrza",
    page_icon="🪪",
    layout="wide",
)

# Title and Header
col1, col2, col3 = st.columns([1,3,1])

with col1:
    st.image("./images/burmistrz.png")
    st.markdown("""#### Skład Sztabu Wybrorczego:
* Artur Gaik - kandydat na burmistrza,
* Justyna Gaik - edukacja i kultura (Pani Burmistrzowa),
* Tomasz Szustakowski - inwestycje i finanse (inwestor strategiczny),
* Patryk Szustakowski - koumnikacja i marketing,
* Kacper Kaszuba - technologia i cyfryzacja
""")

with col2:
    st.title("NOWA RUDA DLA WSZYSTKICH - ZARADNIE,&nbsp;INNOWACYJNIE, Z&nbsp;SERCEM ❤️")
    st.header("O mnie")
    st.write("Dzień Dobry! Nazywam się **Artur Gaik** i zapraszam Cię do przeczytania mojego programu wyborczego.")
    st.write("""Kiedy podróżuję po Polsce w interesach, myślę jedno: ***'Nie ma biednych miejsc są tylko niewykorzystane okazje'***.
    Nowa Ruda ma ich mnóstwo. Mamy historię, położenie, pracowitych ludzi i piękne wsie, w tym Włodowice - miejsce, które przypomina, że polska wieś to nie przeszłość, tylko przyszłość dla tych, którzy myślą z głową.
    """)
    st.write("Nie będę obiecywał cudów. Jako przedstawiciel handlowy wiem, że każda obietnica musi się potem „spiąć w Excelu”. Ten program to plan, który bilansuje się finansowo, logicznie i po ludzku.")

    st.header("Mój program na lata 2029-2034")

    st.write("### O CZYM MÓWIĄ LICZBY (I CZEGO LICZBY NIE MÓWIĄ)")
    st.write("""Statystyki to mądra rzecz - pokazują nam, że od 2010 roku liczba ludności Nowej Rudy spadła o 4,1%, że bezrobocie wynosi 10,4%, że średnia pensja to mniej niż w miastach obok nas. Ale liczby nie mówią nam o tym, że mimo wyzwań demograficznych i gospodarczych, w Nowej Rudzie żyją ludzie o ogromnym potencjale - inżynierowie, nauczyciele, przedsiębiorcy i artyści.

Program, który Wam proponuję, nie obiecuje cudów. Ale obiecuje działanie oparte na faktach, zaradność, które pozwoli nam zamienić wyzwania w szanse.""")

    st.write("### I. GOSPODARKA I RYNEK PRACY: OŻYWIANIE TKANKI EKONOMICZNEJ")
    st.write("Problem: Niski poziom zatrudnienia i wypływ młodych ludzi")
    st.markdown("""Nowa Ruda ma 137 pracujących na 1000 mieszkańców. To połowa średniej wojewódzkiej. Młodzi ludzie wyjeżdżają - bo potrzebują miejsc pracy, perspektyw, możliwości realizacji ambicji. W ciągu ostatnich lat liczba podmiotów gospodarczych spadła, a nasze firmy mają mniej kapitału zagranicznego niż konkurenci w regionie. ​Ale mamy aktywa:
* Noworudzki Park Przemysłowy i Technoinkubator
* Strefy specjalne ekonomiczne (WSSE)
* Pozycję węzłową na trasach wojewódzkich 381, 384, 385

Działania konkretne:
1. **„Akademia Rzemiosła"** - Przywrócenie tradycji, stworzenie nowych zawodów
    * Współpraca z podstawówkami i gimnazjami - edukacja zawodowa od klasy ósmej
    * Kursy dla dorosłych: hydraulika, elektyka, budownictwo, naprawy domowe
    * Granty dla rzemieślników chcących się założyć (szczególnie dla osób do 40 lat)
    * W Włodowicach i większych wsiach: punkty szkoleniowe (e-learning + pracownia)
    * Hasło: **„Polska potrzebuje hydraulików bardziej niż filozofów - ale nasze filozofy mogą naprawiać prysznice lepiej**"
2. **Podatki dla przedsiębiorców z Nowej Rudy**
    * Obniżka o 10% podatku CIT dla nowych firm rejestrowanych w mieście (pierwsze 3 lata)
    * Zwolnienie z podatku od nieruchomości dla warsztatów rzemieślniczych przez 2 lata
    * Uproszczona procedura przydzielania terenów w Parku Przemysłowym
3. **Cyfryzacja dla wszystkich - Inteligentna Wieś 2.0**
    * Szybki internet do każdej wsi gminy (dark fiber + fiber to the home)
    * Cyfrowe usługi edukacyjne dla dzieci w wioskach (uzupełniające ofertę szkolną)
    * Inkubator startupów technologicznych (Włodowice mogą być hubem dla bioinformatyki!)
    * Wsparcie dla freelancerów: pracownie coworkingowe w większych wsiach
4. **Turystyka jako realna gospodarka (nie tylko marzenia)**
    * Rozbudowa Turystycznej Kopalni Węgla (już 10 GWh potencjału w samej kopalni!)
    * Marketing: Nowa Ruda na mapach europejskich tour operatorów
    * Hotele trzygwiazdkowe (wsparcie dla inwestorów prywatnych)
    * Połączenia autokarowe do Zamku Książ, Karłowa, Srebrnej Góry (pakiety)
    * **Nowa Ruda - Turystyczna Stolica Sudetów Środkowych (rebranding)**""")
    

    st.write("### II. INFRASTRUKTURA I ŚRODOWISKO: ŻELAZO I ZIELONE RZECZY 🍃")
    st.write("Problem: Niska emisja, brak gazu w połowie domów, drogi jak mapy topograficzne")
    st.markdown("""Nowa Ruda jest w czołówce miast o najwyższej emisji PM10 i PM2,5. Mieszkańcy ogrzewają się węglem - bo nie mają dostępu do gazu (55,5% bez dostępu). Drogi są w kiepskim stanie, a infrastruktura komunalna wymaga modernizacji. Ale mamy już 2 autobusy elektryczne!

Działania konkretne:
1. **Energia ze Starego Węgla - Geotermia Noworudzka**
    * Inwestycja w system geotermalny oparty na wodach z zatopionych kopalni
    * Potencjał: 10 GWh rocznie dla miasta i wsi
    * Powiązanie z modularnym systemem grzewczym (heat pump dla bloków i domów)
    * Rozbudowa sieci ciepłowniczej do roku 2030 (cel: 80% pokrycia)
    * **Slogan: „Z węglem się żegnamy, ale jego moc nam zostaje"**
2. **Gaz dla wszystkich - Plan rozbudowy sieci gazowej**
    * Priorytet: Włodowice, Jugów, Sokolec, Ludwikowice (największe wsi bez dostępu)
    * Dotacje mieszkańcom na przyłączenia (50% dofinansowania z budżetu)
    * Inwestycja sumaryczna: 45 mln zł (fundusze UE + budżet)
    * Termin: 2026–2028
3. **Drogi do Europy**
    * Remont całych ulic zamiast łatek (nowe technologie – drogi impermeable)
    * Priorytet: główne ulice, szkoły, szpitale, drogi do wsi
    * Ścieżki rowerowe wzdłuż Włodzicy (Nowa Ruda – Drogosław – Włodowice – Jugów)
    * Parkingi parklet'owe (zielone, przyjazne dla środowiska) na dworca
4. **E-mobilność: Z 2 autobusów do Całej Floty**
    * Poszerzenie floty e-busów do 5 sztuk (2026)
    * Stacje ładowania w Drogosławiu, Słupcu, Włodowicach
    * Bezpłatne bilety dla seniorów i uczniów (do 30% rabatu dla pozostałych)
    * Rowery elektryczne do wynajęcia w każdej wsi (system MEVO)""")
    
    st.write("### III. EDUKACJA I KAPITAŁ LUDZKI: MÓZGI NIE WYJEŻDŻAJĄ, JA ICH NIE PUSZCZĘ")
    st.write("Problem: Słabe wyniki egzaminów, niska aktywność NGO, odpływ inteligencji")
    st.markdown("""Wyniki egzaminów w Nowej Rudzie są poniżej średniej wojewódzkiej - szczególnie matematyka. Kapitał społeczny jest słaby (20 NGO na 10 tys. mieszkańców vs 36 w regionie). Młode talenty wyjeżdżają do Wrocławia, Warszawy, Berlina.

Działania konkretne:
1. **Szkoły 21 Wieku - Rewolucja Edukacyjna**
    * Zmiana paradygmatu: od testów do projektów
    * Laboratoria STEM (science, technology, engineering, math) w każdej szkole
    * Zajęcia z przedsiębiorczości od klasy piątej
    * Program dla zdolnych: korepetycje bezpłatne z uniwersytetu w Wrocławiu (online)
    * Szkoła nauki programowania dla dzieci od 8 lat (Włodowice - ośrodek pilotażowy)
2. **Uniwersytet Trzeciego Wieku dla Wszelkiego Wieku**
    * Kursy dla seniorów: informatyka, fotografia, historia lokalna
    * Mentoring: młodzi nauczą starszych komputerów, starsi nauczą młodych o życiu
    * Spotkania pokoleniowe w każdej wsi (rozmowy, gry, wspomnienia)
3. **Stypendia dla Bystrzaków**
    * Stypendium im. Olgę Tokarczuk dla dzieci ze słabszych rodzin (1000 zł/rok)
    * Bezpłatne zajęcia pozalekcyjne (muzyka, sztuka, sport)
    * Mentoring dla dzieciaków z obszarów wiejskich (by znały perspektywy)
4. **Biblioteka jako Centrum Społeczne**
    * Dostęp do e-booków, audiobooków, kursów online
    * Kawiarnia (tanki kawa + rozmowy)
    * Sale do pracy dla freelancerów
    * Księgarnia zajezdna: raz w tygodniu do każdej wsi""")
    
    st.write("### IV. WŁODOWICE I WSIE: PULS ŻYCIA POZA MIASTEM")
    st.write("Problem: Wyludnianie, brak usług, drogi grzęzawe, brak perspektyw")
    st.markdown("""Włodowice to zabytkowa wieś z piękną historią (dwór Stillfriedów, szlaki literackie). Ale połowa budynków to puste domy opuszczonych staruszków, brakuje młodych, brak interesu handlowskiego. To jest tragedią dla wszystkich 17 wsi gminy.

Działania konkretne:
1. **„Włodowice się Budzą" - Model Wsi Żywej**
    * Wsparcie dla inwestorów prywatnych chcących otworzyć noclegi agroturystyczne
    * Grunt na budowę domów za czynsz (nie sprzedaż) dla młodych rodzin
    * Dotacje na remonty zabytkowych domów (dwór, zagrody)
    * Turystyka literacka: Droga Chlebowa jako szlak międzynarodowy
2. **Usługi Bliżej Domu**
    * Mobilna apteka (1 dzień w tygodniu we każdej wsi)
    * Telemedicyna: konsultacje z lekarzami przez internet
    * Paczkomat Amazon w każdej wsi (partnerstwo)
    * Biuro obsługi ZUS/CEIDG w siedzibie sołtysa
3. **Komunalna Komunikacja - Autobusy RAZEM**
    * Bezpłatne przejazdy dla uczniów do szkół w mieście
    * Połączenia do szkół podstawowych w każdej wsi (zamiast wożenia autem)
    * Wyjazdy turystyczne 1 raz w miesiącu (dla seniorów, rodzin)
    * Plan: Każda wieś co 2 godziny (rano i wieczorem), co 4 godziny w dzień
4. **Rolnictwo + Turystyka = Agroturystyka Zintegrowana**
    * Dotacje dla rolników chcących oferować noclegi
    * Szkolenia: jak gospodarz, jak kuchnia regionalna, jak edukacja na wsi
    * Sprzedaż bezpośrednia: targ agroturystyczny w Nowej Rudzie (1 raza w tygodniu)
    * Branding: 'Włodowice to nie wieś, to doświadczenie'""")
    
    st.write("### V. SPOŁECZEŃSTWO I INTEGRACJA: LUDZIE, A NIE STATYSTYKI")
    st.write("Problem: Bezrobocie trwałe, ubóstwo, rozpad więzi społecznych, przestępczość")
    st.markdown("""16 z każdych 100 rodzin korzysta z pomocy społecznej. Młodzież bez perspektyw szuka ujścia w alkoholu, narkotykach. Sąsiedzi się nie znają. Festiwale są rzadkie.
                
Działania konkretne:
1. **Program Walki z Ubóstwem Strukturalnym**
    * Dochód podstawowy dla bezrobotnych powyżej 50 lat (500 zł/miesiąc) + program pracy społecznej
    * Wsparcie dla rodzin monoparentalnych: darmowe przedszkole + obiad w szkole
    * Kuchnia społeczna w każdej dzielnicy (tania, zdrowa kolacja)
    * Bonifikata czynszów za pracę społeczną (remontowanie szkół, parków)
2. **Nowa Ruda Się Integruje - Festiwale, Eventy, Spotkania**
    * Festiwal Góry Literatury - już jest! Będzie większy, promocja międzynarodowa
    * Bieg Górski - co roku, również dla dzieci i seniorów
    * Noc Naukowca w kopalni (pokazy, eksperymenty, muzyka)
    * Święto Włodowic - święto wiosny z koncertami, jedzeniem, tańcem
    * Bal dla seniorów (orkiestra, szampan, tańce z lat 60-tych)
3. **Monitoring i Bezpieczeństwo Społeczne**
    * Policja bliskości: każdy region ma swojego policjanta na terenie
    * Programy profilaktyczne dla młodzieży (sporty, karting, informatyka)
    * Schronienie dla osób bezdomnych (współpraca z NGO)
    * Punkt Interwencji Kryzysowej (24/7 dla osób w kryzysie)
4. **Wolontariat jako Grana Wartość**
    * Wolontariat korporacyjny (firmy biorą urlop na pracę społeczną)
    * Uniwersytet III Wieku + Szkoła Pokoleń = Transfer Wiedzy
    * Wolontariaty dla studentów (staż bezpłatny w mieście = doświadczenie)""")
    
    st.write("### VI. KULTURA I TOŻSAMOŚĆ: BAJKA NOWEJ RUDY")
    st.write("Problem: Brak poczucia tożsamości lokalnej, turystyka powierzchowna")
    st.markdown("""Nowa Ruda ma bogatą historię - górnictwo, tkactwo, procesów czarownic, Droga Chlebowa - ale tę historię marnotrawimo.

Działania konkretne:
1. **Centrum Interpretacji Historii Górnictwa**
    * Ekspozycja: od XIII wieku do teraz
    * Sala VR: przejście przez kopalnię z górnnikiem z 1900 roku
    * Warsztaty dla dzieci: wypróbowanie narzędzi górniczych
    * Muzeum Górnictwa - już jest! Będzie jeszcze bardziej nowoczesne.
2. **Ściany Sztuki - Graffiti dla Niemłodych**
    * Zamówienie dla artystów lokalnych: murale na podestach, blokach
    * Wystawy sztuki co miesiąc (młodzi artyści, osoby niepełnosprawne)
    * Galeria na dworcu (fotografia, malarstwo)
3. **Literatura Żyje - Szlaki Tokarczuk**
    * Droga Chlebowa: znakowanie, schroniska, przewodnicy
    * Spotkania z pisarzami co miesiąc (zaproszenia do Nowej Rudy)
    * Konkursy literackie dla uczniów (nagrody pieniężne!)
    * Pielgrzymka literacka: Nowa Ruda - Włodowice - Šonov (co roku)
4. **Dziedzictwo Kulinarne - Noworudzka Kuchnia**
    * Publikacja: „Smaki Nowej Rudy" (przepisy babci)
    * Szkoła kulinarna dla młodych (edukacja, zawód)
    * Festiwal Potraw Regionalnych (sierpień)
    * Certyfikat 'Smak Nowej Rudy' dla restauracji (marketing)""")
    
    st.write("### VII. ZARZĄDZANIE I FINANSE: UCZCIWIE I ROZSĄDNIE")
    st.markdown("""Obietnice:
1. **Budżet Partycypacyjny - 5% budżetu dla mieszkańców**
    * Głosowanie: projekty za min. 50 tys. zł będą wybierane przez mieszkańców
    * Transparentność: każdy będzie wiedzieć, ile wydajemy na co
    * Sprawozdania co kwartał (bez żargonu biurokratycznego)
2. **Cyfryzacja Urzędu - Urząd Otwarte Drzwi**
    * E-usługi: załatw sprawę bez wychodzenia z domu
    * Spotkania miesięczne z burmistrza w każdej wsi (zamiast czekania w kolejce)
    * Ankiety: „Co myślimy o mieście?" - wyniki publiczkowe
3. **Etyka i Transparentność**
    * Oświadczenia majątkowe publiczkowe dla wszystkich urzędników
    * Zakaz dla urzędników pracowania dla firm, które dostają zamówienia publiczne
    * Skargi: odpowiedź w ciągu 2 tygodni (nie 1 miesiąca)
4. **Źródła Finansowania**
    * Fundusze UE: 60-70% projektów (gaz, energia, drogi, edukacja)
    * Budżet miasta: 20-25%
    * Partnerstwa publiczno-prywatne: 10-15% (turystyka, transport)
    * Granty od NGO, fundacji, gmin siostrzanych""")
    
    st.write("### VIII. HARMONOGRAM: KROK PO KROKU")
    st.markdown("""| Rok       | Priorytet             | Działania                                                       |
| --------- | --------------------- | --------------------------------------------------------------- |
| 2025      | Energia & Transport   | Studium geotermii; e-busy (dalsze); gminna komunikacja          |
| 2025-2026 | Infrastruktura        | Gaz do wsi; drogi główne; ścieżki rowerowe                      |
| 2026-2027 | Edukacja & Gospodarka | Laboratoria STEM; kursy zawodowe; park przemysłowy (inwestycje) |
| 2027-2028 | Turystyka             | Rozbudowa kopalni; szlaki; hotel 3-gwiazdkowy                   |
| 2025-2030 | Całość                | Tożsamość miasta (rebranding)                                   |""")
    
    st.write("### SŁOWO NA ZAKOŃCZENIE")
    st.markdown("""Nowa Ruda to miasto, które ma do powiedzenia coś ważnego Europie - historia, kultura, technologia. Włodowice to wieś, która może być modelą życia na wsi w XXI wieku. A my wszyscy razem możemy udowodnić, że małe miasta nie umierają – rodziły się na nowo.

Nie szukamy powrotu do przeszłości. Szukamy przyszłości, która honor szanuje przeszłość.

Będę Wam służył. Liczę na waszą wiarę.""")

    st.write("### PRZYPIS O ŹRÓDŁACH PROGRAMU")
    st.markdown("""Program oparty jest na:
* Lokalnym Programie Rewitalizacji Gminy Miejskiej Nowa Ruda (2015–2025)
* Danych GUS i DWUP (2010–2015)
* Studium potencjału geotermalnego kopalni Nowej Rudy (MDPI, 2022)
* Raporcie turystycznym i kulturalnym (Ołga Tokarczuk, literatura lokalna)
* Konsultacjach z mieszkańcami, sołtysami i NGO

Wszystkie obietnice są możliwe do realizacji w ciągu 5 lat z wykorzystaniem funduszy UE, budżetu lokalnego i PPP.""")