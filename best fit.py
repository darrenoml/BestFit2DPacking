class Rectangle:
    def __init__(self, width: int, height: int, id: int = None):
        self.width = width
        self.height = height
        self.id = id

class PackingProblem:
    def __init__(self, bin_width: int, bin_height: int):
        self.bin_width = bin_width
        self.bin_height = bin_height
        self.grid = [[0] * bin_width for _ in range(bin_height)]
        self.placed_rectangles = []

    def can_place(self, x: int, y: int, rect: Rectangle) -> bool:
        if x + rect.width > self.bin_width or y + rect.height > self.bin_height:
            return False

        for i in range(rect.height):
            for j in range(rect.width):
                if self.grid[y + i][x + j] != 0:
                    return False

        return True

    def place_rectangle(self, x: int, y: int, rect: Rectangle):
        for i in range(rect.height):
            for j in range(rect.width):
                self.grid[y + i][x + j] = rect.id

        self.placed_rectangles.append((rect, (x, y)))

    def best_fit(self, rectangles: list[Rectangle]):
        for i, rect in enumerate(rectangles):
            rect.id = i + 1 
            best_position = None
            min_waste = float('inf')

            for y in range(self.bin_height):
                for x in range(self.bin_width):
                    if self.can_place(x, y, rect):
                        waste = self.calculate_waste(x, y, rect)
                        if waste < min_waste:
                            min_waste = waste
                            best_position = (x, y)

            if best_position:
                self.place_rectangle(best_position[0], best_position[1], rect)
            else:
                print(f"Could not place Rectangle {rect.width}x{rect.height}")

    def calculate_waste(self, x: int, y: int, rect: Rectangle) -> int:
        temp_grid = [row[:] for row in self.grid]
        
        for i in range(rect.height):
            for j in range(rect.width):
                temp_grid[y + i][x + j] = rect.id

        return sum(row.count(0) for row in temp_grid)

    def gridler(self):
        print("Grid Layout:")
        for row in self.grid:
            print(" ".join(map(str, row)))
        
        print("\nRectangle Placements:")
        for rect, (x, y) in self.placed_rectangles:
            print(f"Rectangle {rect.width}x{rect.height} (ID: {rect.id}) placed at ({x}, {y})")

def main():
    rectangles = [
        Rectangle(4, 2),
        Rectangle(6, 3),
        Rectangle(3, 2),
    ]
    
    packing_problem = PackingProblem(bin_width=6, bin_height=6)
    packing_problem.best_fit(rectangles)
    packing_problem.gridler()

if __name__ == "__main__":
    main()
