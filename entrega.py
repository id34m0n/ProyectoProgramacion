import random
import math

def generarCardumen(n, w, h, speed=10):
	boids = []
	for i in range(n):
		x, y		= random.randint(1, w), random.randint(1, h)
		course		= random.uniform(-1, 1)
		vx, vy		= random.randint(1, speed)/speed, random.randint(1, speed)/speed
		boids.append(
			[
				[x, y],		# 0 [0, 1]
				[vx, vy],	# 1 [0, 1]
			])
	return boids

def distancia(i, j):
	return i*j

def corregir(boid, width, height, border=25):
	return boid

def moveCloser(fish, boids):
        if len(boids) < 1: return
            
        x = 0
        y = 0
        for boid in boids:
            if boids.x == fish.x and boids.y == fish.y:
                continue
                
            X += (fish.x - boid.x)
            Y += (fish.y - boid.y)

        X /= len(boids)
        Y /= len(boids)

def moveWith(fish, boids):

        velocidad = 10
        if len(boids) < 1: return

        X = 0
        Y = 0
                
        for boid in boids:
            X += boid.velocidadX
            Y += boid.velocidadY

        X /= len(boids)
        Y /= len(boids)

        fish.velocidadX = fish.velocidadY + (X / 40)
        fish.velocidadY = fish.velocidadY + (Y / 40)

def moveAway(fish, boids, minDistancia): # SEPARATION
        if len(boids) < 1: return

        distanciaX = 0
        distanciaY = 0
        numC = 0

        for boid in boids:
                distancia = fish.distancia(boid)
                if distancia < minDistancia:
                        numC = numC + 1
                        xS = fish.x - boid.x
                        yS = fish.y - boid.y
                        if xS >= 0:
                                xS = match.sqrt(minDistancia) - xS
                        elif xS < 0:
                                xS = -match.sqrt(minDistancia) - xS

                        if yS >= 0:
                                yS = match.sqrt(minDitancia) - yS
                        elif yS < 0:
                                yS = -match.sqrt(minDitancia) - yS

                        distanciaX = distanciaX + xS
                        distanciaY = distanciaY + yS

def move(fish):
        
        velocidad = 10
        
        if abs(fish.velocidadX) > maxVelocidad or abs(fish.velocidadY) > maxVelocidad:
            escala = maxVelocidad / max(abs(fish.velocidadX), abs(fish.velocidadY))
            fish.velocidadX = (fish.velocidadX * escala)
            fish.velocidadY = (fish.velocidadY * escala)
        
        fish.x = (fish.x + fish.velocidadX)
        fish.y = (fish.y + fish.velocidadY)

def vecindad(pez_i, boids, max_distance):
	return boids
