"""Deterministic training and documentation planning helpers."""
from __future__ import annotations

REQUIRED = ("id", "topic", "owner", "audience")

def validate_module(module):
    missing = [k for k in REQUIRED if not str(module.get(k, "")).strip()]
    steps = module.get("steps") or []
    if not steps:
        missing.append("steps")
    return {"ok": not missing, "missing": missing}

def normalize_steps(steps):
    return [str(step).strip() for step in steps if str(step).strip()]

def review_required(module):
    return bool(module.get("policy_sensitive")) or str(module.get("audience", "")).lower() == "external"

def build_module(module):
    check = validate_module(module)
    if not check["ok"]:
        return {"status": "HOLD", "missing": check["missing"]}
    steps = normalize_steps(module["steps"])
    return {
        "status": "WAITING_REVIEW" if review_required(module) else "READY",
        "id": module["id"],
        "topic": module["topic"],
        "owner": module["owner"],
        "audience": module["audience"],
        "step_count": len(steps),
        "steps": steps,
        "review_required": review_required(module),
    }

def build_plan(modules):
    built = [build_module(m) for m in modules]
    return {
        "total": len(built),
        "ready": sum(x["status"] == "READY" for x in built),
        "waiting_review": sum(x["status"] == "WAITING_REVIEW" for x in built),
        "hold": sum(x["status"] == "HOLD" for x in built),
        "modules": built,
    }

def completion_rate(completed_steps, total_steps):
    if total_steps < 0 or completed_steps < 0:
        raise ValueError("step counts must be non-negative")
    if total_steps == 0:
        return None
    return round((completed_steps / total_steps) * 100, 1)
