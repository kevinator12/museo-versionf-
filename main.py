import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "grey"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 750
    image_height_Portada = 300
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)

    #audios de lenguajes
    fortran = ft.Audio(src="fortran.mp3", volume=1, balance=0)
    page.overlay.append(fortran)
    
    cobol = ft.Audio(src="cobol.mp3",volume=1,balance=0)
    page.overlay.append(cobol)
    
    pascal2 = ft.Audio(src="pascal2.mp3", volume=1,balance=0)
    page.overlay.append(pascal2)
    
    c = ft.Audio(src="c.mp3",volume=1, balance=0)
    page.overlay.append(c)
    
    html = ft.Audio(src="html.mp3",volume=1,balance=0)
    page.overlay.append(html)
    
    python = ft.Audio(src="python.mp3",volume=1,balance=0)
    page.overlay.append(python)
    
    sql = ft.Audio(src="sql.mp3",volume=1,balance=0)
    page.overlay.append(sql)
    
    php = ft.Audio(src="php.mp3",volume=1,balance=0)
    page.overlay.append(php)
    
    java = ft.Audio(src="java.mp3",volume=1,balance=0)
    page.overlay.append(java)
    
    javascript = ft.Audio(src="javascript.mp3",volume=1,balance=0)
    page.overlay.append(javascript)
    
    NoSQL = ft.Audio(src="NoSQL.mp3",volume=1,balance=0)
    page.overlay.append(NoSQL)
    
    perl = ft.Audio(src="perl.mp3",volume=1,balance=0)
    page.overlay.append(perl)
    
    swift = ft.Audio(src="swift.mp3",volume=1,balance=0)
    page.overlay.append(swift)
    
    rust = ft.Audio(src="rust.mp3",volume=1,balance=0)
    page.overlay.append(rust)
#audios de audios 
    snapchat = ft.Audio(src="snapchat.mp3",volume=1,balance=0)
    page.overlay.append(snapchat)
    
    tiktok = ft.Audio(src="tiktok.mp3",volume=1,balance=0)
    page.overlay.append(tiktok)

    facebook = ft.Audio(src="facebook.mp3",volume=1,balance=0)
    page.overlay.append(facebook)

    instagram = ft.Audio(src="instagram.mp3",volume=1,balance=0)
    page.overlay.append(instagram)

    twiter = ft.Audio(src="twiter.mp3",volume=1,balance=0)
    page.overlay.append(twiter)

    whatsApp = ft.Audio(src="whatsApp.mp3",volume=1,balance=0)
    page.overlay.append(whatsApp)

    pinterest = ft.Audio(src="pinterest.mp3",volume=1,balance=0)
    page.overlay.append(pinterest)

    reddit = ft.Audio(src="reddit.mp3",volume=1,balance=0)
    page.overlay.append(reddit)

    weibo = ft.Audio(src="weibo.mp3",volume=1,balance=0)
    page.overlay.append(weibo)

    telegram = ft.Audio(src="telegram.mp3",volume=1,balance=0)
    page.overlay.append(telegram)

    Qzone = ft.Audio(src="Qzone.mp3",volume=1,balance=0)
    page.overlay.append(Qzone)
    
    Skype = ft.Audio(src="Skype.mp3",volume=1,balance=0)
    page.overlay.append(Skype)

    asistentes = ft.Audio(src="asistentes.mp3",volume=1,balance=0)
    page.overlay.append(asistentes)
    
    analitica = ft.Audio(src="analitica.mp3",volume=1,balance=0)
    page.overlay.append(analitica)
    
    automatizacion = ft.Audio(src="automatizacion.mp3",volume=1,balance=0)
    page.overlay.append(automatizacion)
    
    blockchain = ft.Audio(src="blockchain.mp3",volume=1,balance=0)
    page.overlay.append(blockchain)
    
    Chatbot = ft.Audio(src="Chatbot.mp3",volume=1,balance=0)
    page.overlay.append(Chatbot)
    
    seguridad = ft.Audio(src="seguridad.mp3",volume=1,balance=0)
    page.overlay.append(seguridad)
    
    comercio = ft.Audio(src="comercio.mp3",volume=1,balance=0)
    page.overlay.append(comercio)
    
    IA = ft.Audio(src="IA.mp3",volume=1,balance=0)
    page.overlay.append(IA)
    
    internet = ft.Audio(src="internet.mp3",volume=1,balance=0)
    page.overlay.append(internet)
    
    lamigra = ft.Audio(src="lamigra.mp3",volume=1,balance=0)
    page.overlay.append(lamigra)

    llegada = ft.Audio(src="llegada.mp3",volume=1,balance=0)
    page.overlay.append(llegada)
    
    realidad = ft.Audio(src="realidad.mp3",volume=1,balance=0)
    page.overlay.append(realidad)
    #covid 19
    impacto = ft.Audio(src="el impacto de la tecnologia.mp3",volume=1,balance=0)
    page.overlay.append(impacto)
    
    rol = ft.Audio(src="el rol de la tecnologia.mp3",volume=1,balance=0)
    page.overlay.append(rol)
    
    declaracion = ft.Audio(src="declaracion de la informatica.mp3",volume=1,balance=0)
    page.overlay.append(declaracion)
    
    avances = ft.Audio(src="avances tecnologicos.mp3",volume=1,balance=0)
    page.overlay.append(avances)
    
    tecnologia = ft.Audio(src="La tecnología como aliada en el tiempo del Covid-19.mp3",volume=1,balance=0)
    page.overlay.append(tecnologia)
    
    impacto2 = ft.Audio(src="Impacto de la tecnología durante COVID-19.mp3",volume=1,balance=0)
    page.overlay.append(impacto2)
    
    internet2 = ft.Audio(src="el internet en tiempos del covid 19.mp3",volume=1,balance=0)
    page.overlay.append(internet2)
    
    TIC = ft.Audio(src="TIC.mp3",volume=1,balance=0)
    page.overlay.append(TIC)
    
    tecdig = ft.Audio(src="tecdig.mp3",volume=1,balance=0)
    page.overlay.append(tecdig)
    
    covid19 = ft.Audio(src="covid-19 impacto en el sector tecnologico.mp3",volume=1,balance=0)
    page.overlay.append(covid19)
    
    aporte = ft.Audio(src="aporte.mp3",volume=1,balance=0)
    page.overlay.append(aporte)
    
    latec = ft.Audio(src="latec.mp3",volume=1,balance=0)
    page.overlay.append(latec)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        fortran.pause()
        cobol.pause()
        pascal2.pause()
        c.pause()
        html.pause()
        python.pause()
        sql.pause()
        php.pause()
        java.pause()
        javascript.pause()
        cobol.pause()
        NoSQL.pause()
        perl.pause()
        swift.pause()
        rust.pause()
        snapchat.pause()
        tiktok.pause()
        facebook.pause()
        instagram.pause()
        twiter.pause()
        whatsApp.pause()
        pinterest.pause()
        reddit.pause()
        weibo.pause()
        telegram.pause()
        Qzone.pause()
        Skype.pause()
        asistentes.pause()
        analitica.pause()
        automatizacion.pause()
        blockchain.pause()
        Chatbot.pause()
        seguridad.pause()
        comercio.pause()
        IA.pause()
        internet.pause()
        lamigra.pause()
        llegada.pause()
        realidad.pause()
        impacto.pause()
        rol.pause()
        declaracion.pause()
        avances.pause()
        tecnologia.pause()
        impacto2.pause()
        internet2.pause()
        TIC.pause()
        tecdig.pause()
        covid19.pause()
        aporte.pause()
        latec.pause()
        
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
    
    def play_fortran(e):
        StopAll()
        fortran.play()
    
    def play_cobol(e):
        StopAll()
        cobol.play()
        
    def play_pascal2(e):
        StopAll()
        pascal2.play()
    
    def play_c(e):
        StopAll()
        c.play()
    
    def play_html(e):
        StopAll()
        html.play()
    
    def play_python(e):
        StopAll()
        python.play()
    
    def play_sql(e):
        StopAll()
        sql.play()
    
    def play_php(e):
        StopAll()
        php.play()
    
    def play_java(e):
        StopAll()
        java.play()
        
    def play_javascript(e):
        StopAll()
        javascript.play()
    
    def play_NoSQL(e):
        StopAll()
        NoSQL.play()
        
    def play_perl(e):
        StopAll()
        perl.play()
        
    def play_swift(e):
        StopAll()
        swift.play()
        
    def play_rust(e):
        StopAll()
        rust.play()

#audios de redes sociales

    def play_snapchat(e):
        StopAll()
        snapchat.play()

    def play_tiktok(e):
        StopAll()
        tiktok.play()

    def play_facebook(e):
        StopAll()
        facebook.play()

    def play_instagram(e):
        StopAll()
        instagram.play()

    def play_twiter(e):
        StopAll()
        twiter.play()

    def play_whatsApp(e):
        StopAll()
        whatsApp.play()

    def play_pinterest(e):
        StopAll()
        pinterest.play()

    def play_reddit(e):
        StopAll()
        reddit.play()

    def play_weibo(e):
        StopAll()
        weibo.play()

    def play_telegram(e):
        StopAll()
        telegram.play()

    def play_twiter(e):
        StopAll()
        twiter.play()

    def play_Qzone(e):
        StopAll()
        Qzone.play()
    
    def play_Skype(e):
        StopAll()
        Skype.play()
        
    def play_analitica(e):
        StopAll()
        analitica.play()
        
    def play_asistentes(e):
        StopAll()
        asistentes.play()
        
    def play_automatizacion(e):
        StopAll()
        automatizacion.play()
        
    def play_blockchain(e):
        StopAll()
        blockchain.play()
        
    def play_Chatbot(e):
        StopAll()
        Chatbot.play()
        
    def play_comercio(e):
        StopAll()
        comercio.play()
        
    def play_IA(e):
        StopAll()
        IA.play()
        
    def play_internet(e):
        StopAll()
        internet.play()
        
    def play_lamigra(e):
        StopAll()
        lamigra.play()
        
    def play_llegada(e):
        StopAll()
        llegada.play()
        
    def play_seguridad(e):
        StopAll()
        seguridad.play()
        
    def play_realidad(e):
        StopAll()
        realidad.play()
        
    def play_impacto(e):
        StopAll()
        impacto.play()
        
    def play_rol(e):
        StopAll()
        rol.play()
        
    def play_declaracion(e):
        StopAll()
        declaracion.play()
        
    def play_avances(e):
        StopAll()
        avances.play()
        
    def play_tecnologia(e):
        StopAll()
        tecnologia.play()
        
    def play_impacto2(e):
        StopAll()
        impacto2.play()
        
    def play_internet2(e):
        StopAll()
        internet2.play()
        
    def play_TIC(e):
        StopAll()
        TIC.play()
        
    def play_tecdig(e):
        StopAll()
        tecdig.play()
    
    def play_covid19(e):
        StopAll()
        covid19.play()
        
    def play_aporte(e):
        StopAll()
        aporte.play()
        
    def play_latec(e):
        StopAll()
        latec.play()

    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    
    # Botones Tipos de lenguaje btn = ElevatedButton(content=ft.Image(src="",width=img_width,height=img_height, border_radius=border_radius, semantics_label="""))
    btn21 = ElevatedButton(content=ft.Image(src="pascal2.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="pascal"), on_click=play_pascal2)
    btn22 = ElevatedButton(content=ft.Image(src="html.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="html"),on_click=play_html)
    btn23 = ElevatedButton(content=ft.Image(src="python.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="python"),on_click=play_python)
    btn24 = ElevatedButton(content=ft.Image(src="rust.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="rust"),on_click=play_rust)
    btn25 = ElevatedButton(content=ft.Image(src="cobol.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="cobol"), on_click=play_cobol)
    btn26 = ElevatedButton(content=ft.Image(src="NoSQL.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="NoSQL"), on_click=play_NoSQL)
    btn27 = ElevatedButton(content=ft.Image(src="c#.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="C#"),on_click=play_c)
    btn28 = ElevatedButton(content=ft.Image(src="php.jpg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="php"),on_click=play_php)
    btn29 = ElevatedButton(content=ft.Image(src="java.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="java"),on_click=play_java)
    btn30 = ElevatedButton(content=ft.Image(src="javascript.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="javascript"),on_click=play_javascript)
    btn31 = ElevatedButton(content=ft.Image(src="perl.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="perl"),on_click=play_perl)
    btn32 = ElevatedButton(content=ft.Image(src="swift.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="swift"),on_click=play_swift)
    
    #botones de redes sociales
    btn33 = ElevatedButton(content=ft.Image(src="snapchat.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="snapchat"),on_click=play_snapchat)
    btn34 = ElevatedButton(content=ft.Image(src="tiktok.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tiktok"),on_click=play_tiktok)
    btn35 = ElevatedButton(content=ft.Image(src="facebook.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="facebook"),on_click=play_facebook)
    btn36 = ElevatedButton(content=ft.Image(src="instagram.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="instagram"),on_click=play_instagram)
    btn37 = ElevatedButton(content=ft.Image(src="twiter.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="twiter"),on_click=play_twiter)
    btn38 = ElevatedButton(content=ft.Image(src="whatsapp.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="whatsApp"),on_click=play_whatsApp)
    btn39 = ElevatedButton(content=ft.Image(src="pinteres.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="pinterest"),on_click=play_pinterest)
    btn40 = ElevatedButton(content=ft.Image(src="reddit.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="reddit"),on_click=play_reddit)
    btn41 = ElevatedButton(content=ft.Image(src="weibo.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="weibo"),on_click=play_weibo)
    btn42 = ElevatedButton(content=ft.Image(src="telegram.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="telegram"),on_click=play_telegram)
    btn43 = ElevatedButton(content=ft.Image(src="qzone.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="Qzone"),on_click=play_Qzone)
    btn44 = ElevatedButton(content=ft.Image(src="skype.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="Skype"),on_click=play_Skype)
    #botones para covid 19
    btn45 = ElevatedButton(content=ft.Image(src="impacto.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="impacto"),on_click=play_impacto)
    btn46 = ElevatedButton(content=ft.Image(src="rol.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="rol"),on_click=play_rol)
    btn47 = ElevatedButton(content=ft.Image(src="declaracion.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="declaracion"),on_click=play_declaracion)
    btn48 = ElevatedButton(content=ft.Image(src="avances.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="avances"),on_click=play_avances)
    btn49 = ElevatedButton(content=ft.Image(src="aliada.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tecnologia"),on_click=play_tecnologia)
    btn50 = ElevatedButton(content=ft.Image(src="impacto2.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="impacto2"),on_click=play_impacto2)
    btn51 = ElevatedButton(content=ft.Image(src="internet2.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="internet2"),on_click=play_internet2)
    btn52 = ElevatedButton(content=ft.Image(src="tic.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="TIC"),on_click=play_TIC)
    btn53 = ElevatedButton(content=ft.Image(src="tec.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tecdig"),on_click=play_tecdig)
    btn54 = ElevatedButton(content=ft.Image(src="covid19.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="covid19"),on_click=play_covid19)
    btn55 = ElevatedButton(content=ft.Image(src="aporte.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="aporte"),on_click=play_aporte)
    btn56 = ElevatedButton(content=ft.Image(src="lucha.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="latec"),on_click=play_latec)
    #botones para las nuevas tecnologias
    btn57 = ElevatedButton(content=ft.Image(src="asistentes.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="asistentes"),on_click=play_asistentes)
    btn58 = ElevatedButton(content=ft.Image(src="ai.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="ia"),on_click=play_IA)
    btn59 = ElevatedButton(content=ft.Image(src="internet-cosas.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="internet"),on_click=play_internet)
    btn60 = ElevatedButton(content=ft.Image(src="rpa.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="automatizacion"),on_click=play_automatizacion)
    btn61 = ElevatedButton(content=ft.Image(src="ciber-seguridad.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="seguridad"),on_click=play_seguridad)
    btn62 = ElevatedButton(content=ft.Image(src="multi-nube.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="lamigra"),on_click=play_lamigra)
    btn63 = ElevatedButton(content=ft.Image(src="analitica-datos.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="analitica"),on_click=play_analitica)
    btn64 = ElevatedButton(content=ft.Image(src="vr.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="realidad"),on_click=play_realidad)
    btn65 = ElevatedButton(content=ft.Image(src="comercio-linea.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="comercio"),on_click=play_comercio)
    btn66 = ElevatedButton(content=ft.Image(src="block-chain.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="blockchain"),on_click=play_blockchain)
    btn67 = ElevatedButton(content=ft.Image(src="5g.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="llegada"),on_click=play_llegada)
    btn68 = ElevatedButton(content=ft.Image(src="chat-bot.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="chatbot"),on_click=play_Chatbot)
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]),
                                    ft.ElevatedButton(
                                        "la evolucion de los lenguajes de programacion",
                                        on_click=lambda _: [StopAll(), page.go('/lenguajes'),]),
                                    ft.ElevatedButton(
                                        'Las Redes Sociales',
                                        on_click=lambda _: [StopAll(), page.go('/redes')]),
                                    ft.ElevatedButton(
                                        'la informatica durante la pandemia de covid-19',
                                        on_click=lambda _: [StopAll(), page.go('/pandemia')]),
                                    ft.ElevatedButton(
                                        'las nuevas tecnologias',
                                        on_click=lambda _: [StopAll(), page.go('/nuevas')]),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la evolucion de los lenguajes de informatica"',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las redes sociales"',
                                        on_click=lambda _: page.go('/redes')
                                    ),
                                    
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn21,btn22,btn23,btn24]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn25,btn26,btn27,btn28]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn29,btn30,btn31,btn32]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de las redes sociales
        elif page.route == '/redes':
            page.views.append(
                View(
                    "/redes",
                    controls=[
                        AppBar(
                            title=ft.Text("Las redes sociales"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la informatica durante la pandemia"',
                                        on_click=lambda _: page.go('/pandemia')
                                    ),
                                    
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn33,btn34,btn35,btn36]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn37,btn38,btn39,btn40]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn41,btn42,btn43,btn44]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #viata de la informatica durante la pandemia
        elif page.route == '/pandemia':
            page.views.append(
                View(
                    "/pandemia",
                    controls=[
                        AppBar(
                            title=ft.Text("la informatica durante la pandemia de covid-19"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las nuevas tecnologias"',
                                        on_click=lambda _: page.go('/nuevas')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn45,btn46,btn47,btn48]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn49,btn50,btn51,btn52]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn53,btn54,btn55,btn56]
                                    ),
                                    
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #viata de la las nuevas tecnologias
        elif page.route == '/nuevas':
            page.views.append(
                View(
                    "/nuevas",
                    controls=[
                        AppBar(
                            title=ft.Text("las nuevas tecnologias"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn57,btn58,btn59,btn60]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn61,btn62,btn63,btn64]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn65,btn66,btn67,btn68]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")
