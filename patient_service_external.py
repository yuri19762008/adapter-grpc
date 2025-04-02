from fastapi import FastAPI

app = FastAPI()


# just an example list
patients = [
    "101010-1;Romualdo Jimenez;10/10/1940;Los pericos 1920, Pargua;Fonasa",
    "101012-1;Etelvina Gutierrez;10/10/1920;Las bandurrias S/N, Coyhaique;Isapre"
]


@app.get("/patient/{patient_id}")
def patient(patient_id):
    for patient in patients:
        print(patient)
        print(patient.split(";")[0])
        if patient_id == patient.split(";")[0]:
            return {"patient": patient}

    return {"patient": "none"}
