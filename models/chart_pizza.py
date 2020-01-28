from flask_restful import Resource,reqparse
import plotly.graph_objects as go
import os,inspect


class Chart_PizzaModel():
    
    def __init__(self,values,names):
      self.values = values
      self.names = names
    
    
    def gerar_chart(self):
        fig = go.Figure(data=go.Pie(values=self.values,labels=self.names))
        # import sys
        # print(type(self.y), file=sys.stderr)
        name_html = 'pizza_figure.html'   
        fig.write_html(name_html, auto_open=False)
        path_html = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        path_html = path_html.replace('models','')
        return f"{path_html}{name_html}" 
        
        


   

