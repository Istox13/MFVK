import pygame

class Player:
    def __init__(self):
        #Определяе какой файл проигрывать
        #music_file = "C://Users/Istox13/Downloads/1.mp3"

        #Устанавливаем параметры Микшера.
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get right sound)
        #Инициализируем микшер.
        pygame.mixer.init(freq, bitsize, channels, buffer)

        #Устанавливаем грокость - максимум.
        pygame.mixer.music.set_volume(1.0)
        
    def play_music(self, music_file):
        try:
            clock = pygame.time.Clock()
            try:
                #Загружае файл.
                pygame.mixer.music.load(music_file)
                print("Music file %s loaded!" % music_file)
            except pygame.error:
                #Ловим ошибки загрузки
                print("File %s not found! (%s)" % (music_file, pygame.get_error()))
                return
            #Проигрываем
            pygame.mixer.music.play()
            #Ожидаем завершение проигрывания
            
        
        except KeyboardInterrupt:
                # Если пользователь прервёт проигрывание.
                #Завершаем проигрывание, как положено.
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.stop()
                raise SystemExit

    def pause(self):
        pygame.mixer.music.pause()
    
    def stop(self):
        pygame.mixer.music.stop()

    def unpause(self):
        pygame.mixer.music.unpause()


