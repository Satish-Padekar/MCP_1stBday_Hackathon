from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get('/api/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_practice_and_check_flow():
    r = client.post('/api/practice', json={"count":2})
    assert r.status_code == 200
    data = r.json()
    assert 'problems' in data
    problems = data['problems']
    attempts = []
    for p in problems:
        attempts.append({"problem_id": p['id'], "answer": p['solution'], "_solution": p['solution']})
    r2 = client.post('/api/check', json=attempts)
    assert r2.status_code == 200
    res = r2.json()
    assert 'results' in res
    assert all([x['score'] == 1.0 for x in res['results']])
