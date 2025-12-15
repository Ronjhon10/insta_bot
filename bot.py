# <><><><><><><><><><><><><><><><><>
# IMPORTS
# <><><><><><><><><><><><><><><><><>
import time, tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

def comment_click(username, password, comment, times):
    '''
    Initializes the webdriver and pulls the instagram site.
    Uses given arguments to pass the login screen and prepares
    the post feed to be clicked by the type_comment function.
    All arguments should be passed as strings
    '''
    opts = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=opts)
    ### LOGIN ###
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    username_box = driver.find_element(By.NAME, "username")
    username_box.send_keys(username)
    time.sleep(2)
    password_box = driver.find_element(By.NAME, "password")
    password_box.send_keys(password)
    time.sleep(2)
    login = driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[3]/button/div")
    login.click()
    time.sleep(10)
    ### BY-PASS REMEMBER LOGIN ###
    not_now = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
    not_now.click()
    time.sleep(5)
    ### SCROLL POST INTO VIEW ###
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)
    comment_box = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Comment']")
    comment_box.click()
    time.sleep(7)
    ### EXECUTE COMMENT SCRIPT ###
    for _ in range(times):
        type_comment(driver, comment)
        time.sleep(5)

def type_comment(driver, text, timeout=15):
    '''
    Waits for the dynamic post box to load and tries multiple times to access the text box at which
    point it sends the keys specified by whatever string is passed as 'text'. The default timeout is
    set to 15 seconds but can be adjusted.
    The driver argument should be the driver assigned in the comment_click function for continuity.
    '''
    comment_box = (By.XPATH, "/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")
    wait = WebDriverWait(driver, timeout)
    try:
        driver.switch_to.default_content()
    except Exception:
        pass

    tries = 3
    for _ in range(tries):
        try:
            box = wait.until(EC.presence_of_element_located(comment_box))
            wait.until(EC.element_to_be_clickable(comment_box))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", box)
            box.click()
            box.send_keys(text)
            time.sleep(3)
            box.send_keys(Keys.RETURN)
            return
        except StaleElementReferenceException:
            continue
    raise TimeoutException("Could not type comment due to repeated stale elements.")

def user_input():
    '''
    Launches the tkinter window and creates the four input boxes which act as the user interface.
    Returns all of the user input as a tuple organized username, password, text, times to comment.
    '''
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Instagram Comment Bot v0.1")

    tk.Label(root, text="Enter your Username", font=("Arial", 16)).pack(pady=20)
    entry_u = tk.Entry(root); entry_u.pack()

    tk.Label(root, text="Enter your Password", font=("Arial", 16)).pack(pady=10)
    entry_p = tk.Entry(root, show="*"); entry_p.pack()

    tk.Label(root, text="How many comments to send", font=("Arial", 16)).pack(pady=10)
    entry_n = tk.Entry(root); entry_n.pack()

    tk.Label(root, text="What comment to send", font=("Arial", 16)).pack(pady=10)
    entry_c = tk.Entry(root); entry_c.pack()

    result = {}

    def get_input():
        result["username"] = entry_u.get()
        result["password"] = entry_p.get()
        result["comment"]  = entry_c.get()
        result["times"]    = entry_n.get()
        root.quit()
    tk.Button(root, text="START", command=get_input).pack()
    root.mainloop()
    root.destroy()
    username = result.get("username", "")
    password = result.get("password", "")
    comment  = result.get("comment", "")
    try:
        times = int(result.get("times", "0") or 0)
    except ValueError:
        times = 0
    return username, password, comment, times

if __name__ == "__main__":
    username, password, comment, times = user_input()
    comment_click(username, password, comment, times)


