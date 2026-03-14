class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return ones[n]
            elif n < 100:
                rest = " " + ones[n % 10] if n % 10 != 0 else ""
                return tens[n // 10] + rest
            else:
                rest = " " + helper(n % 100) if n % 100 != 0 else ""
                return ones[n // 100] + " Hundred" + rest
        
        result = []
        i = 0
        
        while num > 0:
            if num % 1000 != 0:
                part = helper(num % 1000)
                if thousands[i]:
                    part += " " + thousands[i]
                result.append(part)
            num //= 1000
            i += 1
        
        return " ".join(reversed(result))