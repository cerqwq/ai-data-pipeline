"""
AI Data Pipeline - AI数据管道工具
支持ETL设计、数据流、数据质量
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDataPipelineTools:
    """
    AI数据管道工具
    支持：ETL、数据流、数据质量
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_data_pipeline(self, source: str, destination: str, requirements: str) -> Dict:
        """设计数据管道"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计数据管道：

源：{source}
目标：{destination}
需求：{requirements}

请返回JSON格式：
{{
    "architecture": "架构",
    "stages": [
        {{"name": "阶段", "tool": "工具", "purpose": "目的"}}
    ],
    "schedule": "调度策略",
    "monitoring": "监控方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"pipeline": content}

    def generate_airflow_dag(self, pipeline_name: str, tasks: List[Dict]) -> str:
        """生成Airflow DAG"""
        if not self.client:
            return "LLM客户端未配置"

        tasks_text = json.dumps(tasks, ensure_ascii=False)

        prompt = f"""请生成Airflow DAG：

管道名：{pipeline_name}
任务：{tasks_text}

要求：
1. 完整的DAG定义
2. 任务依赖
3. 错误处理
4. 重试策略"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_spark_job(self, job_name: str, transformation: str) -> str:
        """生成Spark作业"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成Spark作业：

作业名：{job_name}
转换逻辑：{transformation}

要求：
1. PySpark代码
2. 性能优化
3. 错误处理
4. 日志记录"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def design_data_quality(self, data_type: str, rules: List[str]) -> Dict:
        """设计数据质量"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        rules_text = ", ".join(rules)

        prompt = f"""请为{data_type}设计数据质量方案：

规则：{rules_text}

请返回JSON格式：
{{
    "checks": [
        {{"name": "检查名", "rule": "规则", "action": "失败动作"}}
    ],
    "monitoring": "监控方案",
    "alerting": "告警策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"quality": content}

    def generate_dbt_model(self, model_name: str, transformation: str) -> str:
        """生成dbt模型"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成dbt模型：

模型名：{model_name}
转换逻辑：{transformation}

要求：
1. SQL模型
2. 测试定义
3. 文档字符串"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_data_warehouse(self, business_requirements: str) -> Dict:
        """设计数据仓库"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计数据仓库：

业务需求：{business_requirements}

请返回JSON格式：
{{
    "schema": "Schema设计",
    "tables": [
        {{"name": "表名", "type": "事实/维度", "grain": "粒度"}}
    ],
    "etl_strategy": "ETL策略",
    "tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"warehouse": content}


def create_tools(**kwargs) -> AIDataPipelineTools:
    """创建数据管道工具"""
    return AIDataPipelineTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Data Pipeline Tools")
    print()

    # 测试
    pipeline = tools.design_data_pipeline("MySQL", "数据仓库", "每日增量同步")
    print(json.dumps(pipeline, ensure_ascii=False, indent=2))
