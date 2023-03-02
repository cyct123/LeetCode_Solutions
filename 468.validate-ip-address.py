#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (26.60%)
# Likes:    824
# Dislikes: 2575
# Total Accepted:    140.7K
# Total Submissions: 529.2K
# Testcase Example:  '"172.16.254.1"'
#
# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6"
# if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any
# type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255
# and xi cannot contain leading zeros. For example, "192.168.1.1" and
# "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00",
# and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8"
# where:
#
#
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter
# ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
#
#
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
# "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while
# "2001:0db8:85a3::8A2E:037j:7334" and
# "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
#
#
# Example 1:
#
#
# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
#
#
# Example 2:
#
#
# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
#
#
# Example 3:
#
#
# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
#
#
#
# Constraints:
#
#
# queryIP consists only of English letters, digits and the characters '.' and
# ':'.
#
#
#


# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isValidIPv4(queryIP):
            return "IPv4"
        if self.isValidIPv6(queryIP):
            return "IPv6"
        return "Neither"

    def isValidIPv4(self, queryIP: str) -> bool:
        if ":" in queryIP:
            return False
        ip = queryIP.split(".")
        if len(ip) != 4:
            return False
        for i in range(len(ip)):
            if not ip[i].isdigit():
                return False
            if ip[i][0] == "0" and len(ip[i]) > 1:
                return False
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
        return True

    def isValidIPv6(self, queryIP: str) -> bool:
        validChars = set("0123456789abcdefABCDEF")
        if "." in queryIP:
            return False
        ip = queryIP.split(":")
        if len(ip) != 8:
            return False
        for i in range(len(ip)):
            if not ip[i] or len(ip[i]) > 4:
                return False
            for j in range(len(ip[i])):
                if ip[i][j] not in validChars:
                    return False
        return True


# @lc code=end
