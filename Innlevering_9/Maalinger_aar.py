class MaalingerAar:
    def __init__(self, year):
        """
        Konstruktør som tar inn året og setter egenskapene for et tomt objekt.
        """
        self.year = year
        self.total_sunspots = 0  # Total antall solflekker for året
        self.num_measurements = 0  # Antall målinger for året
        self.max_daily = None  # Maksimum antall solflekker på en dag
        self.min_daily = None  # Minimum antall solflekker på en dag

    def add_measurement(self, daily_sunspots):
        """
        Metode for å legge til en ny dags måling.
        Oppdaterer totalen, antall målinger, og sjekker maks og min.
        """
        self.total_sunspots += daily_sunspots
        self.num_measurements += 1

        # Oppdater maks og min om nødvendig
        if self.max_daily is None or daily_sunspots > self.max_daily:
            self.max_daily = daily_sunspots
        if self.min_daily is None or daily_sunspots < self.min_daily:
            self.min_daily = daily_sunspots

    def calculate_average(self):
        """
        Metode for å beregne gjennomsnittlig antall solflekker per dag.
        Returnerer 0 hvis det ikke er noen målinger.
        """
        if self.num_measurements == 0:
            return 0  # Unngå divisjon med null
        return self.total_sunspots / self.num_measurements