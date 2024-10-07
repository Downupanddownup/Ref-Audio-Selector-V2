import webbrowser

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from server.controller.reference_audio.reference_audio_controller import router as audio_router
from server.controller.inference_task.inference_task_controller import router as task_router
from server.controller.long_text_inference.long_text_inference_controller import router as long_text_router
from server.controller.result_evaluation.result_evaluation_controller import router as result_evaluation_router
from server.controller.audio_packaging.audio_packaging_controller import router as audio_packaging_router
from server.controller.common_controller import router as common_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

# 注册路由
app.include_router(audio_router)
app.include_router(task_router)
app.include_router(long_text_router)
app.include_router(result_evaluation_router)
app.include_router(audio_packaging_router)
app.include_router(common_router)

# Mount static files directory
app.mount("/static", StaticFiles(directory="."), name="static")


if __name__ == "__main__":
    import uvicorn

    url = "http://localhost:8000/static/main.html"
    # webbrowser.open(url)

    uvicorn.run(app, host="0.0.0.0", port=8000)
