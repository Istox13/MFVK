import json, requests

class VK_lib:
    
    def get_name(id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)
        return s['title']

    def get_count(self, id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)

        return s['count']

    def get_dict(id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)
        music = dict()
        ms = s['html'].split('\n')
        n_ms = list()
        while ms:
            if len(ms) >= 13:
                n_ms.append(ms[:13])
            ms = ms[13:]
        
        for n, i in enumerate(n_ms):
            composition = dict()
            composition['artist'] = i[11].strip().split('<div class="artist">')[1].split('<')[0]
            composition['name'] = i[10].strip().split('<div class="title">')[1].split('<')[0]
            composition['long'] = i[9].strip().split('<div class="duration">')[1].split('<')[0]
            composition['url'] = i[2].strip().split('<div class="play" data="')[1].split('"')[0]
            music[str(n)] = composition
        return music


    
    



