import tkinter as tk
import random

class SnakeGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Snake Game")
        self.geometry("400x400")
        self.score = 0

        self.canvas = tk.Canvas(self, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(20, 20), (20, 40), (20, 60)] # Initial snake body
        self.food = self.generate_food()

        self.direction = "Right" # Initial direction

        self.bind("<Key>", self.change_direction)

        self.draw_objects()
        self.move_snake()

    def draw_objects(self):
        self.canvas.delete("all")
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", anchor="nw")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")

    def generate_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        else: # Right
            new_head = (head[0] + 20, head[1])

        # Check if snake hits the wall
        if new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400:
            self.game_over()
            return

        # Check if snake eats the food
        if new_head == self.food:
            self.score += 1
            self.snake.insert(0, new_head)
            self.food = self.generate_food()
        else:
            self.snake.pop()
            self.snake.insert(0, new_head)

        # Check if snake hits itself
        if len(set(self.snake)) != len(self.snake):
            self.game_over()
            return

        self.draw_objects()
        self.after(100, self.move_snake)

    def game_over(self):
        self.canvas.create_text(200, 200, text=f"Game Over! Score: {self.score}", fill="white", font=("Arial", 20), anchor="center")
        self.unbind("<Key>") # Disable key events

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()