from turtle import Turtle

# Constants for snake configuration
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    'UP': 90,
    'DOWN': 270,
    'RIGHT': 0,
    'LEFT': 180
}

class Snake:
    """Handles snake creation, movement, and growth"""
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # First segment is head
    
    def create_snake(self):
        """Create initial snake body"""
        for position in STARTING_POSITION:
            self.add_segment(position)

            
    def add_segment(self, position):
        """Add new body segment"""
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """Reset the segment"""
        for seg in self.segments:  # Clear the previous segment 
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        """Add new segment when food is eaten"""
        self.add_segment(self.segments[-1].position())

        
    def move(self):
        """Move snake forward continuously"""
        # Move each segment to position of previous segment
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Direction control methods
    def up(self):
        if self.head.heading() != DIRECTIONS['DOWN']:
            self.head.setheading(DIRECTIONS['UP'])
    
    def down(self):
        if self.head.heading() != DIRECTIONS['UP']:
            self.head.setheading(DIRECTIONS['DOWN'])
    
    def right(self):
        if self.head.heading() != DIRECTIONS['LEFT']:
            self.head.setheading(DIRECTIONS['RIGHT'])
    
    def left(self):
        if self.head.heading() != DIRECTIONS['RIGHT']:
            self.head.setheading(DIRECTIONS['LEFT'])
