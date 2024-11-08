from core.services.connection.connection_service import ConnectionService


class PatientsService:

    def list_patients(self, city):
        if city:
            return [{"id": 1, "name": "João", "city": city}]
        return [{"id": 1, "name": "João"}, {"id": 2, "name": "Maria"}]
