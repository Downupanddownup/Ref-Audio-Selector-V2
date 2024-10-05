from typing import Dict

from server.bean.reference_audio.obj_reference_audio import ObjReferenceAudio
from server.dao.reference_audio.reference_audio_dao import ReferenceAudioDao


class ReferenceAudioService:
    @staticmethod
    def search() -> list[ObjReferenceAudio]:
        return ReferenceAudioDao.search()