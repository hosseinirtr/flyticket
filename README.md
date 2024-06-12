# Ticket System

## Overview

This repository contains a Django-based ticket system that models airports, flights, and passengers. It includes functionality for creating, managing, and validating flights and passenger reservations, with a focus on ensuring data integrity and using Redis for caching.

## Cache Configuration

The project uses Redis for caching to improve performance. The cache configuration is set in `settings.py`:

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
```

## Usage

### Create Airports
Add entries for different airports in the admin interface or via the Django shell.

### Create Flights
Add flight entries ensuring the origin and destination are different.

### Add Passengers
Link passengers to flights and user accounts.

## TODO

- Create HTML templates for views.
- Implement user authentication and authorization.
- Add API endpoints for the models.
- Write tests for the models and views.
