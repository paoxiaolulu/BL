from httprunner import HttpRunner

runner = HttpRunner()
runner.run('/Users/air/Documents/BL/testcases/39_礼品库_我的礼品库.yaml')   # 运行单个测试
# runner.run('/Users/air/Documents/BL/testcases')  # 运行测试集合
summary = runner.summary
runner.gen_html_report(
    html_report_name="v6接口测试"
)
