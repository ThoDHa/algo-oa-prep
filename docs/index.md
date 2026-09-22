# Algo OA Prep Solutions

A study guide spanning three curated problem banks: the [Grind 75](https://www.techinterviewhandbook.org/grind75) and the [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) LeetCode lists, merged into one unified problem table below, and the [Amazon OA](problems/amazon_oa/index.md) bank in its own table. Problems on both LeetCode tracks appear once, credited to each. Each problem page covers the statement and examples, with constraints where available. The [pattern intuition guides](patterns/index.md) explain the mental models behind the recurring algorithm patterns, and the [`practice/`](https://github.com/ThoDHa/algo-oa-prep/tree/main/practice) workspace lets you implement and test each solution yourself.

!!! tip "New to algorithms or interviews?"

    Start with the [Foundations](foundations/index.md) section. It teaches the prerequisites the problem pages assume, Big-O notation, recursion, the core data structures, and a method for approaching any problem, all from zero. For the plan around the problems, time budgeting, and the non-coding rounds, see the [Interview Prep](interview_prep/index.md) section.

Use the navigation sidebar or the tables below.

<!-- unified-leetcode:start -->
## Problem List

The unified LeetCode problem set across the [Grind 75](https://www.techinterviewhandbook.org/grind75) and the [NeetCode 150](https://neetcode.io/practice/practice/neetcode150): 168 unique problems, 59 on both tracks and credited to each. Grind 75 study order first, then the NeetCode-only problems in track order. Tracks names the plan(s) a problem belongs to; Time carries the Grind 75 suggested minutes and stays empty for NeetCode-only problems.

| # | Problem | Difficulty | Category | Tracks | Time |
|---|---------|------------|----------|--------|------|
| [1](https://leetcode.com/problems/two-sum/) | [Two Sum](problems/two_sum.md) | Easy | Array, Hash Table | Grind 75 + NeetCode 150 | 15 minutes |
| [2](https://leetcode.com/problems/valid-parentheses/) | [Valid Parentheses](problems/valid_parentheses.md) | Easy | Stack, String | Grind 75 + NeetCode 150 | 20 minutes |
| [3](https://leetcode.com/problems/merge-two-sorted-lists/) | [Merge Two Sorted Lists](problems/merge_two_sorted_lists.md) | Easy | Linked List | Grind 75 + NeetCode 150 | 20 minutes |
| [4](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Best Time to Buy and Sell Stock](problems/best_time_to_buy_and_sell_stock.md) | Easy | Array | Grind 75 + NeetCode 150 | 20 minutes |
| [5](https://leetcode.com/problems/valid-palindrome/) | [Valid Palindrome](problems/valid_palindrome.md) | Easy | String | Grind 75 + NeetCode 150 | 15 minutes |
| [6](https://leetcode.com/problems/invert-binary-tree/) | [Invert Binary Tree](problems/invert_binary_tree.md) | Easy | Tree | Grind 75 + NeetCode 150 | 15 minutes |
| [7](https://leetcode.com/problems/valid-anagram/) | [Valid Anagram](problems/valid_anagram.md) | Easy | String | Grind 75 + NeetCode 150 | 15 minutes |
| [8](https://leetcode.com/problems/binary-search/) | [Binary Search](problems/binary_search.md) | Easy | Binary Search | Grind 75 + NeetCode 150 | 15 minutes |
| [9](https://leetcode.com/problems/flood-fill/) | [Flood Fill](problems/flood_fill.md) | Easy | Graph, DFS | Grind 75 | 20 minutes |
| [10](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Lowest Common Ancestor of a BST](problems/lowest_common_ancestor_of_a_binary_search_tree.md) | Medium | Tree | Grind 75 + NeetCode 150 | 20 minutes |
| [11](https://leetcode.com/problems/balanced-binary-tree/) | [Balanced Binary Tree](problems/balanced_binary_tree.md) | Easy | Tree | Grind 75 + NeetCode 150 | 15 minutes |
| [12](https://leetcode.com/problems/linked-list-cycle/) | [Linked List Cycle](problems/linked_list_cycle.md) | Easy | Linked List | Grind 75 + NeetCode 150 | 20 minutes |
| [13](https://leetcode.com/problems/implement-queue-using-stacks/) | [Implement Queue using Stacks](problems/implement_queue_using_stacks.md) | Easy | Stack | Grind 75 | 20 minutes |
| [14](https://leetcode.com/problems/first-bad-version/) | [First Bad Version](problems/first_bad_version.md) | Easy | Binary Search | Grind 75 | 20 minutes |
| [15](https://leetcode.com/problems/ransom-note/) | [Ransom Note](problems/ransom_note.md) | Easy | Hash Table | Grind 75 | 15 minutes |
| [16](https://leetcode.com/problems/climbing-stairs/) | [Climbing Stairs](problems/climbing_stairs.md) | Easy | Dynamic Programming | Grind 75 + NeetCode 150 | 20 minutes |
| [17](https://leetcode.com/problems/longest-palindrome/) | [Longest Palindrome](problems/longest_palindrome.md) | Easy | String | Grind 75 | 20 minutes |
| [18](https://leetcode.com/problems/reverse-linked-list/) | [Reverse Linked List](problems/reverse_linked_list.md) | Easy | Linked List | Grind 75 + NeetCode 150 | 20 minutes |
| [19](https://leetcode.com/problems/majority-element/) | [Majority Element](problems/majority_element.md) | Easy | Array | Grind 75 | 20 minutes |
| [20](https://leetcode.com/problems/add-binary/) | [Add Binary](problems/add_binary.md) | Easy | String | Grind 75 | 15 minutes |
| [21](https://leetcode.com/problems/diameter-of-binary-tree/) | [Diameter of Binary Tree](problems/diameter_of_binary_tree.md) | Easy | Tree | Grind 75 + NeetCode 150 | 30 minutes |
| [22](https://leetcode.com/problems/middle-of-the-linked-list/) | [Middle of the Linked List](problems/middle_of_the_linked_list.md) | Easy | Linked List | Grind 75 | 20 minutes |
| [23](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Maximum Depth of Binary Tree](problems/maximum_depth_of_binary_tree.md) | Easy | Tree | Grind 75 + NeetCode 150 | 15 minutes |
| [24](https://leetcode.com/problems/contains-duplicate/) | [Contains Duplicate](problems/contains_duplicate.md) | Easy | Array | Grind 75 + NeetCode 150 | 15 minutes |
| [25](https://leetcode.com/problems/maximum-subarray/) | [Maximum Subarray](problems/maximum_subarray.md) | Medium | Array, Dynamic Programming | Grind 75 + NeetCode 150 | 20 minutes |
| [26](https://leetcode.com/problems/insert-interval/) | [Insert Interval](problems/insert_interval.md) | Medium | Array | Grind 75 + NeetCode 150 | 25 minutes |
| [27](https://leetcode.com/problems/01-matrix/) | [01 Matrix](problems/01_matrix.md) | Medium | BFS | Grind 75 | 30 minutes |
| [28](https://leetcode.com/problems/k-closest-points-to-origin/) | [K Closest Points to Origin](problems/k_closest_points_to_origin.md) | Medium | Heap | Grind 75 + NeetCode 150 | 30 minutes |
| [29](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Longest Substring Without Repeating Characters](problems/longest_substring_without_repeating_characters.md) | Medium | String | Grind 75 + NeetCode 150 | 30 minutes |
| [30](https://leetcode.com/problems/3sum/) | [3Sum](problems/3sum.md) | Medium | Array | Grind 75 + NeetCode 150 | 30 minutes |
| [31](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Binary Tree Level Order Traversal](problems/binary_tree_level_order_traversal.md) | Medium | Tree | Grind 75 + NeetCode 150 | 20 minutes |
| [32](https://leetcode.com/problems/clone-graph/) | [Clone Graph](problems/clone_graph.md) | Medium | Graph | Grind 75 + NeetCode 150 | 25 minutes |
| [33](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Evaluate Reverse Polish Notation](problems/evaluate_reverse_polish_notation.md) | Medium | Stack | Grind 75 + NeetCode 150 | 30 minutes |
| [34](https://leetcode.com/problems/course-schedule/) | [Course Schedule](problems/course_schedule.md) | Medium | Graph | Grind 75 + NeetCode 150 | 30 minutes |
| [35](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Implement Trie (Prefix Tree)](problems/implement_trie_prefix_tree.md) | Medium | Trie | Grind 75 + NeetCode 150 | 35 minutes |
| [36](https://leetcode.com/problems/coin-change/) | [Coin Change](problems/coin_change.md) | Medium | Dynamic Programming | Grind 75 + NeetCode 150 | 25 minutes |
| [37](https://leetcode.com/problems/product-of-array-except-self/) | [Product of Array Except Self](problems/product_of_array_except_self.md) | Medium | Array | Grind 75 + NeetCode 150 | 30 minutes |
| [38](https://leetcode.com/problems/min-stack/) | [Minimum Stack](problems/min_stack.md) | Medium | Stack | Grind 75 + NeetCode 150 | 20 minutes |
| [39](https://leetcode.com/problems/validate-binary-search-tree/) | [Validate Binary Search Tree](problems/validate_binary_search_tree.md) | Medium | Tree | Grind 75 + NeetCode 150 | 20 minutes |
| [40](https://leetcode.com/problems/number-of-islands/) | [Number of Islands](problems/number_of_islands.md) | Medium | Graph | Grind 75 + NeetCode 150 | 25 minutes |
| [41](https://leetcode.com/problems/rotting-oranges/) | [Rotting Oranges](problems/rotting_oranges.md) | Medium | BFS | Grind 75 + NeetCode 150 | 30 minutes |
| [42](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Search in Rotated Sorted Array](problems/search_in_rotated_sorted_array.md) | Medium | Binary Search | Grind 75 + NeetCode 150 | 30 minutes |
| [43](https://leetcode.com/problems/combination-sum/) | [Combination Sum](problems/combination_sum.md) | Medium | Backtracking | Grind 75 + NeetCode 150 | 30 minutes |
| [44](https://leetcode.com/problems/permutations/) | [Permutations](problems/permutations.md) | Medium | Backtracking | Grind 75 + NeetCode 150 | 30 minutes |
| [45](https://leetcode.com/problems/merge-intervals/) | [Merge Intervals](problems/merge_intervals.md) | Medium | Sorting | Grind 75 + NeetCode 150 | 30 minutes |
| [46](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Lowest Common Ancestor of a Binary Tree](problems/lowest_common_ancestor_of_a_binary_tree.md) | Medium | Tree | Grind 75 | 25 minutes |
| [47](https://leetcode.com/problems/time-based-key-value-store/) | [Time Based Key-Value Store](problems/time_based_key_value_store.md) | Medium | Binary Search | Grind 75 + NeetCode 150 | 35 minutes |
| [48](https://leetcode.com/problems/accounts-merge/) | [Accounts Merge](problems/accounts_merge.md) | Medium | Graph | Grind 75 | 30 minutes |
| [49](https://leetcode.com/problems/sort-colors/) | [Sort Colors](problems/sort_colors.md) | Medium | Array | Grind 75 | 25 minutes |
| [50](https://leetcode.com/problems/word-break/) | [Word Break](problems/word_break.md) | Medium | Dynamic Programming | Grind 75 + NeetCode 150 | 30 minutes |
| [51](https://leetcode.com/problems/partition-equal-subset-sum/) | [Partition Equal Subset Sum](problems/partition_equal_subset_sum.md) | Medium | Dynamic Programming | Grind 75 + NeetCode 150 | 30 minutes |
| [52](https://leetcode.com/problems/string-to-integer-atoi/) | [String to Integer (atoi)](problems/string_to_integer_atoi.md) | Medium | String | Grind 75 | 25 minutes |
| [53](https://leetcode.com/problems/spiral-matrix/) | [Spiral Matrix](problems/spiral_matrix.md) | Medium | Array | Grind 75 + NeetCode 150 | 25 minutes |
| [54](https://leetcode.com/problems/subsets/) | [Subsets](problems/subsets.md) | Medium | Backtracking | Grind 75 + NeetCode 150 | 30 minutes |
| [55](https://leetcode.com/problems/binary-tree-right-side-view/) | [Binary Tree Right Side View](problems/binary_tree_right_side_view.md) | Medium | Tree | Grind 75 + NeetCode 150 | 20 minutes |
| [56](https://leetcode.com/problems/longest-palindromic-substring/) | [Longest Palindromic Substring](problems/longest_palindromic_substring.md) | Medium | String | Grind 75 + NeetCode 150 | 25 minutes |
| [57](https://leetcode.com/problems/unique-paths/) | [Unique Paths](problems/unique_paths.md) | Medium | Dynamic Programming | Grind 75 + NeetCode 150 | 20 minutes |
| [58](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Construct Binary Tree from Preorder and Inorder Traversal](problems/construct_binary_tree_from_preorder_and_inorder_traversal.md) | Medium | Tree | Grind 75 + NeetCode 150 | 25 minutes |
| [59](https://leetcode.com/problems/container-with-most-water/) | [Container With Most Water](problems/container_with_most_water.md) | Medium | Array | Grind 75 + NeetCode 150 | 35 minutes |
| [60](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [Letter Combinations of a Phone Number](problems/letter_combinations_of_a_phone_number.md) | Medium | Backtracking | Grind 75 + NeetCode 150 | 30 minutes |
| [61](https://leetcode.com/problems/word-search/) | [Word Search](problems/word_search.md) | Medium | Backtracking | Grind 75 + NeetCode 150 | 30 minutes |
| [62](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [Find All Anagrams in a String](problems/find_all_anagrams_in_a_string.md) | Medium | String | Grind 75 | 30 minutes |
| [63](https://leetcode.com/problems/minimum-height-trees/) | [Minimum Height Trees](problems/minimum_height_trees.md) | Medium | Graph | Grind 75 | 30 minutes |
| [64](https://leetcode.com/problems/task-scheduler/) | [Task Scheduler](problems/task_scheduler.md) | Medium | Heap | Grind 75 + NeetCode 150 | 35 minutes |
| [65](https://leetcode.com/problems/lru-cache/) | [LRU Cache](problems/lru_cache.md) | Medium | Linked List | Grind 75 + NeetCode 150 | 30 minutes |
| [66](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Kth Smallest Element in a BST](problems/kth_smallest_element_in_a_bst.md) | Medium | Tree | Grind 75 + NeetCode 150 | 25 minutes |
| [67](https://leetcode.com/problems/minimum-window-substring/) | [Minimum Window Substring](problems/minimum_window_substring.md) | Hard | String | Grind 75 + NeetCode 150 | 30 minutes |
| [68](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Serialize and Deserialize Binary Tree](problems/serialize_and_deserialize_binary_tree.md) | Hard | Tree | Grind 75 + NeetCode 150 | 40 minutes |
| [69](https://leetcode.com/problems/trapping-rain-water/) | [Trapping Rain Water](problems/trapping_rain_water.md) | Hard | Stack | Grind 75 + NeetCode 150 | 35 minutes |
| [70](https://leetcode.com/problems/find-median-from-data-stream/) | [Find Median from Data Stream](problems/find_median_from_data_stream.md) | Hard | Heap | Grind 75 + NeetCode 150 | 30 minutes |
| [71](https://leetcode.com/problems/word-ladder/) | [Word Ladder](problems/word_ladder.md) | Hard | BFS | Grind 75 + NeetCode 150 | 45 minutes |
| [72](https://leetcode.com/problems/basic-calculator/) | [Basic Calculator](problems/basic_calculator.md) | Hard | Stack | Grind 75 | 40 minutes |
| [73](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | [Maximum Profit in Job Scheduling](problems/maximum_profit_in_job_scheduling.md) | Hard | Binary Search | Grind 75 | 45 minutes |
| [74](https://leetcode.com/problems/merge-k-sorted-lists/) | [Merge k Sorted Lists](problems/merge_k_sorted_lists.md) | Hard | Linked List | Grind 75 + NeetCode 150 | 30 minutes |
| [75](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Largest Rectangle in Histogram](problems/largest_rectangle_in_histogram.md) | Hard | Stack | Grind 75 + NeetCode 150 | 35 minutes |
| - | [Binary Tree Maximum Path Sum](problems/binary_tree_maximum_path_sum.md) | - | - | Grind 75 + NeetCode 150 | - |
| - | [Maximum Frequency Stack](problems/maximum_frequency_stack.md) | - | - | Grind 75 | - |
| [4](https://leetcode.com/problems/group-anagrams/) | [Group Anagrams](problems/group_anagrams.md) | Medium | Arrays & Hashing | NeetCode 150 |  |
| [5](https://leetcode.com/problems/top-k-frequent-elements/) | [Top K Frequent Elements](problems/top_k_frequent_elements.md) | Medium | Arrays & Hashing | NeetCode 150 |  |
| [6](https://leetcode.com/problems/encode-and-decode-strings/) | [Encode and Decode Strings](problems/encode_and_decode_strings.md) | Medium | Arrays & Hashing | NeetCode 150 |  |
| [8](https://leetcode.com/problems/valid-sudoku/) | [Valid Sudoku](problems/valid_sudoku.md) | Medium | Arrays & Hashing | NeetCode 150 |  |
| [9](https://leetcode.com/problems/longest-consecutive-sequence/) | [Longest Consecutive Sequence](problems/longest_consecutive_sequence.md) | Medium | Arrays & Hashing | NeetCode 150 |  |
| [11](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Two Sum II Input Array Is Sorted](problems/two_sum_ii_input_array_is_sorted.md) | Medium | Two Pointers | NeetCode 150 |  |
| [17](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Longest Repeating Character Replacement](problems/longest_repeating_character_replacement.md) | Medium | Sliding Window | NeetCode 150 |  |
| [18](https://leetcode.com/problems/permutation-in-string/) | [Permutation In String](problems/permutation_in_string.md) | Medium | Sliding Window | NeetCode 150 |  |
| [20](https://leetcode.com/problems/sliding-window-maximum/) | [Sliding Window Maximum](problems/sliding_window_maximum.md) | Hard | Sliding Window | NeetCode 150 |  |
| [24](https://leetcode.com/problems/daily-temperatures/) | [Daily Temperatures](problems/daily_temperatures.md) | Medium | Stack | NeetCode 150 |  |
| [25](https://leetcode.com/problems/car-fleet/) | [Car Fleet](problems/car_fleet.md) | Medium | Stack | NeetCode 150 |  |
| [28](https://leetcode.com/problems/search-a-2d-matrix/) | [Search a 2D Matrix](problems/search_a_2d_matrix.md) | Medium | Binary Search | NeetCode 150 |  |
| [29](https://leetcode.com/problems/koko-eating-bananas/) | [Koko Eating Bananas](problems/koko_eating_bananas.md) | Medium | Binary Search | NeetCode 150 |  |
| [30](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Find Minimum In Rotated Sorted Array](problems/find_minimum_in_rotated_sorted_array.md) | Medium | Binary Search | NeetCode 150 |  |
| [33](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Median of Two Sorted Arrays](problems/median_of_two_sorted_arrays.md) | Hard | Binary Search | NeetCode 150 |  |
| [37](https://leetcode.com/problems/reorder-list/) | [Reorder List](problems/reorder_list.md) | Medium | Linked List | NeetCode 150 |  |
| [38](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Remove Nth Node From End of List](problems/remove_nth_node_from_end_of_list.md) | Medium | Linked List | NeetCode 150 |  |
| [39](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Copy List With Random Pointer](problems/copy_list_with_random_pointer.md) | Medium | Linked List | NeetCode 150 |  |
| [40](https://leetcode.com/problems/add-two-numbers/) | [Add Two Numbers](problems/add_two_numbers.md) | Medium | Linked List | NeetCode 150 |  |
| [41](https://leetcode.com/problems/find-the-duplicate-number/) | [Find The Duplicate Number](problems/find_the_duplicate_number.md) | Medium | Linked List | NeetCode 150 |  |
| [44](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Reverse Nodes In K Group](problems/reverse_nodes_in_k_group.md) | Hard | Linked List | NeetCode 150 |  |
| [49](https://leetcode.com/problems/same-tree/) | [Same Tree](problems/same_tree.md) | Easy | Trees | NeetCode 150 |  |
| [50](https://leetcode.com/problems/subtree-of-another-tree/) | [Subtree of Another Tree](problems/subtree_of_another_tree.md) | Easy | Trees | NeetCode 150 |  |
| [54](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Count Good Nodes In Binary Tree](problems/count_good_nodes_in_binary_tree.md) | Medium | Trees | NeetCode 150 |  |
| [60](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Kth Largest Element In a Stream](problems/kth_largest_element_in_a_stream.md) | Easy | Heap / Priority Queue | NeetCode 150 |  |
| [61](https://leetcode.com/problems/last-stone-weight/) | [Last Stone Weight](problems/last_stone_weight.md) | Easy | Heap / Priority Queue | NeetCode 150 |  |
| [63](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Kth Largest Element In An Array](problems/kth_largest_element_in_an_array.md) | Medium | Heap / Priority Queue | NeetCode 150 |  |
| [65](https://leetcode.com/problems/design-twitter/) | [Design Twitter](problems/design_twitter.md) | Medium | Heap / Priority Queue | NeetCode 150 |  |
| [69](https://leetcode.com/problems/combination-sum-ii/) | [Combination Sum II](problems/combination_sum_ii.md) | Medium | Backtracking | NeetCode 150 |  |
| [71](https://leetcode.com/problems/subsets-ii/) | [Subsets II](problems/subsets_ii.md) | Medium | Backtracking | NeetCode 150 |  |
| [72](https://leetcode.com/problems/generate-parentheses/) | [Generate Parentheses](problems/generate_parentheses.md) | Medium | Backtracking | NeetCode 150 |  |
| [74](https://leetcode.com/problems/palindrome-partitioning/) | [Palindrome Partitioning](problems/palindrome_partitioning.md) | Medium | Backtracking | NeetCode 150 |  |
| [76](https://leetcode.com/problems/n-queens/) | [N Queens](problems/n_queens.md) | Hard | Backtracking | NeetCode 150 |  |
| [78](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [Design Add And Search Words Data Structure](problems/design_add_and_search_words_data_structure.md) | Medium | Tries | NeetCode 150 |  |
| [79](https://leetcode.com/problems/word-search-ii/) | [Word Search II](problems/word_search_ii.md) | Hard | Tries | NeetCode 150 |  |
| [81](https://leetcode.com/problems/max-area-of-island/) | [Max Area of Island](problems/max_area_of_island.md) | Medium | Graphs | NeetCode 150 |  |
| [83](https://leetcode.com/problems/walls-and-gates/) | [Walls And Gates](problems/walls_and_gates.md) | Medium | Graphs | NeetCode 150 |  |
| [85](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Pacific Atlantic Water Flow](problems/pacific_atlantic_water_flow.md) | Medium | Graphs | NeetCode 150 |  |
| [86](https://leetcode.com/problems/surrounded-regions/) | [Surrounded Regions](problems/surrounded_regions.md) | Medium | Graphs | NeetCode 150 |  |
| [88](https://leetcode.com/problems/course-schedule-ii/) | [Course Schedule II](problems/course_schedule_ii.md) | Medium | Graphs | NeetCode 150 |  |
| [89](https://leetcode.com/problems/graph-valid-tree/) | [Graph Valid Tree](problems/graph_valid_tree.md) | Medium | Graphs | NeetCode 150 |  |
| [90](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Number of Connected Components In An Undirected Graph](problems/number_of_connected_components_in_an_undirected_graph.md) | Medium | Graphs | NeetCode 150 |  |
| [91](https://leetcode.com/problems/redundant-connection/) | [Redundant Connection](problems/redundant_connection.md) | Medium | Graphs | NeetCode 150 |  |
| [93](https://leetcode.com/problems/network-delay-time/) | [Network Delay Time](problems/network_delay_time.md) | Medium | Advanced Graphs | NeetCode 150 |  |
| [94](https://leetcode.com/problems/reconstruct-itinerary/) | [Reconstruct Itinerary](problems/reconstruct_itinerary.md) | Hard | Advanced Graphs | NeetCode 150 |  |
| [95](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Min Cost to Connect All Points](problems/min_cost_to_connect_all_points.md) | Medium | Advanced Graphs | NeetCode 150 |  |
| [96](https://leetcode.com/problems/swim-in-rising-water/) | [Swim In Rising Water](problems/swim_in_rising_water.md) | Hard | Advanced Graphs | NeetCode 150 |  |
| [97](https://leetcode.com/problems/alien-dictionary/) | [Alien Dictionary](problems/alien_dictionary.md) | Hard | Advanced Graphs | NeetCode 150 |  |
| [98](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [Cheapest Flights Within K Stops](problems/cheapest_flights_within_k_stops.md) | Medium | Advanced Graphs | NeetCode 150 |  |
| [100](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Min Cost Climbing Stairs](problems/min_cost_climbing_stairs.md) | Easy | 1-D Dynamic Programming | NeetCode 150 |  |
| [101](https://leetcode.com/problems/house-robber/) | [House Robber](problems/house_robber.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [102](https://leetcode.com/problems/house-robber-ii/) | [House Robber II](problems/house_robber_ii.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [104](https://leetcode.com/problems/palindromic-substrings/) | [Palindromic Substrings](problems/palindromic_substrings.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [105](https://leetcode.com/problems/decode-ways/) | [Decode Ways](problems/decode_ways.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [107](https://leetcode.com/problems/maximum-product-subarray/) | [Maximum Product Subarray](problems/maximum_product_subarray.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [109](https://leetcode.com/problems/longest-increasing-subsequence/) | [Longest Increasing Subsequence](problems/longest_increasing_subsequence.md) | Medium | 1-D Dynamic Programming | NeetCode 150 |  |
| [112](https://leetcode.com/problems/longest-common-subsequence/) | [Longest Common Subsequence](problems/longest_common_subsequence.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [113](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [Best Time to Buy And Sell Stock With Cooldown](problems/best_time_to_buy_and_sell_stock_with_cooldown.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [114](https://leetcode.com/problems/coin-change-ii/) | [Coin Change II](problems/coin_change_ii.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [115](https://leetcode.com/problems/target-sum/) | [Target Sum](problems/target_sum.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [116](https://leetcode.com/problems/interleaving-string/) | [Interleaving String](problems/interleaving_string.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [117](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Longest Increasing Path In a Matrix](problems/longest_increasing_path_in_a_matrix.md) | Hard | 2-D Dynamic Programming | NeetCode 150 |  |
| [118](https://leetcode.com/problems/distinct-subsequences/) | [Distinct Subsequences](problems/distinct_subsequences.md) | Hard | 2-D Dynamic Programming | NeetCode 150 |  |
| [119](https://leetcode.com/problems/edit-distance/) | [Edit Distance](problems/edit_distance.md) | Medium | 2-D Dynamic Programming | NeetCode 150 |  |
| [120](https://leetcode.com/problems/burst-balloons/) | [Burst Balloons](problems/burst_balloons.md) | Hard | 2-D Dynamic Programming | NeetCode 150 |  |
| [121](https://leetcode.com/problems/regular-expression-matching/) | [Regular Expression Matching](problems/regular_expression_matching.md) | Hard | 2-D Dynamic Programming | NeetCode 150 |  |
| [123](https://leetcode.com/problems/jump-game/) | [Jump Game](problems/jump_game.md) | Medium | Greedy | NeetCode 150 |  |
| [124](https://leetcode.com/problems/jump-game-ii/) | [Jump Game II](problems/jump_game_ii.md) | Medium | Greedy | NeetCode 150 |  |
| [125](https://leetcode.com/problems/gas-station/) | [Gas Station](problems/gas_station.md) | Medium | Greedy | NeetCode 150 |  |
| [126](https://leetcode.com/problems/hand-of-straights/) | [Hand of Straights](problems/hand_of_straights.md) | Medium | Greedy | NeetCode 150 |  |
| [127](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [Merge Triplets to Form Target Triplet](problems/merge_triplets_to_form_target_triplet.md) | Medium | Greedy | NeetCode 150 |  |
| [128](https://leetcode.com/problems/partition-labels/) | [Partition Labels](problems/partition_labels.md) | Medium | Greedy | NeetCode 150 |  |
| [129](https://leetcode.com/problems/valid-parenthesis-string/) | [Valid Parenthesis String](problems/valid_parenthesis_string.md) | Medium | Greedy | NeetCode 150 |  |
| [132](https://leetcode.com/problems/non-overlapping-intervals/) | [Non Overlapping Intervals](problems/non_overlapping_intervals.md) | Medium | Intervals | NeetCode 150 |  |
| [133](https://leetcode.com/problems/meeting-rooms/) | [Meeting Rooms](problems/meeting_rooms.md) | Easy | Intervals | NeetCode 150 |  |
| [134](https://leetcode.com/problems/meeting-rooms-ii/) | [Meeting Rooms II](problems/meeting_rooms_ii.md) | Medium | Intervals | NeetCode 150 |  |
| [135](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | [Minimum Interval to Include Each Query](problems/minimum_interval_to_include_each_query.md) | Hard | Intervals | NeetCode 150 |  |
| [136](https://leetcode.com/problems/rotate-image/) | [Rotate Image](problems/rotate_image.md) | Medium | Math & Geometry | NeetCode 150 |  |
| [138](https://leetcode.com/problems/set-matrix-zeroes/) | [Set Matrix Zeroes](problems/set_matrix_zeroes.md) | Medium | Math & Geometry | NeetCode 150 |  |
| [139](https://leetcode.com/problems/happy-number/) | [Happy Number](problems/happy_number.md) | Easy | Math & Geometry | NeetCode 150 |  |
| [140](https://leetcode.com/problems/plus-one/) | [Plus One](problems/plus_one.md) | Easy | Math & Geometry | NeetCode 150 |  |
| [141](https://leetcode.com/problems/powx-n/) | [Pow(x, n)](problems/powx_n.md) | Medium | Math & Geometry | NeetCode 150 |  |
| [142](https://leetcode.com/problems/multiply-strings/) | [Multiply Strings](problems/multiply_strings.md) | Medium | Math & Geometry | NeetCode 150 |  |
| [143](https://leetcode.com/problems/detect-squares/) | [Detect Squares](problems/detect_squares.md) | Medium | Math & Geometry | NeetCode 150 |  |
| [144](https://leetcode.com/problems/single-number/) | [Single Number](problems/single_number.md) | Easy | Bit Manipulation | NeetCode 150 |  |
| [145](https://leetcode.com/problems/number-of-1-bits/) | [Number of 1 Bits](problems/number_of_1_bits.md) | Easy | Bit Manipulation | NeetCode 150 |  |
| [146](https://leetcode.com/problems/counting-bits/) | [Counting Bits](problems/counting_bits.md) | Easy | Bit Manipulation | NeetCode 150 |  |
| [147](https://leetcode.com/problems/reverse-bits/) | [Reverse Bits](problems/reverse_bits.md) | Easy | Bit Manipulation | NeetCode 150 |  |
| [148](https://leetcode.com/problems/missing-number/) | [Missing Number](problems/missing_number.md) | Easy | Bit Manipulation | NeetCode 150 |  |
| [149](https://leetcode.com/problems/sum-of-two-integers/) | [Sum of Two Integers](problems/sum_of_two_integers.md) | Medium | Bit Manipulation | NeetCode 150 |  |
| [150](https://leetcode.com/problems/reverse-integer/) | [Reverse Integer](problems/reverse_integer.md) | Medium | Bit Manipulation | NeetCode 150 |  |
<!-- unified-leetcode:end -->


<!-- amazon-oa:start -->
## Amazon OA Problems

The Amazon OA coding bank, separate from the LeetCode tables above: 350 Amazon-tagged online-assessment problems, most recently updated first. The problems come from [perixtar/Tech-OA-Interview-Questions](https://github.com/perixtar/Tech-OA-Interview-Questions) with statement pages on [FastPrep](https://www.fastprep.io). The full bank index with companies lives at [problems/amazon_oa/index.md](problems/amazon_oa/index.md); practice stubs live under the [`practice/amazon_oa/`](https://github.com/ThoDHa/algo-oa-prep/tree/main/practice/amazon_oa) workspace.

| # | Problem | Updated |
|---|---------|---------|
| 1 | [Maximize Adjacent Difference With One Reversal](problems/amazon_oa/amazon-maximize-adjacent-difference-with-one-reversal.md) | 2026-09-19 |
| 2 | [Shortest Grid Path With One Wall Break](problems/amazon_oa/amazon-shortest-grid-path-with-one-wall-break.md) | 2026-09-19 |
| 3 | [Course Order and Cycle](problems/amazon_oa/amazon-course-order-and-cycle.md) | 2026-09-18 |
| 4 | [Inventory Allocation](problems/amazon_oa/amazon-inventory-allocation.md) | 2026-09-18 |
| 5 | [LRU Cache for Query Results](problems/amazon_oa/amazon-lru-query-result-cache.md) | 2026-09-18 |
| 6 | [Minimum Stick Connection Cost](problems/amazon_oa/amazon-minimum-stick-connection-cost.md) | 2026-09-18 |
| 7 | [First Non-Repeating Character](problems/amazon_oa/amazon-first-non-repeating-character.md) | 2026-09-14 |
| 8 | [Root-to-Leaf Paths with a Target Sum](problems/amazon_oa/amazon-root-to-leaf-target-sum-paths.md) | 2026-09-14 |
| 9 | [Aggressive Cows](problems/amazon_oa/amazon-aggressive-cows.md) | 2026-09-13 |
| 10 | [All Anagram Start Indices](problems/amazon_oa/amazon-anagram-start-indices.md) | 2026-09-13 |
| 11 | [Basic Calculator](problems/amazon_oa/amazon-basic-calculator.md) | 2026-09-13 |
| 12 | [Largest Binary-String Subset Within Bit Budgets](problems/amazon_oa/amazon-binary-strings-bounded-subset.md) | 2026-09-13 |
| 13 | [Binary Tree Cameras](problems/amazon_oa/amazon-binary-tree-cameras.md) | 2026-09-13 |
| 14 | [Binary Tree Right View](problems/amazon_oa/amazon-binary-tree-right-view.md) | 2026-09-13 |
| 15 | [Calculate Beauty Values](problems/amazon_oa/amazon-calculate-beauty-values.md) | 2026-09-13 |
| 16 | [Capacity To Ship Packages Within D Days](problems/amazon_oa/amazon-capacity-to-ship-packages-within-d-days.md) | 2026-09-13 |
| 17 | [Cheapest Flights Within K Stops](problems/amazon_oa/amazon-cheapest-flights-within-k-stops.md) | 2026-09-13 |
| 18 | [Construct a Tree from Level-Order and Inorder Traversals](problems/amazon_oa/amazon-construct-tree-level-inorder.md) | 2026-09-13 |
| 19 | [Container With Most Water](problems/amazon_oa/amazon-container-with-most-water.md) | 2026-09-13 |
| 20 | [Count Stepping Numbers In Range](problems/amazon_oa/amazon-count-stepping-numbers-in-range.md) | 2026-09-13 |
| 21 | [Count Uni-Valued Subtrees](problems/amazon_oa/amazon-count-univalued-subtrees.md) | 2026-09-13 |
| 22 | [Course Schedule](problems/amazon_oa/amazon-course-schedule.md) | 2026-09-13 |
| 23 | [Course Schedule II](problems/amazon_oa/amazon-course-schedule-ii.md) | 2026-09-13 |
| 24 | [Currency Conversion Rate](problems/amazon_oa/amazon-currency-conversion-rate.md) | 2026-09-13 |
| 25 | [Decode an Encoded String](problems/amazon_oa/amazon-decode-encoded-string.md) | 2026-09-13 |
| 26 | [Distance Between Two Tree Nodes](problems/amazon_oa/amazon-distance-between-tree-nodes.md) | 2026-09-13 |
| 27 | [E-commerce Notification Router](problems/amazon_oa/amazon-ecommerce-notification-router.md) | 2026-09-13 |
| 28 | [Employee Ratings Management System](problems/amazon_oa/amazon-employee-ratings-data-structure.md) | 2026-09-13 |
| 29 | [Find Median from Data Stream](problems/amazon_oa/amazon-find-median-from-data-stream.md) | 2026-09-13 |
| 30 | [Find the Safest Path in a Grid](problems/amazon_oa/amazon-find-safest-path-in-grid.md) | 2026-09-13 |
| 31 | [First Missing Positive](problems/amazon_oa/amazon-first-missing-positive.md) | 2026-09-13 |
| 32 | [First Unique Character in a Stream](problems/amazon_oa/amazon-first-unique-character-stream.md) | 2026-09-13 |
| 33 | [Bit at an Index After Repeated Binary Expansion](problems/amazon_oa/amazon-indexed-bit-after-binary-expansion.md) | 2026-09-13 |
| 34 | [Count Islands with Eight-Direction Adjacency](problems/amazon_oa/amazon-islands-eight-direction.md) | 2026-09-13 |
| 35 | [K Closest Elements in a Sorted Array](problems/amazon_oa/amazon-k-closest-elements-in-sorted-array.md) | 2026-09-13 |
| 36 | [Kth Smallest Sum from Sorted Matrix Rows](problems/amazon_oa/amazon-kth-smallest-row-sum.md) | 2026-09-13 |
| 37 | [Remove Duplicate Letters for the Largest Result](problems/amazon_oa/amazon-largest-lexicographic-unique-letters.md) | 2026-09-13 |
| 38 | [Longest Common Subsequence Length](problems/amazon_oa/amazon-longest-common-subsequence-length.md) | 2026-09-13 |
| 39 | [Longest Happy Prefix](problems/amazon_oa/amazon-longest-happy-prefix.md) | 2026-09-13 |
| 40 | [Longest Increasing Subsequence With Bounded Adjacent Difference](problems/amazon_oa/amazon-longest-increasing-subsequence-bounded-difference.md) | 2026-09-13 |
| 41 | [Max Consecutive Ones III](problems/amazon_oa/amazon-max-consecutive-ones-iii.md) | 2026-09-13 |
| 42 | [Maximize Distance to the Closest Occupied Seat](problems/amazon_oa/amazon-maximize-distance-to-closest-person.md) | 2026-09-13 |
| 43 | [Maximum Non-Adjacent House Value](problems/amazon_oa/amazon-maximum-non-adjacent-house-value.md) | 2026-09-13 |
| 44 | [Maximum Profit in Job Scheduling](problems/amazon_oa/amazon-maximum-profit-job-scheduling.md) | 2026-09-13 |
| 45 | [Maximum Sum BST in a Binary Tree](problems/amazon_oa/amazon-maximum-sum-bst.md) | 2026-09-13 |
| 46 | [Meeting Room Scheduler](problems/amazon_oa/amazon-meeting-room-scheduler.md) | 2026-09-13 |
| 47 | [Merge Intervals](problems/amazon_oa/amazon-merge-intervals.md) | 2026-09-13 |
| 48 | [Merge k Sorted Lists](problems/amazon_oa/amazon-merge-k-sorted-lists.md) | 2026-09-13 |
| 49 | [Stack with Constant-Time Middle Queries](problems/amazon_oa/amazon-middle-stack-operations.md) | 2026-09-13 |
| 50 | [Minimize Malware Spread in a Facility Network](problems/amazon_oa/amazon-minimize-malware-facility-network.md) | 2026-09-13 |
| 51 | [Minimum Window Substring](problems/amazon_oa/amazon-minimum-window-substring.md) | 2026-09-13 |
| 52 | [Nodes at a Given N-ary Tree Level](problems/amazon_oa/amazon-nary-tree-nodes-at-level.md) | 2026-09-13 |
| 53 | [Next Palindromic Time](problems/amazon_oa/amazon-next-palindromic-time.md) | 2026-09-13 |
| 54 | [Next Permutation](problems/amazon_oa/amazon-next-permutation.md) | 2026-09-13 |
| 55 | [Product of Array Except Self](problems/amazon_oa/amazon-product-array-except-self.md) | 2026-09-13 |
| 56 | [Reorganize a String](problems/amazon_oa/amazon-reorganize-string.md) | 2026-09-13 |
| 57 | [Path Through an O/X Grid Using Only Right and Down](problems/amazon_oa/amazon-right-down-grid-path.md) | 2026-09-13 |
| 58 | [Minimum Time to Spread Through a Grid](problems/amazon_oa/amazon-rotting-oranges-variation.md) | 2026-09-13 |
| 59 | [Running Delivery Time Medians](problems/amazon_oa/amazon-running-delivery-time-medians.md) | 2026-09-13 |
| 60 | [Search in a Rotated Sorted Array](problems/amazon_oa/amazon-search-rotated-sorted-array.md) | 2026-09-13 |
| 61 | [Task Scheduler](problems/amazon_oa/amazon-task-scheduler.md) | 2026-09-13 |
| 62 | [Three Sum Closest](problems/amazon_oa/amazon-three-sum-closest.md) | 2026-09-13 |
| 63 | [Fare Between Stops on a Train Route](problems/amazon_oa/amazon-train-route-fare.md) | 2026-09-13 |
| 64 | [Initial and Final Accounts in a Transfer Chain](problems/amazon_oa/amazon-transfer-chain-endpoints.md) | 2026-09-13 |
| 65 | [Trapping Rain Water](problems/amazon_oa/amazon-trapping-rain-water.md) | 2026-09-13 |
| 66 | [Minimum Moves for Two Knights to Meet](problems/amazon_oa/amazon-two-knights-minimum-meeting-moves.md) | 2026-09-13 |
| 67 | [Unique Pairs in a 2D Matrix Summing to Target](problems/amazon_oa/amazon-unique-pairs-2d-target.md) | 2026-09-13 |
| 68 | [Unique String Permutations](problems/amazon_oa/amazon-unique-string-permutations.md) | 2026-09-13 |
| 69 | [Validate a Two-Color Chessboard](problems/amazon_oa/amazon-validate-two-color-chessboard.md) | 2026-09-13 |
| 70 | [Maximum Saw Height for At Least M Cut Length](problems/amazon_oa/amazon-woodcut-saw-height.md) | 2026-09-13 |
| 71 | [Word Break](problems/amazon_oa/amazon-word-break.md) | 2026-09-13 |
| 72 | [Word Break II](problems/amazon_oa/amazon-word-break-ii.md) | 2026-09-13 |
| 73 | [Get Minimum Amount](problems/amazon_oa/amazon-get-min-amount.md) | 2026-09-12 |
| 74 | [Interleaving String](problems/amazon_oa/amazon-interleaving-string.md) | 2026-09-12 |
| 75 | [Dynamic Prefix Search Collection](problems/amazon_oa/amazon-prefix-search-collection.md) | 2026-09-12 |
| 76 | [Word Search II](problems/amazon_oa/amazon-word-search-ii.md) | 2026-09-12 |
| 77 | [Recent Advertisement Click Counts](problems/amazon_oa/amazon-ad-click-counts-sliding-window.md) | 2026-09-10 |
| 78 | [Most Frequent Consecutive Website Pattern](problems/amazon_oa/amazon-consecutive-website-visit-pattern.md) | 2026-09-10 |
| 79 | [Longest Substring Without Repeating Characters](problems/amazon_oa/amazon-longest-substring-without-repeating-characters.md) | 2026-09-10 |
| 80 | [Sliding-Window Rate Limiter](problems/amazon_oa/amazon-sliding-window-rate-limiter.md) | 2026-09-10 |
| 81 | [Find Minimum Cost](problems/amazon_oa/amazon-find-minimum-cost.md) | 2026-09-09 |
| 82 | [Maximum System Memory Capacity](problems/amazon_oa/amazon-maximum-capacity.md) | 2026-09-08 |
| 83 | [Meeting Rooms II](problems/amazon_oa/amazon-meeting-rooms-ii.md) | 2026-09-08 |
| 84 | [Minimum Merge Conflicts](problems/amazon_oa/amazon-minimum-merge-conflicts.md) | 2026-09-08 |
| 85 | [Next Smaller Ticket Price](problems/amazon_oa/amazon-next-smaller-ticket-price.md) | 2026-09-08 |
| 86 | [Remove K Digits](problems/amazon_oa/amazon-remove-k-digits.md) | 2026-09-08 |
| 87 | [Get Distinct Pairs](problems/amazon_oa/amazon-get-distinct-pairs.md) | 2026-09-05 |
| 88 | [Minimum Adjacent Swaps to Group Binary Values](problems/amazon_oa/amazon-minimum-adjacent-swaps-binary-groups.md) | 2026-09-02 |
| 89 | [Maximum Frequency Stack](problems/amazon_oa/amazon-maximum-frequency-stack.md) | 2026-09-01 |
| 90 | [Linked-List Queue with Delete and Deduplication](problems/amazon_oa/amazon-linked-list-queue-operations.md) | 2026-08-31 |
| 91 | [Minimum Grid Inconvenience](problems/amazon_oa/amazon-minimum-grid-inconvenience.md) | 2026-08-28 |
| 92 | [Single Element in a Sorted Array](problems/amazon_oa/amazon-single-element-in-sorted-array.md) | 2026-07-30 |
| 93 | [Count the Number of Complete Components](problems/amazon_oa/amazon-count-complete-components.md) | 2026-07-29 |
| 94 | [Cousins in Binary Tree II](problems/amazon_oa/amazon-cousins-in-binary-tree-ii.md) | 2026-07-29 |
| 95 | [Minimum Operations to Make an Array Continuous](problems/amazon_oa/amazon-minimum-operations-to-make-array-continuous.md) | 2026-07-29 |
| 96 | [Vertical Order Traversal of a Binary Tree](problems/amazon_oa/amazon-vertical-order-traversal-of-binary-tree.md) | 2026-07-29 |
| 97 | [HTTP Request Redirection](problems/amazon_oa/amazon-http-request-redirection.md) | 2026-07-28 |
| 98 | [Resolve Task Dependencies](problems/amazon_oa/amazon-resolve-task-dependencies.md) | 2026-07-27 |
| 99 | [Shortest Distance on a Circular Bus Route](problems/amazon_oa/amazon-shortest-distance-circular-bus-route.md) | 2026-07-26 |
| 100 | [Sort an Array with Rotate and Flip](problems/amazon_oa/amazon-sort-array-with-rotate-and-flip.md) | 2026-07-22 |
| 101 | [Loyal Customers Across Two Days](problems/amazon_oa/amazon-loyal-customers.md) | 2026-07-21 |
| 102 | [Smallest Number With a Given Digit Sum](problems/amazon_oa/amazon-smallest-number-with-digit-sum.md) | 2026-07-21 |
| 103 | [Group Anagrams](problems/amazon_oa/amazon-group-anagrams.md) | 2026-07-12 |
| 104 | [Longest Palindromic Subsequence](problems/amazon_oa/amazon-longest-palindromic-subsequence.md) | 2026-07-12 |
| 105 | [Maximal Square](problems/amazon_oa/amazon-maximal-square.md) | 2026-07-12 |
| 106 | [Maximum Sum of Heights](problems/amazon_oa/amazon-maximum-sum-of-heights.md) | 2026-07-12 |
| 107 | [Number of Islands II](problems/amazon_oa/amazon-number-of-islands-ii.md) | 2026-07-12 |
| 108 | [Sliding Window Maximum](problems/amazon_oa/amazon-sliding-window-maximum.md) | 2026-07-12 |
| 109 | [Domain Weight Calculation](problems/amazon_oa/amazon-domain-weight-calculation.md) | 2026-07-10 |
| 110 | [Minimum Contiguous Replacements](problems/amazon_oa/amazon-minimum-contiguous-replacements.md) | 2026-07-10 |
| 111 | [Minimum Redistribution Cost](problems/amazon_oa/amazon-minimum-redistribution-cost.md) | 2026-07-10 |
| 112 | [Number of Atoms](problems/amazon_oa/amazon-number-of-atoms.md) | 2026-07-10 |
| 113 | [Closest Version Date](problems/amazon_oa/amazon-closest-version-date.md) | 2026-07-08 |
| 114 | [Maximum Concurrent Processes (Bar Raiser Round)](problems/amazon_oa/amazon-max-concurrent-processes.md) | 2026-07-08 |
| 115 | [Package Dependency Order](problems/amazon_oa/amazon-package-dependency-order.md) | 2026-07-08 |
| 116 | [Merge Sorted Array](problems/amazon_oa/amazon-merge-sorted-array.md) | 2026-07-07 |
| 117 | [Get Max Servers](problems/amazon_oa/amazon-find-maximum-number-of-servers.md) | 2026-07-03 |
| 118 | [Permutation Sorter](problems/amazon_oa/amazon-permutation-sorter.md) | 2026-07-03 |
| 119 | [Feasible Indices After Prefix/Suffix Reduction](problems/amazon_oa/amazon-feasible-indices-after-prefix-suffix-reduction.md) | 2026-06-30 |
| 120 | [Frequently Bought Together](problems/amazon_oa/amazon-frequently-bought-together.md) | 2026-06-29 |
| 121 | [Souvenir Shop Purchases](problems/amazon_oa/amazon-souvenir-shop-purchases.md) | 2026-06-29 |
| 122 | [Find Minimum Groups](problems/amazon_oa/amazon-find-minimum-groups.md) | 2026-06-24 |
| 123 | [Maximum Equal Parts for Prefixes](problems/amazon_oa/amazon-maximum-equal-parts-for-prefixes.md) | 2026-06-19 |
| 124 | [Count Promotional Periods](problems/amazon_oa/amazon-count-promotional-periods.md) | 2026-06-09 |
| 125 | [Get Smallest Base Segment](problems/amazon_oa/amazon-get-smallest-base-segment.md) | 2026-06-09 |
| 126 | [Select Least Resource Tasks](problems/amazon_oa/amazon-select-least-resource-tasks.md) | 2026-06-09 |
| 127 | [Lowest Common Ancestor Implemented with Stack](problems/amazon_oa/amazon-lowest-common-ancestor-implemented-with-stack.md) | 2026-05-30 |
| 128 | [Product Category Group Sizes](problems/amazon_oa/amazon-product-category-groups.md) | 2026-05-23 |
| 129 | [Count Connected Components](problems/amazon_oa/amazon-count-connected-components.md) | 2026-05-21 |
| 130 | [Unique Pairs With Target Sum](problems/amazon_oa/amazon-unique-pairs-with-target-sum.md) | 2026-05-13 |
| 131 | [Feasible Indices After Reduction](problems/amazon_oa/amazon-feasible-indices-after-reduction.md) | 2026-04-30 |
| 132 | [Count Similar String Groups](problems/amazon_oa/amazon-count-similar-string-groups.md) | 2026-04-25 |
| 133 | [Get Min Errors](problems/amazon_oa/amazon-get-min-errors.md) | 2026-04-16 |
| 134 | [Maximum Score With Non-Adjacent Values](problems/amazon_oa/amazon-maximum-score-with-non-adjacent-values.md) | 2026-04-14 |
| 135 | [Make Value Groups Contiguous](problems/amazon_oa/amazon-make-value-groups-contiguous.md) | 2026-04-13 |
| 136 | [Dynamic Kth Largest Queries](problems/amazon_oa/amazon-dynamic-kth-largest-queries.md) | 2026-04-09 |
| 137 | [Longest Zero Sum Subarray](problems/amazon_oa/amazon-longest-zero-sum-subarray.md) | 2026-04-09 |
| 138 | [Maximize Minimum Machine Power](problems/amazon_oa/amazon-maximize-minimum-machine-power.md) | 2026-04-09 |
| 139 | [Maximize Protected City Population](problems/amazon_oa/amazon-maximize-protected-city-population.md) | 2026-04-06 |
| 140 | [Minimum Cost to Convert Products to Variant A](problems/amazon_oa/amazon-minimum-cost-to-convert-products-to-variant-a.md) | 2026-04-06 |
| 141 | [Minimum Preparation Time for Two Handlers](problems/amazon_oa/amazon-minimum-preparation-time-for-two-handlers.md) | 2026-04-06 |
| 142 | [Sum Max Plus Min After Decrement Operations](problems/amazon_oa/amazon-sum-max-plus-min-after-decrement-operations.md) | 2026-03-25 |
| 143 | [Sort Error Codes by Frequency](problems/amazon_oa/amazon-sort-error-codes-by-frequency.md) | 2026-03-24 |
| 144 | [Lexicographically Smallest After One Substring Rotation](problems/amazon_oa/amazon-lexicographically-smallest-after-one-substring-rotation.md) | 2026-02-05 |
| 145 | [Minimum Operations to Sort a Permutation](problems/amazon_oa/amazon-minimum-operations-to-sort-permutation.md) | 2026-01-30 |
| 146 | [Lexicographically Maximum Final Sequence](problems/amazon_oa/amazon-lexicographically-maximum-final-sequence.md) | 2026-01-24 |
| 147 | [Package Delivery System](problems/amazon_oa/amazon-package-delivery-system.md) | 2026-01-24 |
| 148 | [VM Rental Revenue](problems/amazon_oa/amazon-vm-rental-revenue.md) | 2026-01-24 |
| 149 | [Longest Arithmetic Subarray After One Change](problems/amazon_oa/amazon-longest-arithmetic-subarray-after-one-change.md) | 2026-01-06 |
| 150 | [Replace Values and Return Sums](problems/amazon_oa/amazon-replace-values-and-return-sums.md) | 2026-01-06 |
| 151 | [Minimum S3 Storage Cost](problems/amazon_oa/amazon-minimum-s3-storage-cost.md) | 2025-12-11 |
| 152 | [Count Picked Items Less Than Queries](problems/amazon_oa/amazon-count-picked-items-less-than-queries.md) | 2025-08-10 |
| 153 | [Fair Prize Distribution](problems/amazon_oa/amazon-fair-prize-distribution.md) | 2025-08-10 |
| 154 | [Largest Number With Digit Sum](problems/amazon_oa/amazon-largest-number-with-digit-sum.md) | 2025-08-03 |
| 155 | [Minimize Binary Subsequence Cost](problems/amazon_oa/amazon-minimize-binary-subsequence-cost.md) | 2025-08-03 |
| 156 | [First Valid Word Segmentation](problems/amazon_oa/amazon-first-word-segmentation.md) | 2025-07-26 |
| 157 | [Nearby Fulfillment Centers with Inventory](problems/amazon_oa/amazon-nearby-fulfillment-centers.md) | 2025-07-26 |
| 158 | [Maximize Pages Before Suspension](problems/amazon_oa/amazon-maximize-pages-before-suspension.md) | 2025-07-08 |
| 159 | [Predict Answer](problems/amazon_oa/amazon-predict-answer.md) | 2025-06-23 |
| 160 | [Find Security Level](problems/amazon_oa/amazon-find-security-level.md) | 2025-06-18 |
| 161 | [Get Min Subsegments](problems/amazon_oa/amazon-get-min-subsegments.md) | 2025-06-18 |
| 162 | [Minimize Variation](problems/amazon_oa/amazon-minimize-variation.md) | 2025-06-18 |
| 163 | [Find Hash](problems/amazon_oa/amazon-find-hash.md) | 2025-06-12 |
| 164 | [Count Special Substrings](problems/amazon_oa/amazon-count-special-substrs.md) | 2025-05-31 |
| 165 | [Find Minimum Days](problems/amazon_oa/amazon-find-minimum-days.md) | 2025-05-31 |
| 166 | [Find Minimum Machine Sizes](problems/amazon_oa/amazon-find-minimum-machines-size.md) | 2025-05-31 |
| 167 | [Get Maximum Count](problems/amazon_oa/amazon-get-maximum-count.md) | 2025-05-31 |
| 168 | [Split Prefix Suffix](problems/amazon_oa/amazon-split-prefix-suffix.md) | 2025-05-31 |
| 169 | [Determine the Best Skipping Strategy](problems/amazon_oa/amazon-determine-the-best-skipping-strategy.md) | 2025-05-25 |
| 170 | [Compute Beauty of Array Products](problems/amazon_oa/amazon-compute-beauty-of-array-products.md) | 2025-04-27 |
| 171 | [Find Idle Skill Query](problems/amazon_oa/amazon-find-idle-skills-query.md) | 2025-04-27 |
| 172 | [Min Dock Bays](problems/amazon_oa/amazon-get-minimum-dock-bays.md) | 2025-04-27 |
| 173 | [Min Num Unique Distribution Hubs](problems/amazon_oa/amazon-get-minimum-number-of-unique-distribution-centers.md) | 2025-04-13 |
| 174 | [Next Perfect String](problems/amazon_oa/amazon-next-greater-perfect-string.md) | 2025-04-13 |
| 175 | [Use Minimum Tokens](problems/amazon_oa/amazon-use-minimum-tokens.md) | 2025-04-13 |
| 176 | [Remove Characters in Frequency Order](problems/amazon_oa/amazon-remove-characters-in-frequency-order.md) | 2025-04-10 |
| 177 | [Optimal Utilization](problems/amazon_oa/amazon-optimal-utilization.md) | 2025-04-05 |
| 178 | [Buy Servers](problems/amazon_oa/amazon-purchase-servers.md) | 2025-04-05 |
| 179 | [Cinema Shows](problems/amazon_oa/amazon-cinema-shows.md) | 2025-03-31 |
| 180 | [Min Retailers](problems/amazon_oa/amazon-minimum-retailers.md) | 2025-03-31 |
| 181 | [Find Replacement](problems/amazon_oa/amazon-find-min-replacements.md) | 2025-03-29 |
| 182 | [Good String](problems/amazon_oa/amazon-convert-to-good-string.md) | 2025-03-28 |
| 183 | [Find Min Max Difference](problems/amazon_oa/amazon-find-min-max-difference.md) | 2025-03-27 |
| 184 | [Max Sum of Non-overlapping Intervals](problems/amazon_oa/amazon-max-sum-of-non-overlapping-intervals.md) | 2025-03-27 |
| 185 | [Get Minimal Cost](problems/amazon_oa/amazon-get-minimal-cost.md) | 2025-03-26 |
| 186 | [Find Least Possible Vulnerability](problems/amazon_oa/amazon-find-least-possible-vulnerability.md) | 2025-03-24 |
| 187 | [Make Array Distinct](problems/amazon_oa/amazon-make-array-distinct.md) | 2025-03-24 |
| 188 | [Ensure Non Zero Load Sum](problems/amazon_oa/amazon-ensure-non-zero-load-sum.md) | 2025-03-23 |
| 189 | [Number Of Well Performing Groups](problems/amazon_oa/amazon-number-of-well-performing-groups.md) | 2025-03-23 |
| 190 | [Get Max Increments](problems/amazon_oa/amazon-get-max-increments.md) | 2025-03-22 |
| 191 | [Password Strength](problems/amazon_oa/amazon-password-strength.md) | 2025-03-22 |
| 192 | [Optimal Level](problems/amazon_oa/amazon-find-optimal-level.md) | 2025-03-21 |
| 193 | [Min Operation](problems/amazon_oa/amazon-min-operation.md) | 2025-03-21 |
| 194 | [Trader Joe Trades](problems/amazon_oa/amazon-trader-joe-trades.md) | 2025-03-21 |
| 195 | [All About Rewards](problems/amazon_oa/amazon-all-about-rewards.md) | 2025-03-20 |
| 196 | [Inventory Processes Survival Possibility](problems/amazon_oa/amazon-inventory-processes-survival-possibility.md) | 2025-03-18 |
| 197 | [All About Medians](problems/amazon_oa/amazon-medians.md) | 2025-03-18 |
| 198 | [Get Largest Number](problems/amazon_oa/amazon-find-partition-cost.md) | 2025-03-13 |
| 199 | [Get The Most Out Of The Data](problems/amazon_oa/amazon-get-most-out-of-the-data.md) | 2025-02-10 |
| 200 | [Maximize Sum of Array Multiplication](problems/amazon_oa/amazon-maximize-sum-of-array-multiplication.md) | 2025-02-05 |
| 201 | [Max Number of Products You can Pick](problems/amazon_oa/amazon-maximum-number-of-products-you-can-pick.md) | 2025-02-05 |
| 202 | [Get Maximum](problems/amazon_oa/amazon-get-maximum.md) | 2025-02-02 |
| 203 | [Sum of Max Subarrys](problems/amazon_oa/amazon-sum-of-max-subarrays.md) | 2025-02-02 |
| 204 | [Calculate Max Salary](problems/amazon_oa/amazon-calculate-max-salary.md) | 2025-01-09 |
| 205 | [Maximize Product of Sizes of Subtrees](problems/amazon_oa/amazon-maximize-product-of-sizes-of-subtrees.md) | 2025-01-09 |
| 206 | [Min Energy Cost](problems/amazon_oa/amazon-minimum-energy-cost.md) | 2025-01-09 |
| 207 | [Optimal Interval Difference](problems/amazon_oa/amazon-optimal-interval-difference.md) | 2025-01-08 |
| 208 | [Find Max Value](problems/amazon_oa/amazon-find-max-value.md) | 2025-01-05 |
| 209 | [Get Max Events](problems/amazon_oa/amazon-get-maximum-events.md) | 2025-01-05 |
| 210 | [Calculate Max Profit](problems/amazon_oa/amazon-calculate-max-profit.md) | 2024-12-22 |
| 211 | [Get Final Location](problems/amazon_oa/amazon-get-final-locations.md) | 2024-12-22 |
| 212 | [Get Stable Periods Count](problems/amazon_oa/amazon-get-stable-periods-count.md) | 2024-12-22 |
| 213 | [Max Transfer Rate](problems/amazon_oa/amazon-max-transfer-rate.md) | 2024-12-22 |
| 214 | [Get Max Stability](problems/amazon_oa/amazon-get-max-stability.md) | 2024-12-20 |
| 215 | [Min Operations](problems/amazon_oa/amazon-make-array-zero-by-subtracting-equal-amounts.md) | 2024-12-20 |
| 216 | [Get Max Stability](problems/amazon_oa/amazon-minimum-swaps-to-make-palindrome.md) | 2024-12-20 |
| 217 | [Get Max Skill Sum](problems/amazon_oa/amazon-get-max-skill-sum.md) | 2024-12-11 |
| 218 | [Get Min Value](problems/amazon_oa/amazon-get-minimum-value.md) | 2024-12-11 |
| 219 | [Find Number](problems/amazon_oa/amazon-find-number.md) | 2024-12-10 |
| 220 | [Get Min Removal](problems/amazon_oa/amazon-get-min-removal.md) | 2024-12-10 |
| 221 | [Find Lexicographically Smallest String](problems/amazon_oa/amazon-find-lexicographically-smallest-string.md) | 2024-12-08 |
| 222 | [Find Password Strength](problems/amazon_oa/amazon-find-password-strength.md) | 2024-12-08 |
| 223 | [Perform Queries](problems/amazon_oa/amazon-perform-queries.md) | 2024-12-08 |
| 224 | [Data Dependence Sum](problems/amazon_oa/amazon-get-data-dependence-sum.md) | 2024-12-03 |
| 225 | [Min Operations](problems/amazon_oa/amazon-get-min-operations2.md) | 2024-12-03 |
| 226 | [Sum of All Days Numbers on Which the Data of the Xth Will Be Dependent](problems/amazon_oa/amazon-sum-of-all-days-numbers-on-which-the-data-of-the-xth-will-be-dependent.md) | 2024-11-27 |
| 227 | [Optimize Identifiers](problems/amazon_oa/amazon-optimize-identifiers.md) | 2024-11-25 |
| 228 | [Min Insertions](problems/amazon_oa/amazon-minimum-insertions.md) | 2024-11-24 |
| 229 | [Min Chars to Append](problems/amazon_oa/amazon-determine-minimum-characters-to-append.md) | 2024-11-23 |
| 230 | [Reduce Memory Usage](problems/amazon_oa/amazon-reduce-memory-usage.md) | 2024-11-20 |
| 231 | [Calculate Truck Distance](problems/amazon_oa/amazon-calculate-truck-distance.md) | 2024-11-18 |
| 232 | [Get Min Change](problems/amazon_oa/amazon-get-minimum-changes.md) | 2024-11-18 |
| 233 | [Find Ideal Days](problems/amazon_oa/amazon-find-ideal-days.md) | 2024-11-17 |
| 234 | [Get Min Moves](problems/amazon_oa/amazon-get-min-moves.md) | 2024-11-14 |
| 235 | [Minimize Effort](problems/amazon_oa/amazon-minimize-effort.md) | 2024-11-14 |
| 236 | [Get Max Discount Pairs](problems/amazon_oa/amazon-get-max-discount-pairs.md) | 2024-11-13 |
| 237 | [Rooks Left](problems/amazon_oa/amazon-rooks-left.md) | 2024-11-12 |
| 238 | [Optimize Identifiers](problems/amazon_oa/amazon-optimized-identifiers.md) | 2024-11-09 |
| 239 | [Cleanup Dataset](problems/amazon_oa/amazon-cleanup-dataset.md) | 2024-10-30 |
| 240 | [Find Min Variance](problems/amazon_oa/amazon-find-minimum-possible-variance.md) | 2024-10-30 |
| 241 | [Find Min Time Required](problems/amazon_oa/amazon-find-minimum-time-required.md) | 2024-10-30 |
| 242 | [Calculate Warehouse Efficiency](problems/amazon_oa/amazon-calculate-warehouse-efficiency.md) | 2024-10-28 |
| 243 | [Find Networking Calls](problems/amazon_oa/amazon-find-network-calls.md) | 2024-10-28 |
| 244 | [Make All Elements Distinct](problems/amazon_oa/amazon-make-all-elements-distinct.md) | 2024-10-28 |
| 245 | [Maximize Similarity](problems/amazon_oa/amazon-maximize-similarity.md) | 2024-10-28 |
| 246 | [Get Min Cost of Purchasing Books](problems/amazon_oa/amazon-get-min-cost-book.md) | 2024-10-22 |
| 247 | [Get Smaller Items](problems/amazon_oa/amazon-get-smaller-items.md) | 2024-10-22 |
| 248 | [About Mortgage](problems/amazon_oa/amazon-maximum-number-of-days-to-survive.md) | 2024-10-22 |
| 249 | [Schedule Tasks](problems/amazon_oa/amazon-schedule-tasks.md) | 2024-10-22 |
| 250 | [Planning the Campaign](problems/amazon_oa/amazon-minimum-weekly-input.md) | 2024-10-20 |
| 251 | [Find Minimum Time](problems/amazon_oa/amazon-find-minimum-time.md) | 2024-10-19 |
| 252 | [Get Max Programs](problems/amazon_oa/amazon-get-max-programs.md) | 2024-10-19 |
| 253 | [Sort Permutation](problems/amazon_oa/amazon-can-sort-permutation-in-given-moves.md) | 2024-10-11 |
| 254 | [Min Time to Create Beautiful Canvas](problems/amazon_oa/amazon-find-minimum-time-to-create-beautiful-canvas.md) | 2024-10-11 |
| 255 | [Get Max Charge](problems/amazon_oa/amazon-get-max-charge.md) | 2024-10-11 |
| 256 | [Rearrange Binary String](problems/amazon_oa/amazon-rearrange-binary-string.md) | 2024-10-11 |
| 257 | [Get Max Alternating Music](problems/amazon_oa/amazon-get-max-alternating-music.md) | 2024-10-08 |
| 258 | [Special String](problems/amazon_oa/amazon-get-special-string.md) | 2024-10-05 |
| 259 | [Find Days S2 Subsequence of S1](problems/amazon_oa/amazon-find-days-s2-subsequence-of-s1.md) | 2024-09-28 |
| 260 | [Find Subarray with Minimum Distinct Integers](problems/amazon_oa/amazon-find-subarray-with-minimum-distinct-integers.md) | 2024-09-27 |
| 261 | [Find Maximum Calories](problems/amazon_oa/amazon-find-maximum-calories.md) | 2024-09-26 |
| 262 | [Find Sum of Beauties](problems/amazon_oa/amazon-find-sum-of-beauties.md) | 2024-09-26 |
| 263 | [Longest Perfect Anagrams](problems/amazon_oa/amazon-longest-perfect-anagrams.md) | 2024-09-26 |
| 264 | [Maximum Quality Sum](problems/amazon_oa/amazon-maximum-quality-sum.md) | 2024-09-26 |
| 265 | [Minimize Warehouse Transfer Cost](problems/amazon_oa/amazon-minimize-warehouse-transfer-cost.md) | 2024-09-26 |
| 266 | [Calculate Total Distrance Travelled](problems/amazon_oa/amazon-calculate-total-distance-travelled.md) | 2024-09-19 |
| 267 | [Maximum Possible Racers](problems/amazon_oa/amazon-maximum-possible-racers.md) | 2024-09-19 |
| 268 | [Distributed Packages](problems/amazon_oa/amazon-distribute-packages.md) | 2024-09-03 |
| 269 | [Find Capable Winners](problems/amazon_oa/amazon-find-capable-winners.md) | 2024-09-03 |
| 270 | [Get Max Information Gain](problems/amazon_oa/amazon-get-max-information-gain.md) | 2024-09-03 |
| 271 | [Get Min Size](problems/amazon_oa/amazon-get-min-size.md) | 2024-08-30 |
| 272 | [Min Operations To Make Zeros](problems/amazon_oa/amazon-find-minimum-number-of-operations.md) | 2024-08-28 |
| 273 | [Choose Warehouse Location](problems/amazon_oa/amazon-choose-warehouses-location.md) | 2024-08-25 |
| 274 | [Minimize Storage Required](problems/amazon_oa/amazon-minimum-storage-capacity-required.md) | 2024-08-23 |
| 275 | [Get Maximum Sum](problems/amazon_oa/amazon-get-maximum-sum.md) | 2024-08-10 |
| 276 | [Assign Tasks](problems/amazon_oa/amazon-assign-tasks.md) | 2024-08-05 |
| 277 | [Get Active Requests Count](problems/amazon_oa/amazon-get-active-requests-count.md) | 2024-08-05 |
| 278 | [Get Operations](problems/amazon_oa/amazon-get-operations.md) | 2024-08-05 |
| 279 | [Process Queries On Cart](problems/amazon_oa/amazon-process-queries-on-cart.md) | 2024-08-05 |
| 280 | [Get Minimum Boxes](problems/amazon_oa/amazon-get-minimum-boxes.md) | 2024-07-25 |
| 281 | [Compute Encoded Product Name](problems/amazon_oa/amazon-compute-encoded-product-name.md) | 2024-07-15 |
| 282 | [Get Redundant Substrings](problems/amazon_oa/amazon-get-redundant-substrings.md) | 2024-07-15 |
| 283 | [Process Queue](problems/amazon_oa/amazon-process-queue.md) | 2024-07-15 |
| 284 | [Max Consecutive ON Servers](problems/amazon_oa/amazon-get-max-consecutive-on.md) | 2024-07-09 |
| 285 | [Get Total Requests](problems/amazon_oa/amazon-get-total-requests.md) | 2024-06-27 |
| 286 | [Maximize Negative Signs](problems/amazon_oa/maximize-negative-signs.md) | 2024-06-24 |
| 287 | [Is Regex Matching](problems/amazon_oa/amazon-is-regex-matching.md) | 2024-06-15 |
| 288 | [Maximum Stability](problems/amazon_oa/amazon-maximum-stability.md) | 2024-06-15 |
| 289 | [Bring Servers Down](problems/amazon_oa/amazon-bring-servers-down.md) | 2024-06-10 |
| 290 | [Maximize Subtree Product](problems/amazon_oa/amazon-maximize-subtree-product.md) | 2024-06-10 |
| 291 | [Find K Level Permutation](problems/amazon_oa/amazon-find-k-level-permutation.md) | 2024-06-02 |
| 292 | [Optimizing Box Weights](problems/amazon_oa/amazon-minimal-heaviest-set-a.md) | 2024-06-02 |
| 293 | [Get Experience](problems/amazon_oa/amazon-get-exp.md) | 2024-05-13 |
| 294 | [Ordered Confirguration](problems/amazon_oa/amazon-orda-layout.md) | 2024-05-04 |
| 295 | [Find Median Of Subarray Uniqueness](problems/amazon_oa/find-median-of-subarray-uniqueness.md) | 2024-04-15 |
| 296 | [Count Pairs](problems/amazon_oa/amazon-count-pairs.md) | 2024-04-12 |
| 297 | [Get Max Pairs](problems/amazon_oa/amazon-get-max-pairs.md) | 2024-04-12 |
| 298 | [Get Min Time](problems/amazon_oa/amazon-get-min-time.md) | 2024-04-12 |
| 299 | [Kth Smallest in Subarray](problems/amazon_oa/amazon-kth-smallest-in-subarray.md) | 2024-04-12 |
| 300 | [Max Negation](problems/amazon_oa/amazon-maximize-the-array-sum-after-negating-at-most-k-elements.md) | 2024-04-12 |
| 301 | [Channel Max Quality](problems/amazon_oa/amazon-calculate-median-sum.md) | 2024-04-09 |
| 302 | [Max Lucky Numbers](problems/amazon_oa/max-lucky-numbers.md) | 2024-04-07 |
| 303 | [Find Kth Minimum Vulnerability ](problems/amazon_oa/amazon-find-kth-minimum-vulnerability.md) | 2024-04-05 |
| 304 | [Max Aggregate Temp Change](problems/amazon_oa/amazon-get-max-aggregate-temperature-change.md) | 2024-03-31 |
| 305 | [Count Faults (Faulty Binding 101 😁)](problems/amazon_oa/amazon-count-faults.md) | 2024-03-19 |
| 306 | [Find Max Num](problems/amazon_oa/amazon-find-maximum-num.md) | 2024-03-19 |
| 307 | [Minimize Sum of Absolute Differences](problems/amazon_oa/amazon-minimize-sum-of-absolute-differences.md) | 2024-03-18 |
| 308 | [Match Strings](problems/amazon_oa/amazon-match-strings.md) | 2024-03-14 |
| 309 | [Find Encrypted Password](problems/amazon_oa/amazon-find-encrypted-password.md) | 2024-03-12 |
| 310 | [Num of Possible Unique Strings](problems/amazon_oa/amazon-find-number-of-possible-unique-strings.md) | 2024-03-12 |
| 311 | [Lexicographically Smallest Palindrome Possible](problems/amazon_oa/amazon-lexicographically-smallest-palindrome-possible.md) | 2024-03-09 |
| 312 | [Ways to Group Parcels](problems/amazon_oa/amazon-find-number-of-ways-to-group-parcels.md) | 2024-03-04 |
| 313 | [Maxmimum Times Word Removed](problems/amazon_oa/amazon-maximum-times-word-removed.md) | 2024-03-03 |
| 314 | [Return Records](problems/amazon_oa/amazon-return-records.md) | 2024-03-02 |
| 315 | [Reverse Binary String](problems/amazon_oa/amazon-reverse-binary-string.md) | 2024-03-02 |
| 316 | [Get Max Racers](problems/amazon_oa/amazon-get-max-racers.md) | 2024-02-20 |
| 317 | [Count Distinct Passwords](problems/amazon_oa/amazon-count-distinct-passwords.md) | 2024-02-19 |
| 318 | [Get Min Num Moves](problems/amazon_oa/amazon-get-min-num-moves.md) | 2024-02-19 |
| 319 | [Find Min Trips](problems/amazon_oa/amazon-find-min-trips.md) | 2024-02-17 |
| 320 | [Max User Traffic](problems/amazon_oa/amazon-maximum-user-traffic.md) | 2024-02-17 |
| 321 | [Fortune Telling](problems/amazon_oa/amazon-minimize-the-range.md) | 2024-02-17 |
| 322 | [Find Recurring Name](problems/amazon_oa/amazon-find-recurring-names.md) | 2024-02-14 |
| 323 | [Find Requests In Queue](problems/amazon_oa/amazon-find-requests-in-queue.md) | 2024-02-14 |
| 324 | [Find Largest Set of Onion Bags](problems/amazon_oa/amazon-find-largest-set-of-onion-bags.md) | 2024-02-06 |
| 325 | [Minimum Total Errors](problems/amazon_oa/amazon-min-errors.md) | 2024-02-06 |
| 326 | [Dropped Requests](problems/amazon_oa/amazon-dropped-requests.md) | 2024-01-27 |
| 327 | [Execute Processes](problems/amazon_oa/amazon-execute-processes.md) | 2024-01-27 |
| 328 | [Find Unique Values](problems/amazon_oa/amazon-find-unique-values.md) | 2024-01-27 |
| 329 | [Group Students](problems/amazon_oa/amazon-group-students.md) | 2024-01-27 |
| 330 | [Number of Suitable Locations](problems/amazon_oa/amazon-num-of-suitable-places.md) | 2024-01-27 |
| 331 | [Rice Bags](problems/amazon_oa/max-set-size.md) | 2024-01-13 |
| 332 | [Get Discount Pairs](problems/amazon_oa/get-discount-pairs.md) | 2024-01-11 |
| 333 | [Get Min Cost Data](problems/amazon_oa/get-min-cost-data.md) | 2024-01-10 |
| 334 | [Count Maximum Profitable Groups](problems/amazon_oa/count-maximum-profitable-groups.md) | 2024-01-07 |
| 335 | [Get Min Distance (AMZ CN)](problems/amazon_oa/amazon-find-minimum-dist.md) | 2023-12-27 |
| 336 | [Count Games Won By Group1 (AMZ CN)](problems/amazon_oa/amazon-how-many-games-did-the-team-win.md) | 2023-12-27 |
| 337 | [Check Similar Passwords](problems/amazon_oa/check-similar-passwords.md) | 2023-12-23 |
| 338 | [Location of Data After Transfers](problems/amazon_oa/location-of-data-after-transfers.md) | 2023-12-23 |
| 339 | [Maximum Score in Balanced String](problems/amazon_oa/maximum-score-in-balanced-string.md) | 2023-12-23 |
| 340 | [Get Success Value](problems/amazon_oa/get-success-value.md) | 2023-12-19 |
| 341 | [Warehouse Distribution](problems/amazon_oa/warehouse-allocation.md) | 2023-12-15 |
| 342 | [Erase Pairs](problems/amazon_oa/erase-pairs.md) | 2023-12-13 |
| 343 | [Get Priorities After Execution](problems/amazon_oa/get-priorities-after-execution.md) | 2023-12-06 |
| 344 | [Count Max Num Teams](problems/amazon_oa/count-max-num-teams.md) | 2023-09-24 |
| 345 | [Get Average Standing](problems/amazon_oa/get-average-standing.md) | 2023-09-24 |
| 346 | [Minimum Time Spent](problems/amazon_oa/minimum-time-spent.md) | 2023-09-24 |
| 347 | [Count Spikes](problems/amazon_oa/count-spikes.md) | 2023-08-31 |
| 348 | [Find Minimum Inefficiency](problems/amazon_oa/find-minimum-inefficiency.md) | 2023-08-31 |
| 349 | [Cet Mean Rank Count](problems/amazon_oa/get-mean-rank-count.md) | 2023-08-31 |
| 350 | [Get Minimum Costs](problems/amazon_oa/get-minimum-cost.md) | 2023-08-31 |
<!-- amazon-oa:end -->


<!-- sources:start -->
## Sources

The three problem banks are curated elsewhere; this site adds the write-ups, pattern guides, and practice workspace.

- [Grind 75](https://www.techinterviewhandbook.org/grind75), curated by the [Tech Interview Handbook](https://www.techinterviewhandbook.org/) team.
- [NeetCode 150](https://neetcode.io/practice/practice/neetcode150), curated by the [NeetCode](https://neetcode.io/) team.
- The Amazon OA bank, from [perixtar/Tech-OA-Interview-Questions](https://github.com/perixtar/Tech-OA-Interview-Questions) with problem pages on [FastPrep](https://www.fastprep.io).
<!-- sources:end -->


## Pattern Intuition

The [pattern intuition guides](patterns/index.md) explain the *why* behind each recurring algorithm pattern: the mental model, when it applies, the invariant that makes it work, and the Grind75 problems that use it. Start there when a problem feels unfamiliar and you need to recognize which pattern fits.

## Practice Workspace

The [`practice/`](https://github.com/ThoDHa/algo-oa-prep/tree/main/practice) directory is a `pytest` workspace for solving the problems yourself. Each problem has a `solution.py` to implement plus two test sets that mirror LeetCode's Run (the examples) and Submit (a full corner-case gauntlet). See its [README](https://github.com/ThoDHa/algo-oa-prep/blob/main/practice/README.md) for setup and the practice loop.
