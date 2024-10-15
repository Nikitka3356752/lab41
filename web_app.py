import datetime
import fastapi
from typing import List, Dict
from model import NoteInfoResponse, NoteTextResponse, CreateNoteResponse

api_router = fastapi.APIRouter()

# Временное хранилище заметок
notes = {
}
# Получение информации о заметке
@api_router.get("/note_info/{note_id}", response_model=NoteInfoResponse)
def get_note_info(note_id: int):
    """
    Получение информации о заметке: created_at и updated_at.
    """
    note = notes.get(note_id)
    if not note:
        return fastapi.HTTPException(status_code=404, detail="Note not found")

    return NoteInfoResponse(
        created_at=note['created_at'],
        updated_at=note['updated_at']
    )


# Получение текста заметки
@api_router.get("/note_text/{note_id}", response_model=NoteTextResponse)
def get_note_text(note_id: int):
    """
    Получение текста заметки по ее id.
    """
    note = notes.get(note_id)
    if not note:
        return fastapi.HTTPException(status_code=404, detail="Note not found")

    return NoteTextResponse(
        id=note_id,
        text=note['text']
    )


@api_router.post("/create_note", response_model=CreateNoteResponse)
def create_note(text: str):
    """
    Создание новой заметки. ID начинается с 1 и увеличивается на 1 с каждой новой заметкой.
    """
    new_id = max(notes.keys()) + 1 if notes else 1  # Если заметок нет, то начинаем с 1

    now = datetime.datetime.now()

    notes[new_id] = {
        "text": text,
        "created_at": now,
        "updated_at": now
    }
    return CreateNoteResponse(
        id=new_id
    )


# Получение списка всех заметок
@api_router.get("/notes", response_model=Dict[int, int])
def get_notes():
    """
    Получение списка всех заметок с их id.
    """
    return {i: note_id for i, note_id in enumerate(notes.keys())}
