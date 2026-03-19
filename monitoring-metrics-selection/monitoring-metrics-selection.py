def compute_monitoring_metrics(system_type, y_true, y_pred):
    metrics = []
    n = len(y_true)

    if system_type == "classification":
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
        tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
        
        acc = (tp + tn) / n
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0
        
        metrics = [("accuracy", acc), ("precision", prec), ("recall", rec), ("f1", f1)]

    elif system_type == "regression":
        mae = sum(abs(t - p) for t, p in zip(y_true, y_pred)) / n
        mse = sum((t - p)**2 for t, p in zip(y_true, y_pred)) / n
        rmse = mse**0.5
        metrics = [("mae", mae), ("rmse", rmse)]

    elif system_type == "ranking":
        # Sort by predicted score descending
        combined = sorted(zip(y_pred, y_true), key=lambda x: x[0], reverse=True)
        top_3 = combined[:3]
        
        rel_in_top_3 = sum(1 for _, label in top_3 if label == 1)
        total_rel = sum(y_true)
        
        p_at_3 = rel_in_top_3 / 3
        r_at_3 = rel_in_top_3 / total_rel if total_rel > 0 else 0.0
        metrics = [("precision_at_3", p_at_3), ("recall_at_3", r_at_3)]

    # Always return sorted alphabetically by metric name
    return sorted(metrics, key=lambda x: x[0])