# Python 專案基礎骨架 (MyProject)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

這是一個遵循現代 Python 開發最佳實踐的標準專案骨架。本專案採用了模組化結構設計，並整合了單元測試、程式碼風格規範與現代專案管理設定，適合做為任何新型 Python 應用程式與服務的起步基礎。

---

## 🌟 特色

* 📦 **標準目錄結構**：使用標準的 `src/` 與 `tests/` 結構，實現源碼與測試代碼的完全分離。
* ⚙️ **現代化專案配置**：遵循 PEP 621 標準，使用 `pyproject.toml` 管理專案中繼資料、建置系統與測試配置。
* 🧪 **完整測試框架**：整合了 `pytest` 測試工具鏈，支援自動測試路徑搜尋與測試覆蓋率分析。
* 🛠️ **強健的開發輔助**：內建標準的 `.gitignore` 以及精緻的模組範例。

---

## 📁 專案目錄結構

本專案的目錄樹如下所示：

```text
myProject/
├── .gitignore               # Git 忽略設定檔
├── pyproject.toml           # 現代 Python 專案中繼設定 (PEP 621)
├── README.md                # 專案說明文件 (Traditional Chinese)
├── requirements.txt         # 開發與執行期相依套件清單
├── src/                     # 專案原始碼目錄
│   ├── main.py              # 應用程式主要進入點 (CLI 介面)
│   └── utils.py             # 通用工具函式庫 (包含型別註記與日誌工具)
└── tests/                   # 單元測試目錄
    ├── test_main.py         # 針對 main.py 的測試案例
    └── test_utils.py        # 針對 utils.py 的測試案例
```

---

## 🚀 快速上手

### 1. 環境建置

建議使用 Python 3.8 以上版本，並搭配 `venv` 建立虛擬環境：

```bash
# 複製/進入專案資料夾
cd myProject

# 建立虛擬環境 (以 Windows 為例)
python -m venv .venv

# 啟用虛擬環境
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Linux/macOS:
source .venv/bin/activate
```

### 2. 安裝相依套件

在虛擬環境啟用後，安裝專案所需的相依套件：

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 執行主程式

主程式提供一個優雅的命令列介面 (CLI)，您可以直接執行：

```bash
# 預設執行 (顯示歡迎訊息)
python src/main.py

# 攜帶自訂參數執行
python src/main.py --name Antigravity

# 查看所有支援的參數說明
python src/main.py --help
```

---

## 🧪 執行測試

本專案使用 `pytest` 進行自動化單元測試。

### 執行所有測試

```bash
pytest
```

### 執行測試並生成詳細報告

```bash
pytest -v
```

### 執行測試並計算覆蓋率

```bash
pytest --cov=src tests/
```

---

## 💡 開發指南

* **程式碼風格**：本專案程式碼皆撰寫了完整的**型別提示 (Type Hints)**與 **Docstrings (Google 風格)**，以提昇可讀性與 IDE 自動補全體驗。
* **新增模組**：若需新增功能，請在 `src/` 目錄下建立對應的 `.py` 檔案，並在 `tests/` 中建立以 `test_` 開頭的測試檔案，以維持高測試覆蓋率。
