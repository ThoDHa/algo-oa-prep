# [E-commerce Notification Router](https://www.fastprep.io/problems/amazon-ecommerce-notification-router)

**Easy** | **NN minutes** | **Array, String, Simulation**

Implement the routing decision for a batch of e-commerce notifications. For notification i, preferredChannels[i] is the user's preferred channel and priorities[i] is either NORMAL or URGENT.A NORMAL notification routes only to the user's preferred channel.An URGENT notification routes to all channels in the fixed order EMAIL, SMS, PUSH.Return one channel array per notification. Implement only the routing decisions; delivery handlers and delivery success are outside this task.

## Examples

### Example 1

**Input:** `preferredChannels = ["EMAIL","SMS","PUSH"]`
**Input:** `priorities = ["NORMAL","URGENT","NORMAL"]`

**Output:** `[["EMAIL"],["EMAIL","SMS","PUSH"],["PUSH"]]`

**Explanation:** The normal notifications use their preferences, while the urgent notification is sent through all three routing channels.

### Example 2

**Input:** `preferredChannels = ["PUSH"]`
**Input:** `priorities = ["URGENT"]`

**Output:** `[["EMAIL","SMS","PUSH"]]`

**Explanation:** Urgency overrides the preferred channel and selects every channel in canonical order.

### Example 3

**Input:** `preferredChannels = ["SMS","EMAIL"]`
**Input:** `priorities = ["NORMAL","NORMAL"]`

**Output:** `[["SMS"],["EMAIL"]]`

**Explanation:** Each normal notification produces exactly one route.

## Constraints

- `1 <= preferredChannels.length == priorities.length <= 10^5.Every preferred channel is EMAIL, SMS, or PUSH.Every priority is NORMAL or URGENT.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
