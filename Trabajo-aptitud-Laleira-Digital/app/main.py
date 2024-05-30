from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Factura(BaseModel):
    price: float = Field(..., gt=0, description="El precio del producto")
    people: int = Field(..., gt=0, description="El número de personas a pagar")
    tip: float = Field(
        ..., ge=0, description="El porcentaje de propina que se tiene que pagar"
    )


"""
Una clase la cual representa la factura la cual contiene los campos:

Atributos:
--------------------
price : float
    El precio del producto 
people : int
    El número de personas a pagar
tip : float
    El porcentaje de propina que se tiene que pagar

"""


@app.post("/calcular_factura/")
async def calcular_factura(factura_input: Factura) -> float:
    factura_total = factura_input.price + (
        factura_input.price * factura_input.tip / 100
    )
    factura_por_persona = factura_total / factura_input.people
    return {
        "total": float(round(factura_total, 2)),
        "factura_por_persona": float(round(factura_por_persona, 2)),
    }


"""
La función calcular_factura calcula la factura total y la factura por persona, la factura total es calculada sumando el
precio más la propina (la cual se clacularía multiplicando el precio por el porcetaje de propina).

Una vez obtenida la factura total esta se divide por el número de personas para obtener cuanto tendría que pagar cada persona.

Parametros
-----------

factura_total : float
    La factura total que se tendría que pagar teniendo en cuenta la propina

factura_por_persona : float
    La factura que cada persona tendría que pagar con propina incluida

Returns
--------
float

La función devulve los valores de factura_total y factura_por_persona redondeados a 2 decimales.

"""
