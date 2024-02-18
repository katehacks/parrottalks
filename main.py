import pygame
import random
import time

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 626
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Parrot Talks")
clock = pygame.time.Clock()
lastTime = time.time()

font = pygame.font.Font(None, 40)

messages = ["Press the space bar to progress the dialogue. Hold the key down to walk.", "Great job!", "You must think that you're the character in the middle of the screen.", "Well. No. That's actually Lilly.", "In this game, you are the pet parrot of Lilly.", "Lilly had a rough day.", "She's had a rough day for the past few years.", "Sometimes, Lilly says mean things to herself.", "As her special pet parrot, you must remind Lilly that she is incredible and strong!", "Click the space bar to help Lilly!", "I never do anything right.", "You are human. Your mistakes do not define you.", "If I am hopeless today, I will be hopeless forever.", "Every day is a new day. You are always evolving.", "People stare at me. It's because my teeth are crooked.", "People tend to focus on their own insecurities. You are beautiful."]
activeMessage = 0
message = messages[activeMessage]
messageLetter = font.render("", True, "white")

messageCounter = 0
messageSpeed = 3
messageDone = False

#Sprite List
parrotCawOriginal = pygame.image.load("parrotCaw.png")
parrotStillOriginal = pygame.image.load("parrotStill.png")
parrotStillMugshotOriginal = pygame.image.load("stillMugshot.png")
player1 = pygame.image.load("Player_1.png")
player2 = pygame.image.load("Player_2.png")
player3 = pygame.image.load("Player_3.png")
player4 = pygame.image.load("Player_4.png")
player5 = pygame.image.load("Player_5.png")
playerMugshotOriginal = pygame.image.load("playerMugshot.png")

#animation list for player walking
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animationListPlayerWalk = []
        self.is_animating = False
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #2
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #3
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #4
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #5
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #6
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #7
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #8
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #9
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #10
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)
        #11
        self.animationListPlayerWalk.append(player1Resized)
        self.animationListPlayerWalk.append(player2Resized)
        self.animationListPlayerWalk.append(player3Resized)
        self.animationListPlayerWalk.append(player4Resized)
        self.animationListPlayerWalk.append(player5Resized)

        self.currentPlayerWalkSprite = 0
        self.image = self.animationListPlayerWalk[self.currentPlayerWalkSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def animate(self):
        self.is_animating = True
    def update(self):
        if self.is_animating == True:
            self.currentPlayerWalkSprite += 0.2
        if self.currentPlayerWalkSprite >= len(self.animationListPlayerWalk):
            self.currentPlayerWalkSprite = 0
            self.is_animating = False
        self.image = self.animationListPlayerWalk[int(self.currentPlayerWalkSprite)]

#Resized Sprites
parrotCawResized = pygame.transform.scale(parrotCawOriginal, (138, 94.5))
parrotStillResized = pygame.transform.scale(parrotStillOriginal, (138, 94.5))
parrotStillMugshotResized = pygame.transform.scale(parrotStillMugshotOriginal, (130, 130))
player1Resized = pygame.transform.scale(player1, (700, 700))
player2Resized = pygame.transform.scale(player2, (700, 700))
player3Resized = pygame.transform.scale(player3, (700, 700))
player4Resized = pygame.transform.scale(player4, (700, 700))
player5Resized = pygame.transform.scale(player5, (700, 700))
playerMugshot = pygame.transform.scale(playerMugshotOriginal, (130, 130))
#Flipped Sprites
parrotCaw = pygame.transform.flip(parrotCawResized, True, False)
parrotStill = pygame.transform.flip(parrotStillResized, True, False)
parrotStillMugshot = pygame.transform.flip(parrotStillMugshotResized, True, False)
#Background Sprites
backgroundOriginalSize = pygame.image.load("background.png")
background = pygame.transform.scale(backgroundOriginalSize, (1200, 626))

running = True
scene1Unplayed = True
scene2Unplayed = True
screen_shake = 0
render_offset = [0, 0]

moving_sprites = pygame.sprite.Group()
playerWalkingWidth = -500
player = Player(playerWalkingWidth, 285)
moving_sprites.add(player)
vel = 10
test = True

while running:
    dt = time.time() - lastTime
    dt *= 60
    lastTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
        if event.type == pygame.USEREVENT: message.update()
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_SPACE] and test == True:
            player.rect.x += vel
            playerWalkingWidth += vel
            player.update()
            if player.rect.x > 10:
                test = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and scene1Unplayed == True:
                player.animate()
                scene1Unplayed = False
            if event.key == pygame.K_SPACE and messageDone and activeMessage < len(messages) - 1:
                activeMessage += 1
                messageDone = False
                message = messages[activeMessage]
                messageWidth = messageLetter.get_width()
                messageCounter = 0
                if activeMessage == len(messages) - 1:
                    scene2Unplayed = True

    else:
        screen.blit(background, render_offset)
        screen.blit(parrotStill, (930, 310))
        if messageCounter < messageSpeed * len(message):
            messageCounter += 1
        elif messageCounter >= messageSpeed * len(message):
            messageDone = True
            # Check if the final message has finished displaying
            if activeMessage == len(messages) - 1 and messageCounter >= messageSpeed * len(message):
                scene2Unplayed = False
        messageLetter = font.render(message[0:messageCounter//messageSpeed], True, "white")
        messageLetterRect = messageLetter.get_rect()
        messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
        if activeMessage == 10:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 550)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 500
            render_offset = [0, 0]
        elif activeMessage == 11:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 0
            render_offset = [0, 0]
        if activeMessage == 12:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 550)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 500
            render_offset = [0, 0]
        elif activeMessage == 13:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 0
            render_offset = [0, 0]
        if activeMessage == 14:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 550)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 500
            render_offset = [0, 0]
        elif activeMessage == 15:
            pygame.draw.rect(screen, "white", (1050, 0, 150, 150))
            pygame.draw.rect(screen, "white", (0, 496, 150, 150))
            messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
            screen.blit(messageLetter, messageLetterRect)
            screen.blit(parrotStillMugshot, (1070, 20))
            screen.blit(playerMugshot, (0, 496))
            screen_shake = 0
            render_offset = [0, 0]
        elif activeMessage < 10:
            messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
            screen.blit(messageLetter, messageLetterRect)


        if screen_shake > 0:
            screen_shake -= 1
        if screen_shake:
            render_offset[0] = random.randint(0, 8) - 4
            render_offset[1] = random.randint(0, 8) - 4
        moving_sprites.draw(screen)
        moving_sprites.update()
        pygame.display.flip()
        clock.tick(60)
        continue
    break
pygame.quit()

