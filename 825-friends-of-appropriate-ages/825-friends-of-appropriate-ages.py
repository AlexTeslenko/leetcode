from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        total_friends = 0
        age_counter = Counter(ages)
 
        for age in age_counter:
            num_ages = age_counter[age]
            for friend_age in age_counter:
                if not (0.5 * age + 7 >= friend_age) and not (friend_age > age) and not(friend_age > 100 and age < 100):    
                    if age != friend_age:
                        total_friends += num_ages*age_counter[friend_age]
                    else:
                        total_friends += num_ages*(age_counter[friend_age] - 1)
        
        return total_friends
        