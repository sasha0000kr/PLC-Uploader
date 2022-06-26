from fastapi import FastAPI, File, UploadFile
import multiprocessing  
import subprocess
import zipfile
import shutil
import os

app = FastAPI (
    title="Загрузчик ПЛК",
    description="Приложение для загркузки и зпуска на программируемых логических контроллеров на базе встраимваемых операционных систем. В основе лежит универсальность и кроссплатформенность. ПО выполнено в рамках курсового проекта КП.15.02.10.22.09. Подробнее о проекте на GitHub.",
    version="0.3",

    contact={
        "name": "Краснов Александр Сергеевич",
        "url": "https://github.com/sasha0000kr/PLC-Uploader",
        "email": "sasha0000kr@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://ru.wikipedia.org/wiki/Лицензия_MIT",
    },
)


def runfile (filename):
    print ("Filename: " + str(filename))
    shortfile = filename [::-1]
    shortfile = shortfile [4:]
    shortfile = shortfile [::-1]
    print ("Short name: " + str (shortfile))

    print ("Extracting file")
    zipfile.ZipFile (filename).extractall (shortfile)
    zipfile.ZipFile (filename).close ()

    os.chdir (shortfile)
    print ("Using directoy: " + str (os.getcwd()))
    print ("Starting subprocess: " + "main.sh")
    print ("Obtaining file execution rights")
    os.system ('chmod +x %s.sh'% "main")
    print ("Starting subprocess: " + "main.sh".center (65, "-"))
    print ("")
    process = subprocess.run ("./%s.sh"% "main", capture_output=True)
    out = process.stdout

    #os.system ("./%s.sh"% "main" )
    #subprocess.call("main.sh", shell=True)
    print ("")
    print ("-".center (65, "-"))

    print ("Process STDOUT:" + str (out))
    print ("Stop subprocess: \n" + str (process) + "\nPROCESS STDOUT: "  + str (out))
    
    print ("Clearing cache")
    os.chdir ("../")
    print ("Work direcotory: " + str (os.getcwd ()))
    os.system ("rmdir --ignore-fail-on-non-empty %s" %shortfile)
    return {"ExitCode": out, "STDOUT": out}


@app.post("/load")
async def create_load_file(file: UploadFile = File (...)):
    with open (f"{file.filename}", "wb") as buffer:
        shutil.copyfileobj (file.file, buffer)

@app.post("/load/run")
async def create_upload_file(file: UploadFile = File (...)):
    with open (f"{file.filename}", "wb") as buffer:
        shutil.copyfileobj (file.file, buffer)
    runfile (file.filename)

@app.get("/remove/{zipfile_name}")
async def remove_item(zipfile_name: str):
    out = os.remove (zipfile_name)
    return out


@app.get("/filelist")
async def file_list():
    return os.listdir (os.getcwd ())

@app.get("/run/{zipfile_name}")
async def read_item(zipfile_name: str):
    runfile (zipfile_name)
