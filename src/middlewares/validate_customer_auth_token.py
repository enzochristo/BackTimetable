import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_customer_auth_token(request: Request, response: Response):
    token = request.cookies.get("customer_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("APPRAISER_JWT_SECRET"), algorithms=["HS256"])
        customer_id = payload.get("id")
        customer_email = payload.get("email")
        request.state.auth_payload = {"costumer_id": customer_id, "customer_email": customer_email}

    except jwt.PyJWTError:
        response.delete_cookie("customer_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True