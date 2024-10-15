from typing import Dict
from pydantic import BaseModel
from datetime import datetime

# Ответ для получения информации о заметке
class NoteInfoResponse(BaseModel):
    created_at: datetime
    updated_at: datetime

# Ответ для получения текста заметки
class NoteTextResponse(BaseModel):
    id: int
    text: str

# Ответ для создания новой заметки
class CreateNoteResponse(BaseModel):
    id: int

# Ответ для полного списка заметок с их текстом и датами
class FullNoteResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime
