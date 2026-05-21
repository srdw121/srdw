from flask import Flask, request, jsonify
app = Flask(__name__)

data_list = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = {
            "设备型号": request.form.get("设备型号"),
            "维护人员": request.form.get("维护人员"),
            "维护时间": request.form.get("维护时间"),
            "gc_result": request.form.get("gc_result"),
            "gc_problem": request.form.get("gc_problem"),
            "sb_result": request.form.get("sb_result"),
            "sb_problem": request.form.get("sb_problem"),
            "lj_result": request.form.get("lj_result"),
            "lj_problem": request.form.get("lj_problem"),
            "gd_result": request.form.get("gd_result"),
            "gd_problem": request.form.get("gd_problem"),
            "tx_result": request.form.get("tx_result"),
            "tx_problem": request.form.get("tx_problem"),
            "fs_result": request.form.get("fs_result"),
            "fs_problem": request.form.get("fs_problem"),
            "sy_result": request.form.get("sy_result"),
            "sy_problem": request.form.get("sy_problem"),
            "ss_result": request.form.get("ss_result"),
            "ss_problem": request.form.get("ss_problem"),
            "gy_result": request.form.get("gy_result"),
            "gy_problem": request.form.get("gy_problem"),
            "fl_result": request.form.get("fl_result"),
            "fl_problem": request.form.get("fl_problem")
        }
        data_list.append(data)
        return "<center><h2 style='color:green'>提交成功！</h2><p>3秒后自动返回</p><script>setTimeout(function(){window.location.href='/'},3000)</script></center>"

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
.section{margin:25px 0;padding:15px;border:1px solid #eee;border-radius:8px}
.section-title{font-size:18px;font-weight:bold;color:#2980b9;margin-bottom:15px}
</style>
<form method=post>
<h2 style="text-align:center;margin-bottom:30px">土壤水分站周维护记录表</h2>

<div class="section">
<div class="section-title">基础信息</div>
<div class=item><label>设备型号</label><input name=设备型号 required></div>
<div class=item><label>维护人员</label><input name=维护人员 required></div>
<div class=item><label>维护时间</label><input name=维护时间 type=date required></div>
</div>

<div class="section">
<div class="section-title">维护检查项（只填结果和问题）</div>

<div class=item><label>1. 观测场设施 - 维护结果</label><textarea name=gc_result></textarea></div>
<div class=item><label>1. 观测场设施 - 存在问题和处理情况</label><textarea name=gc_problem></textarea></div>

<div class=item><label>2. 设备运行情况 - 维护结果</label><textarea name=sb_result></textarea></div>
<div class=item><label>2. 设备运行情况 - 存在问题和处理情况</label><textarea name=sb_problem></textarea></div>

<div class=item><label>3. 各系统之间连接情况 - 维护结果</label><textarea name=lj_result></textarea></div>
<div class=item><label>3. 各系统之间连接情况 - 存在问题和处理情况</label><textarea name=lj_problem></textarea></div>

<div class=item><label>4. 供电情况 - 维护结果</label><textarea name=gd_result></textarea></div>
<div class=item><label>4. 供电情况 - 存在问题和处理情况</label><textarea name=gd_problem></textarea></div>

<div class=item><label>5. 通讯情况 - 维护结果</label><textarea name=tx_result></textarea></div>
<div class=item><label>5. 通讯情况 - 存在问题和处理情况</label><textarea name=tx_problem></textarea></div>

<div class=item><label>6. 传感器防水情况 - 维护结果</label><textarea name=fs_result></textarea></div>
<div class=item><label>6. 传感器防水情况 - 存在问题和处理情况</label><textarea name=fs_problem></textarea></div>

<div class=item><label>7. 前一个月采集数据是否正常 - 维护结果</label><textarea name=sy_result></textarea></div>
<div class=item><label>7. 前一个月采集数据是否正常 - 存在问题和处理情况</label><textarea name=sy_problem></textarea></div>

<div class=item><label>8. 实时观测数据是否正常 - 维护结果</label><textarea name=ss_result></textarea></div>
<div class=item><label>8. 实时观测数据是否正常 - 存在问题和处理情况</label><textarea name=ss_problem></textarea></div>

<div class=item><label>9. 自动土壤水分观测仪是否正常 - 维护结果</label><textarea name=gy_result></textarea></div>
<div class=item><label>9. 自动土壤水分观测仪是否正常 - 存在问题和处理情况</label><textarea name=gy_problem></textarea></div>

<div class=item><label>10. 防雷设施检测 - 维护结果</label><textarea name=fl_result></textarea></div>
<div class=item><label>10. 防雷设施检测 - 存在问题和处理情况</label><textarea name=fl_problem></textarea></div>
</div>

<button type=submit>提交保存</button>
</form>
'''

@app.route('/get_data')
def get_data():
    global data_list
    res = data_list.copy()
    data_list.clear()
    return jsonify(res)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
