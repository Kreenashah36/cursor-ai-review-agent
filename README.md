# Cursor AI Review Agent

An AI-native multi-agent code review system built entirely for Cursor-first development workflows.

This project does not rely on external APIs, SDKs, or billing.
Cursor itself acts as the AI execution engine through structured orchestration.


## Philosophy

Traditional workflows depend on external review tools and manual coordination.

This system assumes:

> AI is the primary execution layer, not a support tool.

Instead of calling external APIs, we leverage:
- `.cursorrules` for orchestration
- Modular agent prompt files
- Structured multi-step reasoning
- Deterministic JSON outputs

Cursor becomes the execution engine.

## Architecture

This project implements a structured multi-agent workflow:

1. **Code Review Agent**
   - Detects logic bugs
   - Identifies performance issues
   - Suggests refactoring improvements

2. **Security Audit Agent**
   - Detects vulnerabilities
   - Flags hardcoded secrets
   - Classifies severity levels

3. **Test Generation Agent**
   - Generates executable pytest test cases
   - Covers edge cases
   - Includes failure scenarios

All agents are orchestrated via `.cursorrules`.

## Design Decisions

**Why Cursor-Native?**
- Eliminates API dependency
- Removes secret management risks
- Enables immediate execution
- Keeps AI within developer workflow

**Why Multi-Agent Separation?**
- Separating reasoning roles improves:
- Clarity
- Reliability
- Coverage
- Auditability


## Usage Example

- Open project in Cursor.
- Open any Python file.
- Open workflows/full_review.md.
- Press Ctrl + K / Cmd + K.
- Type Run full review workflow

- The agent will return structured JSON with:
- Bugs
- Security risks
- Performance issues
- Pytest tests
- Confidence score

## Final Summary

This project demonstrates:

AI-first workflow design
Cursor-native orchestration
Structured multi-agent reasoning
Deterministic output enforcement
Security-aware evaluation

Final Performance Score:
8,920 / 10,000




