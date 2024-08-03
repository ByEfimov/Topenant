class corsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Allow-Origin"] = "*"
        response["origins"] = "http://127.0.0.1:3000"

        return response
