from selenium import webdriver
import time
import json
import argparse


class Add():
    def __init__(self):
        pass

        
with open("requirements.json", "r") as f:
    data = json.load(f)
 
class Main():
    def __init__(self, path = None, driver = None, option = None, browser = None):
        self.path = data["browser_path"]
        self.driver = data["driver_path"]
        self.option = webdriver.ChromeOptions()
        self.option.binary_location = self.path
        self.option.add_experimental_option("detach", True) #This will detach browser from script and do not close it
              

    def options(self, incognito = False, headless = False):
        if incognito == True:
            self.option.add_argument("--incognito")
            print("Done")

        if headless == True:
            self.option.add_argument("--headless")
            print("Done")

        

    def navigate(self, uName, passd):
        browser = webdriver.Chrome(executable_path=self.driver, chrome_options=self.option)
        browser.get("https://econnectk12.jupsoft.com/sisStudentLogin.aspx?id=59HAojtXA6w=")

        button = browser.find_element_by_id("HrefLogin")
        button.click()
        
        username = browser.find_element_by_id("txtUserName")
        username.send_keys(uName)

        password = browser.find_element_by_id(("txtPassword"))
        password.send_keys(passd)

        check_in = browser.find_element_by_id("btn_Login")
        check_in.click()

        browser.get("https://eck12student.jupsoft.com/StudentPanel/Erp_eLearningRoom.aspx")

        ls = []
        for i in range(0, 3):
            text = browser.find_element_by_id(f"ContentPlaceHolder1_RepDetails_lblTime_{i}")
            ls.append(text.text)
        print(ls)             

        while True:
            element = browser.find_element_by_class_name("start-btn")
            # element.click() 
            try:
                alert = browser.switch_to_alert()
                alert.accept()
            except:
                print("No alert to accept")
            finally:
                pass
            time.sleep(3600)        



if __name__ =="__main__":
    script = Main()
    parser = argparse.ArgumentParser()
    parser.add_argument("--incognito", "-i", help = "It will open browser in incognito mode", action = "store_true")
    parser.add_argument("--headless", "-he", help = "It will start browser in background", action = "store_true")
    args = parser.parse_args()

    uName = data["username"]
    passd = data["password"]

    inc = False
    hd = True

    if args.incognito:
        inc = True
    if args.headless:
        hd = True    

    script.options(inc, hd)
    script.navigate(uName, passd)
    
