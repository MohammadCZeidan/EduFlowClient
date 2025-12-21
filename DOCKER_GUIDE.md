# 🐳 Docker Quick Reference for EduFlow

## Prerequisites

Before running Docker commands, make sure:
1. ✅ Docker Desktop is installed and running
2. ✅ Backend `.env` file is configured with Airtable credentials
3. ✅ You're in the `eduflowClient` directory

## Quick Commands

### 🚀 Start Application

```powershell
# Interactive startup (Recommended for Windows)
.\docker-start.ps1

# Full stack (Frontend + Backend + n8n)
docker-compose --profile full up --build -d

# Frontend + Backend only
docker-compose up --build -d

# Frontend only (backend running locally)
docker-compose -f docker-compose.simple.yml up --build -d
```

### 🛑 Stop Application

```powershell
# Stop all services
docker-compose down

# Stop full stack (with n8n)
docker-compose --profile full down

# Stop frontend only
docker-compose -f docker-compose.simple.yml down

# Stop and remove volumes
docker-compose down -v
```

### 📊 View Status

```powershell
# List running containers
docker ps

# View all containers (including stopped)
docker ps -a

# Check service status
docker-compose ps

# View container health
docker inspect eduflow-frontend | Select-String "Health"
docker inspect eduflow-backend | Select-String "Health"
```

### 📝 View Logs

```powershell
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f frontend
docker-compose logs -f backend
docker-compose logs -f n8n

# Last 100 lines
docker-compose logs --tail=100 frontend

# Since specific time
docker-compose logs --since 10m frontend
```

### 🔄 Restart Services

```powershell
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart frontend
docker-compose restart backend

# Rebuild and restart
docker-compose up --build -d frontend
```

### 🧹 Cleanup

```powershell
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything unused (careful!)
docker system prune -a
```

### 🔧 Debugging

```powershell
# Execute command in running container
docker exec -it eduflow-frontend /bin/bash
docker exec -it eduflow-backend /bin/bash

# View container details
docker inspect eduflow-frontend

# Check resource usage
docker stats

# Test backend health
curl http://localhost:8000/health

# Test frontend health
curl http://localhost:8501/_stcore/health
```

## Access URLs

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:8501 | Streamlit dashboard |
| **Backend API** | http://localhost:8000 | FastAPI server |
| **API Docs** | http://localhost:8000/docs | Swagger UI |
| **n8n** | http://localhost:5678 | Automation (if running) |

## Common Issues & Solutions

### Issue: "Cannot connect to Docker daemon"
**Solution:**
```powershell
# Start Docker Desktop
# Then verify:
docker info
```

### Issue: "Port already in use"
**Solution:**
```powershell
# Find process using port
Get-NetTCPConnection -LocalPort 8501

# Stop containers
docker-compose down

# Or change port in docker-compose.yml
```

### Issue: "Container health check failing"
**Solution:**
```powershell
# View logs
docker-compose logs frontend

# Check backend connectivity
docker exec -it eduflow-frontend curl http://backend:8000/health

# Restart service
docker-compose restart frontend
```

### Issue: "Backend shows Airtable errors"
**Solution:**
1. Check `../eduflowServer/backend/.env` has correct credentials
2. Restart backend:
   ```powershell
   docker-compose restart backend
   ```

### Issue: "Changes not reflecting"
**Solution:**
```powershell
# Rebuild containers
docker-compose up --build -d

# Force rebuild
docker-compose build --no-cache
docker-compose up -d
```

## Environment Variables

### Frontend (.env)
```env
BACKEND_URL=http://localhost:8000  # For local backend
# OR
BACKEND_URL=http://backend:8000    # For Docker backend
```

### Backend (.env in ../eduflowServer/backend/)
```env
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_base_id_here
JWT_SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:8501,http://frontend:8501
```

## Docker Compose Files

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Full stack or Frontend+Backend |
| `docker-compose.simple.yml` | Frontend only (backend local) |

## Performance Tips

1. **Use detached mode** (`-d`) to run in background
2. **Limit logs** with `--tail` to avoid memory issues
3. **Prune regularly** to free disk space
4. **Use BuildKit** for faster builds:
   ```powershell
   $env:DOCKER_BUILDKIT=1
   docker-compose build
   ```

## Development Workflow

```powershell
# 1. Start services in detached mode
docker-compose up -d

# 2. Watch logs in separate terminal
docker-compose logs -f

# 3. Make code changes (auto-reload for backend)

# 4. Rebuild if needed (frontend changes)
docker-compose up --build -d frontend

# 5. Stop when done
docker-compose down
```

## Production Deployment

For production, use environment-specific compose file:

```powershell
# Use production config
docker-compose -f docker-compose.prod.yml up -d

# With specific env file
docker-compose --env-file .env.production up -d
```

## Useful Aliases (Add to PowerShell Profile)

```powershell
# $PROFILE = C:\Users\<user>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1

function dc { docker-compose $args }
function dcu { docker-compose up -d $args }
function dcd { docker-compose down $args }
function dcl { docker-compose logs -f $args }
function dps { docker ps $args }
```

Then use:
```powershell
dcu --build      # Instead of: docker-compose up --build -d
dcl frontend     # Instead of: docker-compose logs -f frontend
dcd              # Instead of: docker-compose down
```
