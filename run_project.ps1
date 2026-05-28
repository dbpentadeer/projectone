# 輕鬆啟動 Flask 專案的 PowerShell 腳本
# 把此檔案放在專案根目錄 (myProject) 中，然後在 PowerShell 執行 `.un_project.ps1`

# 1. 進入專案目錄 (若已在此目錄可略過)
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectRoot

# 2. 啟動虛擬環境 (如果尚未建立，請先執行 python -m venv .venv)
$venvActivate = Join-Path $projectRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    Write-Host "Activating virtual environment..."
    & $venvActivate
} else {
    Write-Warning "Virtual environment not found. Creating one now..."
    python -m venv .venv
    & $venvActivate
}

# 3. 安裝需求套件（只在第一次或有變更時執行）
if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Warning "requirements.txt not found. Skipping dependency installation."
}

# 4. 啟動 Flask 伺服器（使用預設的 19191 埠）
Write-Host "Starting Flask server..."
python src\main.py
