class AudioController {
    constructor(audioElements) {
        this.currentPlayingAudio = null;
        this.registerEventListeners(audioElements);
    }

    registerEventListeners(audioElements) {
        audioElements.forEach(audioElement => {
            // 添加播放事件监听器
            audioElement.addEventListener('play', () => {
                if (this.currentPlayingAudio && this.currentPlayingAudio !== audioElement) {
                    this.currentPlayingAudio.pause(); // 如果有其他音频在播放，则先暂停
                }
                this.currentPlayingAudio = audioElement; // 更新当前播放的音频引用
            });

            // 添加暂停事件监听器
            audioElement.addEventListener('pause', () => {
                if (this.currentPlayingAudio === audioElement) {
                    this.currentPlayingAudio = null;
                }
            });

            // 添加播放结束事件监听器
            audioElement.addEventListener('ended', () => {
                if (this.currentPlayingAudio === audioElement) {
                    this.currentPlayingAudio = null;
                }
            });
        });
    }
}


function isTrue(condition, ifTrue, ifFalse) {
    return condition ? ifTrue : ifFalse;
}