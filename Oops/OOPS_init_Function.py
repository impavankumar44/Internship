class Music:
    def __init__(self):
        print("Welcome to the world of soul")

    tone_1 = "melody"
    tone_2 = "base"
    tone_3 = "mixed"
    pitch_1 = "low"
    pitch_2 = "medium"
    pitch_3 = "high"
    singer_1 = "male - 1"
    singer_2 = "female - 1"
    singer_3 = "male and female"
    singer_4 = "male - 2"
    singer_5 = "female - 2"


song_1 = Music()
print(song_1.tone_1,song_1.pitch_3,song_1.singer_5)

song_2 = Music()
print(song_2.tone_2,song_2.pitch_3,song_2.singer_3)


print("")



class Watches:
    def __init__(self,brand,type,working_type):
        self.brand = brand
        self.type = type 
        self.working_type = working_type
        print("Wearing Luxury is living luxury")

watch_1 = Watches("Seiko","Analog","Skeleton Mechanical")
print(watch_1.brand,watch_1.type,watch_1.working_type)
watch_2 = Watches("Hamilton","Semi Analog","Mechanical")
print(watch_2.brand,watch_2.type,watch_2.working_type)