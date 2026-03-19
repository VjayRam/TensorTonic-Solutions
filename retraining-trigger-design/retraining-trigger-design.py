def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """
    retrain_days = []
    current_budget = config['budget']
    days_since_retrain = 0
    last_retrain_day = -config['cooldown'] # Ensures day 1 is valid
    
    for stat in daily_stats:
        day = stat['day']
        days_since_retrain += 1
        
        # 1. Identify Triggers
        drift_trigger = stat['drift_score'] > config['drift_threshold']
        perf_trigger = stat['performance'] < config['performance_threshold']
        stale_trigger = days_since_retrain >= config['max_staleness']
        
        if drift_trigger or perf_trigger or stale_trigger:
            # 2. Check Constraints
            cooldown_ok = (day - last_retrain_day) >= config['cooldown']
            budget_ok = current_budget >= config['retrain_cost']
            
            if cooldown_ok and budget_ok:
                # 3. Retrain
                retrain_days.append(day)
                days_since_retrain = 0
                current_budget -= config['retrain_cost']
                last_retrain_day = day
                
    return retrain_days