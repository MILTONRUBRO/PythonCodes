import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and your toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


#print(toy_story.storyline)
#toy_story.show_trailer()

matrix =  media.Movie("Matrix", "A story of a guy in a fantastic world",
                      "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                      "https://www.youtube.com/watch?v=m8e-FF8MsqU")

star_wars =  media.Movie("Star WArs III", "The revenge of tht Siths",
                         "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                         "https://www.youtube.com/watch?v=5UnjrG_N8hU")

pulp_fiction = media.Movie("Pulp Fiction", "The most crazy movie in the history",
                           "https://upload.wikimedia.org/wikipedia/pt/8/82/Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

avengers = media.Movie("The Avengers", "The most powerfull reunion of heroes of history",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

iron_man = media.Movie("Iron Man", "Genius, Playboy",
                       "https://upload.wikimedia.org/wikipedia/pt/0/00/Iron_Man_poster.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = [toy_story, matrix, star_wars, pulp_fiction, avengers, iron_man]
fresh_tomatoes.open_movies_page(movies)






