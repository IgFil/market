import eel
import requests


eel.init("ui")
@eel.expose
def http_post(action, data):
    data_split = data.split("=")
    data_dic = {
        data_split[0] : data_split[1],
        data_split[2] : data_split[3],        
    }
    req = requests.post(action, data=data_dic)
    return req.text
@eel.expose
def http_post_2(action,data):
    data_split = data.split("=")
    data_dic = {
        data_split[0] : data_split[1],
        data_split[2] : data_split[3],
        data_split[4] : data_split[5],
        data_split[6] : data_split[7],
        data_split[8] : data_split[9],
        data_split[10] : data_split[11],         
    }
    req = requests.post(action, data=data_dic)
    return req.text

@eel.expose
def http_post_3():
    req = requests.post("http://IgFil.pythonanywhere.com/sellers_trade",data={"data": "req"})
    return req.text
@eel.expose
def http_post_4():
    req = requests.post("http://IgFil.pythonanywhere.com/buyers_trade",data={"data": "req"})
    return req.text
eel.start("ui.html", size = (700, 700))

