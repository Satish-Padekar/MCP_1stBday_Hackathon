from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="MCP Core API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class PracticeRequest(BaseModel):
    topic_id: Optional[str] = None
    difficulty: Optional[str] = "easy"
    count: Optional[int] = 5

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/curriculum")
def get_curriculum(grade: Optional[str] = None, subject: Optional[str] = None):
    # Placeholder: return sample topics
    topics = [
        {"id": "math-1", "title": "Addition & Subtraction", "standards": ["K-2"], "source": "sample"},
        {"id": "math-2", "title": "Multiplication Basics", "standards": ["3-4"], "source": "sample"},
    ]
    return {"topics": topics}

@app.post("/api/practice")
def generate_practice(req: PracticeRequest):
    problems = []
    base = 1 if req.difficulty == 'easy' else 5 if req.difficulty == 'medium' else 10
    for i in range(req.count):
        a = base + i
        b = base + i + 1
        problems.append({
            "id": f"p-{a}-{b}",
            "statement": f"What is {a} + {b}?",
            "type": "numeric",
            "choices": None,
            "solution": str(a+b),
            "metadata": {"topic": req.topic_id or "math-1"}
        })
    return {"problems": problems}

@app.post("/api/check")
async def check_homework(attempts: List[dict]):
    results = []
    for a in attempts:
        pid = a.get("problem_id")
        ans = str(a.get("answer", "")).strip()
        # In a real implementation we'd lookup solution; here, heuristic check
        # If client submits 'solution' in payload for placeholder testing
        provided_solution = a.get("_solution")
        if provided_solution is not None:
            score = 1.0 if ans == str(provided_solution) else 0.0
            feedback = "Correct" if score==1.0 else "Try again"
        else:
            score = 0.0
            feedback = "Auto-check not available for this problem"
        results.append({"problem_id": pid, "score": score, "max_score": 1, "feedback": feedback})
    return {"results": results}

@app.post("/api/upload-worksheet")
async def upload_worksheet(file: UploadFile = File(...)):
    content = await file.read()
    size = len(content)
    # Save to disk (dev) - in production use storage service
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        f.write(content)
    return {"filename": file.filename, "size": size, "path": path}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
