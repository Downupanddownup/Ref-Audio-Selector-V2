import sys

from fastapi import APIRouter, Request

from server.bean.reference_audio.obj_reference_audio import ObjReferenceAudioFilter
from server.bean.reference_audio.obj_reference_audio_compare_task import ObjReferenceAudioCompareTask
from server.common.response_result import ResponseResult
from server.dao.data_base_manager import db_config
from server.service.reference_audio.reference_audio_compare_sevice import ReferenceAudioCompareService
from server.service.reference_audio.reference_audio_service import ReferenceAudioService
from server.util.util import ValidationUtils, clean_path, str_to_int
from server.common.log_config import logger
from subprocess import Popen

python_exec = sys.executable or "python"

router = APIRouter(prefix="/audio")

p_similarity = None


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

    count = ReferenceAudioService.find_count(audio_filter)
    audio_list = ReferenceAudioService.find_list(audio_filter)

    return ResponseResult(data=audio_list, count=count)


@router.post("/get_compare_audio_detail_list")
async def get_compare_audio_detail_list(request: Request):
    form_data = await request.form()
    audio_id = str_to_int(form_data.get('audioId'))
    if ValidationUtils.is_empty(audio_id):
        return ResponseResult(code=1, msg="audioId is empty")

    last_task = ReferenceAudioCompareService.get_last_finish_task_by_audio_id(audio_id)

    if last_task is None:
        return ResponseResult(msg='没有完成比较的音频')

    compare_audio_detail_list = ReferenceAudioCompareService.get_compare_detail_list_by_task_id(
        last_task.id)

    return ResponseResult(data=compare_audio_detail_list)


@router.post("/start_compare_audio")
async def start_compare_audio(request: Request):
    form_data = await request.form()
    audio_id = form_data.get('audioId')
    category_name = form_data.get('categoryName')

    if ValidationUtils.is_empty(audio_id) or ValidationUtils.is_empty(category_name):
        return ResponseResult(code=1, msg='参数错误')

    global p_similarity
    if p_similarity is not None:
        return ResponseResult(code=1, msg='正在比较音频，请稍后再试')

    task = ObjReferenceAudioCompareTask(audio_id=audio_id, category_name=category_name)
    task_id = ReferenceAudioCompareService.insert_task(task)

    cmd = f'"{python_exec}" server/tool/speaker_verification/voice_similarity.py '
    cmd += f' -t "{task_id}"'
    cmd += f' -r "{db_config.role_name}"'

    logger.info(cmd)
    p_similarity = Popen(cmd, shell=True)
    p_similarity.wait()

    p_similarity = None

    return ResponseResult(msg='完成音频比较')
