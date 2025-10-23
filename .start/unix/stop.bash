#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${RED}"
echo "================================================"
echo "   Parando Frontend e Backend"
echo "================================================"
echo -e "${NC}"

echo "Procurando processos do Backend (porta 5000)..."
lsof -ti:5000 | xargs kill -9 2>/dev/null

echo ""
echo "Procurando processos do Frontend (porta 4200)..."
lsof -ti:4200 | xargs kill -9 2>/dev/null

echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}   Serviços Parados com Sucesso!${NC}"
echo -e "${GREEN}================================================${NC}"