from ..patients.service.patients import PatientsService


class ServicesFacade:
    def __init__(self):
        self.patients_service = PatientsService()

    def list_patients_facade(self, city):
        return self.patients_service.list_patients(city)
