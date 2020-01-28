from flask_restful import Resource,reqparse
import plotly.graph_objects as go
import os,inspect


class Chart_LineModel():
    
    def __init__(self,y,x):
      self.x = x
      self.y = y
    
    
    def gerar_chart(self):
        fig = go.Figure(data=go.Line(y=self.y,x=self.x))
        # import sys
        # print(type(self.y), file=sys.stderr)
        #fig.add_tra
        name_html = 'line_figure.html'   
        fig.write_html(name_html, auto_open=False)
        path_html = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        path_html = path_html.replace('models','')
        return f"{path_html}{name_html}" 
        
        


   

