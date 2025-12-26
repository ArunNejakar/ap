import sys

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
    try:
        # Default values
        cameraId = "CAM_DEFAULT"
        requestHours = 5
        priority = 3
        existingHours = 10
        capacity = 50

        # Override defaults if arguments are provided
        if len(sys.argv) == 6:
            cameraId = sys.argv[1]
            requestHours = int(sys.argv[2])
            priority = int(sys.argv[3])
            existingHours = int(sys.argv[4])
            capacity = int(sys.argv[5])

        result = bookingDecision(requestHours, priority, existingHours, capacity)

        print("Camera ID      :", cameraId)
        print("Booking Status :", result)

    except ValueError:
        print("Error: All numeric arguments must be valid integers.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
