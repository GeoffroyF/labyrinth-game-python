from services.commands import IUserCommand


class Quit(IUserCommand):
    def get_command_tag(self):
        return "quit"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        return True, state, "Finished"


class GoUp(IUserCommand):
    def get_command_tag(self):
        return "go-up"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        success, above_cell = player.move_up(labyrinth)
        return False, state, str(success) + ": " +str(above_cell)


class GoDown(IUserCommand):
    def get_command_tag(self):
        return "go-down"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        success, above_cell = player.move_down(labyrinth)
        return False, state, str(success) + ": " + str(above_cell)


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return "go-left"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        success, above_cell = player.move_left(labyrinth)
        return False, state, str(success) + ": " + str(above_cell)


class GoRight(IUserCommand):
    def get_command_tag(self):
        return "go-right"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        success, above_cell = player.move_right(labyrinth)
        return False, state, str(success) + ": " + str(above_cell)


class Skip(IUserCommand):
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        return False, state, "step executed"


class ShowLabyrinth(IUserCommand):
    def get_command_tag(self):
        return "show"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, labyrinth, player):
        print("hhh")
        print(labyrinth)
        labyrinth.show_labyrinth()
        return False, state, "labyrinth shown"
