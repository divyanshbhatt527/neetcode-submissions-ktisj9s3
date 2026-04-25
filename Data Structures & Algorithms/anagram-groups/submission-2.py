class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_anagram(s1, s2):
            l1 = len(s1)
            l2 = len(s2)
            if l1!=l2:
                return False
            d1 = {}
            d2 = {}
            for i in range(l1):
                if s1[i] in d1:
                    d1[s1[i]] += 1
                else:
                    d1[s1[i]] = 1

                if s2[i] in d2:
                    d2[s2[i]] += 1
                else:
                    d2[s2[i]] = 1

            if d1 == d2:
                return True
            else:
                return False

        final_ans = []
        str_track = set()
        l = len(strs)
        if not l:
            return

        for i in range(l):
            sub_ans = []
            if strs[i] not in str_track:
                str_track.add(strs[i])
                sub_ans.append(strs[i])
            else:
                continue

            for j in range(i+1,l):
                
                result = check_anagram(strs[i], strs[j])
                if result:
                    sub_ans.append(strs[j])
                    str_track.add(strs[j])

            final_ans.append(sub_ans)
        return final_ans





        