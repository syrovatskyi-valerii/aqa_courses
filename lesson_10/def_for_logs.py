def read_last_n_log_levels(log_file_path, n=3):
    levels = []
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[-n:]:
        parts = line.strip().split(" - ")
        if len(parts) >= 2:
            level = parts[1]
            levels.append(level)
    return levels

def clear_log_file():
    open("login_system.log", "w").close()