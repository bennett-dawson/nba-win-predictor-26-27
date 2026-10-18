import time
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

seasons = [
    "2016-17", "2017-18", "2018-19", "2019-20", "2020-21",
    "2021-22", "2022-23", "2023-24", "2024-25", "2025-26",
]

all_seasons = []

for season in seasons:
    print(f"Pulling {season}...")
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season=season,
        measure_type_detailed_defense="Advanced",
        timeout=60,
    )
    df = stats.get_data_frames()[0]
    df["SEASON"] = season
    df.to_csv(f"data/team_stats_{season}.csv", index=False)
    all_seasons.append(df)
    time.sleep(2)

combined = pd.concat(all_seasons, ignore_index=True)
combined.to_csv("data/team_stats_all.csv", index=False)
print(f"Done! {len(combined)} team-seasons saved.")