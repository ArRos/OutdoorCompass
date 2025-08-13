# OutdoorCompass Development Environment Setup Script
# Run this script from the project root directory

Write-Host "🚀 Setting up OutdoorCompass development environment..." -ForegroundColor Green

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "❌ Virtual environment not found. Please create it first:" -ForegroundColor Red
    Write-Host "   python -m venv .venv" -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment
Write-Host "📦 Activating virtual environment..." -ForegroundColor Blue
& ".venv\Scripts\Activate.ps1"

# Install backend dependencies
Write-Host "🐍 Installing Python dependencies..." -ForegroundColor Blue
pip install -r backend\requirements.txt

# Check if Node.js is installed
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js not found. Please install Node.js 18+ first." -ForegroundColor Red
    exit 1
}

# Install frontend dependencies
Write-Host "⚛️ Installing Node.js dependencies..." -ForegroundColor Blue
Set-Location frontend
npm install
Set-Location ..

# Start development services
Write-Host "🐳 Starting development services..." -ForegroundColor Blue
Set-Location docker
docker-compose -f docker-compose.dev.yml up -d
Set-Location ..

Write-Host "✅ Development environment setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Activate virtual environment: .venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "2. Start backend: cd backend && uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "3. Start frontend: cd frontend && npm run dev" -ForegroundColor White
Write-Host "4. Access services:" -ForegroundColor White
Write-Host "   - Backend: http://localhost:8000" -ForegroundColor White
Write-Host "   - Frontend: http://localhost:3000" -ForegroundColor White
Write-Host "   - MongoDB: localhost:27017" -ForegroundColor White
