import httpx
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from bs4 import BeautifulSoup
from string import *
console = Console()
banner ="""
                                                                                                                           
                                                                                                                           
                                /$$$$$$  /$$   /$$          /$$$$$$   /$$$$$$  /$$  /$$  /$$                               
                               /$$__  $$| $$  | $$         /$$__  $$ /$$__  $$| $$ | $$ | $$                               
                              | $$  \ $$| $$  | $$        | $$  \ $$| $$  \ $$| $$ | $$ | $$                               
                              | $$  | $$| $$  | $$        | $$  | $$| $$  | $$| $$ | $$ | $$                               
                              | $$$$$$$/|  $$$$$$$        | $$$$$$$/|  $$$$$$/|  $$$$$/$$$$/                               
                              | $$____/  \____  $$ /$$$$$$| $$____/  \______/  \_____/\___/                                
                              | $$       /$$  | $$|______/| $$                                                             
                              | $$      |  $$$$$$/        | $$                                                             
                              |__/       \______/         |__/                                                             

            
                                                                                                                           
 /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$ /$$      /$$ /$$      /$$ /$$      /$$ /$$ /$$ /$$                   
| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  /$ | $$| $$  /$ | $$| $$  /$ | $$| $$  /$ | $$| $$| $$| $$                   
| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$ /$$$| $$| $$ /$$$| $$| $$ /$$$| $$| $$ /$$$| $$| $$| $$| $$                   
| $$$$$$$/| $$  | $$| $$  | $$| $$  | $$| $$/$$ $$ $$| $$/$$ $$ $$| $$/$$ $$ $$| $$/$$ $$ $$| $$| $$| $$                   
| $$____/ | $$  | $$| $$  | $$| $$  | $$| $$$$_  $$$$| $$$$_  $$$$| $$$$_  $$$$| $$$$_  $$$$|__/|__/|__/                   
| $$      | $$  | $$| $$  | $$| $$  | $$| $$$/ \  $$$| $$$/ \  $$$| $$$/ \  $$$| $$$/ \  $$$                               
| $$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$/   \  $$| $$/   \  $$| $$/   \  $$| $$/   \  $$ /$$ /$$ /$$                   
|__/       \______/  \______/  \______/ |__/     \__/|__/     \__/|__/     \__/|__/     \__/|__/|__/|__/                   
                                                                                                                                                                                                 
"""

headers = {
    'Host':'1000kitap.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
          }
inchar = "ıöcüş"
endchar = "ioçus"
def main():
    console.print(Panel(f"[italic]{banner}[/italic] "), justify='left',  style='dark_red')

def authorName():
    global names
    global nameReplace

    name = console.input("[bold blue]:writing_hand: Lütfen Yazar Adı Giriniz:[/bold blue] ")
    if name.isspace() or name in '\n':
       console.print(Panel(f"[bold]Hata ![/bold] Boş Bırakılamaz!"), style='bold white on dark_red')
       authorName()
    elif len(name) <= 2:
       console.print(Panel(f"[bold ]Hata ![/bold ] En az 2 karakter olmalı!"), style='bold white on dark_red')
       authorName()
       
    else: 
       names = name.title()
       
       name = name.lower()
       name = name.translate(str.maketrans(inchar, endchar))
       nameReplace = name.replace(' ','-')

def goWeb():
  while True:
   try:
    global r
    r = httpx.get("https://1000kitap.com/yazar/" + nameReplace , headers=headers)
    r = BeautifulSoup(r, 'html.parser')
    
    title = r.find("h1", {"class": "text"  + ' ' + "font-medium" + ' ' + "truncate" + ' ' + "text-18"}).text
    about = r.find("span", {"class": "text"  + ' ' + "text" + ' ' + "text-15"}).text
    degreeAndBirth = r.findAll("div", {"class": "dr"  + ' ' + "mb-1" + ' ' + "min-h-4" + ' ' + "flex-row" + ' ' + "items-start"})
    # 0.cı index unvan 1.index doğum bilgilerini getirir. degreeAndBirth[1].text
    console.print(f"[bold]Yazar : {names} [/bold]",justify="center", style='white on green4')
     
    
    
    table = Table(expand=True)

    table.add_column("[bold]Ad Soyad[/bold]", style="white on gray15", no_wrap=True)
    table.add_column("Hakkında", style=" white on gray15")
    table.add_column("Unvan", justify="right", style="white on gray15")
    table.add_column("Doğum Bilgileri", justify="right", style="white on gray15")
    
    table.add_row(f"{title}", f"{about}", f"{degreeAndBirth[0].text.replace('Unvan:', '')}",f"{degreeAndBirth[1].text.replace('Doğum:', '')}")
    console.print(Panel(table,style='bold white on black'))
    break
   except Exception as e:
      console.print(Panel(f"[bold]Hata ![/bold] Aranılan Yazar Bulunamadı! İsmi Kontrol Ediniz..."), style='bold white on dark_red')
      authorName()
    #console.print(Panel(f"[bold ]{degreeAndBirth[1].text}[/bold ]"), style='bold white on blue')
    
def books():
 console.print(f"[bold]{names} ait  5 Kitap[/bold]",justify="center", style='white on green4')
 global req
 req = httpx.get("https://1000kitap.com/yazar/" + nameReplace + "/kitaplar" , headers=headers)
 req = BeautifulSoup(req, 'html.parser')
 bookLists1 = req.findAll("span", {"class": "text"  + ' ' + "font-bold" + ' ' + "truncate" + ' ' + "text-16" + ' ' + "hover:underline"})
#  while True:
#      bookLists = bookLists1
#      print(bookLists)
#      break
 table1 = Table(expand=True, show_lines=True)

 table1.add_column("[bold]ID[/bold]", style="white on gray15", no_wrap=True)
 table1.add_column("Kitap Ad", style=" white on gray15")
 sayi = 0
 for bookLists in bookLists1:
     # str(bookLists + 1) + '-' + 
   #books = bookLists1[bookLists].text
   bookLists = bookLists.get_text()
   sayi = sayi + 1
   #print(str(bookLists + 1) + '-' + books)
   table1.add_row(f"{sayi}", f"{bookLists}")
   
 console.print(Panel(table1,style='bold white on black'))
 

   

    
    
main()
authorName()
goWeb()
books()
