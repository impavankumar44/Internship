print("Inheritance")
print("Single Inheritance")
class Cars:
    Colour = "Colour : Black  "
    Material = "Material : Steel"


class Tata_car(Cars):
    def __init__(self,Model,Performance):
        self.Model = Model
        self.Performance = Performance

Tata_Nexon = Tata_car("Model : Nexon_45687","  Performance : Moderate to High")
print(Tata_Nexon.Colour,Tata_Nexon.Model,Tata_Nexon.Performance)


print("Multi-Level Inheritance")
class Music:
    Music_Director = "Devi Sri Prasad"
    Lyricist_1 = "Chandra Bose"
    Lyricist_2 = "Anthantha Sriram"
    Lyricist_3 = "Sirivennela Sitaramasastri"

class Music_Academy(Music):
    
        Singer_1 = "Hari Charan"
        Singer_2 = "Sherya Goshal"
        Musician_1 = "Shivamani"
        Musician_2 = "Naveen Kumar" 
class Song_1(Music_Academy):
     Actor = "Morgan"
     Actress = "Selina"

Movie_song = Song_1
print(Movie_song.Music_Director)
print(Movie_song.Lyricist_3,Movie_song.Singer_2)

print("Multiple Inheritance")
class Level_1:
     Beverage_1 = "Black Coffee"
     Steamed_Food_1 = "Idly Sambar"
     Fried_Food = "Vada"
     Curry = "Mutton Curry"
class Level_2:
     Beverage_2 = "Mocha"
     Steamed_Food_2 = "Momos"
     Bread = "French Toast"
     Egg = "Poached Egg"
class Full_Breakfast(Level_1,Level_2):
     Goated_breakfast = "Dosa"
     Supreme = "Masala dosa"

Customer_1 = Full_Breakfast()
print(Customer_1.Beverage_1,Customer_1.Fried_Food,Customer_1.Curry,Customer_1.Egg,Customer_1.Goated_breakfast)


print("Super Method")
class Mathematics:
     def love(self):
          print("We Love mathematics")
class Geometry(Mathematics):
     def love(self):
          super().love()
          print("we love geometry")
        
Ellipse = Geometry()
print(Ellipse.love())



class Maths:
     def Geometry(self):
          print("Ellipse is an interesting concept")
class Maths_1(Maths):
     def Ellipse(self):
          print("Ellipse is very good")
          super().Geometry()
Topic_1 = Maths_1()
print(Topic_1.Ellipse())




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