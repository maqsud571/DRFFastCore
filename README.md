# 🚀 DRFFastCore — Django + FastAPI + PostgreSQL + Docker

**Write only one command and take already prepared Microservice and Build your dream projects.**

Ushbu repository tayyor **Hybrid Microservices Architecture** bo‘lib, Django va FastAPI bitta PostgreSQL ustida birga ishlaydi. Docker Compose orqali butun projectni **bitta komanda bilan** ishga tushirishingiz mumkin.

# 📦 Texnologiyalar

* **Django (DRF)** — Admin panel, model, migration, asosiy backend
* **FastAPI** — High-performance API service
* **PostgreSQL** — Shared database (ikkala service uchun umumiy)
* **Docker + Docker Compose** — One-command setup
* **Production-ready architecture** — volumes, env, lightweight images

# 📁 Project Structure
```
📦 DRFFastCore/
├── str/
│   ├── Core/
│   ├── manage.py
│   ├── apps/...
│   ├── Api/
│   ├── main.py
│   ├── User/
│   └── models/...
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md

```
# 🚀 One-command Start
Projectni ishga tushirish uchun **bitta komandani** bajarish kifoya:

```bash
docker compose up --build -d
```

Bu avtomatik ishga tushiradi:

* PostgreSQL (`datadb`)
* Django (`django-app`)
* FastAPI (`fast-api`)

---


# 🧭 To‘liq Ketma-ketlik (Detailed Setup)

Agar development jarayonida qo‘lda ishlatmoqchi bo‘lsangiz:

### 1️⃣ Repositoryni klon qiling

```bash
git clone https://github.com/maqsud571/DRFFastCore.git
cd DRFFastCore
```

### 2️⃣ `.env` faylni sozlang (root’da turishi shart)

```
POSTGRES_DB=yourdb
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpass

DB_NAME=yourdbname
DB_USER=youruser
DB_PASS=yourpass
DB_HOST=yourhost
DB_PORT=yourport

```

### 3️⃣ Bitta komanda bilan ishga tushirish

```bash
docker compose up --build -d
```

### 4️⃣ Django migratsiyalar (agar automate qilinmagan bo‘lsa)

```bash
docker compose run --rm django-app python3 manage.py makemigrations
docker compose run --rm django-app python3 manage.py migrate
docker compose run --rm django-app python3 manage.py 
createsuperuser
```
### 5️⃣ Container holatini tekshirish

```bash
docker compose ps
```

### 6️⃣ Loglar

```bash
docker compose logs -f fast-api
```

### 7️⃣ Local URL’lar

* FastAPI → [http://localhost:9999/docs](http://localhost:9999/docs)
* Django → [http://localhost:8001/](http://localhost:8001/)

### 8️⃣ Tozalash (Postgres volume bilan birga)

```bash
docker compose down -v
```
---

# 🟦 Django (Core Backend)

Django quyidagi vazifalarni bajaradi:

* Model yaratish
* Migration orqali table yaratish
* Admin panel
* Asosiy ma’lumotlar strukturasini boshqarish
---


# 🟩 FastAPI (High-performance Microservice)

FastAPI quyidagilarni bajaradi:

* Django backend bilan parallel ishlaydi.
* Asinxron (async) endpointlar orqali tezkor ma'lumot olish/jo'natish.
* Ma'lumotlarni saqlash (xizmatlar) orqali boshqaradi.
* Har bir modul (elementlar, foydalanuvchilar) o'z API endpointiga ega
---
# 🗄 PostgreSQL (Shared DB)

* Django va FastAPI uchun umumiy database
* Docker volume orqali saqlanadi
* Localda TablePlus yoki DBeaver orqali ulanishingiz mumkin

---
# 🧪 Quick Checks

* Postgres ishlayaptimi?

```bash
docker compose ps
```

* FastAPI to'g'ri host bilan ishlayaptimi?

```yaml
command: uvicorn api.main:app --host 0.0.0.0 --port 9000
```

* `.env` ignor qilinyaptimi?

```bash
git rm --cached .env
```
# 🎉 Build your dream microservices.

Bitta komanda bilan microservice tayyor:

```bash
docker compose up --build -d
```
