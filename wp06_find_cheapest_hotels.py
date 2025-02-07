
def find_cheapest_hotels(hotel_name, daily_rate):
    return [hotels[0] for hotels in hotel_name if hotels[1] <= daily_rate ]

hotel_daily_rates = [
    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 120),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]

print(find_cheapest_hotels(hotel_daily_rates, 150))