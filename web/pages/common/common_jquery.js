
const CommonSpace = (function () {


    function customJquery($) {
        $.extend($.ajax, {
            _originalAjax: $.ajax,
            _requestStates: {}, // 定义一个全局的状态对象，用于跟踪请求状态

            // 新的 $.ajax 方法
            ajax: function (settings) {
                const _this = this
                // 获取请求的唯一标识符
                const requestKey = settings.url + settings.type + JSON.stringify(settings.data);

                // 检查是否有请求正在进行
                if (_this._requestStates[requestKey]) {
                    console.log('请求已在进行中，不再重复发送。');
                    return;
                }

                // 设置请求状态为进行中
                _this._requestStates[requestKey] = true;

                // 调用原始的 $.ajax 方法
                const jqXHR = _this._originalAjax.apply(_this, settings);

                // 请求完成后清除状态
                jqXHR.always(function () {
                    delete _this._requestStates[requestKey];
                });

                return jqXHR;
            }
        });
    }
    
    
    function loadHtml(url, callback) {
        // 使用 $.ajax 加载 HTML 文件
        $.ajax({
            url: url, // 替换为你的HTML文件路径
            type: 'GET',
            dataType: 'html',
            success: function(data) {
                // 成功加载后，将内容追加到文档末尾
                $(document.body).append(data);
                callback()
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('加载HTML文件失败：', textStatus, errorThrown);
            }
        });
    }
    
    function loadHtmls(urls,callback) {
        const unLoads = new Set(urls)
        const allUrls = new Set(urls)
        allUrls.forEach(url => {
            loadHtml(url, function () {
                unLoads.delete(url)
                if (unLoads.size === 0) {
                    callback()
                }
            })
        })
    }
    
    return {
        customJquery: customJquery,
        loadHtmls: loadHtmls
    }
    
})()
