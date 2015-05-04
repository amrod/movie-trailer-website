import media
import fresh_tomatoes

the_matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_kings_speech = media.Movie("The King's Speech",
                     "The story of King George VI of the United Kingdom of Great Britain and Northern Ireland, his impromptu ascension to the throne and the speech therapist who helped the unsure monarch become worthy of it.",
                     "http://www.movieleadership.com/wp-content/uploads/2012/03/the-kings-speech.jpg",
                     "https://www.youtube.com/watch?v=pzI4D6dyp_o")

true_grit = media.Movie("True Grit",
                     "A tough U.S. Marshal helps a stubborn teenager track down her father's murderer.",
                     "http://upload.wikimedia.org/wikipedia/en/c/ce/True_Grit_Poster.jpg",
                     "https://www.youtube.com/watch?v=qo-RDJb4W28")

twelve_years_a_slave = media.Movie("Twelve Years A Slave",
                     "In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.",
                     "http://upload.wikimedia.org/wikipedia/en/5/5c/12_Years_a_Slave_film_poster.jpg",
                     "https://www.youtube.com/watch?v=z02Ie8wKKRg")

pineapple_express = media.Movie("Pineapple Express",
                     "A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witness his dealer's boss murder a competitor while trying to serve papers on him.",
                     "http://upload.wikimedia.org/wikipedia/en/c/ca/Pineapple_Express_Poster.jpg",
                     "https://youtu.be/sW67OiY7xVw")

slumdog_millioinaire = media.Movie("Slumdog Millionaire",
                     'A Mumbai teen who grew up in the slums, becomes a contestant on the Indian version of "Who Wants To Be A Millionaire?" He is arrested under suspicion of cheating, and while being interrogated, events from his life history are shown which explain why he knows the answers.',
                     "http://8weekly.nl/wp-content/uploads/2009/7089-slumdog-millionaire-c.jpg",
                     "https://www.youtube.com/watch?v=AIzbwV7on6Q")


movies = [the_matrix, the_kings_speech, true_grit, twelve_years_a_slave, pineapple_express, slumdog_millioinaire]

fresh_tomatoes.open_movies_page(movies)