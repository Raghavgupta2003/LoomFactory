# 🏭 Loom Factory - E-commerce Platform

**From Our Looms to Your Rooms** - A Django-based e-commerce platform for home textiles showcasing traditional Indian craftsmanship with modern design.

![Django](https://img.shields.io/badge/Django-5.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation Guide](#installation-guide)
- [Setup Instructions](#setup-instructions)
- [Admin Panel](#admin-panel)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

Loom Factory is a unique e-commerce platform built with Django that specializes in home textiles like bedsheets, curtains, and towels. The project serves as a college assignment showcasing a complete e-commerce solution with modern UI/UX design principles.

**Key Highlights:**
- Traditional Indian craftsmanship meets modern design
- Pan-India service for both retailers and wholesalers
- Responsive Bootstrap 5 interface
- Session-based shopping cart
- Advanced filtering system

## ✨ Features

### 🛒 E-commerce Features
- **Product Catalog** with categories and detailed product pages
- **Shopping Cart** with session management
- **Checkout System** with order processing
- **Search Functionality** across products
- **Advanced Filtering** by fabric type and weave type
- **Featured Products** carousel on homepage

### 🎨 Unique Features
- **Shop by Fabric** (Cotton, Silk, Linen, etc.)
- **Shop by Weave** (Handloom, Powerloom, Traditional, etc.)
- **Our Story Section** showcasing Indian loom heritage
- **Retail vs Wholesale** pricing display
- **Click-to-Call/WhatsApp** integration

### 👨‍💼 Admin Features
- Complete product management
- Category management
- Order tracking and management
- Cart monitoring
- Featured products management

### 📱 Design Features
- **Responsive Bootstrap 5** design
- **Textile-inspired color palette** (cream, beige, soft blue)
- **Modern card-based layout** with rounded borders and shadows
- **Mobile-first approach**

## 🛠 Technology Stack

### Backend
- **Python 3.8+**
- **Django 5.2**
- **SQLite** (Development)
- **Pillow** (Image processing)

### Frontend
- **HTML5, CSS3, JavaScript**
- **Bootstrap 5.3**
- **Font Awesome 6** (Icons)
- **Responsive Design**

### Development Tools
- **Virtual Environment**
- **Django Admin Interface**
- **Git for version control**

## 📥 Installation Guide

### Prerequisites
- Python 3.8 or higher
- Git
- Web browser

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Raghavgupta2003/LoomFactory.git
cd loomfactory
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install django pillow
```

#### 4. Database Setup
```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

#### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account:
- Username: (your choice)
- Email: (optional)
- Password: (your choice)

#### 6. Run Development Server
```bash
python manage.py runserver
```

#### 7. Access the Application
- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## ⚙️ Setup Instructions

### Adding Sample Data

#### 1. Login to Admin Panel
- Go to http://127.0.0.1:8000/admin/
- Use your superuser credentials

#### 2. Add Categories
1. Click on **Categories**
2. Click **ADD CATEGORY**
3. Add sample categories:
   - **Cotton Bedsheets** (Fabric: Cotton, Weave: Handloom)
   - **Silk Curtains** (Fabric: Silk, Weave: Powerloom)
   - **Linen Towels** (Fabric: Linen, Weave: Traditional)

#### 3. Add Products
1. Click on **Products**
2. Click **ADD PRODUCT**
3. Add sample products with:
   - Name, description, price
   - Category selection
   - Product images
   - Stock quantity
   - Fabric and weave types
   - Mark some as "featured" for homepage carousel

### Testing Functionalities

#### 1. Test User Features
- ✅ Browse categories and products
- ✅ Use search functionality
- ✅ Apply fabric/weave filters
- ✅ Add products to cart
- ✅ Complete checkout process
- ✅ Contact via phone/WhatsApp

#### 2. Test Admin Features
- ✅ Manage products and categories
- ✅ View and manage orders
- ✅ Monitor cart sessions
- ✅ Update product information

## 👨‍💼 Admin Panel Guide

### Accessing Admin Panel
```
URL: http://127.0.0.1:8000/admin/
Username: [Your superuser username]
Password: [Your superuser password]
```

### Admin Features

#### 1. Product Management
- Add/edit/delete products
- Set featured products
- Manage inventory stock
- Update pricing (retail and wholesale)

#### 2. Category Management
- Create product categories
- Set fabric and weave types
- Manage category images

#### 3. Order Management
- View all customer orders
- Track order details
- Monitor customer information

#### 4. Cart Monitoring
- View active cart sessions
- Monitor cart items
- Debug cart-related issues

## 📁 Project Structure

```
loomfactory/
├── loomfactory/                 # Project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── shop/                       # Main application
│   ├── migrations/             # Database migrations
│   ├── templates/shop/         # HTML templates
│   │   ├── base.html          # Base template
│   │   ├── home.html          # Homepage
│   │   ├── category.html      # Category page
│   │   ├── product_detail.html # Product details
│   │   ├── cart.html          # Shopping cart
│   │   ├── checkout.html      # Checkout page
│   │   ├── order_success.html # Order confirmation
│   │   ├── about.html         # About page
│   │   ├── contact.html       # Contact page
│   │   └── search_results.html # Search results
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Database models
│   ├── views.py               # Application views
│   ├── urls.py                # App URL routes
│   └── context_processors.py  # Context processors
├── media/                     # User-uploaded files
├── static/                    # Static files (CSS, JS, images)
├── db.sqlite3                 # Database (development)
└── manage.py                  # Django management script
```

## 🚀 Usage Guide

### For Customers
1. **Browse Products**: Visit homepage and explore categories
2. **Search**: Use search bar to find specific products
3. **Filter**: Use fabric and weave filters on category pages
4. **Add to Cart**: Click "Add to Cart" on product pages
5. **Checkout**: Proceed to checkout from cart page
6. **Contact**: Use click-to-call or WhatsApp for queries

### For Admin
1. **Manage Inventory**: Add/update products and categories
2. **Track Orders**: Monitor customer orders in admin panel
3. **Update Content**: Manage featured products and site content
4. **Analytics**: View cart and order statistics

## 📸 Screenshots

*(Add your screenshots here)*
- Homepage with featured products
- Category page with filters
- Product detail page
- Shopping cart
- Checkout process
- Admin panel interface

## 🐛 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# If port 8000 is busy, use another port
python manage.py runserver 8080
```

#### 2. Migration Errors
```bash
# Reset migrations if needed
python manage.py makemigrations
python manage.py migrate
```

#### 3. Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic
```

#### 4. Admin Panel Access Issues
```bash
# Create new superuser if locked out
python manage.py createsuperuser
```

### Debug Mode
The project runs in DEBUG mode by default. For production:
1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)

## 🤝 Contributing

We welcome contributions to improve Loom Factory! Here's how you can help:

### Reporting Issues
1. Check existing issues before creating new ones
2. Provide detailed description and steps to reproduce
3. Include screenshots if applicable

### Feature Requests
1. Describe the feature and its benefits
2. Explain how it aligns with project goals
3. Suggest implementation approach if possible

### Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit pull request with description

## 📄 License

This project is created for educational purposes as a college assignment. Feel free to use and modify for learning purposes.

## 📞 Support

For any queries or support:
- **Phone**: [+91 9314303874](tel:+919314303874)
- **WhatsApp**: [Message Us](https://wa.me/919314303874)
- **Email**: [info@loomfactory.com](mailto:raghavguptadanta@gmail.com)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome for icons
- Indian textile artisans and weavers

---

**Built with ❤️ for traditional Indian craftsmanship and modern e-commerce solutions.**

*Happy Coding! 🚀*