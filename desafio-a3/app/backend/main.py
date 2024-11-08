from fastapi import FastAPI, HTTPException
from api.facade.services import ServicesFacade


app = FastAPI()


# Rotas RESTful
@app.get("/get", tags=["patients"])
def list_patients_for_city(city: str = None):
    try:

        services_facade = ServicesFacade()

        patients = services_facade.list_patients_facade(city)

        if not patients:
            return {"message": "Nenhum paciente encontrado para a cidade especificada."}

        return {"patients": patients}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
