from allergies.services import AllergiesService
from recipes.services import RecipesService
from careplans.services import CareplansService
from claims.services import ClaimsService
from claims_transactions.services import ClaimsTransactionsService
from encounters.services import EncountersService
from immunizations.services import ImmunizationsService
from patients.services import PatientsService
from medications.services import MedicationsService
from procedures.services import ProceduresService
from observations.services import ObservationsService
from organizations.services import OrganizationsService
from suppliers.services import SuppliersService
from devices.services import DevicesService
from payer_transitions.services import PayerTransitionsService
from providers.services import ProvidersService
from payers.services import PayersService
from conditions.services import ConditionsService
from imaging_studies.services import ImagingStudiesService


class ServicesFacade:
    def __init__(self):
        self.allergies_service = AllergiesService()
        self.recipes_service = RecipesService()
        self.careplans_service = CareplansService()
        self.claims_service = ClaimsService()
        self.claims_transactions_service = ClaimsTransactionsService()
        self.encounters_service = EncountersService()
        self.immunizations_service = ImmunizationsService()
        self.patients_service = PatientsService()
        self.medications_service = MedicationsService()
        self.procedures_service = ProceduresService()
        self.observations_service = ObservationsService()
        self.organizations_service = OrganizationsService()
        self.suppliers_service = SuppliersService()
        self.devices_service = DevicesService()
        self.payer_transitions_service = PayerTransitionsService()
        self.providers_service = ProvidersService()
        self.payers_service = PayersService()
        self.conditions_service = ConditionsService()
        self.imaging_studies_service = ImagingStudiesService()

    def get_all_services(self):
        return {
            "allergies": self.allergies_service,
            "recipes": self.recipes_service,
            "careplans": self.careplans_service,
            "claims": self.claims_service,
            "claims_transactions": self.claims_transactions_service,
            "encounters": self.encounters_service,
            "immunizations": self.immunizations_service,
            "patients": self.patients_service,
            "medications": self.medications_service,
            "procedures": self.procedures_service,
            "observations": self.observations_service,
            "organizations": self.organizations_service,
            "suppliers": self.suppliers_service,
            "devices": self.devices_service,
            "payer_transitions": self.payer_transitions_service,
            "providers": self.providers_service,
            "payers": self.payers_service,
            "conditions": self.conditions_service,
            "imaging_studies": self.imaging_studies_service,
        }
