import sys
import time
import requests
from future.moves import subprocess
from concurrent.futures import ThreadPoolExecutor

python_exec = sys.executable or "python"


class RasApiMonitor:

    @staticmethod
    def start_service() -> bool:
        try:
            startup_timeout = 60
            process = start_new_service('server/api/ras_api.py')
            end_time = time.time() + startup_timeout
            while time.time() < end_time:
                if RasApiMonitor.check_service_status():
                    print("Service started successfully.")
                    return True
                time.sleep(1)  # 每隔一秒检查一次
            process.terminate()
            print("Service did not start within the given timeout.")
            return False
        except Exception as e:
            print(f"Error starting service: {e}")
            return False

    @staticmethod
    def check_service_status(timeout: int = 2) -> bool:
        """
        检查服务 B 是否启动。

        :param timeout: 超时时间（秒）
        :return: 如果服务在指定时间内响应，则返回 True，否则返回 False。
        """
        try:
            response = _send_request('/status')
            return response.status_code == 200
        except Exception as e:
            # 可能是超时或网络问题
            print(f"Error checking service status: {e}")
            return False

    @staticmethod
    def stop_service() -> bool:
        """
        关闭服务 B 并检查其状态。

        :return: 如果成功关闭，则返回 True，否则返回 False。
        """
        try:
            _send_request('/stop')
            return not RasApiMonitor.check_service_status()
        except Exception as e:
            print(f"Error stopping service: {e}")
            return False


def _send_request(endpoint: str) -> requests.Response:
    """
    发送 HTTP 请求到指定的端点。

    :param endpoint: URL 的路径部分。
    :return: Response 对象。
    """
    base_url = "http://localhost:8001"
    url = f"{base_url}{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response


def start_new_service(script_path):
    # 对于Windows系统
    if sys.platform.startswith('win'):
        cmd = f'start cmd /k {python_exec} {script_path}'
    # 对于Mac或者Linux系统
    else:
        cmd = f'xterm -e {python_exec} {script_path}'

    proc = subprocess.Popen(cmd, shell=True)

    # 关闭之前启动的子进程
    # proc.terminate()

    # 或者如果需要强制关闭可以使用
    # proc.kill()

    return proc