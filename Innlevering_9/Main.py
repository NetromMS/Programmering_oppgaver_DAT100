import pandas as pd
from Maalinger_aar import MaalingerAar  # Import klassen
if __name__ == "__main__":

    # Les CSV-filen. Juster filstien til CSV-filen din.
    file_path = "/Users/netrom/Library/CloudStorage/OneDrive-UniversitetetiStavanger/Programmering/Programmering_oppgaver_DAT100/Innlevering_9/FIler/solflekkaktivitet_daglig.csv"

    data = pd.read_csv(file_path, sep=";", header=None, encoding='utf-8') #leser CSV filen "har med utf-8 for fremtidige filer (æøå)"

    # Rens og strukturer dataene
    data['date'] = pd.to_datetime(data[[0, 1, 2]].rename(columns={0: 'year', 1: 'month', 2: 'day'}))
    data = data[['date', 6]]
    data.columns = ['date', 'daily_sunspots']

    # Opprett et ordbokslager for dataene per år
    yearly_data = {}
    for _, row in data.iterrows(): #iterer gjennom hver rad og legg til målinger per år
        year = row['date'].year
        sunspots = row['daily_sunspots']
        
        if year not in yearly_data: #Sjekk om året allerede er en nøkkel i dictionary
            yearly_data[year] = MaalingerAar(year)
        
        yearly_data[year].add_measurement(sunspots) #Legg til dagens måling i MaalingerAar-objektet for dette året

    # Print ut statistikk per år
    for year, maaling in yearly_data.items():
        avg_sunspots = maaling.calculate_average()
        print(f"År: {year}, Maks: {maaling.max_daily}, Min: {maaling.min_daily}, Gjennomsnitt: {maaling.calculate_average()}")
