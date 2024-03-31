class Util :
    def calculate_mean (self, arr):
        counter = 0
        for num in arr:
            counter += num
        return counter/len(arr)

    def calculate_var(self, arr):
        mean = self.calculate_mean(arr)
        counter = 0
        for num in arr:
            counter += (mean - num) ** 2
        return conter/len(arr)

    def sort_list(self, arr):
        new_arr[]
        for k in range(0, len(arr)):
            num = arr [k]
            if k == 0:
                new_arr.append(num)
            else:
                for i in range (0, len(new_arr)):
                    if new_arr[i] >= num:
                        new_arr.insert(i, num)
                    if new_arr[i] > num:
                        break

        return new_arr

test_list = [1, 3, 56, 4.5, 438]
util = Util()
print(util)

