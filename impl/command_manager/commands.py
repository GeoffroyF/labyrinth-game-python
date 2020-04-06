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
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoDown(IUserCommand):
    def get_command_tag(self):
        return "go-down"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_down(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return "go-left"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_left(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoRight(IUserCommand):
    def get_command_tag(self):
        return "go-right"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_right(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class Skip(IUserCommand):
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        player.execute_cell_action(labyrinth)
        return False, "step executed"


class GoUpShort(GoUp):
    def get_command_tag(self):
        return "z"


class GoDownShort(GoDown):
    def get_command_tag(self):
        return "s"


class GoLeftShort(GoLeft):
    def get_command_tag(self):
        return "q"


class GoRightShort(GoRight):
    def get_command_tag(self):
        return "d"


class ShowLabyrinth(IUserCommand):
    def get_command_tag(self):
        return "show"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        labyrinth.show_labyrinth()
        return False, "labyrinth shown"
