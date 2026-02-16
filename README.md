# 🚀 API Gasolink

```{=html}
<p align="center">
```
`<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="80" />`{=html}
`<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" width="80" />`{=html}
`<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" width="80" />`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
Backend em `<b>`{=html}FastAPI`</b>`{=html} + Integração com
`<b>`{=html}Supabase`</b>`{=html}`<br>`{=html} Preparado para integração
com `<b>`{=html}React Native (TSX)`</b>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 🧱 Arquitetura do Projeto

    app/
    │
    ├── main.py
    ├── core/
    │   └── config.py
    ├── auth/
    │   └── dependencies.py
    ├── schemas/
    │   └── profile.py
    ├── routers/
    │   └── profile.py
    ├── services/
    │   └── profile_service.py

------------------------------------------------------------------------

## ⚙️ Tecnologias

-   🐍 Python
-   ⚡ FastAPI
-   🔐 JWT (python-jose)
-   🗄 Supabase
-   📱 React Native
-   🟦 TypeScript (TSX)

------------------------------------------------------------------------

## 🔐 Autenticação

A API utiliza JWT do Supabase.

Todas as rotas protegidas exigem:

Authorization: Bearer SEU_TOKEN

------------------------------------------------------------------------

## 📦 Instalação

### Clonar repositório

git clone https://github.com/CyberGabri/api-gasolink.git cd api-gasolink

### Criar ambiente virtual

python -m venv venv

Ativar no Windows:

venv`\Scripts`{=tex}`\activate`{=tex}

### Instalar dependências

pip install fastapi uvicorn python-jose\[cryptography\]
pydantic\[email\]

### Criar .env

SUPABASE_URL=sua_url SUPABASE_ANON_KEY=sua_anon_key

------------------------------------------------------------------------

## ▶️ Executar

uvicorn main:app --reload

Acesse: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 📌 Endpoints

-   POST /profiles/ → Criar perfil\
-   GET /profiles/ → Buscar perfil\
-   PUT /profiles/ → Atualizar perfil\
-   DELETE /profiles/ → Deletar perfil

------------------------------------------------------------------------

Feito com foco em arquitetura limpa e boas práticas 🚀
