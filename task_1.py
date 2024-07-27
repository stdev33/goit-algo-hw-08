import heapq


def min_cost_to_connect_cables(cables):
    # Creating a minimal heap of cable lengths
    heapq.heapify(cables)

    total_cost = 0

    # While there is more than one cable in the pile
    while len(cables) > 1:
        # Pop out the two shortest cables
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)

        # The cost of connecting two shortest cables
        cost = first_min + second_min
        total_cost += cost

        # Push a new cable back to the heap
        heapq.heappush(cables, cost)

    return total_cost


def main():
    cables = [5, 4, 3, 7, 9, 11]
    print(f"The minimum amount of total costs: {min_cost_to_connect_cables(cables)}")


if __name__ == "__main__":
    main()
