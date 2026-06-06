# 🔄 AI Data Pipeline

AI数据管道工具，支持ETL设计、数据流、数据质量。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔄 数据管道设计
- 📊 Airflow DAG生成
- ⚡ Spark作业生成
- ✅ 数据质量设计
- 📦 dbt模型生成
- 🏗️ 数据仓库设计

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_data_pipeline import create_tools

tools = create_tools()

# 数据管道
pipeline = tools.design_data_pipeline("MySQL", "数据仓库", "每日增量同步")

# Airflow DAG
dag = tools.generate_airflow_dag("etl_pipeline", tasks)

# Spark作业
spark = tools.generate_spark_job("数据清洗", "去重、填充空值")

# 数据质量
quality = tools.design_data_quality("用户数据", ["完整性", "唯一性"])

# dbt模型
dbt = tools.generate_dbt_model("dim_users", "用户维度表")

# 数据仓库
warehouse = tools.design_data_warehouse("电商数据分析")
```

## 📁 项目结构

```
ai-data-pipeline/
├── tools.py       # 数据管道工具核心
└── README.md
```

## 📄 许可证

MIT License
