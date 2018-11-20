import wolframalpha
client = wolframalpha.Client("AWEU4P-5L2TWV4VKW")
from VolumeCalculation import calcVolume

def getCals(img1, img2, refSize, food):
    volume = calcVolume(img1, img2, refSize)
    question = "How many calories are there in a %.02f cubic inch %s" % \
               (volume, food)
    res = client.query(question)
    answer = next(res.results).text
    return answer

