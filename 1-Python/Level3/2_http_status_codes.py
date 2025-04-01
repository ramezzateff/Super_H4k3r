#!/usr/bin/python3
# Create a dictionary storing common HTTP status codes and
# 	their meanings (e.g., `{200: 'OK', 404: 'Not Found'}`).
HTTP_status_codes = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    301: 'Moved Permanently',
    302: 'Found (Temporary Redirect)',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable'
}
print(HTTP_status_codes)
