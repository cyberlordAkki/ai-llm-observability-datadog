# AI-Powered Security Log Analyzer with End-to-End Observability

## Overview
This project demonstrates an end-to-end observability strategy for an LLM-powered security log analysis application using Google Cloud Vertex AI (Gemini) and Datadog.

The system analyzes application and security logs using a Large Language Model to detect threats, classify severity, and provide mitigation insights, while streaming full runtime and LLM telemetry into Datadog for monitoring, alerting, and incident response.

## Problem Statement
Modern AI applications lack deep observability into LLM behavior, security risks, latency anomalies, and runtime failures. Engineers struggle to detect prompt abuse, hallucinations, and performance degradation in real time.

## Solution
An AI-driven log analysis service powered by Gemini, instrumented with Datadog to provide:
- Real-time LLM observability
- Security signal detection
- Automated alerts and incidents
- Actionable dashboards for AI engineers

## Architecture
1. Logs are ingested via an API hosted on Google Cloud Run
2. Gemini (Vertex AI) analyzes logs for threats and severity
3. Runtime, LLM, and security telemetry is streamed to Datadog
4. Datadog dashboards visualize system health
5. Detection rules trigger alerts and incidents with full context

## Google Cloud Usage
- Vertex AI (Gemini) for LLM inference
- Cloud Run for API hosting
- Cloud Logging for log ingestion

## Datadog Usage
- APM for request tracing
- Logs for security event analysis
- Metrics for LLM latency and token usage
- Detection rules for anomaly and threat detection
- Dashboards for observability
- Alerts and incidents for response actions

## Detection Rules
- High severity attack frequency spike
- LLM response latency anomaly
- Prompt injection pattern detection
- Error rate threshold breach

## Dashboard Metrics
- LLM request latency (p95)
- Error rate percentage
- Token consumption trends
- Attack severity distribution
- Alert timeline

## Future Enhancements
- Automated remediation actions
- Real-time streaming log ingestion
- Fine-grained prompt risk scoring

## License
MIT License
