#Problem link : https://leetcode.com/problems/lemonade-change/
#Leetcode Problem.860 : Lemonade Change


class Solution(object):
        def lemonadeChange(bills):

            five = ten = 0

            for bill in bills:
            # condition for 5
                if bill == 5:
                    five += 1
            # condition for 10
                elif bill == 10:
                    if not five:
                        return False
                    five -= 1
                    ten += 1
            # condition for 20
                else:
                    if ten and five:
                        ten -= 1
                        five -= 1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False
            return True

        # test the code
        if __name__ == "__main__":
                print(lemonadeChange([5,5,20]))