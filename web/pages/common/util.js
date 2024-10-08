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

    dispatchClickEvent(audioElement) {
        console.log('播放/暂停按钮被点击');
        if (audioElement.paused || audioElement.currentTime === 0) {
            // 如果音频当前是暂停状态或尚未开始播放，则播放音频
            audioElement.play();
            console.log('正在播放音频');
        } else {
            // 如果音频正在播放，则暂停音频
            audioElement.pause();
            console.log('音频已暂停');
        }
    }
    
}


function isTrue(condition, ifTrue, ifFalse) {
    return condition ? ifTrue : ifFalse;
}