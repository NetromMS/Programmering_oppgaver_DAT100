class MålingerÅr:
    def __init__(self, year):
        self.year = year
        self.total_sunspots = 0
        self.num_measurements = 0
        self.max_daily = None
        self.min_daily = None

    def add_measurement(self, daily_sunspots):
        """Legger til en dags måling av solflekker."""
        self.total_sunspots += daily_sunspots
        self.num_measurements += 1
        if self.max_daily is None or daily_sunspots > self.max_daily:
            self.max_daily = daily_sunspots
        if self.min_daily is None or daily_sunspots < self.min_daily:
            self.min_daily = daily_sunspots

    def calculate_average(self):
        """Beregner gjennomsnittlig antall solflekker per dag."""
        if self.num_measurements == 0:
            return 0
        return self.total_sunspots / self.num_measurements

# Bruk av klassen for hvert år
yearly_data = {}
for _, row in data.iterrows():
    year = row['date'].year
    sunspots = row['daily_sunspots']
    
    if year not in yearly_data:
        yearly_data[year] = MålingerÅr(year)
    
    yearly_data[year].add_measurement(sunspots)

# Print statistikk for hvert år
for year, maaling in yearly_data.items():
    print(f"År: {year}, Maks: {maaling.max_daily}, Min: {maaling.min_daily}, Gjennomsnitt: {maaling.calculate_average()}")