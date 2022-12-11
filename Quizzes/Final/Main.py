from Q1_GroupAnagrams import Solution1
from Q2_NumOfIslands import Solution2
from Q3_RemoveMinParentheses import Solution3
from Q4_UniquePath import Solution4

if __name__ == "__main__":
    print("Question1------------------------------------------")
    solution1 = Solution1()
    case1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution1.group_anagrams(case1))

    print("Question2------------------------------------------")
    solution2 = Solution2()
    case1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]  # 1
    case2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]  # 3
    print(solution2.num_of_islands(case1))
    print(solution2.num_of_islands(case2))

    print("Question3------------------------------------------")
    solution3 = Solution3()
    case1 = "lee(t(c)o)de)"     # lee(t(c)o)de
    case2 = "a)b(c)d"   # ab(c)d
    print(solution3.remove_min_parentheses(case1))
    print(solution3.remove_min_parentheses(case2))

    print("Question4------------------------------------------")
    solution4 = Solution4()
    case1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]  # 2
    case2 = [[0, 1], [0, 0]]  # 1
    print(solution4.unique_path(case1))
    print(solution4.unique_path(case2))
