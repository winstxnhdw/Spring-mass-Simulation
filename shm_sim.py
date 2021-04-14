from vpython import *

class Spring:
    
    def __init__(self, mass, k, kd):
        
        # Simulation parameters
        self.time = 0
        self.dt = 1/60
        self.duration = 3600
        self.frameRate = 1 / dt
        self.pivot = vector(-10,0,0)
        self.equilibrium = vector(0,0,0)
        
        # Ball parameters
        ballPosition = vector(10, 0, 0)
        ballRadius = 1
        ballColour = color.blue
        self.ball = sphere(pos=ballPosition, radius=ballRadius, color=ballColour, m=mass, v=vector(0, 0 ,0))
        
        # Spring parameters
        springAxis = ballPosition - pivot
        springRadius = 0.5
        springCoils = 20
        springThickness = 0.1
        springColour = color.red
        self.spring = helix(pos=pivot, axis=springAxis, radius=springRadius, coils=springCoils, constant=k, thickness=springThickness, color=springColour)
        
    def motion(self, k, kd, currentTime, dt, equilibrium):
        
        friction = - kd * self.ball.v
        force = (self.spring.constant * (equilibrium - self.ball.pos)) + friction
        acceleration = force / self.ball.m
        self.ball.v = self.ball.v + (acceleration * dt)
        self.ball.pos = self.ball.pos + (self.ball.v * dt)
        self.spring.axis = self.ball.pos - self.spring.pos
        currentTime += dt
        
        print("Force: {}".format(force))
        print("Acceleration: {}".format(acceleration))
        print("Friction: {}".format(friction))
        print("Velocity: {}\n".format(self.ball.v))
        
        return currentTime
    
def main():
    
    try:
        mass = float(input("\nMass of the sphere: "))
        k = float(input("Spring constant: "))
        kd = float(input("Viscous damping coefficient: "))
        
    except ValueError:
        print("Invalid input.")
        main()
    
    physics = Spring(mass, k, kd)

    while physics.time <= physics.duration:
        rate(physics.frameRate)
        physics.time = physics.motion(k, kd, physics.time, physics.dt, physics.equilibrium)

if __name__ == "__main__":
    main()
