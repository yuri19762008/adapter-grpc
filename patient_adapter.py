import requests
import grpc
import patient_adapter_unary_pb2_grpc as pb2_grpc
import patient_adapter_unary_pb2 as pb2
from concurrent import futures


class LocalPatient:
    def __init__(self, id, name, birth_date, address, health_care_system):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.health_care_system = health_care_system


class PatientAdapter(LocalPatient):
    def __init__(self, id, name, birth_date, address, health_care_system):
        super().__init__(id, name, birth_date, address, health_care_system)


class RemotePatient:
    def __init__(self, patient_data):
        self.patient_data = patient_data


class PatientAdapterServicer(pb2_grpc.PatientAdapterServiceServicer):
    def get_patient(self, request, context):
        request_result = requests.get("http://127.0.0.1:8000/patient/" + request.id)

        remote_patient = RemotePatient(request_result.json()["patient"])

        patient_adapter = PatientAdapter(
            remote_patient.patient_data.split(";")[0],
            remote_patient.patient_data.split(";")[1],
            remote_patient.patient_data.split(";")[2],
            remote_patient.patient_data.split(";")[3],
            remote_patient.patient_data.split(";")[4]
        )

        response_map = {
            "id": patient_adapter.id,
            "name": patient_adapter.name,
            "birth_date": patient_adapter.birth_date,
            "address": patient_adapter.address,
            "health_care_system": patient_adapter.health_care_system
        }

        return pb2.AdaptedPatient(**response_map)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_PatientAdapterServiceServicer_to_server(PatientAdapterServicer(), server)
    server.add_insecure_port("[::]:50050")
    server.start()
    server.wait_for_termination()
