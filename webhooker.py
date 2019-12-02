import requests
from selenium import webdriver

channel = "IMAS"

FB_URL = "https://www.facebook.com/groups/pinostrivia/"

ENDPOINT = "https://discordapp.com/api"

IMAS_webhook_ID = "650911584293617664"
IMAS_webhook_token = "ZkGZdqjoOpJ-uqwRoH9uoMSSViWSU-TNQtoBBMEtgeohTeq1sxpS_ZXf5L-OZPdjSnCr"

vhikk_webhook_ID = "647554996170129419"
vhikk_webhook_token = "Gji_GiyTyfB2-tW4_G7G9FY63cwOr3NpXfG6oKDu5i_QgsnxILYg8Wbw1QzOsTdLBpqB"

if(channel=="IMAS"):
    webhook_ID = IMAS_webhook_ID
    webhook_token = IMAS_webhook_token

elif(channel=="vhikk"):
    webhook_ID = vhikk_webhook_ID
    webhook_token = vhikk_webhook_token

PATH = "/webhooks/" + webhook_ID + "/" + webhook_token

#################################

driver = webdriver.Chrome()

driver.get(FB_URL)
name = driver.find_element_by_xpath("//span[@class='_39_n']").text
message = driver.find_element_by_xpath("//div[@class='_3w8y']").text

payload = name + " Says: \n" + message

requests.post(url=ENDPOINT+PATH, data={"content": payload})