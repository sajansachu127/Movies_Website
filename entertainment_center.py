import media
import fresh_tomatoes

#To add each of my favourite movies everytime a new instance are created
premam = media.Movie("Premam",
                     "It is story of three parts of his life based on a man called Goerge and his love life",
					 "http://ecx.images-amazon.com/images/I/51flle0HSeL.jpg",
					 "https://www.youtube.com/watch?v=9wkq2PNxJys")


anandham = media.Movie("Anandham",
                      "It is story of a CSE dept gang who enjoyed a lot in their IV trip and their love, friendhsip and all",
					  "https://assets.voxcinemas.com/posters/P_HO00004187.jpg",
					  "https://www.youtube.com/watch?v=9B1SDMwQRXk")


vikram_vedha = media.Movie("Vikram Vedha",
                           "It is story based on two yound men and their struggling in their lives",
						   "https://upload.wikimedia.org/wikipedia/en/0/03/Vikram_Vedha_poster.jpg",
						   "https://www.youtube.com/watch?v=8rnTSgcAQus")


sanam_teri_kasam = media.Movie("Sanam Teri Kasam",
                               "It is a Love story with sad ending..  Will make u cry",
       						   "http://im.rediff.com/movies/2016/feb/04sanam-teri-kasam.jpg",
							   "https://www.youtube.com/watch?v=nxR_g-9uHXc")


ms_dhoni = media.Movie("MS Dhoni",
                       "This is bioraphy of cricketer MS Dhoni and his lifestory",
					   "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
					   "https://www.youtube.com/watch?v=6L6XqWoS8tw")


# Here all the movie instance are added to a list
movies = [premam, anandham, vikram_vedha, sanam_teri_kasam, ms_dhoni]
fresh_tomatoes.open_movies_page(movies)
