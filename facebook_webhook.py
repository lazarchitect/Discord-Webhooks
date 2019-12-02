import requests
import json
import websocket
import threading
import time

#############
#CONSTANTS
#############

URL = "https://www.facebook.com/groups/pinostrivia/"

ENDPOINT = "https://discordapp.com/api"

vhikk_ID = "644423562559750164"
Trivia_Channel_ID = "644005512815312897"

channel = vhikk_ID

PATH = "/channels/" + channel + "/messages"

TOKEN = "NjUwOTA1MzcxMTQ5NDY3NjU0.XeSJFw.BH2xpoDm1Z5UT_m_kBI26fyxHjM"

#############
#METHODS
#############

def get_gateway():
    responseStr = str(requests.get(ENDPOINT + "/gateway").content)
    responseObj = responseStr[2:len(responseStr)-1]
    return json.loads(responseObj)["url"]

def create_request(message):
    request = {}
    request["content"] = "application/json"
    request["tts"] = False
    request["embed"] = {}
    request["embed"]["title"] = message
    request["embed"]["description"] = "this is a message."
    return request

def wait_for_server(ws):
    while(True):
        try:
            return json.loads(ws.recv())
        except:
            continue

def heartbeat_handler(ws, heartbeat_interval):
    while(True):
        ws.send(json.dumps({"op":1, "d":None}))
        time.sleep(heartbeat_interval/1000)
        server_msg = ws.recv()
        server_opcode = server_msg["op"]
        if(server_opcode != 11):
            print("incorrect opcode, expecting 11 Heartbeat Ack")
            exit()
        #issue may arise if request_handler sends a heartbeat to answer a request, and then we send another here. is two heartbeats ok?

def request_handler(ws):
    while(True):
        server_msg = ws.recv()
        print("server says: " + server_msg + ". -Jarvis")

#############
#LOGIC
#############

# selenium: get data

# TODO later

payload = "The sky is blue. (This message was sent automatically.)"

# discord: send post request to send message
#first, gotta connect to a Gateway
gateway_url = get_gateway()

ws = websocket.WebSocket()
ws.connect(gateway_url)
server_msg = wait_for_server(ws) #should return an opcode 10 Hello payload

print("Hello opcode? : " + str(server_msg))

server_opcode = server_msg["op"]
if(server_opcode != 10):
    print("incorrect opcode, expecting 10 Hello")
    exit()

heartbeat_interval = server_msg["d"]["heartbeat_interval"]
#heartbeater = threading.Thread(target = heartbeat_handler, args = (ws, heartbeat_interval))
jarvis = threading.Thread(target = request_handler, args = (ws))

print("threads created.")

identifyObject = {}
identifyObject["token"] = TOKEN
identifyObject["properties"] = {}
identifyObject["properties"]["os"] = "windows"
identifyObject["properties"]["browser"] = "chrome"
identifyObject["properties"]["device"] = "penelope"

print("identify Object: " + str(identifyObject))

ws.send(json.dumps(identifyObject))

while(True):
    try:
        ready = ws.recv()
        break
    except:
        continue

print(ready)





