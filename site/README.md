# TRACER 项目网站

GitHub Pages 直接发布本目录。英文为默认入口 `index.html`，中文、日语、韩语分别使用 `zh.html`、`ja.html`、`ko.html`，页面顶部可相互切换。

网站先解释 Lean 和一个最小修复例子，再展示功能、已完成研究结果及目前进度。三步教学示例在浏览器本地切换，不调用 API、不上传输入。`demo/` 保留已有 24 案例演示；本次不改写其历史数据。

修改入口为四个 HTML 文件、`site.css` 和 `walkthrough.js`。`overview.svg` 是 README 中的功能流程图。不要把进行中任务的部分记录替换成最终性能数字。数据口径见 `docs/INTRODUCTION_EVIDENCE.md`。

本地预览：在仓库根目录执行 `python -m http.server 8000 --directory site`，浏览 `http://127.0.0.1:8000/`。
