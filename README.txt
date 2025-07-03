# Istruzioni per deploy su Fly.io

## 1. Installa la CLI Fly.io
curl -L https://fly.io/install.sh | sh

## 2. Login o signup
fly auth signup
fly auth login

## 3. Inizializza progetto
fly launch
# Scegli nome app e regione (es. fra)

## 4. Deploy
fly deploy

## 5. App live su:
https://NOME-APP.fly.dev
