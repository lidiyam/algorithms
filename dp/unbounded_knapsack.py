"""
We use a bottom-up ↴ approach to find the max value at our duffel bag's weight_capacity by finding the max value at every capacity from 0 to weight_capacity.

We allocate a list max_values_at_capacities where the indices are capacities and each value is the max value at that capacity.

For each capacity, we want to know the max monetary value we can carry. To figure that out, we go through each cake, checking to see if we should take that cake.

The best monetary value we can get if we take a given cake is simply:

that cake's value, plus
the best monetary value we can carry in our remaining duffel bag capacity after taking the cake—which we'll already have stored in max_values_at_capacities
To handle weights and values of zero, we return infinity only if a cake weighs nothing and has a positive value.
"""

def max_duffel_bag_value(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                max_value_using_cake = (
                    cake_value
                    + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]

"""
Complexity:
O(n∗k) time, and O(k)O(k) space, where nn is number of types of cake and kk is the capacity of the duffel bag. 
"""