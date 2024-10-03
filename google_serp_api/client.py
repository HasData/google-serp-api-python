from requests import request, Response
from typing import TypedDict, Optional

import urllib.parse

from .default_headers import default_headers


class GetSearchResultsParams(TypedDict, total=False):
    q: str
    location: Optional[str]
    uule: Optional[str]
    domain: Optional[str]
    gl: Optional[str]
    hl: Optional[str]
    lr: Optional[list]
    ludocid: Optional[str]
    lsig: Optional[str]
    kgmid: Optional[str]
    si: Optional[str]
    tbs: Optional[str]
    safe: Optional[str]
    filter: Optional[int]
    tbm: Optional[str]
    deviceType: Optional[str]
    start: Optional[int]
    num: Optional[int]


class GoogleSerpApi:

    api_url = "https://api.hasdata.com/scrape/google/serp"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def getSearchResults(
        self,
        params: GetSearchResultsParams,
        **kwargs
    ) -> Response:
        headers = {
            "x-api-key": self.api_key
        }
        headers.update(default_headers)
        params["source"] = "python_sdk"
        url_params = urllib.parse.urlencode(params)

        url = self.api_url + "/" + "?" + url_params
        return request("GET", url, headers=headers, **kwargs)
