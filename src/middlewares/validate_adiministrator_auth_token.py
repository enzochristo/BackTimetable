import os
import jwt
from fastapi import Request, Response, HTTPException

def validate_administrator_auth_token(request: Request, response: Response):
    token = request.cookies.get("administrator_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")
    
    try:
        # Decodifica o token JWT
        payload = jwt.decode(
            token.split(" ")[1],
            os.getenv("ADMINISTRATOR_JWT_SECRET"),
            algorithms=["HS256"]
        )
        # Extrai informações úteis do token
        admin_id = payload.get("id")
        admin_email = payload.get("email")
        admin_role = payload.get("role")  # Ex.: "Manager" ou "Staff"
        
        # Armazena as informações na requisição para uso posterior
        request.state.auth_payload = {
            "admin_id": admin_id,
            "admin_email": admin_email,
            "admin_role": admin_role
        }

    except jwt.ExpiredSignatureError:
        # Se o token expirou, remove o cookie
        response.delete_cookie("administrator_auth_token")
        raise HTTPException(status_code=401, detail="Token expirado")
    
    except jwt.PyJWTError:
        # Se o token é inválido, remove o cookie
        response.delete_cookie("administrator_auth_token")
        raise HTTPException(status_code=401, detail="Token JWT inválido")
    
    return True
