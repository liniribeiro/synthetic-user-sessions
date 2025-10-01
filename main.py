import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

def create_user_sessions(n_users=100, n_sessions=50000, n_events=500, n_past_days=30):
    devices = ["desktop", "mobile", "tablet"]
    browsers = ["Chrome", "Safari", "Firefox", "Edge"]
    os_list = ["Windows", "macOS", "Linux", "Android", "iOS"]
    countries = ["Brazil", "USA", "UK", "Germany", "India"]
    sources = ["google", "facebook", "email", "direct", "organic"]
    campaigns = ["summer_sale", "black_friday", "retargeting", "new_user_offer"]

    events = []

    for i in range(n_events):
        user_id = random.randint(1, n_users)
        session_id = random.randint(1, n_sessions)
        base_time = fake.date_time_between(start_date=f"-{n_past_days}d", end_date="now")

        # Fixed attributes for this session (consistency!)
        device = random.choice(devices)
        browser = random.choice(browsers)
        os = random.choice(os_list)
        country = random.choice(countries)
        city = fake.city()
        source = random.choice(sources)
        campaign = random.choice(campaigns)
        referrer = fake.url()

        # Decide if this session ends in a purchase
        has_purchase = random.random() < 0.2  # 20% chance

        if has_purchase:
            # Pick ONE product for the whole funnel
            product_id = random.choice([101, 202, 303, 404, 505, 606, 707, 808, 909])
            product_page = f"/product/{product_id}"

            funnel = ["view"]
            if random.random() < 0.6:
                funnel.append("scroll")
            if "scroll" in funnel or random.random() < 0.7:
                funnel.append("click")
            if "click" in funnel or random.random() < 0.8:
                funnel.append("add_to_cart")
                if random.random() < 0.9:
                    funnel.append("purchase")


            for j, event_type in enumerate(funnel):
                timestamp = base_time + timedelta(minutes=j)

                if event_type in ["view", "scroll"]:
                    page_name = product_page  # viewing same product before purchase
                elif event_type == "add_to_cart":
                    page_name = product_page
                else:  # purchase
                    page_name = "/checkout"

                revenue = round(random.uniform(10, 200), 2) if event_type == "purchase" else 0.0

                events.append([
                    user_id, session_id, timestamp, event_type, page_name, product_id,
                    device, browser, os, country, city, source, campaign, referrer, revenue
                ])

        else:
            # Non-purchase random browsing session
            n_non_purchase = random.randint(1, 4)
            timestamps = sorted([base_time + timedelta(minutes=j) for j in range(n_non_purchase)])

            for ts in timestamps:
                event_type = random.choice(["view", "click", "scroll"])
                if event_type in ["view", "scroll"]:
                    page_name = random.choice(["/home", "/search", "/about", "/contact"])
                    product_id = None
                else:
                    product_id = random.choice([101, 202, 303])
                    page_name = f"/product/{product_id}"

                events.append([
                    user_id, session_id, ts, event_type, page_name, product_id,
                    device, browser, os, country, city, source, campaign, referrer, 0.0
                ])

    df = pd.DataFrame(events, columns=[
        "user_id", "session_id", "timestamp", "event_type", "page_name", "product_id",
        "device_type", "browser", "os", "geo_country", "geo_city",
        "traffic_source", "campaign", "referrer_url", "revenue"
    ])
    df.to_csv("data/user_sessions.csv", index=False)
    return df


if __name__ == "__main__":
    n_sessions = 10000
    n_users = 2000
    n_events = 20000

    n_past_days = 400

    session_per_event = n_events / n_sessions
    print(f"Generating {n_events} sessions for {n_users} users with {n_sessions} sessions, this is around {session_per_event} session per event")
    df = create_user_sessions(n_users, n_sessions, n_events, n_past_days)
    print(df[df["event_type"] == "purchase"].head(10))

