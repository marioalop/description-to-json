import json
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from langchain.schema import OutputParserException
from pydantic import BaseModel

import settings
from rulegenerator import RuleGenerator

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY


class Descriptor(BaseModel):
    """
    Rule description schema.
    """

    description: str


rule_generator = RuleGenerator()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    """
    Return the index page.

    Returns
    -------
    HTMLResponse
        The index page.
    """
    with open(settings.INDEX_HTML_PATH, "r") as f:
        content = f.read()
    return HTMLResponse(content=content)


@app.post("/newrule")
async def create_rule(descriptor: Descriptor) -> dict:
    """
    Receive a description and return a rule.

    Parameters
    ----------
    descriptor : Descriptor
        The description of the rule.

    Returns
    -------
    dict
        The generated rule.
    """
    text_generated = rule_generator.generate(descriptor.description)
    if isinstance(text_generated, dict):
        text_generated = text_generated["result"]

    try:
        json_data = json.loads(text_generated)
    except OutputParserException as e:
        json_data = {"error": str(e)}

    except json.decoder.JSONDecodeError:
        try:
            json_data = json.loads(
                text_generated[
                    text_generated.find("{") : text_generated.rfind("}") + 1
                ]
            )
        except json.decoder.JSONDecodeError:
            json_data = {"error": text_generated}

    return json_data
