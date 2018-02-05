def wsgi_application(environ, start_response):
    qs = environ['QUERY_STRING']
    response_body = qs.replace('&','\n')

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]
