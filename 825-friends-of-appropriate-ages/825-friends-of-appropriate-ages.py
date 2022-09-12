from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        total_friends = 0
        age_counter = Counter(ages)
        print(age_counter)
        for age in ages:
            for friend_age in age_counter:
                if not (0.5 * age + 7 >= friend_age) and not (friend_age > age) and not(friend_age > 100 and age < 100):    
                    if age != friend_age:
                        total_friends += age_counter[friend_age]
                    else:
                        total_friends += age_counter[friend_age] - 1
        
        return total_friends
        