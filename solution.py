class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sortedPeople = []
        dict = {}
        for i in range(len(names)):
            dict[heights[i]] = names[i]
        dict_list = dict.items()
        sorted_dict = sorted(dict_list, key=lambda x: x[0])
        for x in sorted_dict:
            sortedPeople.append(x[1])
        return(sortedPeople[::-1])
