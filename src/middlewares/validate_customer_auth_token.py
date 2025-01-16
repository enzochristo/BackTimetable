import os
import jwt
from fastapi import Request, Response, HTTPException

def validate_customer_auth_token(request: Request, response: Response):
    token = request.cookies.get("customer_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")
    
    try:
        # Decodifica o token JWT
        payload = jwt.decode(
            token.split(" ")[1],
            os.getenv("CUSTOMER_JWT_SECRET"),
            algorithms=["HS256"]
        )
        # Extrai informações úteis do token
        customer_id = payload.get("id")
        customer_email = payload.get("email")
        
        # Armazena as informações na requisição para uso posterior
        request.state.auth_payload = {
            "customer_id": customer_id,
            "customer_email": customer_email
        }

    except jwt.PyJWTError:
        # Se o token for inválido, remove o cookie e retorna um erro
        response.delete_cookie("customer_auth_token")
        raise HTTPException(status_code=401, detail="Token JWT inválido")
    
    return True
