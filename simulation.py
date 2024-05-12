import pygame
import random
import time

# Initialize PyGame
pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smart Traffic Management System Simulation")

# Load the background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Resize if needed

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Vehicle class for West Lane:
class VehicleWest:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 30
        self.color = random.choice([(0, 0, 255), (255, 0, 127), (255, 128, 0)])  # Random vehicle color

    def move(self, traffic_light):
        if ((traffic_light.state == "red") and (self.x<(screen_width/2))):
            return  # Don't move if light is red
        self.x += self.speed  # Move to the right

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Vehicle class for East Lane:
class VehicleEast:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 30
        self.color = random.choice([(0, 0, 255), (255, 0, 127), (255, 128, 0)])  # Random vehicle color

    def move(self, traffic_light):
        if ((traffic_light.state == "red") and (self.x>screen_width/2)):
            return  # Don't move if light is red
        self.x -= self.speed  # Move to the left

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Vehicle class for North Lane:
class VehicleNorth:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 30
        self.height = 50
        self.color = random.choice([(0, 0, 255), (255, 0, 127), (255, 128, 0)])  # Random vehicle color

    def move(self, traffic_light):
        if ((traffic_light.state == "red") and (self.y<(screen_height/2))):
            return  # Don't move if light is red
        self.y += self.speed  # Move towards South

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Vehicle class for South Lane:
class VehicleSouth:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 30
        self.height = 50
        self.color = random.choice([(0, 0, 255), (255, 0, 127), (255, 128, 0)])  # Random vehicle color

    def move(self, traffic_light):
        if ((traffic_light.state == "red") and (self.y>(screen_height/2))):
            return  # Don't move if light is red
        self.y -= self.speed  # Move towards South

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Traffic light class
class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "green"  # Initial state

    def currTime():
        return time.time()

    def makeGreen(self):
        self.state = "green"
    def makeRed(self):
        self.state = "red"

    def draw(self, screen):
        color = green if self.state is "green" else yellow if self.state is "yellow" else red
        pygame.draw.circle(screen, color, (self.x, self.y), 20)

# Vehicle list
vehiclesWest = []
vehiclesSouth= []
vehiclesNorth= []
vehiclesEast= []

# Traffic light
traffic_light_South = TrafficLight(500, 500)
traffic_light_North = TrafficLight(325,100)
traffic_light_West= TrafficLight(200,250)
traffic_light_East=TrafficLight(700,375)

last_time=time.time()
cnt=0
duration=0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running is False

    # Generate new vehicles randomly
    if random.random() < 0.01:  # 1% chance each frame
        vehiclesWest.append(VehicleWest(0,275,2))
    if random.random() < 0.01:  # 1% chance each frame
        vehiclesEast.append(VehicleEast(1019,315,2))
    if random.random() < 0.01:  # 1% chance each frame
        vehiclesNorth.append(VehicleNorth(375,31,2))
    if random.random() < 0.01:  # 1% chance each frame
        vehiclesSouth.append(VehicleSouth(425,500,2))

    if((time.time()-last_time)>duration):
        cntWest=0
        cntEast=0
        cntNorth=0
        cntSouth=0
        for v in vehiclesWest:
            if(v.x<(screen_width/2)):
                cntWest=cntWest+1
        for v in vehiclesEast:
            if(v.x>(screen_width/2)):
                cntEast=cntEast+1
        for v in vehiclesNorth:
            if(v.y<(screen_height/2)):
                cntNorth=cntNorth+1
        for v in vehiclesSouth:
            if(v.y>(screen_height/2)):
                cntSouth=cntSouth+1
        if(cnt%4==0):
            if(cntSouth>5):
                duration=25
            else:
                duration=5*cntSouth
            traffic_light_South.makeGreen()
            traffic_light_West.makeRed()
            traffic_light_North.makeRed()
            traffic_light_East.makeRed()
        elif(cnt%4==1):
            if(cntWest>5):
                duration=25
            else:
                duration=5*cntWest
            traffic_light_South.makeRed()
            traffic_light_West.makeGreen()
            traffic_light_North.makeRed()
            traffic_light_East.makeRed()
        elif(cnt%4==2):
            if(cntNorth>5):
                duration=25
            else:
                duration=5*cntNorth
            traffic_light_South.makeRed()
            traffic_light_West.makeRed()
            traffic_light_North.makeGreen()
            traffic_light_East.makeRed()
        else:
            if(cntEast>5):
                duration=25
            else:
                duration=5*cntEast
            traffic_light_South.makeRed()
            traffic_light_West.makeRed()
            traffic_light_North.makeRed()
            traffic_light_East.makeGreen()
        last_time=time.time()
        cnt=cnt+1

    # Clear the screen
    screen.fill(white)
    
    # Draw the background image
    screen.blit(background_image, (0, 0))  # Draw the background on the screen
    
    # Draw traffic light
    traffic_light_West.draw(screen)
    traffic_light_East.draw(screen)
    traffic_light_North.draw(screen)
    traffic_light_South.draw(screen)

    # Move and draw vehicles
    for vehicle in vehiclesWest:
        vehicle.move(traffic_light_West)  # Move based on traffic light
        vehicle.draw(screen)
    for vehicle in vehiclesEast:
        vehicle.move(traffic_light_East)  # Move based on traffic light
        vehicle.draw(screen)
    for vehicle in vehiclesNorth:
        vehicle.move(traffic_light_North)  # Move based on traffic light
        vehicle.draw(screen)
    for vehicle in vehiclesSouth:
        vehicle.move(traffic_light_South)  # Move based on traffic light
        vehicle.draw(screen)

    # Remove vehicles that have exited the screenWidth
    vehiclesWest = [v for v in vehiclesWest if v.x < screen_width]
    vehiclesEast = [v for v in vehiclesEast if v.x > 0]
    vehiclesNorth = [v for v in vehiclesNorth if v.y > 0]
    vehiclesSouth = [v for v in vehiclesSouth if v.y < screen_height]

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(50)
pygame.quit()
