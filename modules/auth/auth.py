# /modules/auth/auth.py
# Antglo 4/20/2024

from flask import request

VALID_TOKENS= ['YOUR_TOKEN_HERE']

# Define a dict to store API tokens
def require_api_token(func):
    def wrapper(*args, **kwargs):
        # get the api token form the header
        token = request.headers.get('X-API-Token')

        # Verify the token
        if token not in VALID_TOKENS:
            return {'error' : 'Unauthorized Access'}, 401
        else:
            # call decorator if token is verified
            return func(*args, **kwargs)
        
    return wrapper
