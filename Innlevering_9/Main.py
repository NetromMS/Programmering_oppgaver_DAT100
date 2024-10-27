import pandas as pd
from Maalinger_aar import MaalingerAar  # Import klassen

# Les CSV-filen. Juster filstien til CSV-filen din.
file_path = "stien/til/din/mappe/solflekkaktivitet_daglig.csv"
data = pd.read_csv(file_path, sep=";", header=None)

# Rens og strukturer dataene
data['date'] = pd.to_datetime(data[[0, 1, 2]].rename(columns={0: 'year', 1: 'month', 2: 'day'}))
data = data[['date', 6]]
data.columns = ['date', 'daily_sunspots']

# Opprett et ordbokslager for dataene per år
yearly_data = {}
for _, row in data.iterrows():
    year = row['date'].year
    sunspots = row['daily_sunspots']
    
    if year not in yearly_data:
        yearly_data[year] = MaalingerAar(year)
    
    yearly_data[year].add_measurement(sunspots)

# Print ut statistikk per år
for year, maaling in yearly_data.items():
    print(f"År: {year}, Maks: {maaling.max_daily}, Min: {maaling.min_daily}, Gjennomsnitt: {maaling.calculate_average()}")