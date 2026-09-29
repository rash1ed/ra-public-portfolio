"""Deterministic workflow controls for operations/process portfolios."""
from __future__ import annotations

def validate_item(item, required=("id","category","priority")):
    missing=[k for k in required if not str(item.get(k,"")).strip()]
    return {"ok":not missing,"missing":missing}

def route_item(item, rules):
    category=str(item.get("category","")).lower()
    priority=str(item.get("priority","")).lower()
    for rule in rules:
        if rule.get("category","").lower() in ("*",category) and rule.get("priority","").lower() in ("*",priority):
            return rule["queue"]
    return "MANUAL_REVIEW"

def fan_out(item):
    actions=item.get("actions") or ["validate","report"]
    return [{"task_id":f"{item.get('id','UNKNOWN')}:{i+1}","action":a} for i,a in enumerate(actions)]

def approval_required(item):
    return bool(item.get("high_risk")) or float(item.get("amount",0) or 0)>=10000

def retry_delay_seconds(attempt, base=60, cap=1800):
    if attempt<1: raise ValueError("attempt must be >= 1")
    return min(base*(2**(attempt-1)),cap)

def run_workflow(item, rules):
    check=validate_item(item)
    if not check["ok"]:
        return {"status":"HOLD","reason":"MISSING_REQUIRED_FIELDS","missing":check["missing"]}
    queue=route_item(item,rules)
    tasks=fan_out(item)
    needs_approval=approval_required(item)
    return {
        "status":"WAITING_APPROVAL" if needs_approval else "READY",
        "queue":queue,
        "approval_required":needs_approval,
        "tasks":tasks,
        "recovery":{"max_attempts":3,"retry_delays":[retry_delay_seconds(i) for i in (1,2,3)]},
    }
