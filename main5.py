total_dolls = 0

class Matryoshka:
    doll_count = 0
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.inner_doll = None
        global total_dolls
        total_dolls += 1
        Matryoshka.doll_count += 1
    
    def add_inner_doll(self, name, size):
        def validate_size(new_size):
            return new_size < self.size
        
        if validate_size(size):
            if self.inner_doll is None:
                self.inner_doll = Matryoshka(name, size)
                return True
            else:
                return self.inner_doll.add_inner_doll(name, size)
        else:
            return False
    
    def display_dolls(self, level=0):
        def print_with_count():
            nonlocal level
            print("  " * level + f"Matryoshka '{self.name}' (size: {self.size})")
        
        print_with_count()
        if self.inner_doll:
            self.inner_doll.display_dolls(level + 1)

def main():
    biggest_doll = Matryoshka("Большая Матрёшка", 10)
    
    biggest_doll.add_inner_doll("Средняя Матрёшка", 7)
    biggest_doll.add_inner_doll("Маленькая Матрёшка", 5)
    biggest_doll.add_inner_doll("Крошечная Матрёшка", 3)
    
    print("\nMatryoshka Doll Structure:")
    print("------------------------")
    biggest_doll.display_dolls()
    
    print("\nStatistics:")
    print(f"Total dolls created (global count): {total_dolls}")
    print(f"Class-level doll count: {Matryoshka.doll_count}")

if __name__ == "__main__":
    main()