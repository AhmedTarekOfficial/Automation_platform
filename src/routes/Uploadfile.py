from opentelemetry.trace import StatusCode
from fastapi import HTTPException
from fastapi import FastAPI, UploadFile 
from pypdf import PdfReader 


app = FastAPI()

Allowed_types = ["application/pdf" , "text/plain"]



@app.post("/upload")
async def upload(file: UploadFile):
    
    if file.content_type not in Allowed_types:
        raise HTTPException(
                status_code=400,
                detail=f"{file.filename} is not allowed. Only JPEG and PNG."
            )
    else : 
        pdfre = PdfReader(file.file)
        text = ""
        for p in pdfre.pages : 
            text+=p.extract_text()

    return text




