from flask import Flask, request, jsonify
app = Flask(__name__)

# 临时存数据
data_list = []

# 表单页面
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = {
            "设备型号": request.form.get("设备型号"),
            "维护人员": request.form.get("维护人员"),
            "维护时间": request.form.get("维护时间"),
            "观测场设施-维护内容": request.form.get("gc_content"),
            "观测场设施-维护结果": request.form.get("gc_result"),
            "观测场设施-问题": request.form.get("gc_problem"),
            "设备运行情况-维护内容": request.form.get("sb_content"),
            "设备运行情况-维护结果": request.form.get("sb_result"),
            "设备运行情况-问题": request.form.get("sb_problem")
        }
        data_list.append(data)
        return "<center><h2 style='color:green'>提交成功</h2></center>"

    return '''
<!DOCTYPE html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>土壤水分站周维护记录表</title>
<style>
body{max-width:700px;margin:30px auto;padding:20px;font-family:微软雅黑}
.item{margin:12px 0}
label{font-weight:bold;display:block;margin-bottom:5px}
input,textarea{width:100%;padding:10px;box-sizing:border-box}
button{background:#009966;color:white;padding:12px 20px;border:none;width:100%;font-size:16px}
</style>
<form method=post>
<h2>土壤水分站周维护记录表</h2>
<div class=item><label>设备型号</label><input name=设备型号 required></div>
<div class=item><label>维护人员</label><input name=维护人员 required></div>
<div class=item><label>维护时间</label><input name=维护时间 type=date required></div>

<h3 style="color:blue">观测场设施</h3>
<div class=item><label>维护内容</label><textarea name=gc_content></textarea></div>
<div class=item><label>维护结果</label><textarea name=gc_result></textarea></div>
<div class=item><label>存在问题</label><textarea name=gc_problem></textarea></div>

<h3 style="color:blue">设备运行情况</h3>
<div class=item><label>维护内容</label><textarea name=sb_content></textarea></div>
<div class=item><label>维护结果</label><textarea name=sb_result></textarea></div>
<div class=item><label>存在问题</label><textarea name=sb_problem></textarea></div>

<button type=submit>提交保存</button>
</form>
'''

# 本地拉数据接口
@app.route('/get_data')
def get_data():
    global data_list
    res = data_list.copy()
    data_list.clear()
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
