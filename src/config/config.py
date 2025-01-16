import os
import dotenv

dotenv.load_dotenv()

# a "URL DO FRONT" é o localhost fornecido pelo front-end. ( Ex: http://localhost:5173 )
config = {
    "client_url": "URL DO FRONT-END" if os.getenv("ENVIRONMENT") == "dev" else ""
}