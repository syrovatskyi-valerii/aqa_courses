from datetime import datetime

def analyze_heartbeat(logfile='hblog.txt', key='TSTFEED0300|7E3E|0400', output_log='hb_test.log'):
    filtered_log = []
    with open(logfile, 'r') as f:
        for line in f:
            if key in line:
                filtered_log.append(line.strip())

    timestamps = []
    for line in filtered_log:
        pos = line.find("Timestamp ")
        if pos != -1:
            time_str = line[pos + len("Timestamp "):pos + len("Timestamp ") + 8]

            try:
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                timestamps.append((time_obj, line))
            except ValueError:
                pass

    timestamps.sort(key=lambda x: x[0])

    with open(output_log, 'w') as logfile:
        for i in range(len(timestamps) - 1):
            current_time, current_line = timestamps[i]
            next_time, _ = timestamps[i + 1]

            diff = (next_time - current_time).total_seconds()

            if 31 < diff < 33:
                logfile.write(f"WARNING: Heartbeat = {diff:.3f} seconds at {current_time.strftime('%H:%M:%S')}\n")
            elif diff >= 33:
                logfile.write(f"ERROR: Heartbeat = {diff:.3f} seconds at {current_time.strftime('%H:%M:%S')}\n")

analyze_heartbeat()
