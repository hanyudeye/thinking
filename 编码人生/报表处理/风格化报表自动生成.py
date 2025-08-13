# 代码执行环节
def main(start_date: str, end_date: str, text: list) -> dict:
    import csv, io, json
    from datetime import datetime

    # 连接文本行
    content = "\n".join(text)
    reader = csv.DictReader(io.StringIO(content), delimiter='|')

    sd = datetime.strptime(start_date, "%Y-%m-%d").date()
    ed = datetime.strptime(end_date,   "%Y-%m-%d").date()

    total_rows = 0
    filtered = []

    for row in reader:
        total_rows += 1

        # 清洗字段名可能含空格
        ct_raw = row.get("创建时间") or row.get(" 创建时间 ") or ""
        ct_raw = ct_raw.strip()
        if not ct_raw:
            continue

        # 解析多种时间格式
        ct = None
        for fmt in ("%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M",
                    "%Y/%m/%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
            try:
                ct = datetime.strptime(ct_raw, fmt)
                break
            except:
                pass
        if not ct:
            continue

        # 筛选时间范围
        if sd <= ct.date() <= ed:
            filtered.append(row)

    output = {
        "total_rows": total_rows,
        "total_filtered": len(filtered),
        "filtered": filtered
    }

    return {"result": json.dumps(output, ensure_ascii=False)}


# LLM提示词
下面有一段 JSON 输出，变量名为{{#1753088011989.result#}}，结构如下：
- total_rows：原始行数
- total_filtered：符合时间范围的记录总数
- filtered：数组，每个元素是一行解析后的字典，包含列字段

请直接生成一段markdown格式周报：
1. 将每一行的标题、备注进行总结，稍微扩展，保证总体意思清晰不啰嗦，放在下方的分类中（项目支持、TMS、成本、日常、其他）；
2. 序号、条理清晰。

示例输出格式：

## 周报摘要
- 总行数：...
- 筛选数：...

# 运维部2025W28

# 项目支持

## 网关

*   复用已有的云效maven仓库，当前规则 
*   开发过程涉及基础设置，无费用新增。可复用，比如已有的云效xxx仓库
*   “绕圈”，不建议。如堡垒机、监控等，流量走一遍阿里云出境再到AWS
*   有费用产生，自行搞定。特殊情况再讨论
*   参与周五AWS workshop，明确需求是，网关团队注意兜底措施，最关键数据库跨云、跨区域、跨账号备份。**厂商答复支持**，待业务稳定后增加

## DMP
*   rocketmq5.0原价使用一年（4.0版本xxx折），申请折扣中，尝试追索些代金券
*   MSE升级完成，未发现异常
*   AU开源版nacos已接入ops平台  
*   kubernetes版本加白，列为技改待办。风险、收益详见文档 。集群承载应用，连接基础设施。和程序框架类似，谨慎升级
# TMS
# 成本
# 日常
# 其他
