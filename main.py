from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tiktoken

app = FastAPI()

# リクエストボディのスキーマ
class TextRequest(BaseModel):
    text: str

# トークン数を返すエンドポイント
@app.post("/count_tokens")
async def count_tokens(request: TextRequest):
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
        token_count = len(encoding.encode(request.text))
        return {"text": request.text, "token_count": token_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
