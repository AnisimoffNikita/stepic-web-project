def wsgi_application(environ, start_response):
    qs = environ['QUERY_STRING']
    response_body = [i + '\n' for i in qs.split('&')]
    print response_body
     
    l = 0
    for x in response_body:
        l += len(x)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(l))
    ]
    start_response(status, response_headers)
    return response_body