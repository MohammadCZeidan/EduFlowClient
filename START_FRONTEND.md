# Starting the EduFlow Frontend

## Option 1: Direct Streamlit (Recommended for Development)

1. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements-frontend.txt
   ```

2. **Start the Streamlit app**:
   ```bash
   streamlit run frontend/app.py
   ```
   
   Or with specific port:
   ```bash
   streamlit run frontend/app.py --server.port=8501
   ```

3. **Access the application**:
   - Open your browser and go to: `http://localhost:8501`
   - The landing page should appear

## Option 2: Using Docker

1. **Build and start all services**:
   ```bash
   docker-compose up --build
   ```

2. **Or start only the frontend**:
   ```bash
   docker-compose up frontend
   ```

3. **Access the application**:
   - Frontend: `http://localhost:8501`

## Quick Start Commands

### Windows PowerShell:
```powershell
# Navigate to project root
cd C:\Users\user\OneDrive\Desktop\eduflowClient

# Install dependencies
python -m pip install -r requirements-frontend.txt

# Start Streamlit
python -m streamlit run frontend/app.py --server.port=8501
```

### Linux/Mac:
```bash
# Navigate to project root
cd ~/eduflowClient

# Install dependencies
pip install -r requirements-frontend.txt

# Start Streamlit
streamlit run frontend/app.py --server.port=8501
```

## Troubleshooting

- **Port already in use**: Change the port with `--server.port=8502`
- **Module not found**: Make sure you're in the project root directory
- **Dependencies missing**: Run `pip install -r requirements-frontend.txt`

## Pages Available

- Landing Page: `http://localhost:8501/` (default)
- Login Page: `http://localhost:8501/login`
- Dashboard: `http://localhost:8501/dashboard` (after login)
- Courses: `http://localhost:8501/courses` (after login)
- Add Course: `http://localhost:8501/add_course` (after login)
- View Course: `http://localhost:8501/view_course` (after login)
- Edit Course: `http://localhost:8501/edit_course` (after login)

