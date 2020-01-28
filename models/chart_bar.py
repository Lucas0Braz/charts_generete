from flask_restful import Resource,reqparse
import plotly.graph_objects as go
import os,inspect


class Chart_BarModel():
    
    def __init__(self,y):
      #  self.x = x
      self.y = y
    
    
    def gerar_chart(self):
        fig = go.Figure(data=go.Bar(y=self.y))
        # import sys
        # print(type(self.y), file=sys.stderr)
        name_html = 'bar_figure.html'   
        fig.write_html(name_html, auto_open=False)
        path_html = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        path_html = path_html.replace('models','')
        return f"{path_html}{name_html}" 
        
        


   

