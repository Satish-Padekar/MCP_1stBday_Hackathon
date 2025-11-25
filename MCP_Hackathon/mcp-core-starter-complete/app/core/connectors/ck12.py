# CK12 connector (placeholder)
import httpx

BASE = 'https://www.ck12.org'

async def fetch_topics(subject: str = None, grade: str = None):
    # For MVP - this would call CK12 APIs or scrape open endpoints
    return [{"id":"ck12-1","title":"Sample CK12 Topic"}]
