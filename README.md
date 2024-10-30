readme_content = """
# Retry Strategies in Python

This project demonstrates various retry strategies implemented in Python, focusing on improving the resilience and reliability of systems. Each retry strategy is designed to handle failures differently, based on common patterns used in distributed systems.

## Table of Contents
- [Overview](#overview)
- [Retry Strategies](#retry-strategies)
  - [Immediate Retry](#immediate-retry)
  - [Fixed Interval Retry](#fixed-interval-retry)
  - [Exponential Backoff Retry](#exponential-backoff-retry)
  - [Exponential Backoff with Jitter](#exponential-backoff-with-jitter)
  - [Fibonacci Backoff](#fibonacci-backoff)
  - [Status Code-Based Retry](#status-code-based-retry)
  - [Retry with Max Attempts](#retry-with-max-attempts)
  - [Circuit Breaker](#circuit-breaker)
  - [Token Bucket Retry](#token-bucket-retry)
  - [Rate Limit Retry](#rate-limit-retry)
  - [Bulkhead Pattern](#bulkhead-pattern)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains implementations of several retry patterns, each tailored for different failure scenarios. The goal is to provide a robust framework that adapts to various error-handling needs, whether it's dealing with transient errors, limiting retries, or controlling the rate of retries.

## Retry Strategies

### Immediate Retry
- Retries are made immediately after a failure, without any delay.
- This strategy is simple but can lead to high loads if failures persist.

### Fixed Interval Retry
- Retries are made at a fixed interval, e.g., every 2 seconds.
- Useful for scenarios where failures are temporary and periodic retries are sufficient.

### Exponential Backoff Retry
- The delay between retries increases exponentially, e.g., 1s, 2s, 4s, 8s, etc.
- Helps to reduce the load on failing systems, allowing time for recovery.

### Exponential Backoff with Jitter
- Similar to exponential backoff, but with added random jitter to prevent "thundering herd" problems.
- Adds randomness to the delay to distribute retry attempts more evenly.

### Fibonacci Backoff
- Retries are based on the Fibonacci sequence, e.g., 1s, 1s, 2s, 3s, 5s, etc.
- An alternative backoff strategy that distributes retries differently.

### Status Code-Based Retry
- Retries are triggered only for specific HTTP status codes (e.g., 500, 502, 503, 504).
- Useful for differentiating between transient and permanent errors.

### Retry with Max Attempts
- Limits the number of retry attempts to a specified maximum.
- Prevents infinite retry loops and resource overconsumption.

### Circuit Breaker
- Stops retries if the failure threshold is reached, entering an "open" state.
- Allows time for the system to recover before further retries are attempted.

### Token Bucket Retry
- Controls the rate of retries using a token bucket algorithm.
- Limits the frequency of retry attempts, ensuring that retries don't exceed a defined rate.

### Rate Limit Retry
- Retries are limited by rate, ensuring that the system is not overwhelmed by too many requests in a short time.
- Useful for APIs and services with strict rate limits.

### Bulkhead Pattern
- Isolates retries into compartments to prevent failures from affecting the entire system.
- Ensures that retries are distributed across different threads or processes, reducing overall impact.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retry-strategies.git
