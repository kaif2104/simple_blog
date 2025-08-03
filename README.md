# Simple Blog System - Django

A full-featured blog web application built with Django, featuring user authentication, CRUD operations for blog posts, and a modern Bootstrap UI.

## Features

- **User Authentication**: Registration, login, and logout with flash messages
- **Blog Management**: Create, read, update, and delete blog posts
- **Authorization**: Users can only edit/delete their own posts
- **Responsive UI**: Bootstrap-powered responsive design
- **Flash Messages**: User feedback for all actions
- **Modern Design**: Clean, mobile-friendly interface

## Tech Stack

- **Backend**: Python, Django 5.2.4
- **Frontend**: HTML, CSS, Bootstrap 5.3.2
- **Database**: SQLite (default)
- **Authentication**: Django's built-in authentication system

## Project Structure

```
blog_project/
├── blog/                   # Main blog app
│   ├── static/
│   │   └── blog/
│   │       └── style.css   # Custom CSS styles
│   ├── templates/          # HTML templates
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   ├── base.html       # Base template with navbar
│   │   ├── home.html       # Homepage with post list
│   │   ├── post_detail.html
│   │   ├── post_new.html
│   │   ├── post_edit.html
│   │   └── post_delete.html
│   ├── models.py           # Post model
│   ├── views.py            # All view logic
│   └── urls.py             # App URL patterns
├── blog_project/           # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation & Setup

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd blog_project

# Or download and extract the project files
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Usage

### For Visitors (Not Logged In)
- View the welcome page with call-to-action buttons
- Browse all published blog posts
- Read individual blog posts
- Sign up for a new account
- Log in to existing account

### For Authenticated Users
- Create new blog posts
- Edit their own posts
- Delete their own posts
- View personalized dashboard
- Receive feedback messages for all actions

## Key Features Implemented

### ✅ Task 1: Project Setup
- Django project initialized with proper structure
- Virtual environment configured
- Git repository ready

### ✅ Task 2: Home Page
- Responsive homepage with post listings
- Navigation bar with authentication links
- Welcome section for new visitors

### ✅ Task 3: User Registration
- Signup form with username, email, password
- Password hashing and validation
- Success messages and redirects

### ✅ Task 4: User Login & Logout
- Secure authentication system
- Session management
- Custom login/logout views with flash messages

### ✅ Task 5: Create Blog Post
- Post creation form (title and content)
- User association with posts
- Form validation and success feedback

### ✅ Task 6: View Blog Posts
- List view with post summaries
- Individual post detail pages
- Author and date information
- "Read more" functionality

### ✅ Task 7: Edit and Delete Posts
- Authorization checks (only post authors)
- Edit form with pre-populated data
- Delete confirmation with warning
- Success/error messages

### ✅ Task 8: UI Enhancement
- Bootstrap 5.3.2 integration
- Template inheritance with `base.html`
- Responsive navbar with user-specific links
- Custom CSS for enhanced styling
- Mobile-friendly design

### ✅ Task 9: Flash Messages
- Success messages for all user actions
- Error handling and feedback
- Bootstrap-styled alert components
- Auto-dismissible notifications

## Database Schema

### Post Model
- `title`: CharField (max 200 characters)
- `content`: TextField (unlimited text)
- `author`: ForeignKey to User model
- `created_at`: DateTimeField (auto-generated)

### User Model
- Uses Django's built-in User model
- Username, email, password fields
- Built-in authentication and session management

## Security Features

- CSRF protection on all forms
- User authentication required for post creation
- Authorization checks for edit/delete operations
- Password hashing and validation
- Session-based authentication

## Future Enhancements (Optional)

- **Categories/Tags**: Organize posts by topics
- **Image Upload**: Add images to blog posts
- **Comments System**: Allow readers to comment
- **Pagination**: Handle large numbers of posts
- **Search Functionality**: Find posts by keywords
- **User Profiles**: Extended user information
- **Rich Text Editor**: WYSIWYG content editing

## Development Notes

- Built following Django best practices
- MVC (Model-View-Controller) pattern implementation
- Template inheritance for consistent UI
- Class-based views for cleaner code
- Bootstrap components for responsive design
- Custom CSS for enhanced styling

## Troubleshooting

### Common Issues

1. **Django not found**: Make sure virtual environment is activated
2. **Database errors**: Run `python manage.py migrate`
3. **Static files not loading**: Check `STATICFILES_DIRS` in settings
4. **Permission denied**: Ensure proper file permissions

### Development Server
- Default port: 8000
- Access: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin/`

## License

This project is created for educational purposes as part of a Django web development internship program.