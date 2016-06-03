
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
    cfg_dic =  retrieve_config()
    print '\n\n######old config file retrieved######'
    #Complete Cofig file include useless item(type:dict)
    print cfg_dic
    #The Key Server Config(type:list)
    print '\n\n######The Key Server Config######'
    server_cfg = cfg_dic['configs']
    for i in server_cfg:
        print i
    len = len(server_cfg)
    for j in range(len):
        server_cfg.pop(len-j-1)
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

def persistent_config(cfg_dic):
    fp = open(path,'w')
    fp.write()

if __name__ == '__main__':
    perform()
