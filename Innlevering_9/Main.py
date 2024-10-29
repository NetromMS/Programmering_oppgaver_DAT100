import matplotlib.pyplot as plt
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
    
    # Listene for plotting
    years = []
    min_sunspots = []
    avg_sunspots = []
    max_sunspots = []

    # Gå gjennom dictionaryet og hent ut data for hvert år
    for year, maaling in sorted(yearly_data.items()):
        years.append(year)
        min_sunspots.append(maaling.min_daily)
        avg_sunspots.append(maaling.calculate_average())
        max_sunspots.append(maaling.max_daily)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plot for minimum, gjennomsnitt og maksimum antall solflekker per år
    plt.plot(years, min_sunspots, label='Minimum antall solflekker', color='blue')
    plt.plot(years, avg_sunspots, label='Gjennomsnittlig antall solflekker', color='green')
    plt.plot(years, max_sunspots, label='Maksimum antall solflekker', color='red')

    # Tilpass plottet
    plt.xlabel('År')
    plt.ylabel('Antall solflekker')
    plt.title('Solflekkaktivitet per år')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    # Vis plot
    plt.tight_layout()
    plt.show()