import requests

faceset = ""
key = ""
secret = ""

datapoint = {"api_key": key, "api_secret": secret}
filepath = "me2.jpg"

def detect_face():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}
    dat = {"api_key": key, "api_secret": secret}
    response = requests.post(http_url, data=dat, files=files)
    req_dict = response.json()
    return req_dict

def facecmp():
    facecmpurl = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    face_token1 = ""
    face_token2 = ""

    dat = {"api_key": key, "api_secret": secret, "face_token1": face_token1, "face_token2": face_token2}
    response = requests.post(facecmpurl, data=dat)
    req_dict = response.json()
    print(req_dict)
    return req_dict

def GetFaceSets():
    GetFaceSetsurl = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets"
    dat = {"api_key": key, "api_secret": secret}
    response = requests.post(GetFaceSetsurl, data=dat)
    req_dict = response.json()
    print(req_dict)
    return req_dict

def FaceSet_add_face(faceset_token, face_tokens):
    addfaceurl = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    dat = {"api_key": key, "api_secret": secret, "faceset_token": faceset_token, "face_tokens": face_tokens}
    response = requests.post(addfaceurl, data=dat)
    req_dict = response.json()
    print(req_dict)
    return req_dict

def FaceSet_Search(faceset_token, face_token):
    addfaceurl = "https://api-cn.faceplusplus.com/facepp/v3/search"
    dat = {"api_key": key, "api_secret": secret, "face_token": face_token, "faceset_token": faceset_token}
    response = requests.post(addfaceurl, data=dat)
    req_dict = response.json()
    print(req_dict)
    return req_dict

def GetFaceSetsDetail(faceset_token):
    GetFaceSetsDetailurl = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"
    dat = {"api_key": key, "api_secret": secret, "faceset_token": faceset_token}
    response = requests.post(GetFaceSetsDetailurl, data=dat)
    req_dict = response.json()
    print(req_dict)
    return req_dict

def CallCamera():
    rawdict=detect_face()
    print(rawdict)
    lis=rawdict['faces']
    print(lis)
    face_t=lis[3]
    return face_t

def judge(faceset_tokn, facetoken):
    res=FaceSet_Search(faceset_tokn, facetoken)
    tmp=res['results']
    dict=tmp[0]
    print(dict['confidence'])

def callCamare():
    rawdict=detect_face()
    lis=rawdict['faces']
    face_t=lis[0]
    print(face_t['face_token'])
    return face_t['face_token']

def addfacetoclass(faceset_token):
    ft=str(callCamare())
    FaceSet_add_face(faceset_token, ft)

def isintheclass(faceset_token):
    ft=str(callCamare())
    res=FaceSet_Search(faceset_token, ft)
    tmp=res['results']
    dict=tmp[0]
    print(dict['confidence'])
    if 75.0 < float(dict['confidence']):
        print("Is in the class.")
    else:
        print("Not in the class.")

isintheclass(faceset)
