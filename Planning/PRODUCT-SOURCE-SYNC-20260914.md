# 视频项目产品来源同步 · 2026-09-14

## 当前权威

运行时任务库：`/Volumes/EXTERNAL/app/EarthOnlineGuide/EarthOnlineGuide/Resources/TaskPacks/earth-online-guide-source-v1.json`

- 实读 contentVersion：`source-v3-copy-171-playability-r1`
- 实算 SHA256：`1df030e75195208ea03b4bb48dd7b734f99fd0c2b4f0c1dcab94526d4531cf4f`
- 1,012 条记录、1,012 个唯一 canonicalTaskID；805 个 core、211 个 egg，4 个同时具备两种资格。
- 本次字节比较与 `/Volumes/EXTERNAL/app/EarthOnlineGuide/Planning/Release-1.7.3/distribution-20260913/PocketRove-Release-1.7.3-2.xcarchive/Products/Applications/EarthOnlineGuide.app/earth-online-guide-source-v1.json` 完全相同；不据此声称所有地区公开上线。
- App Owner 交接说明：610条优化、402条保留；每日仍随机3个核心任务。本次未独立重算版本差异或审计抽取代码。

引用读取 cards[].canonicalTaskID、taskRevisionID、title.zh-Hans、title.en、eligibleTypes。早期 Excel、候选表、旧视频截图不覆盖运行时原文。历史及已抽取任务可能保留旧快照，须核对ID和版本。包内历史 pending 审计字段不替代本次归档字节比较。

## 当前脚本核对

水杯任务：`v3-EGG-0115`

- taskRevisionID：`v3-natural-en-full-r1-v3-EGG-0115-690680845fb3996170db`
- 中文：把拿起水杯的动作演成颁奖典礼
- English：Pick up your cup as if you're accepting an award.
- eligibleTypes：egg。不得宣传为每日免费核心任务。
- 与 `Planning/Jimeng-Retry-20260911/扩展真实任务池.md` 对应条目一致，没有发现该任务文案冲突。
- 当前会话的领奖、感谢水龙头台词属于创作对白，不是 App 原文。此前“任务对应关系待确认”现已由运行时核实；具体水杯任务的原生屏幕素材仍须单独匹配，不能用生成UI充当。
- 顺带核对旧 Ninja Mage 对应 `v3-EGG-0170`：Give yourself a new title for the next five minutes. 仍为egg，与SOP引用一致。
- 此次为以上两项定向核对，不声称所有历史交付包均已逐条更新。

## 真实UI与补充文案入口

新英文原图：`/Volumes/EXTERNAL/app/EarthOnlineGuide/Marketing/AppStore-1.7.3-20260914/raw/`
来源说明：同级上层 `README.md`（本次已读取）。7张PNG：01-welcome、02-daily-clues、03-daily-revealed、04-history、05-souvenirs、06-settings、07-history-detail。

来源是1.7.3 Release Simulator build 1、QA iPhone 17/iOS 26.5，原图1206×2622；不是App Store安装截图。02/03来自同次随机抽取，其他部分使用既有QA存档。此次仅核对目录与来源说明，未逐张重做视觉验收，不断言七张中包含水杯任务。

真实UI独立合成。生成宣传图只作外围美术参考。原文中英不超过3行的产品要求沿用；片外改写不能冒充App正文。

- 拆卡前提示：`/Volumes/EXTERNAL/app/EarthOnlineGuide/EarthOnlineGuide/Resources/task-reveal-hints-171.json`
- 完成后回应：`/Volumes/EXTERNAL/app/EarthOnlineGuide/EarthOnlineGuide/Resources/completion-scenes-150.json`

以上为补充材料入口，本次未全文审阅；不得与任务正文混用。无提示允许问号，不自行补写。

本次仅更新本视频项目资料索引，未修改App、模拟器、其他岗位制作文件或已批准脚本；没有生成或发布视频。
