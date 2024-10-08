class C_ObjReferenceAudio {//参考音频
    constructor(data) {
        this.id = data.id ? data.id : 0; // id
        this.audioName = data.audioName || ''; // 音频名称
        this.audioPath = data.audioPath || ''; // 音频路径
        this.content = data.content || ''; // 音频内容
        this.language = data.language || ''; // 音频语种
        this.category = data.category || ''; // 音频分类
        this.audioLength = data.audioLength || 0; // 音频时长
        this.createTime = data.createTime; // 创建时间, 默认为当前时间
    }
}

class C_ObjInferenceTask {//推理任务
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.taskName = data.taskName || ''; // 任务名称
        this.compareType = data.compareType || ''; // 比较类型
        this.gptSovitsVersion = data.gptSovitsVersion || ''; // 模型版本
        this.gptModelName = data.gptModelName || ''; // GPT模型名称
        this.vitsModelName = data.vitsModelName || ''; // Vits模型名称
        this.topK = data.topK || 0; // top_k值
        this.topP = data.topP || 0; // top_p值
        this.temperature = data.temperature || 0; // 温度
        this.textDelimiter = data.textDelimiter || ''; // 文本分隔符
        this.speed = data.speed || 0; // 语速
        this.otherParameters = data.otherParameters || ''; // 其余参数
        this.inferenceStatus = data.inferenceStatus || 0; // 推理状态 0 待推理 1 推理中 2 推理完成
        this.executeTextSimilarity = data.executeTextSimilarity || 0;//是否已执行文本相似度 0 否 1 是
        this.executeAudioSimilarity = data.executeAudioSimilarity || 0;//是否已执行音频相似度 0 否 1 是
        this.createTime = data.createTime; // 创建时间, 默认为当前时间
        this.taskTextList = data.taskTextList ? data.taskTextList.map(item => new C_ObjInferenceTaskText(item)) : [];
        this.taskAudioList = data.taskAudioList ? data.taskAudioList.map(item => new C_ObjInferenceTaskAudio(item)) : [];
        this.compareParams = data.compareParams ? data.compareParams.map(item => new C_ObjInferenceTaskCompareParams(item)) : [];
    }
}
class C_ObjInferenceTaskText {//推理任务中，相关推理文本
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.taskId = data.taskId || 0; // 推理任务id
        this.textId = data.textId || 0; // 推理文本id
        this.textContent = data.textContent || ''; // 推理文本
        this.textLanguage = data.textLanguage || ''; // 文本语种
        this.createTime = data.createTime; // 创建时间, 默认为当前时间
    }
}
class C_ObjInferenceTaskAudio {//推理任务中，相关参考音频
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.taskId = data.taskId || 0; // 推理任务id
        this.audioId = data.audioId || 0; // 音频id
        this.audioName = data.audioName || ''; // 音频名称
        this.audioPath = data.audioPath || ''; // 音频路径
        this.audioContent = data.audioContent || ''; // 音频内容
        this.audioLanguage = data.audioLanguage || ''; // 音频语种
        this.createTime = data.createTime ? new Date(data.createTime) : null; // 创建时间, 默认为当前时间
    }
}
class C_ObjInferenceTaskCompareParams {//推理任务中，对比的变量
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.taskId = data.taskId || 0; // 任务id
        this.audioCategory = data.audioCategory || ''; // 音频分类
        this.gptSovitsVersion = data.gptSovitsVersion || ''; // 模型版本
        this.gptModelName = data.gptModelName || ''; // GPT模型名称
        this.vitsModelName = data.vitsModelName || ''; // Vits模型名称
        this.topK = data.topK || 0; // top_k值
        this.topP = data.topP || 0; // top_p值
        this.temperature = data.temperature || 0; // 温度
        this.textDelimiter = data.textDelimiter || ''; // 文本分隔符
        this.speed = data.speed || 0; // 语速
        this.otherParameters = data.otherParameters || ''; // 其余参数
        this.createTime = data.createTime ? new Date(data.createTime) : null; // 创建时间, 默认为当前时间
    }
}
class C_ObjInferenceTaskResultAudio {//推理任务的推理结果音频
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.taskId = data.taskId || 0; // 推理任务id
        this.textId = data.textId || 0; // 推理文本id
        this.audioId = data.audioId || 0; // 参考音频id
        this.compareParamId = data.compareParamId || 0; // 比对参数id
        this.path = data.path || ''; // 音频地址
        this.audioLength = data.audioLength || 0; // 时长
        this.asrText = data.asrText || ''; // asr文本
        this.asrSimilarScore = data.asrSimilarScore || 0; // 文本相似度
        this.audioSimilarScore = data.audioSimilarScore || 0; // 音频相似度
        this.score = data.score || 0; // 评分
        this.longTextScore = data.longTextScore || 0; // 长文评分
        this.remark = data.remark || ''; // 备注
        this.createTime = data.createTime ? new Date(data.createTime) : null; // 创建时间, 默认为当前时间
    }
}

class C_ObjInferenceCategory {//参考分类
    constructor(data) {
        this.id = data.id ? data.id : 0; // 自增编号
        this.name = data.name || ''; // 分类名称
        this.createTime = data.createTime ? new Date(data.createTime) : null; // 创建时间, 默认为当前时间
    }
}

class C_ObjReferenceAudioCompareTask {
    constructor(data) {
        this.id = data.id ? data.id : 0;// 自增编号
        this.audioId = data.audioId || 0;// 音频id
        this.categoryName = data.categoryName || '';// 比对目录名称
        this.status = data.status || 0;// 任务状态：0 待执行 1 执行中 2 已完成 3 失败
        this.remark = data.remark || '';// 备注
        this.createTime = data.createTime ? new Date(data.createTime) : null;// 创建时间,
    }
}

class C_ObjReferenceAudioCompareDetail {
    constructor(data) {
        this.id = data.id ? data.id : 0;// 自增编号
        this.taskId = data.taskId || 0;// 比对任务id
        this.compareAudioId = data.compareAudioId || 0;// 被比较的音频id
        this.score = data.score || 0;// 相似度分值
        this.createTime = data.createTime ? new Date(data.createTime) : null;// 创建时间,
        this.compareAudio = data.compareAudio ? new C_ObjReferenceAudio(data.compareAudio) : null;
    }
}

class C_GptModel {
    constructor(data) {
        this.version = data.version || '';//模型版本
        this.name = data.name || '';//模型名称
    }
}

class C_VitsModel {
    constructor(data) {
        this.version = data.version || '';//模型版本
        this.name = data.name || '';//模型名称
    }
}



