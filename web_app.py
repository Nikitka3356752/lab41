import datetime
import fastapi
from typing import List, Dict
from model import NoteInfoResponse, NoteTextResponse, CreateNoteResponse, FullNoteResponse

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


# Создание новой заметки
@api_router.post("/create_note", response_model=CreateNoteResponse)
def create_note(text: str):
    """
    Создание новой заметки. ID начинается с 1.
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


# Получение полного списка заметок с текстом и датами
@api_router.get("/all_notes", response_model=List[FullNoteResponse])
def get_all_notes():
    """
    Получение всех заметок с текстом, id, датой создания и обновления.
    """
    return [
        FullNoteResponse(
            id=note_id,
            text=note_data['text'],
            created_at=note_data['created_at'],
            updated_at=note_data['updated_at']
        )
        for note_id, note_data in notes.items()
    ]


# Удаление заметки
@api_router.delete("/delete_note/{note_id}", response_model=str)
def delete_note(note_id: int):
    """
    Удаление заметки по id.
    """
    if note_id not in notes:
        return fastapi.HTTPException(status_code=404, detail="Note not found")

    del notes[note_id]
    return f"Note {note_id} deleted"


# Обновление текста заметки
@api_router.put("/update_note/{note_id}", response_model=NoteTextResponse)
def update_note(note_id: int, new_text: str):
    """
    Обновление текста заметки по id.
    """
    note = notes.get(note_id)
    if not note:
        return fastapi.HTTPException(status_code=404, detail="Note not found")

    # Обновляем текст и дату обновления
    notes[note_id]['text'] = new_text
    notes[note_id]['updated_at'] = datetime.datetime.now()

    return NoteTextResponse(
        id=note_id,
        text=new_text
    )
