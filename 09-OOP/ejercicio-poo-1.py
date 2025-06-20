# Ejercicio 1
# Crear una clase Serie (título, capítulos, finalizada, capítulos_vistos)
# Añadirle las funcionalidades siguientes:
# - Ver capítulo
# - Obtener los capítulos restantes
# - Obtener si ya la hemos visto

class Serie:

    def __init__(self, title, episodes, finished, seen_episodes):
        self.title = title
        self.episodes = episodes
        self.finished = finished
        self.seen_episodes = seen_episodes


    def watch_episode(self):
        if self.seen_episodes >= self.episodes:
            return f"You've already completed {self.title}..."
        else:
            self.seen_episodes += 1
            return "done."


    def get_remaining_chapters_to_see(self):
        if self.seen_episodes >= self.episodes: return f"You've already completed {self.title}..."
        else: return self.episodes - self.seen_episodes


    def get_whether_finished(self):
        if self.seen_episodes == self.episodes: return "Yeah youre done."
        else: return f"you're not done yet... you still got {self.episodes - self.seen_episodes} to go."