from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
#Html Page Parser
class MyHtmlParser(HTMLParser):

    def __init__(self, datas = []):
        HTMLParser.__init__(self)
        self.datas = datas

    def handle_starttag(self,tag,attrs):
        #print ('<%s>' % tag)
        pass

    def handle_endtag(self,tag):
        #print ('<%s>' % tag)
        pass

    def handle_startendtag(self,tag,attrs):
        #print ('<%s>' % tag)
        pass

    def handle_data(self,data):
        #start = data.index(':')
        #real = data[start:]
        self.datas.append(data)
    def handle_comment(self,data):
        #print('<!-->')
        pass

    def handle_entltyref(self,name):
        #print('&%s;' % name)
        pass
    def handle_charref(self,name):
        #print('&#%s;' % name)
        pass
    def get_datas(self):
        return self.datas
