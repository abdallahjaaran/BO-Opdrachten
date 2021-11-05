# Add your Python code here. E.g.
from microbit import *


import time


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    

def start():
    print(style.WHITE + 'Jaar: 2005\nLand: Lebanon\nNaam: Mohammad\nLeeftijd: 20 jaar oud.')
    sleep(2000)
    print(style.BLUE + 'Je bent Mohammad in dit verhaal.')
    sleep(2000)
    print(style.YELLOW + 'Je bent een hardwerkende jongen man. Die moeilijk een toekomst kan vinden in Lebanon.')
    print(style.YELLOW + 'Het verschil tussen rijk en arm is groot en als je in een arme famillie geboren bent.')
    print(style.YELLOW + 'Is het moeilijk om naar de rijke kant te gaan.')
    print(style.YELLOW + 'Omdat je zo arm bent heb je eten en geld gestolen van rijke mensen')
    print(style.YELLOW + 'Ze hebben de politie ingeschakeld.')
    sleep(10000)
    stuk1_1()


def stuk1_1():
    print(style.WHITE + 'Je loopt op straat in lebenon, twee agenten zien je wat doe je?')
    sleep(5000)
    print(style.MAGENTA + 'A: Je drijt je om en loopt rustig weg')
    print(style.MAGENTA + 'B: Je begroet de agenten en doet jezelf voor als een ander persoon')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bent ontkomen van de agenten')
            stuk1_goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'De agenten hebben je door')
            stuk1_fout()
            break


def stuk1_fout():
    print(style.WHITE + 'De agenten gaan je nu aresteren. Wat ga je doen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Je gaat het gevecht met ze aan.')
    print(style.MAGENTA + 'B: Je probeerd te ontsnappen.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bent ontsnapt')
            stuk1_middengoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Ze hebben je opgepakt en je hebt de dood straf gekregen.')
            break
        
        
def stuk1_goed():
    print(style.WHITE + 'Je wilt vluchten uit Lebanon. Je loopt nu richting je huis, onderweg zie je twee vrienden groepen.') 
    print(style.WHITE + 'De eerste groep zijn echte goede vrienden van je mij ze zijn niet zo sterk of slim als de tweede groep.') 
    print(style.WHITE + 'De tweede groep is redelijk te vertrouwen maar dus niet zo goed als de eerste vrienden groep.') 
    print(style.WHITE + 'Je gaat ze om hulp vragen maar je kan maar een vrienden groep meenemen.') 
    print(style.WHITE + 'Want anders wordt het teveel en heb je meer kans dat je gepakt wordt.')
    sleep(5000)
    print(style.MAGENTA + 'A: Eerste vrienden groep.')
    print(style.MAGENTA + 'B: Tweede vrienden groep.')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt de goede keuze gemaakt. Want vertrouwen is belangrijk.')
            stuk1_2goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Nu ga je vluchten met vrienden die misschien achterbaks zijn.')
            stuk1_2slecht()
            break
            
            
def stuk1_middengoed():
    print(style.WHITE + 'Je bent dus ontsnapt. Je moet nu onderschuilen voor de agenten die je hebben gezien')
    print(style.WHITE + 'Je kan onderschuilen bij twee vrienden groepen. De eerste vrienden groep zijn je echte goede vrienden.')
    print(style.WHITE + 'Maar ze zijn niet zo sterk of slim als de tweede groep.')
    print(style.WHITE + 'De tweede groep is redelijk te vertrouwen maar dus niet zo goed als de eerste vrienden groep')
    sleep(5000)
    print(style.MAGENTA + 'A: Eerste vrienden groep')
    print(style.MAGENTA + 'B: Tweede vrienden groep')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt deking gezocht bij de goede vrienden je besluit met hun te vluchten naar Nederland.')
            stuk1_2goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je zochenaamde vrienden gaan je dwingen om te vluchten en zo het risco te nemen dat je alles verliest.')
            stuk1_2slecht()
            break
        
        
def stuk1_2goed():
    print(style.WHITE + 'Met je vrienden ga je nu beslissen wat jullie volgende stap is.')
    sleep(5000)
    print(style.MAGENTA + 'A: Jullie pakken de auto.')
    print(style.MAGENTA + 'B: Jullie gaan met de voet.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Met je vrienden probeer je nu naar Jordanië te gaan naar het vliegveld van Amman.')
            stuk1_dereisgoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie gaan proberen naar de dichtbijzijndse vliegveld in Lebanon te gaan.')
            stuk1_dereisslecht()
            break


def stuk1_2slecht():
    print(style.WHITE + 'Ze gaan nu beslissen wat de volgende stap is. Jij hebt er een woord in wat gaan jullie doen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Jullie gaan lopend.')
    print(style.MAGENTA + 'B: Jullie gaan met de auto')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je gaat nu proberen om naar Jordanië te gaan. Je wilt het vliegveld van Amman halen.')
            stuk1_dereisgoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je gaat nu proberen om naar de dichtsbijzijndse vliegveld van Lebanon te gaan.')
            stuk1_dereisslecht()
            break


def stuk1_dereisgoed():
    print(style.WHITE + 'Jullie moeten een auto kiezen, je hebt een opvallende auto maar hij is wel snel.\n Of je kunt kiezen voor een slomme onopvallende auto.')
    sleep(5000)
    print(style.MAGENTA + 'A: Onopvallende auto')
    print(style.MAGENTA + 'B: Opvallende auto')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt een slomme oponvallende auto gekozen je kunt makkelijk naar Amman toe zonder dat je opvalt.')
            stuk1_aankomstvliegveld()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt voor de snelle opvallende auto gekozen. Niet alleen is die opvallend maar ook snel.\n Wat hem meer opvallend maakt.')
            stuk1_dereismiddengoedauto()
            break
        

def stuk1_dereisslecht():
    print(style.WHITE + 'Je moet nu kiezen hoe je gaat lopen, pak je de snelle maar opvallende weg. Of de slomme maar onopvallende weg.')
    sleep(5000)
    print(style.MAGENTA + 'A: Onpvallende weg')
    print(style.MAGENTA + 'B: Opvallende weg')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt gekozen voor de slomme maar onopvallende weg. Je kan makkelijk naar het vliegveld komen.\n Zonder dat je opgemerkt wordt.')
            stuk1_aankomstvliegveld()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt gekozen voor de opvallende weg. Je kan er moeilijk doorheen want veel agenten lopen door deze weg heen.')
            stuk1_dereismiddengoedlopend()
            break
        

def stuk1_dereismiddengoedauto():
    print(style.WHITE + 'Een agent stopt jullie auto onderweg, hij vraagt voor jullie id.')
    sleep(5000)
    print(style.MAGENTA + 'A: We rijden super hard weg')
    print(style.MAGENTA + 'B: Je doet je voor als iemand die op vakantie is en de taal niet kan spreken. ')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Het is gelukt je vrienden hebben gezegd dat je je id niet bij je hebt en dat je komt uit Turkey.')
            stuk1_aankomstvliegveldamman()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie zijn super hard weg gereden de agent heeft andere agenten erbij geroepen. Jullie zijn gepakt en je hebt levenslang gekregen.')
            break


def stuk1_dereismiddengoedlopend():
    print(style.WHITE + 'Je loopt door de weg een agent stopt jullie, hij vraagt om jullie id.')
    sleep(5000)
    print(style.MAGENTA + 'A: Je rent super hard weg.')
    print(style.MAGENTA + 'B: Je doet je voor als iemand die op vakantie is gekomen en die de taal niet kan spreken.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Het is gelukt je vrienden hebben gezegd dat je je id niet bij je hebt en dat je komt uit Turkey.')
            stuk1_aankomstvliegveldlebanon()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie zijn hard weg gerend voor de agent. De agent heeft andere agenten erbij geroepen. Jullie zijn gepakt en je hebt levenslang gekregen.')
            break
        
        
def stuk1_aankomstvliegveldamman():
    print(style.WHITE + 'Jullie zijn nu aangekomen bij het vliegveld van Amman. Je kan alleen niet naar Nederland vliegen maar wel naar Turkey.\n Je hebt ook de optie om met de boot te gaan.')
    sleep(5000)
    print(style.MAGENTA + 'A: Turkey')
    print(style.MAGENTA + 'B: Met de boot')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je gaat naar Turkey vliegen. De reis is lang en spanned.')
            stuk_eindeprefect1()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt besloten om met de boot naar Nederland proberen te gaan.')
            stuk_einderedelijk1()
            break
        

def stuk1_aankomstvliegveldlebanon():
    print(style.WHITE + 'Jullie zijn nu aangekomen bij het vliegveld van Lebanon. Je hebt moeite om er doorheen te gaan. Je hebt wel een fake id')
    print(style.WHITE + 'Je kan ervoor kiezen de fake id te gebruiken of met de auto naar het vliegveld van Syrië te gaan')
    sleep(5000)
    print(style.MAGENTA + 'A: Fake id gebruiken')
    print(style.MAGENTA + 'B: Vliegveld van Syrië')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je besluit om naar het vliegveld van Syrië te gaan.')
            stuk_eindegoed1()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je gaat je fake id gebruiken. Ze hebben de politie geroept.')
            stuk_eindeslecht1()
            break
        

def stuk_eindeprefect1():
    print(style.WHITE + 'Je bent in Turkey aangekomen. Je kan nu gerust door naar nederland. Wil je dat en je leven achterlaten en een nieuw leven beginnen of niet?
    sleep(5000)
    print(style.MAGENTA + 'A: Ik wil door wel.')
    print(style.MAGENTA + 'B: Ik wil terug.')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je gaat door naar Nederland. Je weet niet wat je te wachten staat')
            stuk_eindeprefect2()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je gaat terug. Je wilt weer proberen je leven goed opteleiden.')
            break
        
        
def stuk_eindegoed1():
    print(style.WHITE + 'Door lang moeite te doen ben je aangekomen in het vliegveld van Syrië. Je hebt te horen gekregen dat je niet naar Nederland kan.')
    print(style.WHITE + 'Je moet nu kiezen je kan met de boot of met de bus naar Nederland gaan.')
    sleep(5000)
    print(style.MAGENTA + 'A: Boot')
    print(style.MAGENTA + 'B: Bus')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt gekozen voor de boot. Je hebt een lange weg te gaan.')
            stuk_eindegoed2()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt gekozen voor de bus. Je moet vaak stoppen bij duanes en bent gepakt.')
            break
        
        
def stuk_einderedelijk1():
    print(style.WHITE + 'Onderweg merk je dat de boot stuk aan het gaan is. Blijf je erop of pak je de risico om te zwemmen.')
    sleep(5000)
    print(style.MAGENTA + 'A: Ik ga zwemmen.')
    print(style.MAGENTA + 'B: Ik blijf erop.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt besloten om erop te blijven de boot heeft het goed volgehouden.')
            stuk_einderedelijk2()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt besloten om te zwemmen. Het water is zo heftig dat je verdronken bent.')
            break
        
        
def stuk_eindeslecht1():
    print(style.WHITE + 'Je gaat nu weg rennen voor de politie. Je kan via de raam eruit gaan of via de voor deur.
    sleep(5000)
    print(style.MAGENTA + 'A: Via de raam.')
    print(style.MAGENTA + 'B: Via de voor deur.')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bent nu buiten. Voor nu ben je ontkomen aan de agenten.')
            stukeindeslecht2()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Bij de voor deur zaten de agenten je op te wachten je bent gepakt.')
            break
        
    
def stuk_eindeprefect2():
    print(style.WHITE + 'Je bent aangekomen in Nederland in Amsterdam.\n Wat ga je nu doen tegen de agenten zeggen dat je een vluchteling bent of proberen illigaal te leven.
    sleep(5000)
    print(style.MAGENTA + 'A: Tegen de agenten zeggen dat ik een vluchteling ben.')
    print(style.MAGENTA + 'B: Illigaal proberen te leven.')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'De agenten nemen je mee naar een kantoor.')
            stuk_eindeprefect3()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Het is je niet gelukt om te blijven zonder dat je gepakt werd. Je bent terug gestuurd naar Lebanon.')
            break
    

def stuk_eindegoed2():
    print(style.WHITE + 'Je bent aangekomen in Rotterdam. Met de mensen waarmee je deze weg mee hebt gelopen.')
    print(style.WHITE + 'Wil je met die mensen blijven of een andere weg nemen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Met ze blijven')
    print(style.MAGENTA + 'B: Andere weg op gaan.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt besloten om een andere weg op te gaan. Je hebt een baan gevonden en je hebt een nieuwe famillie opgestart.')
            print(style.GREEN + 'Je bent nu gelukkig maar je mist wel je eigen land nog. Je hebt meestal de goede keuzes genomen om zo ver te komen.')
            print(style.GREEN + 'Je hebt het gehaald en nu ga je veder met je nieuwe leven in Nederland.')
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt met hun een bedrijf gestart maar is uiteindelijk uit elkaar gegaan. Ze zijn andere wegen op gegaan.')
            print(style.RED + 'Het is wel gelukt om later met een paar van de mensen een goed werkend bedrijf op te kunnen starten.')
            print(style.RED + 'Maar het kost je wel veel moeite om dit bedrijf werkend te houden vanwege de stres die zich rond speelt.')
            print(style.RED + 'Je gaat nu je leven zo veder in Nederland')
            break
        
       
def stuk_einderedelijk2():
    print(style.WHITE + 'Een oude vrouw wilt springen om te zwemmen en een jonge jongen die nog geen eens 5 jaar oud lijkt te zijn.')
    print(style.WHITE + 'Wie ga je reden?')
    sleep(5000)
    print(style.MAGENTA + 'A: Oude vrouw.')
    print(style.MAGENTA + 'B: Jonge jongen.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt besloten de jonge jongen te reden. Zijn ouders waren zo blij dat je hun jongen hebt gered.')
            print(style.GREEN + 'Je bent nu aangekomen in Nederland de overheid heeft gehoord wat je hebt gedaan je ontvangt 1 miljoen voor je goede gedrag.')
            print(style.GREEN + 'Je bent nu miljoener in Nederland en hebt een goed leven')
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt de oude vrouw gered. De jonge jongen is verdronken.')
            print(style.RED + 'Je bent aangekomen in Nederland de ouders van de jonge jongen zijn kapot. Ze hebben hun kind verloren.')
            print(style.RED + 'Je gaat nu je leven veder wetend dat een jonge jongen door jouw dood is gegaan.')
            break
        


def stuk_eindeslecht2():
    print(style.WHITE + 'Een agent heeft je gevonden je gaat weer op de vlucht.')
    print(style.WHITE + 'Je moet nu kiezen steel je de auto van de agent of blijf je rennen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Auto stelen.')
    print(style.MAGENTA + 'B: blijven rennen.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bleef rennen je bent uiteindelijk beland bij een famillie die je naar Turkey kan brengen.')
            print(style.GREEN + 'Je gaat nu een nieuw leven starten in Turkey. Je hebt een nu een famillie met twee kinderen.')
            print(style.GREEN + 'Daarnaast heb je ook een goede baan dit wordt jouw leven in Turkey nu')
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Heb je niet geleerd van je fouten aan het begin?')
            print(style.RED + 'Je bent opgepakt en hebt nu dubbel zoveel straf gekregen dan dat je eerst zou krijgen')
            print(style.RED + 'Het is je niet gelukt om naar Nederland te vluchten je hebt nu levenslang gekregen.')
            print(style.RED + 'Je gaat nu de rest van je leven leven in een cel.')
            break
        
   
 def stuk_eindeprefect3():
    print(style.WHITE + 'Je hebt te horen gekregen dat je mag blijven. Je hebt de keuze of je gaat in Amsterdam leven waar alles duur is.')
    print(style.WHITE + 'Of erbuiten waar alles goedkoop is')
    sleep(5000)
    print(style.MAGENTA + 'A: Erbuiten')
    print(style.MAGENTA + 'B: Amsterdam')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt een goed leven in Amsterdam met veel vrienden en veel sociaal contact.')
            print(style.GREEN + 'Je hebt kan het makkelijk vinden met mensen en je beleeft veel plezier.')
            print(style.GREEN + 'Gefeliciteerd je hebt het gemaakt in Nederland en gaat zo je goede leven veder leven!')
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Het is saai buiten Amsterdam en te rustig. Je kan geen andere vrienden maken.')
            print(style.RED + 'Je hebt niet genoeg sociaal contact en beleeft geen plezier.')
            print(style.RED + 'Je hebt het wel in Nederland gemaakt en kan nu rustig je leven leven.')
            break
        
        
start()