from fastapi import FastAPI
from pylatexenc.latex2text import LatexNodes2Text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(latex: str):
    latex = latex.replace('{','{(')
    latex = latex.replace('}',')}')
    result = LatexNodes2Text().latex_to_text(latex)
    result = result.replace(';','},{')
    result = result.replace('[','{ {')
    result = result.replace(']','} }')
    return {"text":  result}