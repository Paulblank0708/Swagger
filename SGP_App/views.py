@swagger_auto_schema (
    
    methods =  ["POST"],
    request_body = LivroSerializer,
    tags = ["Livroo"],

)
from django.shortcuts import render

paginator = PageNumberPagination()
#http://127.0.0.1:8000/api/livro/?pageSize=10
paginator.page_size = request.query_params.get("pageSize",1)
livros = models.Livro.objects.all()
paginated_livros = paginator.paginate_queryset(livros, request)
serializer = LivroSerializer(paginated_livros, many=True)
return paginator.get_paginated_response(serializer.data)


# Create your 
