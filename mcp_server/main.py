# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T08:48:58+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query
from pydantic import conint

from models import (
    LatexCompiler,
    TemplatesTemplateTokenCompilePostRequest,
    TemplatesTemplateTokenCompilePostResponse,
)

app = MCPProxy(
    contact={
        'email': 'info@advicement.io',
        'name': 'Igor Rodionov',
        'url': 'https://advicement.io/dynamic-documents-api',
        'x-twitter': 'Rapid_API',
    },
    description="ADVICEment's [DynamicDocs API automates your document generation](https://advicement.io/dynamic-documents-api) and creates dynamic, optimized, interactive PDFs. Write your templates in LaTeX and call the API with JSON data to get your PDFs in seconds.\n\nThe template files are stored in your dashboard and can be edited, tested and published online. Document templates can contain dynamic text using logic statements, include tables stretching multiple pages and show great-looking charts based on the underlying data. LaTeX creates crisp, high-quality documents where every detail is well-positioned and styled.\n\nIntegrate with ADVICEment DynamicDocs API in minutes and start creating beautiful [dynamic PDF documents](https://advicement.io/dynamic-documents-api) for your needs.\n\nFor more information, visit [DynamicDocs API Home page](https://advicement.io/dynamic-documents-api).",
    termsOfService='https://advicement.io/terms-of-service',
    title='DynamicDocs',
    version='1.0',
    servers=[
        {'description': 'via RapidAPI.com', 'url': 'https://dynamicdocs.p.rapidapi.com'}
    ],
)


@app.post(
    '/templates/{template-token}/compile',
    description=""" Compile a PDF document from a specific template """,
    tags=['document_generation'],
    security=[
        APIKeyHeader(name="ADVICEment API Key"),
        APIKeyHeader(name="RapidAPI.com API Key"),
    ],
)
def compile(
    content__type: str = Header(..., alias='Content-Type'),
    doc_url_expires_in: Optional[int] = Query(None, alias='doc-url-expires-in'),
    latex_compiler: Optional[LatexCompiler] = Query(None, alias='latex-compiler'),
    latex_runs_: Optional[conint(ge=1, le=3)] = Query(None, alias='latex-runs '),
    main_file_name: Optional[str] = Query(None, alias='main-file-name'),
    doc_file_name: Optional[str] = Query(None, alias='doc-file-name'),
    template_token: str = Path(..., alias='template-token'),
    body: TemplatesTemplateTokenCompilePostRequest = None,
):
    """
    Compile New Document PDF
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
