# @author: yprakash
import json
import urllib.request


class Solution:
    def __init__(self, url=''):
        if url:
            with urllib.request.urlopen("https://" + url) as url:
                self.contacts = json.load(url)
        else:
            s = '[{"id":1,"name":"Vinay Kumar","username":"vinayk","email":' + \
                '"vinayk@abcu.com","address":{"street":"random1","suite":"APR",' + \
                '"city":"Mumbai","zipcode":"192008-13874","geo":{"lat":"-17.3159",' + \
                '"lng":"91.1496"}},"website":"seuinfra.org","company":{"name":"sec infra",' + \
                '"basename":"seu infra tech"}},{"id":2,"name":"Anandita Basu","username":' + \
                '"PrernaB","email":"Anandita.b@abc1f.cpm","address":{"street":"Hawroh Bridge",' + \
                '"suite":"ATY","city":"Kolkata","zipcode":"700001","geo":{"lat":"-67.3159",' + \
                '"lng":"91.8006"}},"website":"techInfar.org","company":{"name":' + \
                '"tech infar world","basename":"seu infra tech"}},{"id":3,"name":' + \
                '"Charvi Malhotra","username":"CharviM","email":"Charvim@mail.net",' + \
                '"address":{"street":"whitehouse Extension","suite":"A782","city":"Bengaluru",' + \
                '"zipcode":"560001","geo":{"lat":"-68.6102","lng":"-47.0653"}},"website":' + \
                '"Infesystem.info","company":{"name":"infeystems","basename":"Information E stsyem"}}]'

            self.contacts = json.loads(s)

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
    result = Solution()
    testcases = [
        ["username", "EQUALS", "vinayk"],  # [1]
        ["address.city", "EQUALS", "Kolkata"],  # [2]
        ["address.city", "IN", "Mumbai,Kolkata"],  # [1, 2]
        ["username", "EQUALS", "Tom"],  # [-1]
    ]
    for inputList in testcases:
        res = result.api_response_parser(inputList, len(inputList))
        print(res)
