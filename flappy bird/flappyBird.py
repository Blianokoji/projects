import pygame as py
import random

#initialize pygame
sc_width = 1000
sc_height = 800
sc_size = (sc_width,sc_height)

py.init()
py.mixer.init()

# Game variables
pipe_width = 70
pipe_height = 400
pipe_gap = 150
pipe_speed = 5
score=0
score_increment = 1
#setting up the screen
sc = py.display.set_mode(sc_size)

#title and icon
py.display.set_caption("Flappy Bird")
icon_path=r"bird.png"
icon = py.image.load(icon_path)
py.display.set_icon(icon)

running = True

# Load sounds
flap_sound = py.mixer.Sound('flap.wav')
collision_sound = py.mixer.Sound('collision.wav')
score_sound = py.mixer.Sound('score.wav')
over=py.mixer.Sound('over.wav')
py.mixer.music.load('background_music.mp3')

# Play background music
py.mixer.music.play(-1)  # Play the music in a loop

#player
class Bird:
    def __init__(self) :
        self.image=py.image.load(icon_path)
        self.image=py.transform.scale(self.image,(60,50))
        self.initialx=(sc_width/2)-sc_width/3 
        self.initialy=sc_height/2 
        self.bird_rect = py.Rect(self.initialx,self.initialy, self.image.get_width(), self .image.get_height())

    def gravity(self):
        self.bird_rect.centery+=5

    def jump(self):
        self.bird_rect.centery -=40

    def draw(self):
        sc.blit(self.image,self.bird_rect.topleft)




#pipes
class Pipe:
    def __init__(self) -> None:
        pipe_path=r"pipe.png"
        self.pipe=py.image.load(pipe_path)
        self.pipe=py.transform.scale(self.pipe,(600,400))


    def create_pipe(self):
        pipe_gap=random.randint(120,200)
        self.pipe_height = random.randint(120, sc_height - pipe_gap - 150)
        self.bottom_pipe = py.Rect(sc_width, pipe_height, pipe_width, pipe_height)
        self.top_pipe = py.Rect(sc_width, pipe_height - pipe_gap - pipe_height, pipe_width, pipe_height)
        return self.top_pipe, self.bottom_pipe
    
        
    def move_pipes(self,pipes):
        for pipe in pipes:
            pipe.centerx -= pipe_speed
        return [pipe for pipe in pipes if pipe.right > 0]

    def draw(self,pipes):
        for pipe in pipes:
            if pipe.y < 0:  # Top pipe
                sc.blit(py.transform.flip(self.pipe, False, True), pipe.topleft)
            else:  # Bottom pipe
                sc.blit(self.pipe, pipe.topleft)
    



#clouds
class Clouds:
    def __init__(self) :
        self.cloud=py.image.load(r"73.png")
        self.cloud=py.transform.scale(self.cloud,sc_size)

    def draw(self):
        sc.blit(self.cloud,(0,0))


#land
class Land:
    def __init__(self) :
        self.land=py.image.load(r"buildings and land.png")
        self.land=py.transform.scale(self.land,sc_size)

    def draw(self):
        sc.blit(self.land,(0,0))

class gameOver:
    def __init__(self) -> None:
        self.image=py.image.load(r"GAME OVER.png")
        self.image=py.transform.scale(self.image,(sc_width*1.5,sc_height*1.25))
    def draw(self):
        sc.blit(self.image,(sc_width/2-690,sc_height/2-450))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


play=Bird()
cloud=Clouds()
land =Land()
pipe=Pipe()
game=gameOver()

bird_mask = py.mask.from_surface(play.image)
pipe_mask = py.mask.from_surface(pipe.pipe)


def check_collision(bird_rect, pipes):
    for piper in pipes:
        pipe_rect = py.Rect(piper)
        if piper.y < 0:
            pipe_mask_flipped = py.mask.from_surface(py.transform.flip(pipe.pipe, False, True))
            offset = (pipe_rect.x - bird_rect.x, pipe_rect.y - bird_rect.y)
            if bird_mask.overlap(pipe_mask_flipped, offset):
                py.mixer.music.pause()
                collision_sound.play()
                return True
        elif(bird_rect.y<=0 or bird_rect.y>=sc_height):
                py.mixer.music.pause()
                collision_sound.play()
                return True
        else:
            offset = (pipe_rect.x - bird_rect.x, pipe_rect.y - bird_rect.y)
            if bird_mask.overlap(pipe_mask, offset):
                py.mixer.music.pause()
                collision_sound.play()
                return True
    return False




def main():
    bird_rect = play.bird_rect
    running = True
    m_paused=False
    font = py.font.Font(None, 36)
    pipes = []
    spawn_pipe_event = py.USEREVENT
    py.time.set_timer(spawn_pipe_event, 1600)
    global score
    score=0
    while running:
        #i+=1
        for event in py.event.get():
            if event.type == spawn_pipe_event:
                pipes.extend(pipe.create_pipe())
            if event.type == py.QUIT:
                running=False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    flap_sound.play()
                    play.jump()
                else:
                    running=True
        
        
        pipes=pipe.move_pipes(pipes) #move pipes
       
        
        play.gravity()
        prev_score=score
        for piper in pipes:
                if piper.right < bird_rect.left:
                    score += score_increment
                    if score > prev_score+65:
                        score_sound.play()

        #rgb values for screen background base
        sc.fill((0,200,225))
        cloud.draw()
        land.draw()
        play.draw()
        pipe.draw(pipes)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        sc.blit(score_text, (10, 10))
         # Check for collisions
        if check_collision(bird_rect, pipes):
            game.draw()
            py.display.update()
            
            py.time.wait(1000)
            over.play()
            py.time.wait(2000)
            running = False
       
        py.time.wait(10)
        py.display.update()
    py.quit()

if __name__ =="__main__":
    main()

