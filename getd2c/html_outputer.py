'''
Created on 2016年12月30日

@author: Zephyr
'''





class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def ouput_html(self):
        fout=open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
    
    
    



