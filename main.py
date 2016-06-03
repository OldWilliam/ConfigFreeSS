
from MyHtmlParser import MyHtmlParser
import urllib
import json

config_entry={"server":"","server_port":443,"password":"","method":"aes-256-cfb","remarks":""}
config_path ="/cygdrive/c/Software/shadowsocks/gui-config.json"

def perform():
    parser = MyHtmlParser()
    link = urllib.urlopen('http://www.ishadowsocks.net')
    page = link.read()
    link.close()
    index = page.index('<section id="free">')
    sec = page[index:11556]
    parser.feed(sec)
    datas = parser.get_datas()
    datas = filter(has_mao,datas)
    datas = map(cut_uses,datas)
    datas = filter(not_empty,datas)
    print '\n\n######key data has been combined to a list######'
    for i in datas:
        print i
    new_server_cfg = handle_pack(datas)
    cfg_dic = retrieve_config()
    print '\n\n######old config file retrieved######'
    #Complete Cofig file include useless item(type:dict)
    print cfg_dic
    #The Key Server Config(type:list)
    print '\n\n######The Key Server Config######'
    server_cfg = cfg_dic['configs']
    for i in server_cfg:
        print i
    le = len(server_cfg)
    for j in range(le):
        server_cfg.pop(le-j-1)
    server_cfg.extend(new_server_cfg)
    print'\n\n######test'
    print cfg_dic




    return datas

def not_empty(s):
    return s and s.strip()

def has_mao(s):
    return ':' in s

def cut_uses(s):
    return s[s.index(':')+1:]

def retrieve_config(path=config_path):
    fp = open(path,'r')
    f = fp.read()
    fp.close()
    dict_cfg = json.loads(f)
    return dict_cfg

def opersistent_config(cfg_dic):
    fp = open(path,'w')
    fp.write()

def handle_pack(datas):
    tag=["server","server_port","password","method"]
    d1 ={"remarks":""}
    d2 ={"remarks":""}
    d3 ={"remarks":""}
    l = [d1,d2,d3]
    for i in range(3):
        for j in range(4):
            l[i][tag[j]]=datas[j]
    print '\n\n######The New'
    print l
    return l



if __name__ == '__main__':
    perform()
