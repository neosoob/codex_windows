from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    highlights = [
        {
            "title": "本地协作",
            "description": "Codex Windows 运行在桌面环境中，直接读取你的工作区，适合一边看代码一边协作修改。",
        },
        {
            "title": "动手能力",
            "description": "不仅能解释思路，还能检查项目结构、编辑文件、执行命令，并把结果整理成可落地的改动。",
        },
        {
            "title": "工程化输出",
            "description": "从页面、脚本到功能修复，都会尽量结合上下文完成实现、验证和交付，而不是只停留在建议层面。",
        },
    ]

    workflow = [
        "读取当前仓库和约束，理解已有结构。",
        "定位目标文件，提出或直接实施改动。",
        "在可行范围内执行验证，并反馈结果与风险。",
    ]

    return render_template(
        "index.html",
        highlights=highlights,
        workflow=workflow,
    )


if __name__ == "__main__":
    app.run(debug=True)
