class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n != 0:
                product *= n

        n_zeros = nums.count(0)
        if n_zeros >= 2:
            return [0] * len(nums)
        
        output = []
        if n_zeros == 1:
            for n in nums:
                if n == 0:
                    output.append(product)
                else:
                    output.append(0)
            return output

        for n in nums:
            if n == 0:
                o = product
            else:
                o = int(product / n)
            output.append(o)
        return output
