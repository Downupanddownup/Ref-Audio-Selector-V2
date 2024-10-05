from fastapi import APIRouter, Request

from server.common.response_result import ResponseResult
from server.dao.data_base_manager import db_config
from server.util.util import ValidationUtils

router = APIRouter(prefix="/common")


@router.get("/switch_role_workspace")
async def switch_role_workspace(request: Request):
    form_data = await request.form()
    workspace = form_data.get("workspace")
    role_name = form_data.get("roleName")
    if ValidationUtils.is_empty(workspace):
        return ResponseResult(code=1, msg="workspace is empty")
    if ValidationUtils.is_empty(role_name):
        return ResponseResult(code=1, msg="roleName is empty")
    db_config.update_db_path(workspace, role_name)
    return ResponseResult(code=0, msg="success")
