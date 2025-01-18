import json
import os


class MovieLibrary:
    """
    Classe per la gestione di una collezione di film.
    """

    def __init__(self, json_file):
        """
        Inizializza la classe MovieLibrary.

        :param json_file: Percorso assoluto del file JSON contenente i film.
        """
        if not os.path.exists(json_file):
            # Se il file non esiste, solleva un'eccezione
            raise FileNotFoundError(f"File not found: {json_file}")

        # Carica i dati dal file JSON
        self.json_file = json_file

        try:
            # Apre il file in lettura
            with open(json_file, 'r', encoding='utf-8') as file:
                # Carica i dati dal file JSON
                self.movies = json.load(file)
                # Verifica che i dati siano una lista
                if not isinstance(self.movies, list):
                    # Se i dati non sono una lista, solleva un'eccezione
                    raise ValueError("Il contenuto del file non è una lista valida.")
        except (json.JSONDecodeError, ValueError):
            # Se il file è vuoto o contiene dati non validi, lo inizializza a una lista vuota
            self.movies = []

    def get_movies(self):
        """
        Restituisce tutti i film nella collezione.

        :return: Lista di film.
        """
        return self.movies

    def add_movie(self, title: str, director: str, year: int, genres: list[str]):
        """
        Aggiunge un nuovo film alla collezione.

        :param title:
        :param director:
        :param year:
        :param genres:
        :return: Dizionario rappresentante il film aggiunto.
        """
        # Verifica che il film non esista già
        movie = self.get_movie_by_title(title)

        if movie:
            # Se il film esiste già, solleva un'eccezione
            raise ValueError(f"Film '{title}' already exists in the collection.")

        # Crea un dizionario rappresentante il nuovo film
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }

        # Aggiunge il nuovo film alla collezione
        self.movies.append(new_movie)
        # Aggiorna il file JSON
        self.__update_json_file()
        # Restituisce il film aggiunto
        return new_movie

    def remove_movie(self, title: str):
        """
        Rimuove un film dalla collezione.

        :param title: Stringa del titolo del film da rimuovere.
        :return: Film rimosso.
        """
        # Verifica che il film esista
        movie = self.get_movie_by_title(title)

        if not movie:
            # Se il film non esiste, solleva un'eccezione
            raise MovieLibrary.MovieNotFoundError()

        # Rimuove il film dalla collezione
        self.movies.remove(movie)
        # Aggiorna il file JSON
        self.__update_json_file()
        # Restituisce il film rimosso
        return movie

    def update_movie(self, title: str, director=None, year=None, genres=None):
        """
        Aggiorna i dettagli di un film esistente.

        :param title: Titolo del film da aggiornare.
        :param director: Regista del film da aggiornare.
        :param year: Anno di uscita del film da aggiornare.
        :param genres: Generi del film da aggiornare.
        :return: Film aggiornato.
        """
        # Verifica che il film esista
        movie = self.get_movie_by_title(title)
        if not movie:
            # Se il film non esiste, solleva un'eccezione
            raise MovieLibrary.MovieNotFoundError()
        if director:
            # Se il parametro director viene passato, aggiorna i dettagli del film
            movie["director"] = director
        if year:
            # Se il parametro year viene passato, aggiorna i dettagli del film
            movie["year"] = year
        if genres:
            # Se il parametro genres viene passato, aggiorna i dettagli del film
            movie["genres"] = genres
        # Aggiorna il file JSON
        self.__update_json_file()
        # Restituisce il film aggiornato
        return movie

    def get_movie_titles(self):
        """
        Restituisce una lista di titoli di tutti i film nella collezione.

        :return: Lista di titoli.
        """
        # Crea una lista vuota per i titoli
        movie_titles = []
        for movie in self.movies:
            # Aggiunge il titolo di ciascun film alla lista
            movie_titles.append(movie["title"])
        # Restituisce la lista di titoli
        return movie_titles

    def count_movies(self):
        """
        Restituisce il numero totale di film nella collezione.

        :return: Numero totale di film.
        """
        # Restituisce la lunghezza della lista di film
        return len(self.movies)

    def get_movie_by_title(self, title: str):
        """
        Restituisce un film dalla collezione in base al titolo.

        :param title: Titolo del film da cercare.
        :return: Film o None se non è stato trovato.
        """
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                # Confronta i titoli in modo case-insensitive, se il titolo corrisponde, restituisci il film
                return movie
        # Se non è stato trovato un film con quel titolo, restituisci None
        return None

    def get_movies_by_title_substring(self, substring: str):
        """
        Restituisce una lista di film che contengono la stringa nel titolo.

        :param substring: Sotto stringa da cercare.
        :return: Lista di film.
        """
        # Inizializza una lista vuota per i film corrispondenti
        matching_movies = []
        for movie in self.movies:
            # Controlla se la sotto stringa è presente nel titolo del film (case insensitive)
            if substring.lower() in movie["title"].lower():
                # Aggiunge il film alla lista
                matching_movies.append(movie)
        # Restituisce la lista di film corrispondenti
        return matching_movies

    def get_movies_by_year(self, year: int):
        """
        Restituisce una lista di film con l'anno di uscita specificato.

        :param year: Anno di uscita.
        :return: Lista di film.
        """
        # Inizializza una lista vuota per i film corrispondenti
        matching_movies = []
        for movie in self.movies:
            # Per ogni film, controlla se l'anno di uscita corrisponde all'anno specificato
            if movie["year"] == year:
                # Se l'anno di uscita del film corrisponde all'anno specificato aggiunge il film alla lista
                matching_movies.append(movie)
        # Restituisce la lista di film corrispondenti
        return matching_movies

    def get_movies_by_director(self, director: str):
        """
        Restituisce una lista di film con il regista specificato.

        :param director: Regista da cercare.
        :return: Lista di film.
        """
        # Inizializza una lista vuota per i film corrispondenti
        matching_movies = []
        for movie in self.movies:
            # Per ogni film, controlla se il regista corrisponde al regista specificato
            if movie["director"].lower() == director.lower():
                # Aggiunge il film alla lista
                matching_movies.append(movie)
        # Restituisce la lista di film corrispondenti
        return matching_movies

    def get_movies_by_genre(self, genre: str):
        """
        Restituisce una lista di film che appartengono a un genere specificato.

        :param genre: Genere da cercare.
        :return: Lista di film.
        """
        # Inizializza una lista vuota per i film corrispondenti
        matching_movies = []
        for movie in self.movies:
            # Per ogni film, confronta il genere specificato con i generi del film (case insensitive)
            for g in movie["genres"]:
                if genre.lower() == g.lower():
                    # Se il genere corrisponde, aggiunge il film alla lista
                    matching_movies.append(movie)
                    # Esce dal ciclo interno dopo aver trovato una corrispondenza
                    break
        # Restituisce la lista di film corrispondenti
        return matching_movies

    def get_oldest_movie_titles(self):
        """
        Restituisce una lista di titoli dei film più vecchi nella collezione.

        Mi sono permesso di modificare il metodo per restituire una lista di titoli
        invece di un singolo titolo per evitare di non coprire il caso d'uso in cui
        ci siano più film con lo stesso anno. Spero non sia un problema :)

        :return: Lista di titoli o None se la collezione è vuota.
        """
        # Gestione del caso in cui la lista sia vuota
        if not self.movies:
            return None

        # Inizializza con il primo anno nella collezione
        oldest_year = self.movies[0]["year"]
        for movie in self.movies:
            # Per ogni film, controlla se l'anno di uscita è più vecchio
            if movie["year"] < oldest_year:
                # Se l'anno di uscita del film è più vecchio, aggiorna l'anno più vecchio
                oldest_year = movie["year"]

        # Raccogli tutti i titoli dei film con l'anno più vecchio
        oldest_titles = []
        for movie in self.movies:
            # Per ogni film, controlla se l'anno di uscita è uguale all'anno più vecchio
            if movie["year"] == oldest_year:
                # Se l'anno di uscita del film è uguale all'anno più vecchio, aggiunge il titolo alla lista
                oldest_titles.append(movie["title"])

        return oldest_titles

    def get_average_release_year(self):
        """
        Restituisce la media degli anni di uscita dei film nella collezione.

        :return: Media degli anni di uscita o None se la collezione è vuota.
        """
        # Gestione del caso in cui la lista sia vuota
        if not self.movies:
            return None

        # Inizializza la somma degli anni
        total_years = 0

        # Calcola la somma degli anni di uscita iterando sui film
        for movie in self.movies:
            total_years += movie["year"]

        # Calcola la media degli anni di uscita
        average_year = total_years / len(self.movies)

        return average_year

    def get_longest_titles(self):
        """
        Restituisce una lista di titoli dei film con il titolo più lungo.

        Mi sono permesso di modificare il metodo per restituire una lista di titoli
        invece di un singolo titolo per evitare di non coprire il caso d'uso in cui
        ci siano più film con lo stesso numero di caratteri. Spero non sia un problema :)

        :return: Lista di titoli o None se la collezione è vuota.
        """
        # Gestione del caso in cui la lista sia vuota
        if not self.movies:
            return None

        # Inizializza la lunghezza massima del titolo
        max_length = 0
        for movie in self.movies:
            # Per ogni film, calcola la lunghezza del titolo
            title_length = len(movie["title"])
            if title_length > max_length:
                # Se la lunghezza del titolo è maggiore della lunghezza massima, aggiorna la lunghezza massima
                max_length = title_length

        # Raccoglie tutti i titoli con la lunghezza massima
        longest_titles = []
        for movie in self.movies:
            # Per ogni film, controlla se la lunghezza del titolo è uguale alla lunghezza massima
            if len(movie["title"]) == max_length:
                # Se la lunghezza del titolo del film è uguale alla lunghezza massima, aggiunge il titolo alla lista
                longest_titles.append(movie["title"])

        return longest_titles

    def get_titles_between_years(self, start_year: int, end_year: int):
        """
        Restituisce una lista di titoli dei film con anno di uscita compreso tra start_year ed end_year.

        :param start_year: Anno di inizio.
        :param end_year: Anno di fine.
        :return: Lista di titoli o None se la collezione è vuota.
        """
        # Gestione del caso in cui la lista sia vuota
        if not self.movies:
            return None

        # Inizializza una lista vuota per i titoli corrispondenti
        matching_titles = []

        # Itera su tutti i film per controllare l'anno di uscita
        for movie in self.movies:
            if start_year <= movie["year"] <= end_year:
                # Aggiunge il titolo se l'anno è nel range
                matching_titles.append(movie["title"])

        return matching_titles

    def get_most_common_year(self):
        """
        Restituisce l'anno più comune tra i film nella collezione.

        :return: Anno più comune o None se la collezione è vuota.
        """
        # Gestione del caso in cui la lista sia vuota
        if not self.movies:
            return None

        # Crea un dizionario per contare il numero di film per ogni anno
        year_counts = {}
        for movie in self.movies:
            # Per ogni film, controlla l'anno di uscita
            year = movie["year"]
            if year in year_counts:
                # Se l'anno è già presente, incrementa il conteggio
                year_counts[year] += 1
            else:
                # Se l'anno non è presente, inizializza il conteggio a 1
                year_counts[year] = 1

        # Trova l'anno con il conteggio massimo
        most_common_year = None
        max_count = 0
        for year, count in year_counts.items():
            # Per ogni anno, controlla il conteggio
            if count > max_count:
                # Se il conteggio è maggiore del conteggio massimo, aggiorna il conteggio massimo e l'anno più comune
                max_count = count
                most_common_year = year

        return most_common_year

    def __update_json_file(self):
        """
        Aggiorna il file JSON con i dati correnti della collezione.
        """
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump(self.movies, file, indent=4)

    class MovieNotFoundError(Exception):
        """
        Eccezione personalizzata per film non trovati.
        """
        def __init__(self, message="Movie was not found"):
            super().__init__(message)