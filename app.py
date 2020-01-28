from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.chart_bar import Chart_BarResource
from resources.chart_line import Chart_LineResource
from resources.chart_pizza import Chart_PizzaResource

#resource == stuffs that your api can return

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'luke'
api = Api(app)


api.add_resource(Chart_BarResource, '/chart_bar')
api.add_resource(Chart_LineResource,'/chart_line')
api.add_resource(Chart_PizzaResource,'/chart_pizza')


app.run(port=5000, debug=True)
    