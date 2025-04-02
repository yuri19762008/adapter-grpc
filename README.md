# adapter-grpc

Adapter for Talento Futuro. The adapter (patient_adapter.py) is a gRPC service that is called by a gRPC client
(patient_client.py). The adapter interfaces with the external patient service (patient_service_external). 
This external service is a FastAPI-based one.

Remember to recompile protos with `$ python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./*.proto`