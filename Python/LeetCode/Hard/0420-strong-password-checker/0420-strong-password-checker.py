class Solution:
    def strongPasswordChecker(self, s):
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        digits = set([str(elem) for elem in range(10)])

        num_deletions = max(0, len(s) - 20)

        has_lowercase = any([character in lowercase for character in s])
        has_uppercase = any([character in uppercase for character in s])
        has_digits = any([character in digits for character in s])
        num_missing_types = (not has_lowercase) + (not has_uppercase) + (not has_digits)

        substring_lengths = self.count_substring_lengths(s)
        self.break_substrings_with_deletions(substring_lengths, num_deletions)
        num_substring_breaks = sum(
            [length // 3 for length in substring_lengths if length >= 3]
        )

        num_insertions = max(0, 6 - len(s))

        return num_deletions + max(
            num_missing_types, num_substring_breaks, num_insertions
        )

    def count_substring_lengths(self, s):
        # "aaabbc" => [3, 2, 1]
        result = [1]
        last_seen_character = s[0]
        for idx in range(1, len(s)):
            if s[idx] == last_seen_character:
                result[-1] += 1
            else:
                result.append(1)
            last_seen_character = s[idx]
        return result

    def break_substrings_with_deletions(self, substring_lengths, num_deletions):
        while num_deletions > 0:
            best_tuple_to_delete = min(
                enumerate(substring_lengths),
                key=lambda pair: pair[1] % 3 if pair[1] >= 3 else float("inf"),
            )
            best_idx_to_delete = best_tuple_to_delete[0]
            substring_lengths[best_idx_to_delete] -= 1
            num_deletions -= 1