class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping_dict = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                grouping_dict[(-1,)].append(string)
            else:
                char_diffs = []

                i = 1

                while i < len(string):
                    char_diffs.append((ord(string[i]) - ord(string[i-1])) % 26)


                    i += 1

                grouping_dict[tuple(char_diffs)].append(string)

        return list(grouping_dict.values())