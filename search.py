#!/bin/python3
import re, os 
from time import sleep

try:
    import lxml.html as html
    import mechanicalsoup
    import requests
except Exception as f:
    print(f)
    print("Instalando.......")
    os.system("pip install mechanicalsoup")
    os.system("pip install lxml")
import mechanicalsoup
import requests 
import lxml.html as html


#--------------------------------------
#            author telegram @pes528
#--------------------------------------


green = "\033[1;32m"
rojito = "\033[1;34m"
fin = "\033[0m"


def verifi(lista : list) -> bool:
    try:
        lista[0]
        return True
    except:
        return False

def total(text:str) -> int:
    numero=[]
  
    for i in text:
        e = text.replace("\n", "")
    e = text.replace("\v", "")
    e = text.replace(",", "")
    
    for j in e.split():
        try:
            int(j)
            numero.append(j)
        except:
            pass
    return int(numero[0])


def others(link, search) -> list:
    res = requests.get(link)
    #res = res.text
    body = res.content.decode("utf-8")
    parser = html.fromstring(body)
    resp = parser.xpath(search)
    return resp
        


class searchGitt():
    
    linkSegundaPagina = ""
    bodyMain = ""
    resp = []
    repositoriosActuales = 0
    def __init__(self, answer):
        self.numPage = 0
        self.morePages = False
        self.answer = answer
        self.totalRepos = 0
        self.links = '//div[@class="f4 text-normal"]//@href'
        self.url = "https://github.com/search"
        self.nextPage = '//a[@class="next_page"]/@href'
        self.form = "" 
    
    
    def buscarRepos(self):
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(self.url)
        browser.select_form("form[method='get']")
        
        browser["q"]=self.answer

        browser.launch_browser()
        #browser.form.print_summary()
        resp = browser.submit_selected()
        body = resp.content.decode("utf-8")
        self.bodyMain = body
        parser = html.fromstring(self.bodyMain)
        
        self.resp = parser.xpath(self.links)
        tot = parser.xpath('//div[@class="d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative"]/h3/text()')
        if tot:
            self.totalRepos = total(tot[0])
            self.repositoriosActuales = len(self.resp)
            if self.totalRepos > 10:
                
                self.morePage = True
    
    def viewResult(self):
        for i in self.resp:
            print(f"---> {green}https://github.com{i}{fin}")
    
    def secondPage(self):
        resp = html.fromstring(self.bodyMain)
        parser = resp.xpath(self.nextPage)
        if parser:
            self.linkSegundaPagina = f"https://github.com{parser[0]}"
        
            self.numPage = re.findall('[0-9]+', parser[0])
            e = requests.get(self.linkSegundaPagina)
            e = e.content.decode("utf-8")
            parse = html.fromstring(e)
            self.resp = parse.xpath(self.links)
            self.repositoriosActuales += len(self.resp)
            for i in self.resp:
                print(f"---> {green}https://github.com{i}{fin}")
        
    def otherPages(self, num):
        answer = self.answer.replace(" ", "+")
        other = f"https://github.com/search?p={num}&q={answer}&ref=simplesearch&type=Repositories"
        otros = others(other, self.links)
        self.repositoriosActuales += len(otros)
        for i in otros:
            print(f"---> {green}https://github.com{i}{fin}")


#https://github.com/search?p=2&q=asd&ref=simplesearch&type=Repositories

def logo():
    print("""
░██████╗░██╗████████╗██╗░░██╗██╗░░░██╗██████╗░
██╔════╝░██║╚══██╔══╝██║░░██║██║░░░██║██╔══██╗
██║░░██╗░██║░░░██║░░░███████║██║░░░██║██████╦╝
██║░░╚██╗██║░░░██║░░░██╔══██║██║░░░██║██╔══██╗
╚██████╔╝██║░░░██║░░░██║░░██║╚██████╔╝██████╦╝
░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═════╝░\n""")
    print("\033[1;101m                    𝙎𝙀𝘼𝙍𝘾𝙃                \033[0m")
    print("                 𝗯𝘆 Telegram:@𝗽𝗲𝘀𝟱𝟮𝟴 	\n")
    print("""
    ----------------------------------------
    Encuentra repositorios alojados en github
                        v1.0
    ----------------------------------------
    """)
def main() -> None:
    os.system("clear")
    logo()
    
    print("Escribe el nombre del respositorio que quieres buscar\nPreciona 0 para salir\n")
    repositorio = input("BUSCAR---> ")
    if repositorio == "0":
        os.system("clear")
        print("Saliste, para volver a iniciar escribe: python search.py")
    else:
        gitt = searchGitt(repositorio)
        gitt.buscarRepos()
        print(f"TOTAL ENCONTRADOS PARA [{rojito}{gitt.answer}{fin}] --> {rojito}{gitt.totalRepos}{fin}")
        gitt.viewResult()
        print("")
        paginasTotales = gitt.totalRepos/10
        numPag = 3
        contRepos = 0
    
        if gitt.totalRepos > 10:
            gitt.secondPage()

            while gitt.repositoriosActuales < gitt.totalRepos:
                print("—"*40)
                print(f"TOTAL RESPOSITORIOS VISTOS --> \033[1;31m {gitt.repositoriosActuales}\033[0m \nQUEDAN POR VER --> \033[1;31m{gitt.totalRepos-gitt.repositoriosActuales}\033[0m \n")
                sleep(3)
                u = input("Preciona enter para continuar\nPreciona 0 para volver\nOpcion-> : ")
                if u == "0":
                    return main()
                else:
                    gitt.otherPages(numPag)
                    numPag += 1
            print("Llegaste al final 😉 ")
            input("Preciona cualquier tecla para volver: ")
            main()
        elif gitt.totalRepos < 10:
            gitt.secondPage()
            input("Preciona enter para volver: ")
            main()

    

if __name__ == "__main__":
    main()


