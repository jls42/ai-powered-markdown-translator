#!/usr/bin/env python3
"""Quota Codex de l'abonnement, sans rien consommer : `codex app-server` en
JSON-RPC sur stdin, `initialize` puis `account/rateLimits/read`.
Ne lit ni n'écrit ~/.codex/auth.json : c'est le CLI qui s'authentifie.

    python3 .claude/skills/aipmt-tour-modeles/scripts/quota_codex.py
"""

import json
import os
import subprocess  # nosec B404 — lance `codex app-server`, argv fixe
import sys

# Les clés d'API sont retirées : le CLI doit répondre pour l'abonnement.
ENV = {k: v for k, v in os.environ.items() if not k.endswith("_API_KEY")}


def main():
    proc = subprocess.Popen(
        ["codex", "app-server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        env=ENV,
    )

    def send(payload):
        proc.stdin.write(json.dumps(payload) + "\n")
        proc.stdin.flush()

    def read(expected_id):
        for line in proc.stdout:
            try:
                message = json.loads(line)
            except ValueError:
                continue
            if message.get("id") == expected_id:
                return message
        return {}

    try:
        send(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {"clientInfo": {"name": "aipmt-quota", "version": "1"}},
            }
        )
        read(1)
        send({"jsonrpc": "2.0", "method": "initialized"})
        send({"jsonrpc": "2.0", "id": 2, "method": "account/rateLimits/read"})
        answer = read(2)
    finally:
        proc.stdin.close()
        proc.terminate()
        proc.wait(timeout=10)
    if "error" in answer or "result" not in answer:
        print("lecture impossible :", json.dumps(answer)[:300])
        return 1
    limits = answer["result"].get("rateLimits", answer["result"])
    for name in ("primary", "secondary"):
        window = limits.get(name) or {}
        print(
            f"{name}: utilisé {window.get('usedPercent')} % | fenêtre {window.get('windowDurationMins')} min | remise à zéro {window.get('resetsAt')}"
        )
    print("limite atteinte :", limits.get("rateLimitReachedType"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
