from movie_library import MovieLibrary

"""
File di test per la libreria MovieLibrary.
"""

def main():
    # Percorso del file JSON
    json_path = "movies.json"

    # Crea un'istanza della libreria
    library = MovieLibrary(json_path)

    while True:
        print("\nScegli un'operazione:")
        print("1. Visualizza tutti i film")
        print("2. Aggiungi un nuovo film")
        print("3. Rimuovi un film")
        print("4. Aggiorna un film")
        print("5. Ottieni i titoli di tutti i film")
        print("6. Conta il numero totale di film")
        print("7. Cerca film per titolo")
        print("8. Cerca film per substring nel titolo")
        print("9. Cerca film per anno")
        print("10. Cerca film per regista")
        print("11. Cerca film per genere")
        print("12. Trova i titoli dei film più vecchi")
        print("13. Calcola la media degli anni di uscita dei film")
        print("14. Trova i titoli dei film con il titolo più lungo")
        print("15. Trova i film compresi tra due anni")
        print("16. Trova l'anno più comune tra i film")
        print("0. Esci")

        choice = input("Inserisci il numero dell'operazione: ")

        if choice == "0":
            print("Uscita dal programma.")
            break

        try:
            if choice == "1":
                print("\nFilm nella collezione:")
                print(library.get_movies())

            elif choice == "2":
                title = input("Inserisci il titolo: ")
                director = input("Inserisci il regista: ")
                year = int(input("Inserisci l'anno di uscita: "))
                genres = input("Inserisci i generi (separati da virgola): ").split(",")
                print(library.add_movie(title, director, year, genres))

            elif choice == "3":
                title = input("Inserisci il titolo del film da rimuovere: ")
                print(library.remove_movie(title))

            elif choice == "4":
                title = input("Inserisci il titolo del film da aggiornare: ")
                director = input("Nuovo regista (premi Invio per lasciare invariato): ") or None
                year = input("Nuovo anno (premi Invio per lasciare invariato): ")
                year = int(year) if year else None
                genres = input("Nuovi generi (separati da virgola, premi Invio per lasciare invariati): ")
                genres = genres.split(",") if genres else None
                print(library.update_movie(title, director, year, genres))

            elif choice == "5":
                print("\nTitoli dei film:")
                print(library.get_movie_titles())

            elif choice == "6":
                print("\nNumero totale di film:")
                print(library.count_movies())

            elif choice == "7":
                title = input("Inserisci il titolo del film da cercare: ")
                print(library.get_movie_by_title(title))

            elif choice == "8":
                substring = input("Inserisci la substring da cercare nel titolo: ")
                print(library.get_movies_by_title_substring(substring))

            elif choice == "9":
                year = int(input("Inserisci l'anno di uscita: "))
                print(library.get_movies_by_year(year))

            elif choice == "10":
                director = input("Inserisci il regista: ")
                print(library.get_movies_by_director(director))

            elif choice == "11":
                genre = input("Inserisci il genere: ")
                print(library.get_movies_by_genre(genre))

            elif choice == "12":
                print("\nTitoli dei film più vecchi:")
                print(library.get_oldest_movie_titles())

            elif choice == "13":
                print("\nMedia degli anni di uscita dei film:")
                print(library.get_average_release_year())

            elif choice == "14":
                print("\nTitoli dei film con il titolo più lungo:")
                print(library.get_longest_titles())

            elif choice == "15":
                start_year = int(input("Inserisci l'anno di inizio: "))
                end_year = int(input("Inserisci l'anno di fine: "))
                print(library.get_titles_between_years(start_year, end_year))

            elif choice == "16":
                print("\nAnno più comune tra i film:")
                print(library.get_most_common_year())

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print(f"Errore: {e}")

if __name__ == "__main__":
    main()
