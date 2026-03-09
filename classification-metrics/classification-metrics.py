import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    classes = np.unique(np.concatenate([y_true, y_pred]))
    
    # 1. Accuracy (Global)
    accuracy = np.mean(y_true == y_pred)
    
    # 2. Per-class metrics
    per_class = {}
    for cls in classes:
        tp = np.sum((y_true == cls) & (y_pred == cls))
        fp = np.sum((y_true != cls) & (y_pred == cls))
        fn = np.sum((y_true == cls) & (y_pred != cls))
        support = np.sum(y_true == cls)
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        per_class[cls] = {"p": precision, "r": recall, "f1": f1, "s": support, "tp": tp, "fp": fp, "fn": fn}

    # 3. Averaging Logic
    if average == "binary":
        metrics = per_class.get(pos_label, {"p": 0.0, "r": 0.0, "f1": 0.0})
        return {"accuracy": float(accuracy), "precision": float(metrics["p"]), 
                "recall": float(metrics["r"]), "f1": float(metrics["f1"])}

    if average == "micro":
        total_tp = sum(v["tp"] for v in per_class.values())
        total_fp = sum(v["fp"] for v in per_class.values())
        total_fn = sum(v["fn"] for v in per_class.values())
        
        p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
        r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
        f1 = 2 * (p * r) / (p + r) if (p + r) > 0 else 0.0
        return {"accuracy": float(accuracy), "precision": float(p), "recall": float(r), "f1": float(f1)}

    # Macro and Weighted
    ps, rs, f1s, weights = [], [], [], []
    for cls in classes:
        ps.append(per_class[cls]["p"])
        rs.append(per_class[cls]["r"])
        f1s.append(per_class[cls]["f1"])
        weights.append(per_class[cls]["s"])
        
    if average == "macro":
        return {"accuracy": float(accuracy), "precision": float(np.mean(ps)), 
                "recall": float(np.mean(rs)), "f1": float(np.mean(f1s))}
    
    if average == "weighted":
        w = np.array(weights) / np.sum(weights)
        return {"accuracy": float(accuracy), "precision": float(np.average(ps, weights=w)), 
                "recall": float(np.average(rs, weights=w)), "f1": float(np.average(f1s, weights=w))}