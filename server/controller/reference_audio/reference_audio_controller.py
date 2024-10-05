from fastapi import APIRouter, Request

from server.common.response_result import ResponseResult
from server.dao.data_base_manager import db_config
from server.service.reference_audio.reference_audio_service import ReferenceAudioService

router = APIRouter(prefix="/audio")


@router.get("/")
async def root():
    db_config.update_db_path(r'E:\GPT-SoVITS\Ref-Audio-Selector-V2\example.db')
    return {"message": "Hello World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.post("/get_reference_audio_list")
async def get_reference_audio_list(request: Request):
    form_data = await request.form()
    param1 = form_data.get("param1")
    param2 = form_data.get("param2")

    list = ReferenceAudioService.search()

    result = ResponseResult(code=0, data=list, msg="success")
    return result
