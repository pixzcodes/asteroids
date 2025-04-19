import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Returns true or false.
    # Collision between circles is checked by the
    # distance between the center of the two circles
    # and the radius of the circles.
    # If the distance is less than the radius then
    # the circles are colliding.
    def checkCollision(self, circleShapeObj):
        dist = self.position.distance_to(circleShapeObj.position)

        total_radius = self.radius + circleShapeObj.radius

        if dist <= total_radius:
            return True
        else:
            return False
