class Solution:
    
    def numberToWords(self, num: int) -> str:

        num_dict = { 0: "Zero",
                     1: "One",
                     2: "Two",
                     3: "Three",
                     4: "Four",
                     5: "Five",
                     6: "Six",
                     7: "Seven",
                     8: "Eight",
                     9: "Nine",
                     10: "Ten",
                     11: "Eleven",
                     12: "Twelve",
                     13: "Thirteen",
                     15: "Fifteen",
                     18: "Eighteen",
                     20: "Twenty",
                     30: "Thirty",
                     40: "Forty",
                     50: "Fifty",
                     80: "Eighty"}
        
        num_s = str(num).lstrip('0')
        num_digits = len(str(num))

        if num_digits == 1:
            return num_dict[num]
        
        elif num_digits == 2:
            first_digit = int((str(num)[0]))
            second_digit = int((str(num)[1]))
            if num_dict.get(num, None) != None:
                return num_dict[num]
            else:
                if first_digit == 1:
                    return num_dict[second_digit] + "teen"
                elif first_digit == 2:
                    return num_dict[20] + " " + num_dict[second_digit]
                elif first_digit == 3:
                    return num_dict[30] + " " + num_dict[second_digit]
                elif first_digit == 4:
                    return num_dict[40] + " " + num_dict[second_digit]
                elif first_digit == 5:
                    return num_dict[50] + " " + num_dict[second_digit]
                elif first_digit == 8:
                    return num_dict[80] + " " + num_dict[second_digit]
                else:
                    if second_digit == 0: 
                         return num_dict[first_digit] + "ty" 
                    else:
                         return num_dict[first_digit] + "ty" + " " + num_dict[second_digit]
                
        elif num_digits == 3:
            
            first_digit = int(num_s[0])
            second_digit = int(num_s[1])
            third_digit = int(num_s[2])
            
            if int(num_s[1]) == 0 and int(num_s[2]) == 0: 
                return num_dict[first_digit] + " " + "Hundred"
            else: 
                p = second_digit*10 + third_digit
                temp = self.numberToWords(p)
                return num_dict[first_digit] + " Hundred " + temp
            
        elif num_digits == 4: 
            if int(num_s[1]) == 0 and int(num_s[2]) == 0 and int(num_s[3]) == 0: 
                return num_dict[int(num_s[0])] + " Thousand"
            else:
                p = int(num_s[1:])
                temp = self.numberToWords(p)
                return num_dict[int(num_s[0])] + " Thousand " + temp
        
        elif num_digits == 5: 
            first_part = int(num_s[:2])
            second_part = int(num_s[2:])
            temp1 = self.numberToWords(first_part)
            if second_part == 0:
                return temp1 + " Thousand"
            else:
                temp2 = self.numberToWords(second_part)
                return temp1 + " Thousand " + temp2
        elif num_digits == 6: 
            first_part = int(num_s[:3])
            second_part = int(num_s[3:])
            temp1 = self.numberToWords(first_part)
            if second_part == 0:
                return temp1 + " Thousand"
            else: 
                temp2 = self.numberToWords(second_part)
                return temp1 + " Thousand " + temp2
        elif num_digits>= 7 and num_digits < 10: 
            first_part = 0
            second_part = 0
            if num_digits == 7:
                first_part = int(num_s[0])
                second_part = int(num_s[1:])
            elif num_digits == 8: 
                first_part = int(num_s[:2])
                second_part = int(num_s[2:])
            else:
                first_part = int(num_s[:3])
                second_part = int(num_s[3:])
                
            temp1 = self.numberToWords(first_part)
            if second_part == 0: 
                return temp1 +" Million"
            else: 
                temp2 = self.numberToWords(second_part)
                return temp1 + " Million " + temp2
        elif num_digits == 10: 
            first_part = int(num_s[0])
            second_part = int(num_s[1:])
            temp1 = num_dict[first_part]
            if second_part == 0: 
                return temp1 + " Billion"
            else: 
                temp2 = self.numberToWords(second_part)
                return temp1 + " Billion " + temp2