from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# SOAL 1.0
class Biodata(BaseModel):
    nama: str
    tahunMasuk: int

biodataMahasiswa = []
biodataId = 0

@app.post("/soal1.0")
async def postMahasiswa(permintaan: Biodata):
    global biodataId

    biodataId += 1
    biodataMahasiswa.append({"id": biodataId, "data": permintaan})
    print(biodataMahasiswa)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {biodataId} berhasil dikirim!"
    }

@app.get("/soal1.0")
def getMahasiswa(id: int):
    for biodata in biodataMahasiswa:
        if biodata["id"] == id:
            return {
                "code": 200,
                "message": "success",
                "hasil": f"{biodata["data"].nama} Seorang Mahasiswa Angkatan {biodata["data"].tahunMasuk}"
            }
        
    return None


#SOAL 2.0 (IF STATEMENT)
class Kalkulator(BaseModel):
    a: float
    b: float
    opt: str

kalkulatorData = []
kalkulatorId = 0

@app.post("/soal2.0")
def postKalkulator(permintaan: Kalkulator):

    global kalkulatorId

    kalkulatorId += 1
    kalkulatorData.append({"id": kalkulatorId, "data": permintaan})
    print(kalkulatorData)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {kalkulatorId} telah dikirim!"
        }

@app.get("/soal2.0")
def getKalkulator(id: int):
    for kalkulator in kalkulatorData:
        if kalkulator["id"] == id:
            
            opt = kalkulator["data"].opt
            a = kalkulator["data"].a
            b = kalkulator["data"].b

            if opt == '+':
                c = a + b
            elif opt == '-':
                c = a - b
            elif opt == '*':
                c = a * b
            elif opt == '/':
                c = a / b
            else:
                raise HTTPException(status_code=400, detail="Operasi tidak valid.")

            return {
                "code": 200,
                "message": "success",
                "a": a,
                "b": b,
                "operator": opt,
                "hasil": f"{a} {opt} {b} sama dengan {c}"
            }
        
    return None


#SOAL 2.1 (SWITCH CASE)
class Kalkulator(BaseModel):
    a: float
    b: float
    opt: str

kalkulatorData = []
kalkulatorId = 0

@app.post("/soal2.1")
def postKalkulator(permintaan: Kalkulator):

    global kalkulatorId

    kalkulatorId += 1
    kalkulatorData.append({"id": kalkulatorId, "data": permintaan})
    print(kalkulatorData)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {kalkulatorId} telah dikirim!"
        }

@app.get("/soal2.1")
def getKalkulator(id: int):
    for kalkulator in kalkulatorData:
        if kalkulator["id"] == id:
            
            opt = kalkulator["data"].opt
            a = kalkulator["data"].a
            b = kalkulator["data"].b

            match opt:
                case '+':
                    c = a + b
                case '-':
                    c = a - b
                case '*':
                    c = a * b
                case '/':
                    c = a / b
                case '_':
                    raise HTTPException(status_code=400, detail="Operasi tidak valid.")

            return {
                "code": 200,
                "message": "success",
                "a": a,
                "b": b,
                "operator": opt,
                "hasil": f"{a} {opt} {b} sama dengan {c}"
            }
        
    return None


#SOAL 2.2 (TERNARY)
class Kalkulator(BaseModel):
    a: float
    b: float
    opt: str

kalkulatorData = []
kalkulatorId = 0

@app.post("/soal2.2")
def postKalkulator(permintaan: Kalkulator):

    global kalkulatorId

    kalkulatorId += 1
    kalkulatorData.append({"id": kalkulatorId, "data": permintaan})
    print(kalkulatorData)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {kalkulatorId} telah dikirim!"
        }

@app.get("/soal2.2")
def getKalkulator(id: int):
    for kalkulator in kalkulatorData:
        if kalkulator["id"] == id:
            
            opt = kalkulator["data"].opt
            a = kalkulator["data"].a
            b = kalkulator["data"].b

            c = (
                a + b if opt == '+' else
                a - b if opt == '-' else
                a * b if opt == '*' else
                a / b if opt == '/' else

                None
            )

            if c is None:
                raise HTTPException(status_code=400, detail="Operasi tidak valid.")

            return {
                "code": 200,
                "message": "success",
                "a": a,
                "b": b,
                "operator": opt,
                "hasil": f"{a} {opt} {b} sama dengan {c}"
            }
        
    return None


#SOAL 3.0 (FOR LOOP)
class hitungUmur(BaseModel):
    tahunLahir: int
    bulanLahir: int

dataHitungUmur = []
hitungUmurId = 0

@app.post("/soal3.0")
def postHitungUmur(permintaan: hitungUmur):
    global hitungUmurId

    hitungUmurId += 1
    dataHitungUmur.append({"id": hitungUmurId, "data": permintaan})
    print(dataHitungUmur)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {hitungUmurId} telah dikirim!"
    }

@app.get("/soal3.0")
def getHitungUmur(id: int):
    for dataUsia in dataHitungUmur:
        if dataUsia["id"] == id:

            tahunLahir = dataUsia["data"].tahunLahir
            bulanLahir = dataUsia["data"].bulanLahir

            sekarang = datetime.now()
            tahunSekarang = sekarang.year
            bulanSekarang = sekarang.month

            umurTahun = 0
            umurBulan = 0

            for tahun in range(tahunLahir, tahunSekarang):
                umurTahun += 1

            if bulanSekarang < bulanLahir:
                umurTahun -= 1
                umurBulan = (12 - bulanLahir) + bulanSekarang

            else:
                umurBulan = bulanSekarang - bulanLahir

            return {
                "code": 200,
                "message": "success",
                "data": f"Umur anda {umurTahun} tahun {umurBulan} bulan"
            }
        
    return None


#SOAL 3.1 (WHILE LOOP)
class hitungUmur(BaseModel):
    tahunLahir: int
    bulanLahir: int

dataHitungUmur = []
hitungUmurId = 0

@app.post("/soal3.1")
def postHitungUmur(permintaan: hitungUmur):
    global hitungUmurId

    hitungUmurId += 1
    dataHitungUmur.append({"id": hitungUmurId, "data": permintaan})
    print(dataHitungUmur)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {hitungUmurId} telah dikirim!"
    }

@app.get("/soal3.1")
def getHitungUmur(id: int):
    for dataUsia in dataHitungUmur:
        if dataUsia["id"] == id:

            tahunLahir = dataUsia["data"].tahunLahir
            bulanLahir = dataUsia["data"].bulanLahir

            sekarang = datetime.now()
            tahunSekarang = sekarang.year
            bulanSekarang = sekarang.month

            umurTahun = 0
            umurBulan = 0

            while tahunLahir < tahunSekarang:
                umurTahun += 1
                tahunLahir += 1

            if bulanSekarang < bulanLahir:
                umurTahun -= 1
                umurBulan = (12 - bulanLahir) + bulanSekarang

            else:
                umurBulan = bulanSekarang - bulanLahir

            return {
                "code": 200,
                "message": "success",
                "data": f"Umur anda {umurTahun} tahun {umurBulan} bulan"
            }
        
    return None


#SOAL 3.2 (FOREACH)
class hitungUmur(BaseModel):
    tahunLahir: int
    bulanLahir: int

dataHitungUmur = []
hitungUmurId = 0

@app.post("/soal3.2")
def postHitungUmur(permintaan: hitungUmur):
    global hitungUmurId

    hitungUmurId += 1
    dataHitungUmur.append({"id": hitungUmurId, "data": permintaan})
    print(dataHitungUmur)

    return {
        "code": 200,
        "message": f"Posting dibuat, data dengan id {hitungUmurId} telah dikirim!"
    }

@app.get("/soal3.2")
def getHitungUmur(id: int):
    for dataUsia in dataHitungUmur:
        if dataUsia["id"] == id:

            tahunLahir = dataUsia["data"].tahunLahir
            bulanLahir = dataUsia["data"].bulanLahir

            sekarang = datetime.now()
            tahunSekarang = sekarang.year
            bulanSekarang = sekarang.month

            umurTahun = 0
            umurBulan = 0

            rentangTahun = list(range(tahunLahir, tahunSekarang))

            for tahun in rentangTahun:
                umurTahun += 1

            if bulanSekarang < bulanLahir:
                umurTahun -= 1
                umurBulan = (12 - bulanLahir) + bulanSekarang

            else:
                umurBulan = bulanSekarang - bulanLahir

            return {
                "code": 200,
                "message": "success",
                "data": f"Umur anda {umurTahun} tahun {umurBulan} bulan"
            }
        
    return None