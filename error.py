import json

with open('error-detection.json') as json_data:
    teste = ""
    data = json.load(json_data)
    data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptionMsgPatterns'][1] = []
    data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptions'] = []
    for line in open('erros.txt').readlines(  ): 
        # print(data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptions'])
        data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptions'].append(u'{}'.format(line).replace("\n", ""))

        # print(data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptions'])
        # print(data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptionMsgPatterns'][1][0])
        # print(data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptionMsgPatterns'][1])
        # error_msg = '["com.singularity.ee.controller.api.dto.transactionmonitor.transactiondefinition.StringMatch",\r\n {"matchType" : "NOT_EMPTY",\r\n "matchPattern" : "<not empty>",\r\n "inverse" : false,\r\n "inList" : null,\r\n "extendedMatchType" : "NOT_EMPTY",\r\n "extendedMatchPattern" : "<not empty>",\r\n "regexGroups" : null\r\n}],'
        error_msg = ["com.singularity.ee.controller.api.dto.transactionmonitor.transactiondefinition.StringMatch", {"matchType" : "NOT_EMPTY", "matchPattern" : "<not empty>", "inverse" : False, "inList" : None, "extendedMatchType" : "NOT_EMPTY", "extendedMatchPattern" : "<not empty>", "regexGroups" : None }]

        data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptionMsgPatterns'][1].append(error_msg)
        # print("=============")
        # print(data['entities'][1][0][1]['errorConfig'][1]['ignoreExceptionMsgPatterns'][1])

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)