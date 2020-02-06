def parsejson(tst):
    import json, ast
    x = ast.literal_eval(json.loads(json.dumps(tst.replace('null','""')))) # convert resp to proper format, parse to string, format to tuple
    return x
