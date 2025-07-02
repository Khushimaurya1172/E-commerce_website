# 🌸 AromaAura — Perfume E-Commerce Website (Django)

AromaAura is a beautiful and minimal perfume e-commerce website built using **Django (Python)**. It offers a smooth product browsing experience, cart functionality, and a simple checkout — all wrapped in a pink & teal luxury feel.

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap (CDN)
- **Backend**: Python 3, Django Framework
- **Database**: SQLite (default)
- **Tools**: Django Admin, Django ORM, Django Templates, Session Storage

---

## ✨ Features

- 🏠 Home page with all perfume products  
- 🔍 Product detail view  
- 🛒 Add to cart & remove from cart (session-based)  
- 💳 Checkout form with success page  
- 🧾 Admin dashboard for product management  
- 🎨 Beautiful pink + teal styling for a premium brand feel  

---

## 📸 Screenshots

> 📷 Add images of your home page, cart page, checkout page here

---

## 🚀 How to Run This Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/aromaaura-ecommerce.git
cd aromaaura-ecommerce
python -m venv env
env\Scripts\activate   # For Windows
# source env/bin/activate   # For Mac/Linux
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
