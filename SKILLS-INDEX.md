# AI 视频项目 Skills 安装索引

安装日期：2026-09-09。项目根目录：`/Volumes/EXTERNAL/ai视频`。

## 项目范围

沿用用户在本项目会话中的要求：面向英语母语者，适配 Instagram、TikTok、Reddit 等海外社媒，通常 30 秒以内；提供创意、英文脚本、分镜、运镜、关键帧设计与制作提示词，不生成视频、不默认发布。

本次安装仅提供技能正文及随包引用/脚本文件。文件存在不等于脚本、模型、API、账号或渲染运行时已可用。对外生成、付费、上传、发布、运行底座安装均未执行。

## 安装位置和使用

- 项目级技能目录：`/Volumes/EXTERNAL/ai视频/.agents/skills/`
- 来源、固定 Git 提交与每文件 SHA-256：`/Volumes/EXTERNAL/ai视频/skill-support/installed-manifest.json`
- 安装工具：`/Volumes/EXTERNAL/ai视频/skill-support/install_selected.py`（保留用于追溯，不要默认重跑）
- 当前共 25 个顶层技能包；`seedance-prompt-en` 另附中文子入口，因此 SKILL.md 文件数可大于包数。

下一轮优先使用宿主发现的项目技能。若技能清单未刷新，可直接完整读取本索引列出的具体 `SKILL.md` 及其必需引用；无需为刷新再创建会话或重复安装。

## 强钩子必读入口（2026-09-13）

创意阶段先读 [HOOK-FIRST-SOP.md](HOOK-FIRST-SOP.md)。`director-agent`负责事件与回报，`hyperframes-creative`的 `references/story-spine.md`、`references/beat-direction.md`负责钩子表达及节奏。该门槛通过后再用分镜与视频提示词技能；已有技能不等于已验证留存，不必全部读取。

## 日常优先入口

| 用途 | 相对 `.agents/skills/` 的路径 |
| --- | --- |
| 创意、脚本、对白、人物因果与导演方案 | `director-agent/SKILL.md` |
| 剧本转分镜、摄影机路径、景别、光线和跨镜连续性 | `ai-storyboard-director/SKILL.md` |
| 轻量镜头表和可复制视频提示词 | `storyboard-prompt-assistant/SKILL.md` |
| 通用运镜、焦点、风格、音效与时间轴提示词 | `prompt-videos/SKILL.md` |
| Seedance 中文提示词 | `seedance-prompt/SKILL.md` |
| Seedance 英文提示词 | `seedance-prompt-en/SKILL.md` |
| 人物身份、外形与参考任务 | `character-asset/SKILL.md` |
| 场景空间、光源与材质 | `scene-asset/SKILL.md` |
| 产品和道具结构、比例、持用状态 | `prop-asset/SKILL.md` |
| 拆解用户提供的参考视频 | `video-understand/SKILL.md` |

## 视觉风格

均以对应目录下的 `SKILL.md` 为入口，按作品需要选用，勿同时套用全部风格：

- `cyberpunk-design`：赛博朋克。
- `epic-design`：史诗与空间尺度。
- `fantasy-design`：奇幻。
- `horror-design`：恐怖与空间不安。
- `noir-design`：黑色电影与犯罪。
- `romance-design`：爱情与人物关系。
- `war-design`：战争。
- `wuxia-design`：武侠。

## 按需参考，不自动生成或安装依赖

| 目录 | 用途及边界 |
| --- | --- |
| `seedance-whitebox` | 上游 Skill 名是 `huashu-seedance`；文件夹使用本地消歧名称。参考白模空间/运镜设计；渲染预演需要用户明确要求。 |
| `hyperframes-creative` | 节拍、版式、视觉风格与字幕设计参考；不因文档中的 bootstrap 指令自动安装软件。 |
| `hyperframes-animation` | 运动态势、动效与转场参考；未建立 HyperFrames 渲染项目。 |
| `media-use` | 调色、LUT、配乐、音效与素材处理参考；尚未登录或配置 HeyGen 等服务。 |
| `remotion-best-practices` | 官方 Remotion 主技能及随包参考；未安装 React/Remotion 运行依赖，未启动或渲染视频。 |
| `remotion-transitions` | 转场技法与代码参考；未运行示例。 |
| `video-edit` | 剪辑技法与 FFmpeg 命令参考；当前项目不默认剪出成片。 |

## 来源和版本

远端文件固定于下列提交，安装时未运行上游安装器或业务脚本：

| 来源 | 提交 | 安装内容 |
| --- | --- | --- |
| `62656456/ai-film-skills` | `678edc06d3318c1516f6eb73503f740427fdd831` | 编剧/分镜、3 类资产、8 类风格，共 13 包 |
| `seaartpublic/skills` | `a3edc17605d525b54b2a5f61a4800f2dd8dd8b30` | `storyboard-prompt-assistant` |
| `alchaincyf/seedance-skill` | `f14d8fa19b57c83f674c70e5730a19df4ef4accd` | `seedance-whitebox` |
| `remotion-dev/skills` | `11986e44eeb672b083354e68967f2b194df73b7c` | `remotion-best-practices` |
| `Ashad001/remotion-transitions` | `2bf15881f1f9d74e4b76979cd0846aefffc9962c` | `remotion-transitions` |

其余 8 包来自 `/Users/USER/.agents/skills/` 的完整本地快照，复制后逐文件 SHA-256 比较一致；不声称这些快照等于上游最新版本。

Seedance 指南中版本、素材数量、时长、真人参考限制等可能过时或互相冲突。写具体平台参数前按用户所用版本核对一手文档；摄影和叙事知识可作参考，固定参数不作为当前事实。

尚未安装/配置：Replicate MCP、DaVinci Resolve MCP、ComfyUI、完整 Everything AI Filmmaking 工作室框架、视频生成服务与账号。完整工作室框架含其自己的规则、hooks 和工作流，未将其混入本项目根规则。

本次验证范围：文件安装、入口存在、源快照复制一致、完整性清单；非实片质量/脚本执行/生成运行时验收。
