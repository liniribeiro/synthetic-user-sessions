
# Synthetic User Sessions

## Overview
This repository contains a Python function to generate a **synthetic dataset of user sessions** for web analytics, e-commerce, and marketing analytics.  
It simulates realistic user behavior across multiple sessions, including **views, scrolls, clicks, add-to-cart events, and purchases**, with consistent session attributes and probabilistic funnels.

This dataset is ideal for:
- Practicing **ETL pipelines**
- Building **SQL/Pandas analysis**
- Simulating **funnel analysis**
- Testing dashboards and analytics workflows

---

## Features
- Generates `user_id`, `session_id`, timestamps, event types, page URLs, product IDs, and revenue.
- Consistent session-level attributes: device, browser, OS, location, traffic source, campaign.
- Probabilistic funnels with realistic abandonment rates:
  - `view` → `scroll` → `click` → `add_to_cart` → `purchase`
- Non-purchase sessions include browsing events only.

---

## Columns
| Column Name       | Description |
|------------------|-------------|
| `user_id`         | Unique identifier for a user |
| `session_id`      | Session ID (same for all events in a session) |
| `timestamp`       | Date and time of the event |
| `event_type`      | Event type: view, scroll, click, add_to_cart, purchase |
| `page_name`       | Page URL |
| `product_id`      | Product ID (if applicable) |
| `device_type`     | Device used (desktop, mobile, tablet) |
| `browser`         | Browser used |
| `os`              | Operating system used |
| `geo_country`     | Country of the user |
| `geo_city`        | City of the user |
| `traffic_source`  | Traffic source (google, facebook, email, direct, organic) |
| `campaign`        | Marketing campaign |
| `referrer_url`    | Referrer URL |
| `revenue`         | Revenue generated (only for purchases) |

---

## Installation
```bash
git clone https://github.com/yourusername/synthetic-user-sessions.git
cd synthetic-user-sessions
pip install -r requirements.txt
```


### Notes
- session_id is consistent across all events in a session.
- Non-purchase sessions simulate browsing behavior only.
- The dataset can be saved to CSV using the function’s built-in option.