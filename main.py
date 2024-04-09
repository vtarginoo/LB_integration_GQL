from uvicorn import run
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL as ASGIGraphQL
from schemas.schema import QueryProducao
import strawberry

from starlette.responses import Response

# Cria o aplicativo Starlette
app = Starlette()

# Lista de origens permitidas
origins = ["http://localhost:5173", "https://main--zesty-gaufre-81c1f3.netlify.app/"]

# Aplica o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


# Define o aplicativo GraphQL
@app.route("/graphql", methods=["OPTIONS","POST","GET"])
async def graphql_options(request):
    return Response(headers={
        # "Access-Control-Allow-Origin": "http://localhost:5173",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST",
        "Access-Control-Allow-Headers": "Content-Type",
    })

# Define o aplicativo GraphQL com o middleware CORS aplicado
app.mount("/graphql", ASGIGraphQL(schema=strawberry.Schema(query=QueryProducao)))

# Executa o servidor Uvicorn
if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8001)