from fastapi import APIRouter, Request

from server.bean.reference_audio.obj_reference_audio import ObjReferenceAudioFilter
from server.common.response_result import ResponseResult
from server.dao.data_base_manager import db_config
from server.service.reference_audio.reference_audio_service import ReferenceAudioService
from server.util.util import ValidationUtils, clean_path

router = APIRouter(prefix="/audio")


@router.post("/load_audio_list_file")
async def load_audio_list_file(request: Request):
    form_data = await request.form()
    audio_list_file = form_data.get("audioListFile")
    if ValidationUtils.is_empty(audio_list_file):
        return ResponseResult(code=1, msg="audioListFile is empty")
    audio_list_file = clean_path(audio_list_file)

    audio_list = ReferenceAudioService.convert_from_list(audio_list_file, f'{db_config.get_work_dir()}\\refer_audio')
    count = ReferenceAudioService.insert_reference_audio_list(audio_list)

    return ResponseResult(msg=f'导入{count}个音频')


@router.post("/get_reference_audio_list")
async def get_reference_audio_list(request: Request):
    form_data = await request.form()
    audio_filter = ObjReferenceAudioFilter(form_data)

    audio_list = ReferenceAudioService.find_list(audio_filter)

    return ResponseResult(data=audio_list)
