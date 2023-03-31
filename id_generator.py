class IDGenerator:
    current_id = 0

    def get_next_id(self: int) -> int:
        self.current_id += 1
        return self.current_id

    def get_previous_id(self: int) -> int:
        self.current_id -= 1
        return self.current_id
