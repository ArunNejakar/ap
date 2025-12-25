def bookingDecision(requestHours, priority, existingHours, capacity):
    if capacity <= 0:
        return "INVALID_CAPACITY"

    totalUsage = requestHours + existingHours
    riskScore = (totalUsage / capacity) * 100 - (priority * 5)

    if riskScore < 50:
        return "APPROVED"
    elif riskScore <= 75:
        return "CONDITIONAL"
    else:
        return "REJECTED"


def main():
    # Assertions similar to your C++ code
    assert bookingDecision(2, 5, 2, 10) == "APPROVED"
    assert bookingDecision(4, 2, 4, 10) == "CONDITIONAL"
    assert bookingDecision(6, 1, 5, 10) == "REJECTED"
    print("All tests passed!")


if __name__ == "__main__":
    main()