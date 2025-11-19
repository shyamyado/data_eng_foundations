# Data Engineering Foundations Sandbox

A clean, minimal sandbox for experimenting with data-engineering concepts locally. Everything starts with a single command.

## 🚀 Quick Start

```bash
docker compose up -d
```

* **First start:** ~40 seconds
* **Subsequent restarts:** < 5 seconds

---

## 🧩 Services

| Service          | URL                                            | Credentials                                  |
| ---------------- | ---------------------------------------------- | -------------------------------------------- |
| **ClickHouse**   | [http://localhost:8123](http://localhost:8123) | DB: `mydb` · User: `myuser` · Pass: `mypass` |
| **Spark Master** | [http://localhost:9090](http://localhost:9090) | —                                            |
| **Spark Worker** | [http://localhost:9091](http://localhost:9091) | —                                            |

---

## 🛠️ Connecting via DBeaver

Use the ClickHouse HTTP interface:

```
Host: localhost
Port: 8123
Database: mydb
Username: myuser
Password: mypass
```

---

## 📂 Data Layout

* **Raw input files** → `data/raw/`
  *(git‑ignored — place any datasets here)*

* **ClickHouse storage** → `data/clickhouse/`
  *(auto‑created, git‑ignored, persists across restarts)*

---

## 🎯 Purpose

A stable, zero‑noise environment for learning, testing, and prototyping modern data‑engineering workflows.

Enjoy the cleanest possible local data‑engineering playground!
