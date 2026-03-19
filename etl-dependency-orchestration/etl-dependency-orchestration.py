def schedule_pipeline(tasks, resource_budget):
    current_time = 0
    completed = set()
    running = [] # List of {"name", "end_time", "resources"}
    remaining = {t['name']: t for t in tasks}
    scheduled_output = []

    while remaining or running:
        # 1. Complete tasks
        still_running = []
        for r in running:
            if r['end_time'] <= current_time:
                completed.add(r['name'])
            else:
                still_running.append(r)
        running = still_running

        # 2. Find Ready tasks
        ready_names = []
        for name, t in remaining.items():
            if all(dep in completed for dep in t['depends_on']):
                ready_names.append(name)
        
        # 3. Sort Alphabetically
        ready_names.sort()

        # 4. Greedy Assign
        current_res = sum(r['resources'] for r in running)
        for name in ready_names:
            t = remaining[name]
            if current_res + t['resources'] <= resource_budget:
                scheduled_output.append((name, current_time))
                running.append({
                    "name": name, 
                    "end_time": current_time + t['duration'], 
                    "resources": t['resources']
                })
                current_res += t['resources']
                del remaining[name] # It's now scheduled

        # 5. Advance Time
        if running:
            current_time = min(r['end_time'] for r in running)
        else:
            break

    return sorted(scheduled_output, key=lambda x: (x[1], x[0]))