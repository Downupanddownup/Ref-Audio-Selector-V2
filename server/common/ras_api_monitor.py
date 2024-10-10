import sys
import time
import requests
import json
from future.moves import subprocess

from server.bean.inference_task.gpt_model import GptModel
from server.bean.inference_task.vits_model import VitsModel
from server.common.log_config import logger

python_exec = sys.executable or "python"


class InferenceParams:
    def __init__(self,
                 refer_wav_path: str = None,
                 prompt_text: str = None,
                 prompt_language: str = None,
                 text: str = None,
                 text_language: str = None,
                 cut_punc: str = None,
                 top_k: int = 10,
                 top_p: float = 1.0,
                 temperature: float = 1.0,
                 speed: float = 1.0
                 ):
        self.refer_wav_path = refer_wav_path
        self.prompt_text = prompt_text
        self.prompt_language = prompt_language
        self.text = text
        self.text_language = text_language
        self.cut_punc = cut_punc
        self.top_k = top_k
        self.top_p = top_p
        self.temperature = temperature
        self.speed = speed

    def to_dict(self):
        return {
            "refer_wav_path": self.refer_wav_path,
            "prompt_text": self.prompt_text,
            "prompt_language": self.prompt_language,
            "text": self.text,
            "text_language": self.text_language,
            "cut_punc": self.cut_punc,
            "top_k": self.top_k,
            "top_p": self.top_p,
            "temperature": self.temperature,
            "speed": self.speed
        }


class RasApiMonitor:

    @staticmethod
    def get_api_service_url() -> str:
        port = 8001
        return f'http://localhost:{port}'

    @staticmethod
    def start_service() -> bool:
        if RasApiMonitor.check_service_status():
            logger.info("Service has started")
            return True
        try:
            startup_timeout = 60
            service_process = _start_new_service('server/api/ras_api.py')
            end_time = time.time() + startup_timeout
            while time.time() < end_time:
                if RasApiMonitor.check_service_status():
                    logger.info("Service started successfully.")
                    return True
                time.sleep(1)  # 每隔一秒检查一次
            service_process.terminate()
            logger.error("Service did not start within the given timeout.")
            return False
        except Exception as e:
            logger.error(f"Error starting service: {e}")
            return False

    @staticmethod
    def check_service_status(timeout: int = 2) -> bool:
        """
        检查服务 B 是否启动。

        :param timeout: 超时时间（秒）
        :return: 如果服务在指定时间内响应，则返回 True，否则返回 False。
        """
        try:
            url = f'{RasApiMonitor.get_api_service_url()}/status'
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.status_code == 200
        except Exception as e:
            # 可能是超时或网络问题
            return False

    @staticmethod
    def stop_service() -> bool:
        """
        关闭服务 B 并检查其状态。

        :return: 如果成功关闭，则返回 True，否则返回 False。
        """
        try:
            # _send_request('/stop')
            url = f'{RasApiMonitor.get_api_service_url()}/control?command=exit'
            response = requests.get(url)
            response.raise_for_status()
            return not RasApiMonitor.check_service_status()
        except Exception as e:
            return not RasApiMonitor.check_service_status()

    @staticmethod
    def inference_audio_from_api(params: InferenceParams):
        url = f'{RasApiMonitor.get_api_service_url()}/ras'
        json_data = json.dumps(params.to_dict())
        # 发起GET请求
        response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'}, stream=True)

        # 检查响应状态码是否正常（例如200表示成功）
        if response.status_code == 200:
            # 返回音频数据的字节流
            return response.content
        else:
            raise Exception(
                f"Failed to fetch audio from API. Server responded with status code {response.status_code}.message: {response.json()}")

    @staticmethod
    def set_api_models(gpt_model: GptModel, sovits_model: VitsModel):
        url = f'{RasApiMonitor.get_api_service_url()}/set_model'

        # 将字典转换为JSON格式的字符串
        json_data = json.dumps({
            "gpt_model_path": gpt_model.path,
            "sovits_model_path": sovits_model.path
        })

        # 发送POST请求
        response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

        # 检查请求是否成功
        response.raise_for_status()  # 如果响应状态码不是200，将抛出HTTPError异常

        # 返回响应对象
        return response.text


def _start_new_service(script_path: str) -> subprocess:
    # 对于Windows系统
    if sys.platform.startswith('win'):
        cmd = f'start cmd /c {python_exec} {script_path}'
    # 对于Mac或者Linux系统
    else:
        cmd = f'xterm -e {python_exec} {script_path}'

    proc = subprocess.Popen(cmd, shell=True)

    # 关闭之前启动的子进程
    # proc.terminate()

    # 或者如果需要强制关闭可以使用
    # proc.kill()

    return proc
