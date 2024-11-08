from pydantic import BaseModel


class NameRequest(BaseModel):
    city: str


@app.post("/validate-pydantic/")
async def validate_field_pydantic(request: NameRequest):
    return {"message": f"O campo 'name' foi validado com sucesso. Valor recebido: {request.name}"}
