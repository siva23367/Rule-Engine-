import os
from dotenv import load_dotenv






load_dotenv()

############################################################################
# intialising the database connection
############################################################################

TORTOISE_ORM={
    "connections": {
        "default":{
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("POSTGRES_HOST","localhost"),
                "port": os.getenv("POSTGRES_PORT",5432),
                "user": os.getenv("POSTGRES_USER","rule_engine_USER"),
                "password": os.getenv("POSTGRES_PASSWORD","rule_engine"),
                "database": os.getenv("POSTGRES_DB","rule_engine_DB"),
            }
        }
},
    "apps": {
        "models": {
            "models": ["aerich.models", "Ast.models"],  # Replace 'your_app.models' with your actual models path
            "default_connection": "default",
        }
    }
}