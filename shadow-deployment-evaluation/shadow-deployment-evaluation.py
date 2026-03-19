def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    n = len(production_log)

    prod_correct = sum(1 for log in production_log if log['prediction'] == log['actual'])
    shad_correct = sum(1 for log in shadow_log if log['prediction'] == log['actual'])

    prod_acc = prod_correct / n
    shad_acc = shad_correct / n
    acc_gain = shad_acc - prod_acc

    latencies = sorted([log['latency_ms'] for log in shadow_log])
    p95_idx = math.ceil(0.95 * n) - 1
    p95_latency = latencies[p95_idx]

    agreements = sum(1 for p, s in zip(production_log, shadow_log) if p['prediction'] == s['prediction'])
    agreement_rate = agreements / n

    promote = (acc_gain >= criteria['min_accuracy_gain'] and p95_latency <= criteria['max_latency_p95'] and agreement_rate >= criteria['min_agreement_rate'])

    return {
        "promote": promote,
        "metrics": {
            "shadow_accuracy": shad_acc,
            "production_accuracy": prod_acc,
            "accuracy_gain": acc_gain,
            "shadow_latency_p95": p95_latency,
            "agreement_rate": agreement_rate
        }
    }