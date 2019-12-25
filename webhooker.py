import requests
from selenium import webdriver

channel = "vhikk"

FB_URL = "https://www.facebook.com/groups/pinostrivia/"

ENDPOINT = "https://discordapp.com/api"

Topics_webhook_ID = "650911584293617664"
Topics_webhook_token = "ZkGZdqjoOpJ-uqwRoH9uoMSSViWSU-TNQtoBBMEtgeohTeq1sxpS_ZXf5L-OZPdjSnCr"

Coming_webhook_ID = "651281444735287317"
Coming_webhook_token = "UI0R_c5wuZOjAAwFcA_yZLXC8fgh8ilP5rcqYirP9gL6YXMjkhvEmFomgF5zTSaDa8eB"

vhikk_webhook_ID = "647554996170129419"
vhikk_webhook_token = "Gji_GiyTyfB2-tW4_G7G9FY63cwOr3NpXfG6oKDu5i_QgsnxILYg8Wbw1QzOsTdLBpqB"

if(channel=="Topics"):
    webhook_ID = Topics_webhook_ID
    webhook_token = Topics_webhook_token

elif(channel=="Coming"):
    webhook_ID = Coming_webhook_ID
    webhook_token = Coming_webhook_token

elif(channel=="vhikk"):
    webhook_ID = vhikk_webhook_ID
    webhook_token = vhikk_webhook_token

PATH = "/webhooks/" + webhook_ID + "/" + webhook_token

#################################

driver = webdriver.Chrome()

driver.get(FB_URL)
name = driver.find_element_by_xpath("//span[@class='_39_n']").text
message = driver.find_element_by_xpath("//div[@role='feed']").text

payload = name + " Says: \n" + message
#payload = "Coming to Trivia? \nIf you are coming, react with an exclamation point. \nNot Sure? React with a question mark. \nNot coming? Don't react.";


def postToWebhook(payload):
    requests.post(url=ENDPOINT+PATH, data={"content": payload})


postToWebhook(payload)