from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains 

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
actions = ActionChains(driver)

wait = WebDriverWait(driver, 5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ---------------------- Test 1 - Radio buttons ---------------------------------
print("--------------------- Test 1 Start --------------------------")
# Find all radio buttons and theck if only $TARGET_BUTTON is selected
def radio_buttons_tester(radio_buttons_list: list):
    for button_index in range(len(radio_buttons_list)):
        radio_button = radio_buttons_list[button_index]

        button_name = radio_button.get_attribute("value")

        if radio_button.is_selected():
            print("\t{0} - SELECTED".format(button_name))
        else:
            print("\t{0} - NOT SELECTED".format(button_name))

# Click radio button 3
driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='radio3']").click()

radio_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//input[@class='radioButton']")))
radio_buttons_tester(radio_buttons)




# Click radio button 2
driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='radio2']").click()
radio_buttons_tester(radio_buttons)

print("--------------------- Test 1 End --------------------------")
sleep(3)

# ---------------------- END - Radio buttons ------------------------------------------




driver.refresh()




# ---------------------- Test 2 - Suggestion ------------------------------------------
print("--------------------- Test 2 Start --------------------------")
autocomplete_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#autocomplete")))
autocomplete_input.send_keys("South")
options_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//li[@class='ui-menu-item']//div")))

for option in options_list:
    if option.text == "South Africa":
        option.click()
        break

sleep(1)

autocomplete_input.clear()
sleep(1)

autocomplete_input.send_keys("Republic")

# Wait for results to be rendered
sleep(3)

options_list_2 = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//li[@class='ui-menu-item']//div")))

options_list_2[0].click()

print("--------------------- Test 2 End --------------------------")
sleep(3)
# ---------------------- END - Suggestion ---------------------------------------------




driver.refresh()




# ---------------------- Test 3 - Checkbox ---------------------------------------------
print("--------------------- Test 3 Start --------------------------")
def checkbox_tester(checkbox_list: list):
    for button_index in range(len(checkbox_list)):
        checkbox = checkbox_list[button_index]

        checkbox_name = checkbox.get_attribute("value")

        if checkbox.is_selected():
            print("\t{0} - SELECTED".format(checkbox_name))
        else:
            print("\t{0} - NOT SELECTED".format(checkbox_name))

checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))

for item in checkboxes:
    item.click()

checkbox_tester(checkboxes)
sleep(3)

for item in checkboxes:
    if item.get_attribute("value") == "option1":
        item.click()
        break

checkbox_tester(checkboxes)

print("--------------------- Test 3 End --------------------------")
sleep(3)
# ---------------------- END - Checkbox ------------------------------------------------



driver.refresh()



# ---------------------- Test 4 - Show/Hide --------------------------------------------
print("--------------------- Test 4 Start --------------------------")
hide_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hide-textbox")))
show_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#show-textbox")))

displayed_element = wait.until(EC.presence_of_element_located((By.ID, 'displayed-text')))

hide_button.click()

if not displayed_element.is_displayed():
    print("\tHide/Show == Hidden")

sleep(2)

show_button.click()

if displayed_element.is_displayed():
    print("\tHide/Show == Showing")

print("--------------------- Test 4 End --------------------------")
sleep(3)
# ---------------------- END - Show/Hide -----------------------------------------------


driver.refresh()



# ---------------------- Test 5 - Web Table fixed header --------------------------------
print("--------------------- Test 5 Start --------------------------")
table_row_6_columns = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[6]/td[4]")))
if int(table_row_6_columns[0].text) == 46:
    print("\tTRUE")

total_amount_collected = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[2]/fieldset[2]/div[2]")))
amount = int(total_amount_collected[0].text.split(":")[1].strip())
if amount == 296:
    print("\tTRUE")

table_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr")))
total = 0

for row_index in range(1, len(table_rows) + 1):
    column = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[{0}]/td[4]".format(row_index))))
    total += int(column[0].text)
    sleep(1)
print("\tTotal = {0}".format(total))

print("--------------------- Test 5 End --------------------------")
sleep(3)
# ---------------------- END - Web Table fixed header -----------------------------------
driver.refresh()

# ---------------------- Test 6 - iFrame ---------------------------------------------
print("--------------------- Test 6 Start --------------------------")
if driver.find_elements(By.TAG_NAME, 'iframe'):
    print("\tiFrame PRESENT")
else:
    print("\tiFrame ABSENT")

iframe = driver.find_element(By.ID, 'courses-iframe')
actions.move_to_element(iframe).perform()
sleep(1)

driver.switch_to.frame("courses-iframe")
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/header/div[2]/div/div/div[2]/div[2]/a")))
login_button.click()

sleep(1)
driver.switch_to.default_content()


print("--------------------- Test 6 End --------------------------")
sleep(3)
# ---------------------- END - iFrame ------------------------------------------------
driver.close()