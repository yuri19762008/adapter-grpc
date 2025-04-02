# this rpc program requests a patient's information through a patient adapter
import grpc
import patient_adapter_unary_pb2_grpc as pb2_grpc
import patient_adapter_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson


def patient_info():
    with (grpc.insecure_channel("localhost:50050") as channel):
        adapter_stub = pb2_grpc.PatientAdapterServiceStub(channel)

        message = pb2.PatientID(
            id="101012-1"
        )

        print(f"Message sent:\n{MessageToJson(message)}\n")

        response = adapter_stub.get_patient(message)

        # this is the adapted data
        print(response)


if __name__ == '__main__':
    patient_info()
