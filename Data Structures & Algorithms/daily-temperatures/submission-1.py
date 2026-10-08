class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                waiting_idx = stack.pop()

                output[waiting_idx] = idx - waiting_idx

            stack.append(idx)
        return output


        


        