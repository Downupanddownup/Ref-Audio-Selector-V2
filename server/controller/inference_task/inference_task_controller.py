from fastapi import APIRouter, Request

from server.bean.inference_task.obj_inference_task import ObjInferenceTaskFilter
from server.bean.inference_task.obj_inference_text import ObjInferenceTextFilter, ObjInferenceText
from server.common.response_result import ResponseResult
from server.service.inference_task.inference_task_service import InferenceTaskService
from server.service.inference_task.inference_text_service import InferenceTextService
from server.util.util import str_to_int

router = APIRouter(prefix="/task")


@router.post("/get_inference_text_list")
async def get_inference_text_list(request: Request):
    form_data = await request.form()
    text_filter = ObjInferenceTextFilter(form_data)

    count = InferenceTextService.find_count(text_filter)
    text_list = InferenceTextService.find_list(text_filter)

    return ResponseResult(data=text_list, count=count)


@router.post("/insert_inference_text")
async def insert_inference_text(request: Request):
    form_data = await request.form()
    text = ObjInferenceText(
        category=form_data.get('category'),
        text_content=form_data.get('text_content'),
        text_language=form_data.get('text_language')
    )

    text_id = InferenceTextService.insert_inference_text(text)

    return ResponseResult(data={"text_id": text_id})


@router.post("/update_inference_text")
async def update_inference_text(request: Request):
    form_data = await request.form()
    text = ObjInferenceText(
        id=str_to_int(form_data.get('text_id')),
        category=form_data.get('category'),
        text_content=form_data.get('text_content'),
        text_language=form_data.get('text_language')
    )
    if text.id < 1:
        return ResponseResult(code=1, msg="text_id is invalid")

    result = InferenceTextService.update_inference_text_by_id(text)

    return ResponseResult(data={"result": result})


@router.post("/delete_inference_text")
async def delete_inference_text(request: Request):
    form_data = await request.form()
    text_id = str_to_int(form_data.get('text_id')),
    if text_id < 1:
        return ResponseResult(code=1, msg="text_id is invalid")

    result = InferenceTextService.delete_inference_text_by_id(text_id)

    return ResponseResult(data={"result": result})


@router.post("/get_inference_task_list")
async def get_inference_task_list(request: Request):
    form_data = await request.form()
    task_filter = ObjInferenceTaskFilter(form_data)

    count = InferenceTaskService.find_count(task_filter)
    task_list = InferenceTaskService.find_list(task_filter)

    return ResponseResult(data=task_list, count=count)
