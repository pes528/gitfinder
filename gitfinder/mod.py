import re, os 
from time import sleep

try:
    import lxml.html as html
    import mechanicalsoup
    import requests
except Exception as f:
    print(f)
    print("Instalando dependencias espera un momento por favor....\n")
    os.system("pip install mechanicalsoup")
    os.system("pip install lxml")
    os.system("pip install rqeuests")
import mechanicalsoup
import requests 
import lxml.html as html


green = "\033[1;32m"
rojito = "\033[1;34m"
fin = "\033[0m"



def total(text:str) -> int:
    try:
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
    except IndexError:return False
        


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
            if total(tot[0]) == False:
                tot = parser.xpath('//span[@class="v-align-middle"]//text()')
                self.totalRepos = total(tot[0])
            else:

                self.totalRepos = total(tot[0])
            
            
            self.repositoriosActuales = len(self.resp)
            if self.totalRepos > 10:
                
                self.morePage = True
        
    def viewResult(self):
        for i in self.resp:
            print("---> https://github.com"+i)
    
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
                print("---> https://github.com"+i)
        
    def otherPages(self, num):
        answer = self.answer.replace(" ", "+")
        other = f"https://github.com/search?p={num}&q={answer}&ref=simplesearch&type=Repositories"
        otros = others(other, self.links)
        self.repositoriosActuales += len(otros)
        for i in otros:
            print("---> https://github.com"+i)
