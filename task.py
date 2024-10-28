from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

#SOAL 1.0 (BIODATA)
class Biodata(BaseModel):
    nama: str
    tahunMasuk: int

@app.post("/soal1.0")
def mahasiswa(permintaan: Biodata):

    if all(char.isalpha() or char.isspace() for char in permintaan.nama):

        if permintaan.nama != "":
            return {
                "code": 200,
                "message": "success",
                "data": f"{permintaan.nama} Seorang Mahasiswa Angkatan {permintaan.tahunMasuk}"
            }
        
        else:
            raise HTTPException(status_code=400, detail="Nama tidak boleh kosong.")

    else:
        raise HTTPException(status_code=400, detail="Nama tidak boleh menggunakan symbol khusus.")


#SOAL 2.0 (IF STATEMENT)
class KalkulasiPermintaan(BaseModel):
    a: float
    b: float
    operator: str

@app.post("/soal2.0")
def perhitungan(permintaan: KalkulasiPermintaan):
    a = permintaan.a
    b = permintaan.b
    operator = permintaan.operator

    if operator == '+':
        c = a + b
        opt = "tambah"
    elif operator == '-':
        c = a - b
        opt = "kurang"
    elif operator == '*':
        c = a * b
        opt = "kali"
    elif operator == '/':
        c = a / b
        opt = "bagi"
    else:
        raise HTTPException(status_code=400, detail="Operasi tidak valid.")
    
    return {
        "code": 200,
        "message": "success",
        "a": a,
        "b": b,
        "operation": operator,
        "result": f"{a} di{opt} {b} sama dengan {c}"
    }


#SOAL 2.1 (SWITCH CASE)
@app.post("/soal2.1")
def perhitungan(permintaan: KalkulasiPermintaan):
    a = permintaan.a
    b = permintaan.b
    operator = permintaan.operator

    match operator:
        case '+':
            c = a + b
            opt = "tambah"
        case '-':
            c = a - b
            opt = "kurang"
        case '*':
            c = a * b
            opt = "kali"
        case '/':
            c = a / b
            opt = "bagi"
        case _:
            raise HTTPException(status_code=400, detail="Operasi tidak valid")
    
    return {
        "code": 200,
        "message": "success",
        "a": a,
        "b": b,
        "operation": operator,
        "result": f"{a} di{opt} {b} sama dengan {c}"
    }


#SOAL 2.2 (TERNARY)
@app.post("/soal2.2")
def perhitungan(permintaan: KalkulasiPermintaan):
    a = permintaan.a
    b = permintaan.b
    operator = permintaan.operator

    c = (
        a + b if operator == '+' else
        a - b if operator == '-' else
        a * b if operator == '*' else
        a / b if operator == '/' else
        None
    )

    if c is None:
        raise HTTPException(status_code=400, detail="Operasi tidak valid.")

    return {
        "code": 200,
        "message": "success",
        "a": a,
        "b": b,
        "operation": operator,
        "result": f"{a} {operator} {b} sama dengan {c}"
    }


#SOAL 3.0 (FOR LOOP)
class KalkulasiKelahiran(BaseModel):
    tahunLahir: int
    bulanLahir: int

@app.post("/soal3.0")
def hitungUmur(kelahiran: KalkulasiKelahiran):

    tahunLahir = kelahiran.tahunLahir
    bulanLahir = kelahiran.bulanLahir

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
        "tahun lahir": tahunLahir,
        "bulan lahir": bulanLahir,
        "data": f"Umur saya adalah {umurTahun} tahun {umurBulan} bulan"
    }


#SOAL 3.1 (WHILE LOOP)
@app.post("/soal3.1")
def hitungUmur(kelahiran: KalkulasiKelahiran):

    tahunLahir = kelahiran.tahunLahir
    bulanLahir = kelahiran.bulanLahir

    sekarang = datetime.now()
    tahunSekarang = sekarang.year
    bulanSekarang = sekarang.month

    tahunLahirAsli = tahunLahir

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
        "tahun lahir": tahunLahirAsli,
        "bulan lahir": bulanLahir,
        "data": f"Umur saya adalah {umurTahun} tahun {umurBulan} bulan"
    }


#SOAL 3.2 (FOR EACH)
@app.post("/soal3.2")
def hitungUmur(kelahiran: KalkulasiKelahiran):

    tahunLahir = kelahiran.tahunLahir
    bulanLahir = kelahiran.bulanLahir

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
        "tahun lahir": tahunLahir,
        "bulan lahir": bulanLahir,
        "data": f"Umur saya adalah {umurTahun} tahun {umurBulan} bulan"
    }