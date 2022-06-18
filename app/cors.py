from fastapi.middleware.cors import CORSMiddleware

# This module is not in use anywhere at the moment,
# and is only a placeholder for a future dynamic cors implementation

origins = [
    "https://domain.com",
]


def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["POST"],
        allow_headers=["*"],
    )
    