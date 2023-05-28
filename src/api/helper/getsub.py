'''Async functions for interacting with the Codefun API (consider it the API)'''
import aiohttp
import logging
from ..models.submission import Submission

async def get_submissions(user: str = "", problem: str = "") -> list[Submission]:
    '''Get all submissions matching a particular set of criteria'''
    request_url = "https://codefun.vn"
    params = {
        "owner": user,
        "problem": problem,
        "limit": 50
    }
    result = []
    async with aiohttp.ClientSession(base_url=request_url) as session:
        page_idx = 1
        while True:
            async with session.get("/api/submissions", params=params | {"page": page_idx}) as response:
                logging.debug("Performing request on: %s", response.url)
                rdict = await response.json(encoding="utf-8")
            rdict = rdict["data"]
            if rdict is None: break
            for sub in rdict:
                result.append(Submission(sub))
            page_idx += 1
    return result
