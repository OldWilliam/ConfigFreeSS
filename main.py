
from MyHtmlParser import MyHtmlParser
import urllib
import json
import phone_config

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
    datas = filter(has_colon,datas)
    datas = map(cut_after_colon,datas)
    datas = filter(not_empty,datas)

    print '\n\n######key data has been combined to a list######'
    for i in datas:
        print i

    #transform the list to the correct format that a list contain three dic
    new_server_cfg = transform(datas)

    #complete config file include useless item from the disk(type:dict)
    cfg_dic = retrieve_config()

    #key SS config Segment(type:list)
    server_cfg = cfg_dic['configs']

    #clear the list of server config
    le = len(server_cfg)
    for j in range(le):
        server_cfg.pop(le-j-1)

    #add the new server config
    server_cfg.extend(new_server_cfg)
    print'\n\n######Finally Config File######'
    print cfg_dic

    #persistent config file
    persistent_config(cfg_dic)

    #generate phone config file
    phone_config.main(datas)




def not_empty(s):
    return s and s.strip()

def has_colon(s):
    return ':' in s

def cut_after_colon(s):
    return s[s.index(':')+1:]

def retrieve_config(path=config_path):
    fp = open(path,'r')
    f = fp.read()
    fp.close()
    dict_cfg = json.loads(f)
    return dict_cfg

def persistent_config(cfg_dic):
    f = json.dumps(cfg_dic)
    fp = open(config_path,'w')
    fp.write(f)
    fp.close()

def transform(datas):
    tag=["server","server_port","password","method","remarks"]
    d1 = dict()
    d2 = dict()
    d3 = dict()
    l = [d1,d2,d3]
    index = 0
    for i in range(3):
        for j in range(4):
            l[i][tag[j]]=datas[index]
            index = index + 1
        l[i][tag[j+1]]=''
    print '\n\n######New Server Config Generate######'
    print l
    return l



if __name__ == '__main__':
    perform()
