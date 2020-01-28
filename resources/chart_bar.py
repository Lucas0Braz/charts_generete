
from flask_restful import Resource,reqparse

from models.chart_bar import Chart_BarModel


     
class Chart_BarResource(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('x',
    #                         type=str,
    #                         required=False,
    #                         help="This field x cannot be left blank"
    #         )
    parser.add_argument('y',
                            #type=list,
                            action='append',
                            required=True,
                            help="This field Y cannot be left blank"
            )
        
    
    
    def post(self):
        data = self.parser.parse_args()
        import sys
        print(type(data), file=sys.stderr)
        chart = Chart_BarModel(**data)
        path_chart = chart.gerar_chart()
        if path_chart is not None:
            return {"path_chart":f"{path_chart}"},200
        
        
        
        return {"message":"Something went bad"}, 404  