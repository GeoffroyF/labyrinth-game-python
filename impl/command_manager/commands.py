from services.commands import IUserCommand


class Quit(IUserCommand):
    def get_command_tag(self):
        return "quit"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        return True, "Finished"


class GoUp(IUserCommand):
    def get_command_tag(self):
        return "go-up"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_up(labyrinth)
        player.pick_up_object(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoDown(IUserCommand):
    def get_command_tag(self):
        return "go-down"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_down(labyrinth)
        player.pick_up_object(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return "go-left"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_left(labyrinth)
        player.pick_up_object(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoRight(IUserCommand):
    def get_command_tag(self):
        return "go-right"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_right(labyrinth)
        player.pick_up_object(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class Skip(IUserCommand):
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        return False, "step executed"


class ShowLabyrinth(IUserCommand):
    def get_command_tag(self):
        return "show"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        labyrinth.show_labyrinth()
        return False, "labyrinth shown"
