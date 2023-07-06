from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from base64 import b64encode
__author__="MaggieLOL"
def _encode_text(text):
    result=""
    for i in text:
        if ord(i) < 257:
            result+=i
        else:
            result+=f"%u{hex(ord(i)).split('x',1)[1]}"
    return result
class NoteMS:
    def __init__(self,driver=webdriver.Chrome,options=Options):
        options=options()
        options.headless=True
        self.driver=driver(options=options)
        self.page=None
    def goto(self,page):
        self.driver.get(f"https://note.ms/{page}")
        sleep(0.5)
    def write(self,page,content):
        self.goto(page)
        #write
        b64ed=b64encode(_encode_text(content).encode("latin-1")).decode("ascii")
        script=f"document.querySelector('body > div > div.layer > div > div > textarea').innerHTML=unescape(atob('{b64ed}'))"
        self.driver.execute_script(script)
        sleep(0.2)
        return True
    def load(self,page):
        self.goto(page)
        success=False
        while not success:
            try:
                content=self.driver.find_element("xpath","/html/body/pre").get_attribute("innerText")
                success=True
            except:
                pass
        return content
    def close(self):
        self.driver.close()
