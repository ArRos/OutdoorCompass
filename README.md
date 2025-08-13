# OutdoorCompass

A modern outdoor activity planning and navigation application built with FastAPI, React, and MongoDB.
Note: Cursor will be used as the main editor for this project, with caution since the goal is also to learn along the way.

## 🏗️ Project Structure

```
OutdoorCompass/
├── .venv/                    # Python virtual environment
├── backend/                  # FastAPI backend
│   ├── app/                 # Main application code
│   │   ├── api/             # API routes
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   ├── database/        # MongoDB operations
│   │   └── utils/           # Helper functions
│   ├── tests/               # Backend tests
│   └── requirements.txt     # Python dependencies
├── frontend/                 # React/Next.js frontend
│   ├── src/                 # Source code
│   └── public/              # Static assets
├── docker/                   # Docker configurations
│   ├── docker-compose.yml   # Production setup
│   └── docker-compose.dev.yml # Development setup
├── .github/workflows/        # CI/CD workflows
└── docs/                     # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- MongoDB (or use Docker)

### Development Setup

1. **Clone and setup virtual environment:**
   ```bash
   git clone <your-repo>
   cd OutdoorCompass
   .venv\Scripts\activate  # Windows
   pip install -r backend/requirements.txt
   ```

2. **Start development services:**
   ```bash
   cd docker
   docker-compose -f docker-compose.dev.yml up -d
   ```

3. **Run backend (in virtual environment):**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Run frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### Production Setup

```bash
cd docker
docker-compose up -d
```

## 🐳 Docker Services

- **Backend**: FastAPI on port 8000
- **Frontend**: Next.js on port 3000
- **MongoDB**: Database on port 27017
- **Nginx**: Reverse proxy on port 80/443

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📚 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 Configuration

Environment variables can be set in `.env` files or Docker Compose:
- `MONGODB_URL`: MongoDB connection string
- `ENVIRONMENT`: `development` or `production`
- `DEBUG`: Enable debug mode

## 🚀 Deployment

The project includes GitHub Actions workflows for:
- Automated testing on push/PR
- Production deployment on main branch

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
