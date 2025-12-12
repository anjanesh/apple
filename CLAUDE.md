# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django-based Apple product pricing comparison website that tracks prices from multiple resellers in India. The site displays products (Mac, iPhone, iPad, Apple Watch) with pricing information and related articles.

## Development Commands

### Running the Development Server
```bash
python manage.py runserver
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Static Files
```bash
# Collect static files for production
python manage.py collectstatic
```

### Running Tests
```bash
python manage.py test product
```

## Architecture

### Settings Configuration
The project uses a two-tier settings approach:
- `apple/settings.py` - Production settings (DEBUG=False, limited ALLOWED_HOSTS)
- `apple/local_settings.py` - Local development overrides (DEBUG=True, localhost allowed)

The settings module attempts to import `local_settings.py` at the end, falling back gracefully if not present. When developing locally, ensure `local_settings.py` exists with appropriate DEBUG and ALLOWED_HOSTS values.

### URL Structure
The application uses a single-app architecture where all URLs are defined in `apple/urls.py` and map to views in the `product` app. Key URL patterns:
- Admin interface at `/backend/` (not `/admin/`)
- Product listings by category: `/mac`, `/iphone`, `/ipad`, `/watch`
- Individual product pages use slug-based URLs: `/<category>/<slug>/`
- iPhone filtering by version: `/iphone/12/`, `/iphone/13/`, etc. (regex-based)
- Reseller pages: `/resellers` and `/reseller/<slug>/`

### Models Architecture
Located in `product/models.py`:

**Product Model**: Central model representing Apple products
- Uses `TypeOfComputer` choices for product categorization
- Auto-generates slugs from title on creation
- Related to Items through ForeignKey for pricing data
- Always annotate with `Min('item__price')` when querying for display to show lowest price

**Item Model**: Represents product listings from specific resellers
- Links Product to Reseller with pricing and offer details
- Includes `last_updated` timestamp for tracking price changes
- Order by `price` when displaying items for a product

**Article Model**: News/events/rumors about products
- Uses `TypeOfComputer` for product association (nullable)
- Has its own `TypeOfArticle` choices (Event, News, Rumour, Announcement)
- Auto-generates slugs from title

**Reseller Model**: Stores authorized reseller information with contact details and logos

**ServiceCenter Model**: Stores Apple service center information

### View Patterns
Located in `product/views.py`:

The application follows a consistent view pattern with helper functions:
- `viewAllProducts()` - Generic function that handles product listing logic for all categories
  - Takes `typeOfProduct` parameter ('mac', 'iphone', 'ipad', 'watch')
  - Builds Q objects for filtering by product type
  - Annotates products with `minimal_price` using `Min('item__price')`
  - Fetches latest relevant Article using complex Q queries
  - Applies pagination (100 items per page)
  - Formats prices using Indian currency format (₹)

- `viewProduct()` - Generic function for individual product detail pages
  - Takes slug parameter
  - Fetches product and related items ordered by price
  - Formats prices using `currency_in_indian_format()` utility

Each category has dedicated view functions that call these helpers:
- Mac: `viewAllMacs()`, `viewMac()`
- iPhone: `viewAlliPhones()`, `viewiPhone()`
- iPad: `viewAlliPads()`, `viewiPad()`
- Watch: `viewAllWatches()`, `viewWatch()`

### Utilities
Located in `product/utils.py`:

**currency_in_indian_format(n)**: Converts numbers to Indian numbering format (lakhs/crores with proper comma placement). Used throughout views to format prices with ₹ symbol.

**date_last_modified_static()**: Returns modification timestamp of template files, used with Django's `@last_modified` decorator for HTTP caching.

### Template Structure
Templates located in `product/templates/`:
- `base.html` - Base template with common structure
- `navbar.html`, `footer.html` - Shared components
- `product/` subdirectory contains category-specific templates:
  - `mac.html`, `iphone.html`, `ipad.html`, `watch.html` - Listing pages
  - `view.html` - Generic product detail template (used for all categories)
  - `article-title.html` - Article component

### Admin Interface
Located at `/backend/` (customized from default `/admin/`):
- ProductAdmin customizes product listing with specific display fields and search
- Other models registered without custom admin classes

## Deployment

### Google App Engine
The project is configured for deployment to Google App Engine (see `app.yaml`):
- Runtime: Python 3.12
- Instance class: F1
- Static files served from `/static` directory
- Production URL: ambient-cubist-425701-d0.uc.r.appspot.com
- Custom domain: apple.ind.in

### Database
Uses SQLite for development and production. Database file: `db.sqlite3`

### Media Files
Product images and reseller logos stored in `MEDIA_ROOT` (media/ directory)

## Important Notes

- When adding new products, ensure the slug is unique or leave empty to auto-generate
- Price queries should always use `.annotate(minimal_price=Min('item__price'))` pattern
- All price displays use Indian currency format utility
- The TypeOfComputer enum drives both product categorization and article filtering
- Complex Q query patterns are used for article filtering by product type