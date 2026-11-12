# AutoDL H3 跨任务调用入口

本机同一 macOS 用户下的任务可复用。远程或云任务不会自动拥有本机密钥。
当前状态：客户端本地准备完成；用户已配置本地密钥，2026-09-10 已只读确认文件存在、非空、普通文件及权限 600。未读取密钥内容；服务端鉴权及真实生成闭环尚未验证。

## 一次性配置（用户在自己的终端完成）

```sh
python3 '/Volumes/EXTERNAL/ai视频/Integrations/autodl-h3/setup_token.py'
```

从 AutoDL.Art 的令牌管理复制 ComfyUI 分组密钥，在终端隐藏输入提示中粘贴。脚本保存到 `~/.config/pocket-rove/autodl-comfyui.token`，文件权限 600；同一系统用户的任务可读取。勿打印、提交 Git 或把它写进聊天/交接文档。也可使用环境变量 AUTODL_COMFYUI_TOKEN（优先级更高）。

## 已确认接口

POST `https://autodl.art/api/v1/comfyui/comfyui_workflow/{workflow_id}`
GET `https://autodl.art/api/v1/comfyui/comfyui_workflow/result/{task_id}`
Headers：Authorization 值为平台 Token 原文；Content-Type 为 application/json。不要擅自加 Bearer。

文生视频 workflow_id：`minimax_h3_lightx2v_no_pic`

```json
{
  "duration": 5,
  "prompt": "A yellow ceramic cup on a wooden cafe table beside a window. Static camera, warm natural daylight, subtle steam rising. No people, no text, no logos.",
  "resolution": "768p竖"
}
```

界面参数：duration 1–15 整秒；prompt 1–200000 字符（本地客户端保守限制 10000）；resolution 枚举，已确认 768p竖。不要猜测额外参数。
2026-09-10 页面：768p 08:00–24:00 ¥0.03/秒、00:00–08:00 ¥0.02/秒；执行前复核现价，不能推广到别的工作流。

多参考图候选：`minimax_h3_zm_u24`，ref_image_0 必需，最多 9 张图/3段音频；其价格与完整枚举尚未验证。人物一致性用这个候选另行小样验收。真实 App 界面保持原始素材后期合成。

## 调用方式

在本任务独有输出目录准备 request.json；不要与其他任务共用记录文件。下列以当前目录为例：

```sh
python3 '/Volumes/EXTERNAL/ai视频/Integrations/autodl-h3/client.py' validate request.json
# 仅在用户已批准本次内容和费用/预算时执行：
python3 '/Volumes/EXTERNAL/ai视频/Integrations/autodl-h3/client.py' submit minimax_h3_lightx2v_no_pic request.json --approved-charge --record submission.json
python3 '/Volumes/EXTERNAL/ai视频/Integrations/autodl-h3/client.py' status TASK_ID --record status-001.json
```

--approved-charge 是操作者声明已获批准，不是平台硬性预算限制。令牌当前由用户创建为无限额度、永不过期；不等于无限制调用授权。
记录文件禁止覆盖，后续查询换 status-002.json 等新名字。轮询可间隔 15–30 秒，检查 code 和 data.status。SUCCESS 后从 data.results 获取媒体链接及时下载到本任务目录；当前客户端只保存响应，未自动下载。下载链接不携带 Authorization 请求头，不在聊天公开签名链接。FAILED/异常状态停止，超时或网络中断先查平台调用日志，禁止盲目重发 POST。

## 给其他任务的指令

读取本文件并复用现有 client.py，不必租 GPU。只在用户批准的视频内容与费用预算内生成。不得读取或输出密钥内容；让客户端自行加载。保存本任务唯一 request/提交/查询/媒体记录。完成标准为真实任务 SUCCESS、成品可播放并核对实际扣费；仅本地检查或拿到任务 ID 不算生成成功。

来源：https://autodl.art/docs/comfyui_api/
