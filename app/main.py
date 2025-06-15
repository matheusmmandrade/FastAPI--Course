from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any
app = FastAPI()


shipments = {
    10291: {
        "weight": 1,
        "content": "wooden table",
        "status": "in transit"
    },
    1441: {
        "weight": 10.5,
        "content": "iron table",
        "status": "in transit"
    },
    1: {
        "weight": 13,
        "content": "diamond table",
        "status": "in transit"
    },
    1191: {
        "weight": 20.6,
        "content": "gold table",
        "status": "in transit"
    },
    10231: {
        "weight": 9,
        "content": "ruby table",
        "status": "in transit"
    },
    101: {
        "weight": 2,
        "content": "copper table",
        "status": "in transit"
    }
}


@app.get("/shipment/latest")
def get_latest_shipment():
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:

    if id not in shipments:
        return {"detail": "Given id doesnt exist"}
    return shipments[id]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
