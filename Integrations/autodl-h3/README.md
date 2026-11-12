# AutoDL H3 接入准备

状态：本地客户端已准备；尚未鉴权、提交生成任务或产生 API 费用。

- 文档：https://autodl.art/docs/comfyui_api/
- 令牌分组必须为 ComfyUI；通过环境变量 AUTODL_COMFYUI_TOKEN 读取，不写入代码或聊天。
- submit 仅提交一次，不自动重试。网络超时不能视为提交失败，须先查平台调用日志。
- status 通过 task_id 查询。响应保存到指定的新文件，终端仅输出状态及任务 ID。
- 下载链接短期有效；成功后需及时保存成品。尚未实现下载，因为结果字段结构尚未取得真实样本。
- smoke-text.json 是无人物、无产品素材的 5 秒文生视频接入测试草稿。只通过本地 JSON 检查；需按选定文生视频工作流复核 resolution 等参数。不能用于需要 ref_image_0 的 U24。
- 首次实际提交前必须确认工作流价格、账号余额及用户同意的测试费用。

命令：python3 client.py --help
验收：平台返回任务 ID → 查询 SUCCESS → 下载可播放视频 → 核对实际账单。
