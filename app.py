from flask import Flask, render_template_string, request, jsonify
import time

app = Flask(__name__)

# 临时存储提交的数据（最多保存100条，防止溢出）
data_queue = []

# ====================== 【必须修改这2处】 ======================
# 表单标题（可自定义）
FORM_TITLE = "请填写表单"
# 你的Excel模板第一行的字段名，顺序必须完全一致！
fields = ["姓名", "部门", "日期", "内容"]
# ==============================================================

# 表单页面HTML（无需修改）
FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #45a049; }
        .success { color: green; font-size: 18px; text-align: center; margin-top: 50px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    {% if success %}
        <div class="success">提交成功！感谢您的填写。<br><br>
        <button onclick="window.location.href='/'">继续填写</button></div>
    {% else %}
        <form method="POST">
            {% for field in fields %}
            <div class="form-group">
                <label for="{{ field }}">{{ field }}</label>
                <input type="text" id="{{ field }}" name="{{ field }}" required>
            </div>
            {% endfor %}
            <button type="submit">提交</button>
        </form>
    {% endif %}
</body>
</html>
"""

# 表单提交页面
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 收集表单数据
        data = {}
        for field in fields:
            data[field] = request.form.get(field, "")
        # 加入时间戳，方便区分
        data['timestamp'] = time.time()
        # 存入队列
        data_queue.append(data)
        # 队列最多保留100条数据，防止内存溢出
        if len(data_queue) > 100:
            data_queue.pop(0)
        return render_template_string(FORM_HTML, fields=fields, title=FORM_TITLE, success=True)
    return render_template_string(FORM_HTML, fields=fields, title=FORM_TITLE, success=False)

# 本地拉取数据的接口（关键，无需修改）
@app.route('/get_new_data')
def get_new_data():
    global data_queue
    if data_queue:
        # 返回所有数据并清空队列
        result = data_queue.copy()
        data_queue.clear()
        return jsonify(result)
    return jsonify([])

# Render云端运行入口（无需修改）
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
