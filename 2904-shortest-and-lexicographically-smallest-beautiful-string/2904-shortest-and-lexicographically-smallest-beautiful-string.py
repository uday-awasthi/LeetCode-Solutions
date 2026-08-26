class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                count += 1

            # We have exactly k ones
            if count == k:

                # Remove leading zeros
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                # Update answer
                if ans == "" or len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans) and curr < ans:
                    ans = curr

                # Move left past the first 1
                left += 1
                count -= 1

        return ans