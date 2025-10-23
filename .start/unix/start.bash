#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "================================================"
echo "   Iniciando Frontend e Backend Separadamente"
echo "================================================"
echo -e "${NC}"

# Verificar se o backend está pronto
echo -e "${BLUE}[1/3] Verificando ambiente do Backend...${NC}"
if [ ! -d ".venv" ]; then
    echo -e "${RED}ERRO: Ambiente virtual não encontrado!${NC}"
    echo "Execute: python -m venv .venv"
    echo "         source .venv/bin/activate"
    echo "         pip install -r requirements.txt"
    exit 1
fi

# Verificar se o frontend está pronto
echo -e "${BLUE}[2/3] Verificando ambiente do Frontend...${NC}"
if [ ! -d "frontend/node_modules" ]; then
    echo -e "${YELLOW}AVISO: node_modules não encontrado!${NC}"
    echo "Instalando dependências..."
    cd frontend
    npm install
    cd ..
fi

echo -e "${BLUE}[3/3] Iniciando serviços...${NC}"
echo ""

# Detectar sistema operacional
OS="$(uname -s)"

case "${OS}" in
    Linux*)
        # Linux - usar gnome-terminal ou xterm
        if command -v gnome-terminal &> /dev/null; then
            gnome-terminal --title="Backend - FastAPI (Port 5000)" -- bash -c "source .venv/bin/activate && echo 'Iniciando Backend...' && uvicorn backend.main:app --host 0.0.0.0 --port 5000 --reload; exec bash"
            sleep 2
            gnome-terminal --title="Frontend - Angular (Port 4200)" -- bash -c "cd frontend && echo 'Iniciando Frontend...' && npm start; exec bash"
        elif command -v xterm &> /dev/null; then
            xterm -title "Backend - FastAPI (Port 5000)" -e "source .venv/bin/activate && uvicorn backend.main:app --host 0.0.0.0 --port 5000 --reload; bash" &
            sleep 2
            xterm -title "Frontend - Angular (Port 4200)" -e "cd frontend && npm start; bash" &
        else
            echo -e "${RED}Erro: gnome-terminal ou xterm não encontrado!${NC}"
            exit 1
        fi
        ;;
    
    Darwin*)
        # macOS - usar Terminal.app
        osascript -e 'tell application "Terminal" to do script "cd '"$(pwd)"' && source .venv/bin/activate && echo \"Iniciando Backend...\" && uvicorn backend.main:app --host 0.0.0.0 --port 5000 --reload"'
        sleep 2
        osascript -e 'tell application "Terminal" to do script "cd '"$(pwd)/frontend"' && echo \"Iniciando Frontend...\" && npm start"'
        ;;
    
    *)
        echo -e "${RED}Sistema operacional não suportado: ${OS}${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}   Serviços Iniciados com Sucesso!${NC}"
echo -e "${GREEN}================================================${NC}"
echo ""
echo -e "${BLUE}Backend:${NC}  http://localhost:5000"
echo -e "${BLUE}Frontend:${NC} http://localhost:4200"
echo -e "${BLUE}Docs API:${NC} http://localhost:5000/docs"
echo ""
echo -e "${YELLOW}Para parar os serviços, feche as janelas abertas.${NC}"