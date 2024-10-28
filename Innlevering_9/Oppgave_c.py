import pandas as pd
from Maalinger_aar import MaalingerAar  # Importer klassen

if __name__ == "__main__":
    # Sti til CSV-filen
    file_path = "stien/til/din/mappe/solflekkaktivitet_daglig.csv"
    
    # Les CSV-filen, spesifiser separator, og kolonner
    data = pd.read_csv(file_path, sep=";", header=None, usecols=[0, 4], encoding='utf-8')
    data.columns = ['year', 'daily_sunspots']  # Navngi kolonnene
    
    # Filtrer ut rader der antall solflekker er -1
    data = data[data['daily_sunspots'] != -1]
    
    # Opprett et dictionary for å lagre dataene per år
    yearly_data = {}

    # Iterer gjennom hver rad og legg til målinger per år
    for _, row in data.iterrows():
        year = row['year']
        sunspots = row['daily_sunspots']
        
        # Sjekk om året allerede er en nøkkel i dictionary
        if year not in yearly_data:
            yearly_data[year] = MaalingerAar(year)  # Opprett et nytt MaalingerAar-objekt for året
        
        # Legg til dagens måling i MaalingerAar-objektet for dette året
        yearly_data[year].add_measurement(sunspots)
    
    # Print ut statistikk for hvert år
    for year, maaling in yearly_data.items():
        avg_sunspots = maaling.calculate_average()
        print(f"År: {year}, Maks: {maaling.max_daily}, Min: {maaling.min_daily}, Gjennomsnitt: {avg_sunspots}")