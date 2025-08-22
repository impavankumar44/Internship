print("Inheritance") # The output gives the string 'Inheritance'

print("Single Inheritance") # The output gives the string 'Single Inheritance'


class Cars:
    colour = "Colour : Black  "
    material = "Material : Steel"


class Tata_car(Cars):
    def __init__(self,model,performance):
        self.model = model
        self.performance = performance


tata_nexon = Tata_car("Model : Nexon_45687","  Performance : Moderate to High")
print(tata_nexon.colour,tata_nexon.model,tata_nexon.performance)
# The output gives the string 'Colour : Black ' , 'Model : Nexon_45687' and 'Performance : Moderate to High'


class Music:
     music_director = "Devi Sri Prasad"
     lyricist_1 = "Chandra Bose"
     lyricist_2 = "Anthantha Sriram"
     lyricist_3 = "Sirivennela Sitaramasastri"

    
class Music_academy(Music):
        singer_1 = "Hari Charan"
        singer_2 = "Sherya Goshal"
        musician_1 = "Shivamani"
        musician_2 = "Naveen Kumar" 

        
class Song_1(Music_academy):
     actor = "Morgan"
     actress = "Selina"


movie_song = Song_1
print(movie_song.music_director) # Gives the output 'Devi Sri Prasad'
print(movie_song.lyricist_3,movie_song.singer_2) 
# Gives the output 'Sirivennela Sitaramasastri' and 'Sherya Goshal'


print("Multiple Inheritance") # The Output gives the string 'Multiple Inheritance'


class Level_1:
     beverage_1 = "Black Coffee"
     steamed_food_1 = "Idly Sambar"
     fried_food = "Vada"
     curry = "Mutton Curry"


class Level_2:
     beverage_2 = "Mocha"
     steamed_food_2 = "Momos"
     bread = "French Toast"
     egg = "Poached Egg"


class Full_breakfast(Level_1,Level_2):
     goated_breakfast = "Dosa"
     supreme = "Masala dosa"


customer_1 = Full_breakfast()
print(customer_1.beverage_1,customer_1.fried_food,
      customer_1.curry,customer_1.egg,customer_1.goated_breakfast
)
#The Output gives the string 'Black Coffee' , 'Vada' , 'Mutton Curry' , 'Poached Egg' and 'Dosa'


print("Super Method") # The Output gives the string 'Super Method'


class Mathematics:

     def love(self):
          print("We Love mathematics") # Gives the output 'We Love mathematics'


class Geometry(Mathematics):

     def love(self):
          super().love()
          print("we love geometry")
          # The Output gives the string 'we love geometry' 

        
ellipse = Geometry()
print(ellipse.love())


class Maths:
     def geometry(self):
          print("Ellipse is an interesting concept")


class Maths_1(Maths):

     def ellipse(self):
          print("Ellipse is very good")
          super().geometry()


topic_1 = Maths_1()
print(topic_1.ellipse())
# Returns the output 'Ellipse is very good'
# Returns the output 'Ellipse is an interesting concept'


# super method in __init__ function
class Movies:

     def __init__(self,cast):
          self.cast = cast
          print(f"The main money returing cast is {self.cast}")


class Baahubali(Movies):
          
          def __init__(self,cast,gross):
               self.gross = gross

               super().__init__(cast)
               print(f"The movie has collected a gross of {gross}")


reason = Baahubali("Rajamouli and Prabas","1200Cr")
print(reason.cast,reason.gross)
# The output returns the string 'The main money returing cast is Rajamouli and Prabas'
# The output returns the string 'The movie has collected a gross of 1200Cr'