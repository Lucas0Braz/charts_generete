
from flask_restful import Resource,reqparse

from models.chart_line import Chart_LineModel


     
class Chart_LineResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('x',
                            #type=list,
                            action='append',
                            required=True,
                            help="This field X cannot be left blank, and must be a list of integers"
            )
    parser.add_argument('y',
                            #type=list,
                            action='append',
                            required=True,
                            help="This field Y cannot be left blank, and must be a list of integers"
            )
        
    
    
    def post(self):
        data = self.parser.parse_args()
        import sys
        print(type(data), file=sys.stderr)
        chart = Chart_LineModel(**data)
        path_chart = chart.gerar_chart()
        if path_chart is not None:
            return {"path_chart":f"{path_chart}"},200
        
        
        
        return {"message":"Something went bad"}, 404  