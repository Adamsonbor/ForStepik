class GenericView:
    def __init__(self, methods):
        self.methods = methods


    def __is_valid_request(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')


    def get(self, request):
        self.__is_valid_request(request)
        return f"url: {request['url']}"

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass



class DetailView(GenericView):

    def __init__(self, methods=('GET',)):
        super().__init__(methods)


    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return self.__getattribute__(method.lower())(request)






a = DetailView()
print(a.render_request({'url': 'helllo', 'data': 'helllo world'}, "GET"))
