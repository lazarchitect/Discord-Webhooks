import requests, random, time

def scrub(string):
    return string.replace("&#039;", "'").replace("&quot;","\"")

API = "https://opentdb.com/api.php?amount=10"

# get info from trivia: question and answer(s)
response = requests.get(API).json()

question = response["results"][0]["question"]
correct  = response["results"][0]["correct_answer"]
incorrect= response["results"][0]["incorrect_answers"]

incorrect.append(correct)
random.shuffle(incorrect)

payload = "-------------------\n"+question + "\n"
for i in incorrect:
    payload += i+"\n"

payload += ("\n(The correct answer will be posted in five minutes.)")

IMAS = "https://discordapp.com/api/webhooks/653364099702456340/D_He1O4_4uCrfApfDi4LQA7JRD-EHHNMXrl3EY2a8hmY_gdqJ9ClTjZAnYZZaXi2izbP"
SPIDEY = "https://discordapp.com/api/webhooks/653366444071059475/iZZUzQRr5Zx06mZ2aoo8qwaJk7tsWfgPOTZBD7PbEH7oywQrbggmXRnxp4gthG-osQqX"

WEBHOOK = SPIDEY

# send to discord
requests.post(url=WEBHOOK, data={"content": scrub(payload)})

time.sleep(300)

payload = "The correct answer is: " + correct

requests.post(url=WEBHOOK, data={"content": scrub(payload)})


