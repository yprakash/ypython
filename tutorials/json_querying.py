# @author: yprakash
import json
import urllib.request


class Solution:
    def __init__(self, url=''):
        if url:
            with urllib.request.urlopen("https://" + url) as url:
                self.contacts = json.load(url)

        print(len(self.contacts), 'contacts loaded')

    def api_response_parser(self, input_list=[], size=0):
        if len(input_list) != 3:
            return self.contacts
        results = []

        for value in self.contacts:
            id = value['id']
            for field in input_list[0].split('.'):
                value = value[field]
            if input_list[1] == 'IN':
                if value in input_list[2].split(','):
                    results.append(id)
            else:
                if value == input_list[2]:
                    results.append(id)

        if not results:
            results.append(-1)
        return results


if __name__ == "__main__":
    lru = ''
    result = Solution(''.join(list(reversed(lru))))
    testcases = [
        ["username", "EQUALS", "vinayk"],  # [1]
        ["address.city", "EQUALS", "Kolkata"],  # [2]
        ["address.city", "IN", "Mumbai,Kolkata"],  # [1, 2]
        ["username", "EQUALS", "Tom"],  # [-1]
    ]
    for inputList in testcases:
        res = result.api_response_parser(inputList, len(inputList))
        print(res)
