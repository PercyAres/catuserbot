#  Copyright (C) @chsaiujwal 2020-2021
import requests
import os
import re
import asyncio
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from uniborg.util import CMD_LIST

@bot.on(admin_cmd(outgoing=True, pattern="book$"))
@bot.on(sudo_cmd(pattern="book$", allow_sudo=True))
async def gibbooks(book):
    if book.fwd_from:
        return
    input_str = book.pattern(1)
    lool = 0
    await book.edit("searching for the book...")
    lin = "https://b-ok.cc/s/"
    text = input_str
    link = lin+text

    headers = ['User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0']
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    f = open("book.txt",'w')
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
      nbx = nb.replace("(", "").replace(")", "")
    if nbx == "0":
        await event.edit("No Books Found with that name.")
    else:

        for tr in soup.find_all('td'):
            for td in tr.find_all('h3'):
                for ts in td.find_all('a'):
                    title = ts.get_text()
                    lool = lool+1
                for ts in td.find_all('a', attrs={'href': re.compile("^/book/")}):
                    ref = (ts.get('href'))
                    link = "https://b-ok.cc" + ref

                f.write("\n"+title)
                f.write("\nBook link:- " + link+"\n\n")

        f.write("Yippie!!! I found your books")
        f.close()
        caption="By Friday.\n Get Your Friday From @FRIDAYCHAT"
        
        await borg.send_file(event.chat_id, "book.txt", caption=f"**BOOKS GATHERED SUCCESSFULLY!\n\nBY FRIDAY.**")
        os.remove("book.txt")
        await book.delete()
        
CMD_HELP.update(
    {
        "You'll get the required book"
    }
)
# Credits to Friday userbot (and it's owner @Midhun_xD)
